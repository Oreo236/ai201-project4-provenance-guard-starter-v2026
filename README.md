# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. **The route — `POST /submit` in `app.py`.** The JSON body arrives and Flask
   turns it into a dict. *Adds:* a place for the request to land. In unit 8 the
   rate limiter checks the caller here, before anything else runs.
2. **Validation — also in the route.** Checks that `text` is a string, isn't
   blank, is long enough to score and isn't too long, and that `creator_id` is
   there. A bad request gets a 400 or 413 with a reason and is logged as a
   rejection. *Adds:* a guarantee that everything below gets text it can
   score, so bad input gets an answer instead of crashing the service with a 500.
3. **Signal one — `detector.model_signal`.** gpt2 reads the first 400 tokens
   (about 300 words) and measures how predictable they are. *Adds:*
   `model_score`, 0–1, where higher means more AI-like.
4. **Signal two — `stylometry.style_signal`.** Measures the shape of the text:
   how much sentence length varies, how varied the vocabulary is, and how
   punctuation is used. *Adds:* `style_score`, 0–1, same direction.
5. **The combining rule — `scoring.combine_signals`.** *Adds:* one combined
   score from the two signals, and decides what happens when they disagree.
6. **The label mapping — `scoring.score_to_label`.** *Adds:* the `guess`
   (`ai` / `unsure` / `human`) and the sentence a person actually reads.
7. **The record — `audit.log_decision`, then the response.** The route gives
   the submission a `content_id` and writes all nine fields to
   `logs/audit.jsonl`. Then it replies with the label, both signal scores and
   the `content_id`. *Adds:* a permanent trace, and the one handle the writer
   needs to appeal.

The full request and response contract, plus the false-positive trace, is in
[design.md](design.md).


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** Predictability. gpt2 computes the perplexity of the
first 400 tokens, meaning how surprised it is by each next word on average.
That number is squashed onto 0–1, with perplexity 45 landing at 0.5. Lower
perplexity gives a higher score, which means more AI-like.

**Why that might differ between human and AI writing:** A language model
writes by picking a likely next word again and again, so its output is text
that models find easy to predict. People make odd word choices, take abrupt
turns and reach for specific details, all of which a model doesn't expect.

**What it can't see:** Who wrote the text. It measures how *ordinary* the
words are, not where they came from. Plain human writing in common words and
short sentences scores like machine text. A plainly written paragraph scored
**0.86** and a textbook AI paragraph scored **0.89**, almost the same. That
puts second-language writers, younger writers and anyone writing plainly on
purpose at risk. It fails the other way too: ornate prose full of rare words
scored **0.08** (perplexity 212), so AI text prompted to sound "literary" can
pass as human. It also never reads past the first ~300 words, so anything
after that has no effect on the score. And it can't tell "a machine wrote
this" from "gpt2 has read this before". The Gettysburg Address scored **0.73**,
almost certainly because the famous speech was in gpt2's training data, so
quoting famous human writing looks like AI.

### Signal two — the style signal

**What it measures:** The shape of the text without reading it, using two
measures:

- **Sentence-length spread**, worth 0.6 of the signal. This is the standard
  deviation of sentence lengths divided by the mean. A spread of 0.25 or less
  reads fully AI-like and 0.65 or more reads fully human-like. Two-sentence
  texts keep only a third of their pull and one-sentence texts score a neutral
  0.5, because a spread from so few sentences means little.
- **Punctuation**, worth 0.4. This counts every mark except full stops, per
  word, and scores how close the text sits to AI's typical rate of about 0.05.
  It is *not* "more punctuation = more human". My casual pieces used 0.00–0.03
  marks per word, formal human prose used 0.08, and AI sat in between. So being
  far from typical in *either* direction reads as human.

Type-token ratio is computed (`type_token_ratio`, averaged over 25-word
windows) but gets no vote. On my test texts it tracked length more than
authorship. AI text also had *more* varied vocabulary (0.77–0.91) than formal
human prose (0.63–0.69), the opposite of the theory.

**Why that might differ between human and AI writing:** "Most likely next
word" averages out to even, mid-length sentences, safe vocabulary and tidy
punctuation. Human writing is lumpier: a three-word sentence sits next to a
forty-word one, with a dash or a fragment thrown in.

**What it can't see:** Meaning. It reacts to surface changes that leave the
content alone. Typos, chopping sentences up, a pasted quotation or an extra
dash all move it, and any of those costs an attacker seconds. It is also
thrown off by length, because type-token ratio falls as text gets longer, so
long and short submissions aren't directly comparable. Plain writers get hit
here too, since even sentences and repeated common words look "AI-shaped" to
both signals at once. The punctuation measure in particular can be moved
either way just by adding or deleting commas.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** Average the two signals, weighted equally. But if they disagree
by more than 0.30, hold the result between 0.40 and 0.60, inside the unsure
band. Two methods disagreeing is genuine uncertainty, so neither label can be
reached on one signal's say-so. That matters most for the writer signal one
misreads, someone whose plain or familiar-sounding text scores high on the
model but whose writing doesn't have AI's shape.

**The numbers** (all in `config.py`):

| Setting | Value |
|---|---|
| `WEIGHT_MODEL_SIGNAL` / `WEIGHT_STYLE_SIGNAL` | 0.5 / 0.5 |
| `DISAGREEMENT_GAP` | 0.30 |
| `SPLIT_FLOOR` / `SPLIT_CEILING` | 0.40 / 0.60 |
| `HUMAN_THRESHOLD` / `AI_THRESHOLD` | 0.35 / 0.65 (unchanged, until Milestone 5) |

The weights are equal because each signal's blind spot lands on different
writers: plain writers for the model, anyone reshaping text for style.
Neither has earned more trust.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**The four calibration inputs, plus my own pieces:**

| Input | model | style | combined | Lands in |
|---|---|---|---|---|
| Clearly AI (starter sample) | 0.886 | 0.801 | 0.844 | AI |
| Clearly AI (generated essay) | 0.813 | 0.681 | 0.747 | AI |
| Clearly human (my piece 1) | 0.259 | 0.375 | 0.317 | human |
| Clearly human (my piece 2) | 0.261 | 0.293 | 0.277 | human |
| Formal human (Gettysburg Address) | 0.727 | 0.349 | 0.538 | unsure |
| Formal human (Darwin, *Origin of Species*) | 0.685 | 0.417 | 0.551 | unsure |
| Lightly-edited AI (essay with contractions, shorter sentences) | 0.709 | 0.756 | 0.732 | AI |

Both formal human texts would have been flagged as AI on signal one alone.
Signal two is what pulls them back to unsure. The lightly-edited AI stays
caught, because adding contractions didn't change its even sentence lengths or
its middle-of-the-road punctuation.

These cutoffs (0.25 / 0.65 spread, 0.05 ± 0.03 punctuation) were tuned on
these few texts, so they will fit them better than they fit anything new.
Unit 8's attack set is the honest test.

**A case where my two signals split, and what my rule does with it:**

The Gettysburg Address. Signal one says **0.73** (AI-like): gpt2 finds it
easy to predict, almost certainly because it has read it. Signal two says
**0.35** (human-like): sentences of 30, 24, 11, 27 and 11 words, and heavy
punctuation. They're 0.38 apart, past the 0.30 gap, so the rule holds the
score inside 0.40–0.60. It lands at **0.538, unsure**. A straight average
happens to land there too.

Where the rule actually changes the outcome is the plain-writing paragraph
from the false-positive trace in [design.md](design.md). Model **0.86**,
style **0.52**, 0.34 apart. A straight average gives 0.69, which would be
labelled **AI**. The rule caps it at **0.60, unsure**. That's the writer this
rule exists for.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "This weekend I went back home to celebrate a friends of mines birthday. So we just went to several restaurants and I showed her around my city since she is not from there", "creator_id": "oreoluwa"}'
```

```json
{
  "confidence": null,
  "content_id": "5808bd8b49fb4c6dba7582bc0368f6e1",
  "creator_id": "oreoluwa",
  "guess": "pending",
  "label": "PLACEHOLDER",
  "model_score": 0.2587,
  "status": "decided",
  "style_score": null
}
```

<!-- Milestone 3 run: only signal one is wired in. confidence, guess, label
     and style_score are placeholders until Milestones 4 and 5. -->

**A refused submission** (too short to score)

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "too short", "creator_id": "oreoluwa"}'
```

```json
{
  "error": "text_too_short",
  "message": "Send at least 20 words — shorter text can't be scored reliably."
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": null,
      "content_id": "5808bd8b49fb4c6dba7582bc0368f6e1",
      "creator_id": "oreoluwa",
      "guess": "pending",
      "label": "PLACEHOLDER",
      "model_score": 0.2587,
      "status": "decided",
      "style_score": null,
      "timestamp": "2026-10-26T06:53:34+00:00"
    },
    {
      "creator_id": "oreoluwa",
      "event": "rejected",
      "http_status": 400,
      "reason": "text_too_short",
      "status": "rejected",
      "timestamp": "2026-10-26T06:53:34+00:00"
    }
  ]
}
```

<!-- Milestone 3 run. Re-run after the appeal is built (Milestone 5) so this
     shows the appeal entry too. -->

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**

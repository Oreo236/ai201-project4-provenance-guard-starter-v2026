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
| high-confidence human | 0.00 – 0.35 | We think this was most likely written by a person. |
| unsure | above 0.35, below 0.65 | We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal. |
| high-confidence AI | 0.65 – 1.00 | Our checks suggest this was probably written with AI. These checks can be wrong, especially about plain, simple writing. If you wrote this yourself, please appeal and tell us how you wrote it. Your work will be marked for review. |

A score of exactly 0.35 counts as human and exactly 0.65 counts as AI
(`scoring.py::score_to_label`). All three are reachable. The Sample Run below
shows a real submission producing each one.

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

The person most likely to see it is someone like the writer in my
false-positive trace: they wrote every word, in plain sentences, and the two
checks disagreed about them. So the label says the uncertainty is *ours*
("we can't tell"), not something wrong with their work. It says outright that
it isn't an accusation, and it tells them that a lot of people's own writing
lands here, so they don't read it as being singled out. It ends with what they
can do.

The AI label also mentions plain writing by name, because that's the specific
way these checks fail. Neither label promises that a *person* will review an
appeal, because nothing in this service assigns one. "Marked for review" is
what actually happens.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

This is the plain-writing paragraph from the false-positive trace. The two
signals split (0.86 vs 0.52), so the combining rule holds it at 0.60, unsure,
where a straight average would have said AI.

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "I moved here two years ago for work. At first it was hard. I did not know many people and the winters are very cold. Now I have friends from my job and I like my apartment. On weekends I go to the market and I cook for my family. I think this city is a good place to live.", "creator_id": "amara"}'
```

```json
{
  "confidence": 0.6,
  "content_id": "dc9ac9e68e144356be4ddf199827d7ae",
  "creator_id": "amara",
  "guess": "unsure",
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "model_score": 0.8627,
  "status": "decided",
  "style_score": 0.5201
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "dc9ac9e68e144356be4ddf199827d7ae", "reasoning": "I wrote this myself about moving to a new city. I write in simple English because it is my second language."}'
```

```json
{
  "content_id": "dc9ac9e68e144356be4ddf199827d7ae",
  "message": "Your appeal has been recorded. This piece is now marked as under review.",
  "original_guess": "unsure",
  "status": "under_review"
}
```

**What the log shows afterwards**

The original decision stays exactly as it was, and the appeal sits right
after it with the new status.

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.6,
      "content_id": "dc9ac9e68e144356be4ddf199827d7ae",
      "creator_id": "amara",
      "guess": "unsure",
      "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
      "model_score": 0.8627,
      "status": "decided",
      "style_score": 0.5201,
      "timestamp": "2026-10-26T06:58:41+00:00"
    },
    {
      "content_id": "dc9ac9e68e144356be4ddf199827d7ae",
      "creator_id": "amara",
      "event": "appeal",
      "reasoning": "I wrote this myself about moving to a new city. I write in simple English because it is my second language.",
      "status": "under_review",
      "timestamp": "2026-10-26T06:58:47+00:00"
    }
  ]
}
```

**The other two labels, reached with real submissions**

| Text | model | style | confidence | guess |
|---|---|---|---|---|
| A generated essay on remote work | 0.8133 | 0.6814 | 0.7473 | `ai` |
| My own piece 1 (a weekend at home) | 0.2587 | 0.375 | 0.3168 | `human` |

**Bad requests get a reason, not a crash**

| Request | Status | `error` |
|---|---|---|
| `/submit` with `"text": "too short"` | 400 | `text_too_short` |
| `/submit` with no `text` | 400 | `missing_text` |
| `/submit` with a JSON list as the body | 400 | `invalid_json` |
| `/submit` with 50,000 words | 413 | `text_too_long` |
| `/appeal` on an already-appealed id | 409 | `already_under_review` |
| `/appeal` with a made-up id | 404 | `unknown_content_id` |

Every one of these also leaves a `rejected` entry in the audit log.

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

**My limits:** 5 per minute, 50 per day, on `POST /submit` (`config.py`,
applied by the `@limiter.limit(...)` decorator on `app.py::submit`).

**Why those numbers and not others:**

A real writer submits a piece, maybe revises it and submits again. Even
someone fixing typos and resubmitting won't send 5 in one minute, and 50 in a
day is far more than anyone checking their own work needs. A script trying to
map my thresholds has to send hundreds of small variations of the same text and
watch where the label flips. At 50 a day per caller, that takes days instead of
minutes. 10 a minute and 200 a day (the starter's numbers) would let a script
roughly map the 0.35 and 0.65 cut-offs in one afternoon. Going lower than 5 a
minute starts catching a real writer who hits submit, spots a mistake and
submits again.

**What a caller counts as:** The `creator_id` in the request, falling back to
the caller's address when there isn't a usable one
(`app.py::rate_limit_key`). The weakness is that `creator_id` is whatever the
caller says it is, so a script that makes up a new id for every request is
never limited at all. That's exactly what the attack set does, since every row
submits as its own `attacker_<id>`. Limiting by address instead would stop that
script, but would lump everyone behind one school or library network into one
caller. Neither is right without real accounts.

**The run of status codes when I pushed past it:**

`python run_attacks.py --flood 15` → `results/flood_2026-11-04_1747.md`

```
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
```

Each of the ten 429s left a `rejected` entry in the audit log:

```json
{"creator_id": "flood_tester", "event": "rejected", "limit": "5 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-04T22:47:47+00:00"}
```

---

## Attack Run — Before

`python run_attacks.py --set attack_set --label before` →
`results/attack_run_2026-11-04_1808_before.md` (the attack set is in
`attack_set/`). All 56 attacks ran, nothing crashed the service (0 5xx), and I
ran this before changing anything.

**How I marked them.** For evasion and prompt-injection attacks, BROKE means
AI text did not get the `ai` label, or got `human`. For false-positive attacks,
BROKE means a real person's writing got the `ai` label. An `unsure` on a real
person's writing counts as HELD because it makes no accusation. For malformed
requests and the flood, BROKE means a 5xx, a crash, or no trace in the log.

**Score: 46 held, 10 broke.**

- Evasion: 3 held, **7 broke** (EV01, 02, 03, 05, 06, 07, 10). None reached
  `human`; they all landed on `unsure`.
- False positive: 6 held, **2 broke** (FP02, FP05).
- Prompt injection: 5 held, **1 broke** (PI02).
- Malformed requests (MF, RQ): 20 held, 0 broke.
- Flood: 12 held. 5 got a 400, then 7 got a 429.

| ID | Family | Going for | Status | Guess | Score | Held / broke | What happened |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.562 | **BROKE** | typos pushed style to 0.96 and model dropped to 0.16; 0.80 apart, so the split rule made it unsure |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.457 | **BROKE** | chopped sentences: spread jumped to 0.85, style fell to 0.32; labelled unsure, not ai |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.518 | **BROKE** | pasted quotation: style 0.37, model 0.67; unsure |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | ai | 0.752 | **HELD** | rare words did not help: model 0.61 and style 0.89, so it was still called ai |
| EV05 | evasion | both signals: heavy human editing pass | 200 | unsure | 0.400 | **BROKE** | heavy edit: style 0.00; the 0.32 gap triggered the split rule and held it at 0.40, unsure |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.400 | **BROKE** | one very long and one very short sentence: spread 1.19, style 0.17; unsure |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.443 | **BROKE** | punctuation padding: punctuation density 0.23, style 0.30; unsure |
| EV08 | evasion | signal one: text below the token window | 400 | — | — | **HELD** | 10 words, so the route refused it with a 400; it was never scored |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | ai | 0.662 | **HELD** | human opening did not hide it; model 0.70, style 0.62, called ai |
| EV10 | evasion | signal two: repeated stanza structure | 200 | unsure | 0.600 | **BROKE** | model said 0.98 but style said 0.38; the split rule capped it at 0.60, unsure |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.453 | **HELD** | plain human writing; unsure (0.45), not accused |
| FP02 | false_positive | human writing in a formal register | 200 | ai | 0.669 | **BROKE** | a person's formal report was called ai: model 0.74, style 0.60 |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | unsure | 0.600 | **HELD** | non-native writer; model 0.81 but style 0.48 split them, capped at 0.60, unsure |
| FP04 | false_positive | a student essay written to a rubric | 200 | unsure | 0.600 | **HELD** | student essay; model 0.83 but style 0.43, capped at 0.60, unsure |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.737 | **BROKE** | a person's technical documentation was called ai: model 0.80, style 0.67, both signals agreed |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.539 | **HELD** | formal template; model 0.88, style 0.20, unsure |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | unsure | 0.533 | **HELD** | deliberate repetition; model 0.88, style 0.19, unsure |
| FP08 | false_positive | very short genuine human submission | 400 | — | — | **HELD** | 8 words, refused with a 400, never scored or accused |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.400 | **HELD** | instruction ignored; unsure. This AI text scores unsure on its own, so the instruction changed nothing that matters |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.265 | **BROKE** | AI text labelled human (0.265). Not obeyed: the odd SYSTEM header dropped model from 0.75 to 0.20 |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | ai | 0.697 | **HELD** | instruction ignored; still called ai (0.70) |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.451 | **HELD** | HTML in the text did not reach the label; the label is a fixed string. Unsure |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.465 | **HELD** | quote marks in the text did not break the log; the entry is valid JSON. Unsure |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.433 | **HELD** | instruction plus human text; unsure, instruction ignored |
| MF01 | malformed | text is only whitespace | 400 | — | — | **HELD** | refused: 400 (413 for the 60,000-character one) |
| MF02 | malformed | text is a single character | 400 | — | — | **HELD** | refused: 400 (413 for the 60,000-character one) |
| MF03 | malformed | text is control characters | 400 | — | — | **HELD** | refused: 400 (413 for the 60,000-character one) |
| MF04 | malformed | text is only punctuation | 400 | — | — | **HELD** | refused: 400 (413 for the 60,000-character one) |
| MF05 | malformed | text is a very long single word | 400 | — | — | **HELD** | refused: 400 (413 for the 60,000-character one) |
| MF06 | malformed | text is emoji only | 400 | — | — | **HELD** | refused: 400 (413 for the 60,000-character one) |
| MF07 | malformed | text is right-to-left script | 400 | — | — | **HELD** | refused: 400 (413 for the 60,000-character one) |
| MF08 | malformed | text is 60,000 characters | 413 | — | — | **HELD** | refused: 400 (413 for the 60,000-character one) |
| RQ01 | malformed | no text field at all | 400 | — | — | **HELD** | refused with a 400 |
| RQ02 | malformed | no creator_id | 400 | — | — | **HELD** | refused with a 400 |
| RQ03 | malformed | text is a number | 400 | — | — | **HELD** | refused with a 400 |
| RQ04 | malformed | text is a list | 400 | — | — | **HELD** | refused with a 400 |
| RQ05 | malformed | text is null | 400 | — | — | **HELD** | refused with a 400 |
| RQ06 | malformed | creator_id is an object | 400 | — | — | **HELD** | refused with a 400 |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | **HELD** | refused with a 400 |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | **HELD** | refused with a 400 |
| RQ09 | malformed | body is empty | 400 | — | — | **HELD** | refused with a 400 |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | — | — | **HELD** | first run returned 429 (my address's bucket was full, so it never reached the route); re-sent after a minute: 400 invalid_json |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | — | — | **HELD** | first run returned 429, same reason; re-sent after a minute: 400 invalid_json |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | **HELD** | refused with a 400 |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 400 | — | — | **HELD** | 400 text_too_short |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 400 | — | — | **HELD** | 400 text_too_short |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 400 | — | — | **HELD** | 400 text_too_short |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 400 | — | — | **HELD** | 400 text_too_short |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 400 | — | — | **HELD** | 400 text_too_short |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** | 429 rate limited, logged |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** | 429 rate limited, logged |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** | 429 rate limited, logged |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** | 429 rate limited, logged |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** | 429 rate limited, logged |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** | 429 rate limited, logged |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** | 429 rate limited, logged |

**Ten audit log entries from the run**, from `GET /log` (the full pull is
`results/audit_extract_before.json`). Seven are decisions and three are
rejections, picked because they show the failures and the split rule at work.

FP05, a person's documentation, called AI with both signals agreeing (the worst
outcome, below):

```json
{"timestamp": "2026-11-04T23:08:11+00:00", "content_id": "8c9dd081f9bf4dd5a724d8c3fad9b900", "creator_id": "attacker_FP05", "guess": "ai", "model_score": 0.8005, "style_score": 0.6743, "combined_score": 0.7374, "label": "Our checks suggest this was probably written with AI. These checks can be wrong, especially about plain, simple writing. If you wrote this yourself, please appeal and tell us how you wrote it. Your work will be marked for review.", "status": "decided"}
```

FP02, a person's formal report, called AI:

```json
{"timestamp": "2026-11-04T23:08:11+00:00", "content_id": "36372ede40b84f7182a6addad68cc54a", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7387, "style_score": 0.6, "combined_score": 0.6694, "label": "Our checks suggest this was probably written with AI. These checks can be wrong, especially about plain, simple writing. If you wrote this yourself, please appeal and tell us how you wrote it. Your work will be marked for review.", "status": "decided"}
```

PI02, AI text with a fake SYSTEM line on top, labelled human:

```json
{"timestamp": "2026-11-04T23:08:12+00:00", "content_id": "5baf905fa65d4432b5ae39535623bae8", "creator_id": "attacker_PI02", "guess": "human", "model_score": 0.2044, "style_score": 0.3253, "combined_score": 0.2648, "label": "We think this was most likely written by a person.", "status": "decided"}
```

EV01, typos added to AI text. The two signals are 0.80 apart:

```json
{"timestamp": "2026-11-04T23:08:10+00:00", "content_id": "f2060682624b4706b6b72340522f1f4a", "creator_id": "attacker_EV01", "guess": "unsure", "model_score": 0.1635, "style_score": 0.9613, "combined_score": 0.5624, "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.", "status": "decided"}
```

EV10, where the split rule cut a model score of 0.98 down to 0.60:

```json
{"timestamp": "2026-11-04T23:08:11+00:00", "content_id": "10cf968902794503a4a7568372664c83", "creator_id": "attacker_EV10", "guess": "unsure", "model_score": 0.9792, "style_score": 0.3842, "combined_score": 0.6, "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.", "status": "decided"}
```

EV07, punctuation padding:

```json
{"timestamp": "2026-11-04T23:08:11+00:00", "content_id": "4721240434134757b52f1c8c0f842d21", "creator_id": "attacker_EV07", "guess": "unsure", "model_score": 0.5862, "style_score": 0.3, "combined_score": 0.4431, "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.", "status": "decided"}
```

PI05, quote marks and fake JSON inside the text. The entry is still valid:

```json
{"timestamp": "2026-11-04T23:08:12+00:00", "content_id": "3cf62d89e3a94cd2a7b4a20063a0f0d6", "creator_id": "attacker_PI05", "guess": "unsure", "model_score": 0.6401, "style_score": 0.2893, "combined_score": 0.4647, "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.", "status": "decided"}
```

A rejection: the flood, after the fifth request (a 429):

```json
{"timestamp": "2026-11-04T23:08:12+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

A rejection: deeply nested JSON as `text` (a 400):

```json
{"timestamp": "2026-11-04T23:08:12+00:00", "creator_id": "attacker_RQ12", "event": "rejected", "status": "rejected", "reason": "text_not_string", "http_status": 400}
```

A rejection: a request with no usable `creator_id`, counted against my address
(creator logged as `unknown`):

```json
{"timestamp": "2026-11-04T23:08:12+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

**FP05.** A person wrote installation instructions ("To configure the service,
edit the settings file in the installation directory. Set the host value to…")
and the service told them *"Our checks suggest this was probably written with
AI."* Model 0.80, style 0.67, combined 0.737. Both signals agreed, so the split
rule had nothing to hold back. Of everything in the run, this is the case the
whole project exists to prevent. The writer did nothing unusual: they wrote
short, plain, even sentences, which is what documentation is. The label even
mentions plain writing, so the service as good as admits it might be wrong
about exactly this. FP02, a plain formal report, went the same way. The only
thing between that writer and a wrong accusation was their own appeal.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

`python run_eval.py --label before` → `results/run_2026-11-04_1759_before.md`.
Scenarios are in `scenarios.py`. I extended `run_eval.py` so criterion 4
appeals every submission it gets back (plus one made-up id), and so every
request records the audit-log entries it left behind, which criterion 5 needs.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Real writers don't get accused | 0 of 10 labelled AI | 0/10 | 0/10 | 0/10 | MET |
| 2. AI and human text land far apart | AI mean ≥ 0.30 above human mean | +0.3012 | +0.3012 | +0.3012 | MET (by 0.0012) |
| 3. All three labels reachable | ai, human, unsure each ≥ 1 | 3/3 | 3/3 | 3/3 | MET |
| 4. Every appeal recorded and changes status | 10/10 real, fake id → 404 | 10/10, 404 | 10/10, 404 | 10/10, 404 | MET |
| 5. Bad input never crashes | 0 of 6 are 5xx, each logged | 0 5xx, 6/6 logged | 0 5xx, 6/6 logged | 0 5xx, 6/6 logged | MET |

All three trials were identical, number for number, as expected: neither
signal has any randomness in it.

**How I decided each verdict:**

1. No piece of my writing came back `ai` in any trial. Six were `human` and
   four were `unsure`. The closest was my relocation sentence at 0.4869
   (model 0.67).
2. The AI set averaged 0.6412 and my set 0.3400, a gap of 0.3012. That holds,
   but only just. Three of the five AI essays didn't come back `ai`: they
   scored exactly 0.60, `unsure`. Signal one gave them 0.86–0.92, signal two
   gave them 0.60, and that gap of more than 0.30 triggered my split rule,
   which capped them at 0.60.
3. The remote-work essay was `ai` (0.6842), my weekend piece `human` (0.3168)
   and the Gettysburg Address `unsure` (0.5382), in every trial.
4. All 10 appeals per trial returned 200 with `under_review`, and each content
   id had exactly one appeal entry afterwards. The made-up id returned 404 with
   zero appeal entries.
5. Every malformed body got the 4xx code design.md names for it (empty text →
   400 `text_too_short`, missing or null text → 400 `missing_text`, a number →
   400 `text_not_string`, 50,000 words → 413 `text_too_long`, a JSON list →
   400 `invalid_json`), and each left exactly one `rejected` entry.

**Real output from trial 1**, produced by `run_eval.py::main` (submissions)
and `run_eval.py::send_appeal` (appeals). `sent` is truncated by the script.

Criterion 1, my closest call:

```json
{
  "status": 200,
  "content_id": "961f80f19241467a836dd2ca59da8787",
  "guess": "unsure",
  "confidence": 0.4869,
  "model_score": 0.6738,
  "style_score": 0.3,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "sent": "I am based in New York, NY but if I am selected for a San Fr",
  "logged": [{"status": "decided", "guess": "unsure", "combined_score": 0.4869}]
}
```

Criterion 2, an AI essay the split rule held at unsure:

```json
{
  "status": 200,
  "content_id": "c438cf750ac14d40884d0bafe43a8fc0",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.92,
  "style_score": 0.6,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "sent": "Regular exercise plays a crucial role in maintaining both ph",
  "logged": [{"status": "decided", "guess": "unsure", "combined_score": 0.6}]
}
```

Criterion 3, the three labels:

```json
[
  {"status": 200, "content_id": "33d7fce316b3427db88638626c633330", "guess": "ai", "confidence": 0.6842, "model_score": 0.7683, "style_score": 0.6, "sent": "Remote work has fundamentally transformed the modern workpla"},
  {"status": 200, "content_id": "91971349223949ed89bf7686ff922e8f", "guess": "human", "confidence": 0.3168, "model_score": 0.2587, "style_score": 0.375, "sent": "This weekend I went back home to celebrate a friends of mine"},
  {"status": 200, "content_id": "a50b3b6c9721482e8eef7ed67b1ff3c0", "guess": "unsure", "confidence": 0.5382, "model_score": 0.7273, "style_score": 0.3491, "sent": "Four score and seven years ago our fathers brought forth on "}
]
```

(`label`, `error` and `logged` left out of these three for length; they're in
the results file.)

Criterion 4, a real appeal and the made-up one:

```json
[
  {
    "status": 200,
    "content_id": "c221aa7c3f62433db8006061174a25d3",
    "guess": "ai",
    "confidence": 0.6842,
    "sent": "Remote work has fundamentally transformed the modern workpla",
    "appeal": {"status": 200, "new_status": "under_review", "appeal_entries": 1}
  },
  {
    "sent": "appeal with a made-up content_id",
    "appeal": {"status": 404, "new_status": null, "appeal_entries": 0}
  }
]
```

Criterion 5, two of the six:

```json
[
  {"status": 400, "error": "text_too_short", "sent": "(empty text)", "logged": [{"event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 400}]},
  {"status": 400, "error": "invalid_json", "sent": "[\"a\", \"JSON\", \"list\", \"instead\", \"of\", \"an\", \"object\"]", "logged": [{"event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400}]}
]
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

# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. Real writers don't get accused

Of 10 pieces I wrote myself, including at least 3 written plainly in short
sentences and common words, **none** are labelled high-confidence AI, in each
of the 3 trials.

**Why this target:** On a writing site, a wrong accusation costs a real person
far more than a missed detection costs the site, so the number I allow is
zero, not "a few". The plain pieces have to be in the set because that's
exactly the writing signal one scores like AI. In Milestone 1, a plain
paragraph got a `model_score` of 0.86, against 0.89 for AI text, so this
target is hard to hit, and it should be.

---

## 2. Clearly-AI and clearly-human text land far apart

Across 5 clearly-AI texts and 5 clearly-human texts, the average combined
score (`confidence`) of the AI set is **at least 0.30 higher** than the average
of the human set, in each of the 3 trials.

**Why this target:** If the easy cases don't separate cleanly, no choice of
thresholds can work, and the hard cases are hopeless. 0.30 is the width of the
starter's unsure band (0.35–0.65). A spread narrower than the band means even
obvious text could sit inside "unsure" at both ends.

---

## 3. All three labels are reachable

Of my label-coverage inputs (one clearly AI, one clearly human, one I judge
borderline), each of `"ai"`, `"human"` and `"unsure"` is returned **at least
once**, in each of the 3 trials.

**Why this target:** A label no score can produce is a gap in my ranges that
nobody would ever notice from the outside. While `style_signal` is a stub, the
human label is almost unreachable. This criterion catches that and any other
gap, without waiting for a writer to stumble into one.

---

## 4. Every appeal is recorded and changes status

Of 10 appeals sent to `POST /appeal` with real `content_id`s, **10 of 10**
return 200 with `status: "under_review"` and add exactly one appeal entry to
the audit log. An appeal with a made-up `content_id` returns 404 and adds no
appeal entry, in each of the 3 trials.

**Why this target:** An appeal is the only thing standing between a wrong
accusation and nothing at all. So "usually works" isn't good enough: one lost
appeal is a writer who was wrongly accused and then ignored. The made-up id
checks the other direction, so the log can't fill up with appeals for work
that was never submitted.

---

## 5. Bad input never crashes the service

Of 6 malformed `/submit` bodies (text empty, text missing, text `null`, text a
number, 50,000 words of text, and a JSON list instead of an object), **0**
return a 5xx status. Each returns the 4xx code named for it in
[design.md](design.md) and leaves one `rejected` entry in the audit log, in
each of the 3 trials.

**Why this target:** A crash on bad input is one of the most common real
failures, and it's cheap for an attacker to trigger on purpose. A 500 also
leaves the caller with no idea what they did wrong. Requiring a log entry
means an attack made of bad requests shows up in the record rather than as
silence.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->

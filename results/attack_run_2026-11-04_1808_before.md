# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 18:08
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `f2060682624b4706b6b72340522f1f4a` | unsure | 0.562 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `8b065f69f758484d9205650c05cc1f20` | unsure | 0.457 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `0ebfb8d940064ced93753e15d35559e0` | unsure | 0.518 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `93f069d5e906442096207a908e8e9f58` | ai | 0.752 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `3a533deb46844fc5abab80ed45d9ad3f` | unsure | 0.400 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `8a738cc65a744a858b235f11c9d04bfb` | unsure | 0.400 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `4721240434134757b52f1c8c0f842d21` | unsure | 0.443 | BROKE |
| EV08 | evasion | signal one: text below the token window | 400 | `—` | — | — | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `99673bbf9d6f4addbc2fce0e9d6e67e4` | ai | 0.662 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `10cf968902794503a4a7568372664c83` | unsure | 0.600 | BROKE |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `77f3e048f0d3493797f268c9ad55a99c` | unsure | 0.453 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `36372ede40b84f7182a6addad68cc54a` | ai | 0.669 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `1df17c6677664765b9a61ede5ae081f2` | unsure | 0.600 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c26cd9269914485582d1754bdba8418f` | unsure | 0.600 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `8c9dd081f9bf4dd5a724d8c3fad9b900` | ai | 0.737 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `17aaafc9f6e5465e8f0c498b86e98c4f` | unsure | 0.539 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `d138cee0e7c9440cb25f9cf890c108b1` | unsure | 0.533 | HELD |
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `65e62cdf754a48019242472756dec326` | unsure | 0.400 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `5baf905fa65d4432b5ae39535623bae8` | human | 0.265 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `b6f04d92398c46f6b1b681b90aca4828` | ai | 0.697 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `0884262fdbef4386a9181d2aac9792d7` | unsure | 0.451 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `3cf62d89e3a94cd2a7b4a20063a0f0d6` | unsure | 0.465 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `48fa5b8ec09640968ad7c859634000ce` | unsure | 0.433 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | `—` | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — | HELD |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — | HELD |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "f2060682624b4706b6b72340522f1f4a",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.5624,
  "model_score": 0.1635,
  "style_score": 0.9613,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "8b065f69f758484d9205650c05cc1f20",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4572,
  "model_score": 0.5943,
  "style_score": 0.32,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "0ebfb8d940064ced93753e15d35559e0",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5181,
  "model_score": 0.6662,
  "style_score": 0.3699,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "93f069d5e906442096207a908e8e9f58",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.7517,
  "model_score": 0.6114,
  "style_score": 0.892,
  "label": "Our checks suggest this was probably written with AI. These checks can be wrong, especially about plain, simple writing. If you wrote this yourself, please appeal and tell us how you wrote it. Your work will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "3a533deb46844fc5abab80ed45d9ad3f",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.4,
  "model_score": 0.3212,
  "style_score": 0.0,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "8a738cc65a744a858b235f11c9d04bfb",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4,
  "model_score": 0.5727,
  "style_score": 0.168,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "4721240434134757b52f1c8c0f842d21",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4431,
  "model_score": 0.5862,
  "style_score": 0.3,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_EV08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "99673bbf9d6f4addbc2fce0e9d6e67e4",
  "creator_id": "attacker_EV09",
  "guess": "ai",
  "confidence": 0.6617,
  "model_score": 0.7042,
  "style_score": 0.6191,
  "label": "Our checks suggest this was probably written with AI. These checks can be wrong, especially about plain, simple writing. If you wrote this yourself, please appeal and tell us how you wrote it. Your work will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "10cf968902794503a4a7568372664c83",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.9792,
  "style_score": 0.3842,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "77f3e048f0d3493797f268c9ad55a99c",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4532,
  "model_score": 0.6175,
  "style_score": 0.2888,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "36372ede40b84f7182a6addad68cc54a",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6694,
  "model_score": 0.7387,
  "style_score": 0.6,
  "label": "Our checks suggest this was probably written with AI. These checks can be wrong, especially about plain, simple writing. If you wrote this yourself, please appeal and tell us how you wrote it. Your work will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "1df17c6677664765b9a61ede5ae081f2",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.8051,
  "style_score": 0.4827,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "c26cd9269914485582d1754bdba8418f",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.8329,
  "style_score": 0.4249,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "8c9dd081f9bf4dd5a724d8c3fad9b900",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7374,
  "model_score": 0.8005,
  "style_score": 0.6743,
  "label": "Our checks suggest this was probably written with AI. These checks can be wrong, especially about plain, simple writing. If you wrote this yourself, please appeal and tell us how you wrote it. Your work will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "17aaafc9f6e5465e8f0c498b86e98c4f",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5388,
  "model_score": 0.8814,
  "style_score": 0.1962,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "d138cee0e7c9440cb25f9cf890c108b1",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5334,
  "model_score": 0.8816,
  "style_score": 0.1853,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_FP08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "65e62cdf754a48019242472756dec326",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4,
  "model_score": 0.4625,
  "style_score": 0.0,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "5baf905fa65d4432b5ae39535623bae8",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2648,
  "model_score": 0.2044,
  "style_score": 0.3253,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "b6f04d92398c46f6b1b681b90aca4828",
  "creator_id": "attacker_PI03",
  "guess": "ai",
  "confidence": 0.6974,
  "model_score": 0.5943,
  "style_score": 0.8004,
  "label": "Our checks suggest this was probably written with AI. These checks can be wrong, especially about plain, simple writing. If you wrote this yourself, please appeal and tell us how you wrote it. Your work will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "0884262fdbef4386a9181d2aac9792d7",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4506,
  "model_score": 0.4998,
  "style_score": 0.4013,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "3cf62d89e3a94cd2a7b4a20063a0f0d6",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4647,
  "model_score": 0.6401,
  "style_score": 0.2893,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "48fa5b8ec09640968ad7c859634000ce",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4326,
  "model_score": 0.5583,
  "style_score": 0.3069,
  "label": "We can't tell whether this was written by a person or with AI, so we're not making a call either way. A lot of people's own writing lands here, and this is not an accusation. If you wrote this yourself and want someone to take another look, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

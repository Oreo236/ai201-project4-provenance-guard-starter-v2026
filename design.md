# Provenance Guard — design (unit 7, Milestone 1)

The path a submission takes and what each signal measures are in the README
(**What This Does**, **Signals and Scoring**). This file holds the other two
parts of Milestone 1: the false-positive trace and the endpoint contract.

---

## The false positive, traced

**The person.** Amara writes in her second language. She sticks to words she's
sure of and keeps her sentences short. She submits a paragraph she wrote
herself about moving to a new city:

> I moved here two years ago for work. At first it was hard. I did not know
> many people and the winters are very cold. Now I have friends from my job and
> I like my apartment. …

*(The paragraph is a stand-in written in that style. The numbers below are real
output from `detector.py` on it. In Milestone 4, rerun this with plainly
written human text you've collected yourself.)*

**What happens to her, stage by stage, with the starter's current settings:**

| Stage | What it does with her text | Result |
|---|---|---|
| Route + validation | Valid text, valid `creator_id` | accepted |
| Signal one | Perplexity **14.3**. Common words in a predictable order | `model_score` **0.86** |
| Signal two | Still the stub | `style_score` 0.50 |
| Combining rule | 0.5 × 0.86 + 0.5 × 0.50 | **0.68** |
| Label mapping | 0.68 is above `AI_THRESHOLD` (0.65) | `guess: "ai"` |
| Record | Logged as `decided` | `content_id` returned |

For comparison, a textbook AI paragraph scores `model_score` **0.89**. Signal
one can barely tell her apart from a machine.

It gets worse once signal two is built. Even sentence lengths and repeated
common words are exactly what it treats as AI-shaped. Her `style_score` is
likely to land *above* 0.5, so both signals would agree that she's a machine.

> **Update after Milestone 4:** with signal two built, her paragraph scores
> style **0.52**. A straight average would give 0.69, still labelled AI. The
> two signals are 0.34 apart, though, so the combining rule's split check holds
> her at **0.60, unsure**. She is no longer called AI, but she is still told
> the system isn't sure about her own work. That's why the unsure label has to
> be written for her.

**What the label says to her.** Right now it's a placeholder. Whatever it
becomes, a high-confidence AI label tells her that her own work is suspected of
being fake, and the decision is wrong. Nothing in the response tells her *why*,
and nothing tells her what she can do about it.

**What she can do about it.** She can send her `content_id` and her reasons
to `POST /appeal`. Her item moves to `under_review`, and the original decision
stays in the log beside the appeal. That's all she can do. Nothing re-scores
her text, no person is assigned to review it, and she isn't told how long to
wait. She also has to know the appeal path exists, so the label itself has to
tell her.

**What this decides for Milestones 4 and 5:**

- Signal one can't separate plain human writing (0.86) from AI writing
  (0.89), so **it must never send text to the AI label on its own**. The
  combining rule should only reach "AI" when both signals point that way, and
  should treat a split as "unsure".
- The AI threshold has to sit **above where plain human writing lands**, using
  the calibration inputs from Milestone 4, not the 0.65 placeholder. Every
  point it moves down catches a little more AI text and accuses a few more
  writers like Amara.
- The AI label and the unsure label both have to **tell the reader they can
  appeal**, and how.

---

## Endpoint contract

Rules that apply to both endpoints:

- Requests and responses are JSON objects, sent with
  `Content-Type: application/json`.
- All scores are floats from 0 to 1, rounded to 4 places. **Higher always
  means more likely AI.**
- Every error has the same shape, `{"error": "<code>", "message": "<a sentence a
  person can read>"}`, and is written to the audit log with
  `audit.log_rejection`.
- Unknown request fields are ignored, not rejected.

### `POST /submit`

**Request**

| Field | Type | Required | Rules |
|---|---|---|---|
| `text` | string | yes | After trimming whitespace: at least **20 words**, at most **20,000 characters** |
| `creator_id` | string | yes | 1–64 characters, not blank. Identifies the writer, and the rate limiter counts against it in unit 8 |

Only the first ~300 words (400 tokens) reach signal one. Longer text is
accepted, but the model signal doesn't see anything after that point. Signal
two reads the whole text.

**Response — `200 OK`**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | A new UUID4 hex string, unique to this submission. The writer needs it to appeal |
| `creator_id` | string | Echoed from the request |
| `guess` | string | Exactly one of `"ai"`, `"unsure"`, `"human"` |
| `confidence` | float | **The combined score** from `combine_signals`. It is *not* "how sure we are of the guess". It's the same number as `combined_score` in the log. The unit 8 tools print this field as "Score" |
| `label` | string | The full sentence shown to the writer, from `score_to_label` |
| `model_score` | float | Signal one |
| `style_score` | float | Signal two |
| `status` | string | Always `"decided"` on a new submission |

```json
{
  "content_id": "3f9c2a7e5b1d4c8e9a0f6b2d7e1c4a95",
  "creator_id": "amara",
  "guess": "unsure",
  "confidence": 0.58,
  "label": "<the unsure label text>",
  "model_score": 0.8627,
  "style_score": 0.31,
  "status": "decided"
}
```

**Errors**

| Status | `error` | When |
|---|---|---|
| 400 | `invalid_json` | The body is missing, doesn't parse, or isn't a JSON object (for example a bare list) |
| 400 | `missing_text` | `text` is absent or `null` |
| 400 | `text_not_string` | `text` is a number, list or object |
| 400 | `text_too_short` | Fewer than 20 words after trimming, which includes empty text |
| 413 | `text_too_long` | More than 20,000 characters |
| 400 | `missing_creator_id` | `creator_id` is absent, blank or not a string |
| 429 | `rate_limited` | Unit 8. Shape already defined in `app.py`, plus a `limit` field |
| 503 | `detector_unavailable` | The model couldn't load. The request isn't scored and isn't logged as a decision |

Validation runs in the order of that table, and the first failure wins, so a
request with two problems gets one predictable error.

### `POST /appeal`

**Request**

| Field | Type | Required | Rules |
|---|---|---|---|
| `content_id` | string | yes | Must match a submission in the audit log |
| `reasoning` | string | yes | The writer's explanation. Not blank after trimming, at most 5,000 characters |

`creator_id` is **not** taken from the caller. The appeal is recorded against
the `creator_id` stored with the original decision.

**Response — `200 OK`**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | Echoed |
| `status` | string | Always `"under_review"` |
| `original_guess` | string | What the service decided, so the writer can see what they're appealing |
| `message` | string | A sentence confirming the appeal was received and what happens next |

```json
{
  "content_id": "3f9c2a7e5b1d4c8e9a0f6b2d7e1c4a95",
  "status": "under_review",
  "original_guess": "ai",
  "message": "Your appeal has been recorded. This piece is now marked as under review."
}
```

**Errors**

| Status | `error` | When |
|---|---|---|
| 400 | `invalid_json` | The body is missing, doesn't parse, or isn't a JSON object |
| 400 | `missing_content_id` | `content_id` is absent, blank or not a string |
| 400 | `missing_reasoning` | `reasoning` is absent, blank or not a string |
| 413 | `reasoning_too_long` | More than 5,000 characters |
| 404 | `unknown_content_id` | No submission with that id is in the log |
| 409 | `already_under_review` | This item has already been appealed. A second appeal is not logged again |

---

## Read back: could someone build against this without asking?

Mostly, yes. The questions a builder would still have to ask:

1. **Who may appeal?** There's no login, so anyone holding a `content_id` can
   appeal it. That's acceptable for this course, because the id is effectively
   the writer's receipt, but it should be a stated decision rather than an
   accident.
2. **Is `confidence` the right name?** A caller will read 0.58 as "58% sure",
   but it actually means "leans AI". The name stays because the unit 8 tools
   read it, and the definition above has to carry the meaning.
3. **Are the 20-word and 20,000-character limits right?** They're starting
   values. Milestone 4's calibration may show that short texts need a higher
   floor before either signal means anything.

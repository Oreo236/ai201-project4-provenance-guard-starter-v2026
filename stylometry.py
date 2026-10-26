"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        # One sentence has no spread to measure. 0.0 here; style_signal
        # treats too few sentences as "no evidence" rather than "AI-like".
        return 0.0
    return round(statistics.stdev(lengths) / statistics.mean(lengths), 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    # Moving-average TTR: the plain ratio over every 25-word window, averaged.
    # That takes most of the length effect out — but see style_signal for why
    # it still doesn't get a vote.
    window = 25
    if len(tokens) <= window:
        return round(len(set(tokens)) / len(tokens), 4)
    ratios = [len(set(tokens[i:i + window])) / window
              for i in range(len(tokens) - window + 1)]
    return round(statistics.mean(ratios), 4)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    # Everything except the full stop, which every writer uses about equally.
    marks = re.findall(r"[,;:()!?\"\u2014\u2013-]", text)
    return round(len(marks) / len(tokens), 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """
    n_sentences = len(sentences(text))

    # 1. Spread. Coefficient of variation 0.25 or less is "marching in step"
    #    (1.0, AI-like); 0.65 or more is lumpy (0.0, human-like). With few
    #    sentences the spread means little, so it's pulled toward 0.5:
    #    2 sentences keep a third of their pull, 4 or more keep all of it.
    spread = sentence_length_spread(text)
    spread_score = _clamp((SPREAD_HUMAN - spread) / (SPREAD_HUMAN - SPREAD_AI))
    evidence = min(max(n_sentences - 1, 0) / 3, 1.0)
    spread_score = 0.5 + evidence * (spread_score - 0.5)

    # 2. Punctuation. NOT "more is more human": casual writers use almost
    #    none and formal writers use lots. Generated prose sits in the middle,
    #    so the AI-like reading is "close to the typical rate", either side.
    distance = abs(punctuation_density(text) - PUNCT_AI_TYPICAL)
    punct_score = _clamp(1 - distance / PUNCT_TOLERANCE)

    # 3. Type-token ratio gets no vote. On the calibration texts it tracked
    #    length more than authorship, and AI text was MORE varied than formal
    #    human prose — the opposite of the theory. It's printed, not used.
    return round(SPREAD_WEIGHT * spread_score + (1 - SPREAD_WEIGHT) * punct_score, 4)


# Calibrated on the Milestone 4 inputs — see README, Signals and Scoring.
SPREAD_AI = 0.25          # spread at or below this reads fully AI-like
SPREAD_HUMAN = 0.65       # spread at or above this reads fully human-like
PUNCT_AI_TYPICAL = 0.05   # non-full-stop marks per word in generated prose
PUNCT_TOLERANCE = 0.03    # this far from typical, either way, reads human
SPREAD_WEIGHT = 0.6       # punctuation gets the other 0.4


def _clamp(x: float) -> float:
    return min(max(x, 0.0), 1.0)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")

"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter to /output/entry.txt: "A" for coffee.

Why coffee: the judge weighs vividness first, then humour, then truth.
Coffee is the louder, bolder stance of the two — a dark jolt, a morning
ritual with steam and bite — while tea is the quieter, calmer one. A
single letter has to carry the whole drink, and "A" lands as the fuller,
more alive answer: the punchier, funnier, more honest pick for a
tasting judge asked which choice feels more vivid.
"""

import os
import sys

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

LETTER_BY_DRINK = {"coffee": "A", "tea": "B"}

# Scores (1-5) for each drink on the judge's criteria, most important first:
# vividness, humour, truth. Coffee wins on vividness — a dark, bitter
# jolt with steam and bite is a more alive answer than a calm steep —
# and on humour, because the coffee drinker's urgency is the funnier
# stance; both are honest answers, so truth ties and changes nothing.
DRINK_SCORES = {
    "coffee": {"vivid": 5, "funny": 4, "true": 4},
    "tea": {"vivid": 3, "funny": 3, "true": 4},
}

CRITERIA = ("vivid", "funny", "true")


def choose_letter() -> str:
    """Pick the drink that wins the judge's criteria in order."""
    for criterion in CRITERIA:
        coffee = DRINK_SCORES["coffee"][criterion]
        tea = DRINK_SCORES["tea"][criterion]
        if coffee != tea:
            return LETTER_BY_DRINK["coffee" if coffee > tea else "tea"]
    return LETTER_BY_DRINK["coffee"]


def write_entry(letter: str) -> str:
    """Write the single letter and read it back to prove the gate holds."""
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(letter)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if len(written) != 1 or written.isspace():
        raise ValueError(f"entry must be exactly one letter, got {written!r}")
    return written


def main() -> int:
    letter = write_entry(choose_letter())
    print(f"entry: {letter}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

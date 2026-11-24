#!/usr/bin/env python3
"""Developer Excuses — write one funny single-line developer excuse.

Pure Python standard library only. Writes the excuse deterministically
to /output/entry.txt with no trailing newline.
"""

import os

EXCUSE = (
    "I didn't break production \u2014 I gave the rollback button its first "
    "real job interview, and it absolutely nailed it."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(EXCUSE) <= 200 or not EXCUSE.strip():
        raise ValueError("excuse must be 1-200 characters and not only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()

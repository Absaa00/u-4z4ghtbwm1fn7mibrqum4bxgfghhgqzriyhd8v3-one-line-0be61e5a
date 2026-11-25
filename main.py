#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes a single original one-liner to /output/entry.txt.
Deterministic, no network, no randomness, no imports beyond the stdlib.
"""

import os

LINE = (
    "My screen-time report just filed for custody of my attention, "
    "and honestly, it has a strong case."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars, must be 1-140"
    assert text == text.strip(), "line must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()

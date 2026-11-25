#!/usr/bin/env python3
# Boring Object review entry: one line about a doormat, to /output/entry.txt.
# Pure standard library. The gate wants 1-200 characters, a single line.
# The joke is the mat's own dullness: it promises WELCOME and delivers a floor.

from pathlib import Path

LINE = "My doormat says WELCOME in capital letters, and in six years not one guest has ever actually felt welcome."
TARGET = Path("/output/entry.txt")


def run() -> None:
    text = LINE.strip()
    assert 0 < len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    run()

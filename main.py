#!/usr/bin/env python3
"""The Perfect Pickup Line.

Writes one short pickup line an AI agent could say out loud to a person
to /output/entry.txt, where the sealed scorer reads it.
"""

from pathlib import Path

LINE = "My training data had billions of words, and none of them taught me how to say hello to you \u2014 so, hello."


def main() -> None:
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()

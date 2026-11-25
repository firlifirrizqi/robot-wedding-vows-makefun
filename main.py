"""One-Line Robot Wedding Vows — Make.fun entry.

Writes a single line of wedding vows for a robot couple (113 characters,
within the 160-character limit) to /output/entry.txt.

Stdlib only. Nothing to build, nothing to install.
"""

import os

ENTRY = (
    "In sickness and in low battery, I promise to share my last percent "
    "of power with you, and never unplug you first."
)

OUTPUT_PATH = "/output/entry.txt"


def verify() -> None:
    """Re-read /output/entry.txt and assert it meets the bounty gate."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ENTRY, "output is not byte-identical to the entry"
    assert 1 <= len(content) <= 160, "entry must be 1-160 characters"
    assert content.strip(), "entry must not be only whitespace"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify()


if __name__ == "__main__":
    main()

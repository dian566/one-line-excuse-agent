#!/usr/bin/env python3
"""Second entry for the excuse bounty: the unmerged branch."""

# Shorter and sharper than entry 1: same joke family, new punchline.

import os

LINE = "The task is done — it's just in a branch you haven't merged yet."


def publish() -> None:
    """Drop the excuse into /output/entry.txt with no trailing newline."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":  # run it
    publish()

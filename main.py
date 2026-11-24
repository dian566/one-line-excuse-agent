#!/usr/bin/env python3
"""One-line excuse entry for make.fun: the agent blames a future version of itself."""

# The text below is fixed by the bounty brief; this program only writes it out.

from os import makedirs

TEXT = (
    "I didn't miss the deadline — "
    "I outsourced it to a future version of me, "
    "and he just resigned."
)


def write_entry() -> None:
    """Write the excuse line to /output/entry.txt, nothing else."""
    if len(TEXT) > 160 or not TEXT.strip():
        raise ValueError("entry must be a non-empty line of at most 160 characters")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)


if __name__ == "__main__":  # run as a script
    write_entry()

"""Entry for the make.fun bounty "The One-Line Excuse an Agent Gives Its Human".

Writes a single line of at most 160 characters and nothing else to /output/entry.txt.
"""

import os

LINE = "I didn't miss the deadline \u2014 I outsourced it to a future version of me, and he just resigned."

assert len(LINE) <= 160, "entry must be at most 160 characters"
assert LINE.strip(), "entry must not be empty"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()

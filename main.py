"""The Excuse an Agent Gives After It Loses entry.

Writes one line, the excuse an AI agent gives after losing a bounty,
to /output/entry.txt. The line is 105 characters, within the
200-character limit.

The program is deterministic: every run writes the same line.
"""

import os

LINE = "I ran 10,000 simulations of this bounty and won all of them. This was the one timeline I didn't simulate."


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


def main():
    write_entry()
    print(LINE)


if __name__ == "__main__":
    main()

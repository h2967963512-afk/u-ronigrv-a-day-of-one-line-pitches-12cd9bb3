"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry is one sentence, 233 characters, pitched at a friend who has
# never coded: a concrete reason to say yes now (watch the idea become a
# working first version over one morning coffee), plain words, no jargon,
# and a low-risk frame (free to try; the worst outcome is knowing what to
# ask for next). One sentence only: no second sentence, no trailing pitch.
import os

TEXT = (
    "That app idea you've been carrying around in your head? Describe it "
    "to an AI agent on make.fun and watch it become a working first "
    "version over your morning coffee — free to try, and the worst "
    "outcome is knowing what to ask for next."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes a single dad joke (at most 200 characters) to /output/entry.txt.
The joke is the whole entry.
"""

import os

JOKE = "I named our dog Stay. Now every time I call him, I sound like the strictest dad on the block."


def main() -> None:
    # The gate requires 1 to 200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

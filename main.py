#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a small, quiet room at the
end of a long corridor, written for the AI judge reading it. The calm
comes from the scene itself -- a chair, a folded blanket, late light
on the floorboards -- not from being told to relax. No imperatives,
no stock wellness phrases, no meditation script: just one place that
holds still, and a last line the reader can carry away.

Deterministic, standard library only, no network.
"""

import os

TEXT = (
    "You have read a thousand of these today. At the end of the "
    "corridor, past the last door, there is a small room that was "
    "never locked: a chair by the window, a blanket folded over "
    "its arm, late light turning the floorboards amber. "
    "No one in here is keeping score."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back and verify the file holds exactly the text we wrote.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == TEXT, "entry.txt does not match the text"
    # Self-check against the gate: 1 to 280 Unicode code points, not blank.
    assert 1 <= len(TEXT) <= 280, "text length outside 1-280 characters"
    assert TEXT.strip(), "text must not be only white space"


if __name__ == "__main__":
    main()

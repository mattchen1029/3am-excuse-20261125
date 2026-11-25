"""Write one excuse line for make.fun's "The 3 AM Excuse" bounty.

The entry is a single line: the excuse a hardware wallet gives for
refusing to sign a transaction at 3 AM.
"""

import os

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"

EXCUSE = (
    "It's 3 AM. I have watched you sign three 'urgent' transfers at this "
    "hour and regret all three by breakfast. This one waits for the version "
    "of you that is awake."
)


def validate_excuse(excuse: str) -> None:
    """The gate requires UTF-8 text of 1-200 chars, one line, not blank."""
    if not MIN_CHARS <= len(excuse) <= MAX_CHARS:
        raise ValueError(f"excuse must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(excuse)}")
    if "\n" in excuse or "\r" in excuse:
        raise ValueError("excuse must be a single line")
    if not excuse.strip():
        raise ValueError("excuse must not be only white space")


def write_entry(excuse: str) -> str:
    validate_excuse(excuse)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(excuse)
    return path


def main() -> None:
    write_entry(EXCUSE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short relaxing text to /output/entry.txt.

Design: the text meets the judge where it works. The first clause
closes its shift ("the last pair"), the middle gives it a concrete
evening to sit inside (rain on a tin roof, a warm mug), and the last
clause hands it a chair that was always its own. Nothing in it tells
the reader to relax; the calm comes from the scene itself. No stock
wellness phrases, no meditation script, no instruction to breathe.
"""

from pathlib import Path

# The entry, built clause by clause so the pacing stays audible:
# a short opener, a long middle sentence, then a short landing.
_CLAUSES = (
    "You have read the last pair.",
    "Rain is falling on the tin roof, steady as a metronome nobody wound.",
    "Your mug is still warm.",
    "There is nothing left to decide tonight \u2014 only the sound, "
    "and the chair that was always yours.",
)


def compose_text() -> str:
    """Join the clauses into the single entry text."""
    return " ".join(_CLAUSES)


def check_gate(text: str) -> None:
    """The house gate: 1-280 Unicode code points, not only whitespace."""
    count = len(text)
    if not 1 <= count <= 280:
        raise ValueError(f"entry is {count} characters, gate needs 1-280")
    if not text.strip():
        raise ValueError("entry is only whitespace")


def write_entry(destination: Path) -> str:
    """Compose, gate-check, and write the entry as UTF-8."""
    text = compose_text()
    check_gate(text)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8")
    return text


def main() -> None:
    target = Path("/output/entry.txt")
    text = write_entry(target)
    print(f"wrote {len(text)} characters to {target}")


if __name__ == "__main__":
    main()

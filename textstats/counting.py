"""Compute immutable statistics from decoded text without performing IO.

Only CR, LF and CRLF terminate logical lines. Word boundaries follow Python's
Unicode whitespace rules; one leading BOM may be removed before counting.
"""

from dataclasses import dataclass
import re


@dataclass(frozen=True, slots=True)
class TextStats:
    """Immutable, nonnegative counts produced by a text counting operation.

    Attributes:
        lines: Number of logical lines, without a phantom trailing line.
        words: Number of whitespace-separated tokens.
    """

    lines: int
    words: int


def count_text(text: str, *, strip_bom: bool = True) -> TextStats:
    """Count logical lines and Unicode whitespace-separated words.

    Args:
        text: Decoded input string. Only CR, LF and CRLF terminate lines;
            other Unicode separators may divide words but do not divide lines.
        strip_bom: Remove exactly one leading U+FEFF when true. Interior BOMs,
            and all BOMs when false, remain ordinary non-whitespace characters.

    Returns:
        A new immutable result with nonnegative integer counts. Empty text
        after BOM handling has zero lines and words. A trailing terminator
        creates no extra line.

    This pure operation does not print, mutate input or acquire resources.
    Caller argument types outside the declared signature are not supported.
    """
    return _count_selected(text, None, strip_bom=strip_bom)


def _count_selected(
    text: str, line_range: tuple[int, int] | None, *, strip_bom: bool = True
) -> TextStats:
    """Count a decoded source after global BOM handling and optional selection.

    Endpoints are validated positive inclusive positions supplied by the CLI.
    This private source-independent seam accepts decoded files and stdin.
    Selected segments retain terminators; their exposed BOM is never stripped.
    """
    if strip_bom and text.startswith("\ufeff"):
        text = text[1:]
    if line_range is not None:
        start, end = line_range
        segments = re.finditer(r"[^\r\n]*(?:\r\n|\r|\n)|[^\r\n]+$", text)
        text = "".join(
            match.group() for position, match in enumerate(segments, 1)
            if start <= position <= end
        )

    # Subtract paired terminators so that CRLF counts once, not twice.
    lines = text.count("\r") + text.count("\n") - text.count("\r\n")
    if text and not text.endswith(("\r", "\n")):
        lines += 1
    return TextStats(lines=lines, words=len(text.split()))

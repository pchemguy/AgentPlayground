"""Read named UTF-8 files and delegate statistics to the pure counting core.

The file adapter owns each handle it opens; it does not print or translate
standard-library read and decoding exceptions into process outcomes.
"""

import os

from .counting import TextStats, _count_selected


def count_file(path: str | os.PathLike[str], *, strip_bom: bool = True) -> TextStats:
    """Read a complete UTF-8 file and return immutable text statistics.

    Args:
        path: Named file path, as a string or string-valued path-like object.
        strip_bom: Remove exactly one leading decoded BOM when true; false
            retains every BOM. The counting core owns this policy.

    Returns:
        Nonnegative line and word counts using count_text semantics.

    Raises:
        OSError: The named file cannot be opened or read.
        UnicodeDecodeError: File bytes are not valid UTF-8.

    The adapter opens and closes its own handle, including on failure. It
    leaves the file unchanged and produces no stdout or stderr output.
    """
    return _count_file_selected(path, None, strip_bom=strip_bom)


def _count_file_selected(
    path: str | os.PathLike[str], line_range: tuple[int, int] | None,
    *, strip_bom: bool = True,
) -> TextStats:
    """Strictly decode the entire owned file before private core selection.

    Owned handles close on success and all read/decode failures. Selection
    never skips validation of bytes outside its requested endpoints.
    """
    with open(path, "r", encoding="utf-8", newline="") as handle:
        text = handle.read()
    return _count_selected(text, line_range, strip_bom=strip_bom)

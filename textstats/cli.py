"""Present named-file and binary-stdin TextStats results through the module CLI.

Argument parsing, stdin acquisition and output belong here; the file adapter
owns named UTF-8 input and the core owns newline, word and BOM semantics.
"""

import argparse
import re
import sys
from collections.abc import Sequence

from .files import count_file, _count_file_selected
from .counting import _count_selected



def _parse_range(value: str) -> tuple[int, int]:
    """Validate positive ASCII-decimal endpoints without a digit-count limit."""
    if re.fullmatch(r"[0-9]+:[0-9]+", value) is None:
        raise argparse.ArgumentTypeError("expected positive inclusive START:END")
    def decimal(digits: str) -> int:
        # Small chunks avoid Python's string-to-integer digit safety limit.
        number = 0
        for offset in range(0, len(digits), 9):
            chunk = digits[offset:offset + 9]
            number = number * 10 ** len(chunk) + int(chunk)
        return number
    start, end = (decimal(part) for part in value.split(":"))
    if start == 0 or end == 0 or start > end:
        raise argparse.ArgumentTypeError("endpoints must satisfy 1 <= START <= END")
    return start, end


class _SingleRange(argparse.Action):
    """Reject repeated range options before any source is acquired."""

    def __call__(self, parser, namespace, values, option_string=None):
        if getattr(namespace, self.dest) is not None:
            parser.error("--lines may be specified only once")
        setattr(namespace, self.dest, values)


def main(argv: Sequence[str] | None = None) -> int:
    """Count one UTF-8 file or binary stdin and write exact plain output.

    Args:
        argv: Command-line arguments without the program name. None selects
            process arguments. Input - selects stdin. --keep-bom retains the
            leading decoded BOM;
            --lines START:END selects existing one-based inclusive lines.

    Returns:
        Zero after writing one lines/words record to stdout; one for read or
        UTF-8 decoding failure with a useful stderr diagnostic and no success
        output. Successful calls produce no stderr and never modify input.

    Raises:
        SystemExit: argparse handles help or invalid command-line arguments.

    The file adapter owns its handles. API read/decode exceptions are translated
    here without a traceback. Stdin is read completely as binary, strictly
    decoded as UTF-8 independent of locale, and never closed by this function.
    Selection follows decoding and global BOM handling, including failures
    outside the selected lines.
    """
    parser = argparse.ArgumentParser(
        prog="python -m textstats", description="Count lines and words in a UTF-8 file or stdin."
    )
    parser.add_argument("--keep-bom", action="store_true", help="retain the leading UTF-8 BOM")
    parser.add_argument("--lines", type=_parse_range, action=_SingleRange,
                        metavar="START:END",
                        help="select one-based inclusive lines; count the available subset at EOF")
    parser.add_argument("input", metavar="INPUT", help="named UTF-8 file, or - for binary UTF-8 stdin")
    arguments = parser.parse_args(argv)
    source = "stdin" if arguments.input == "-" else arguments.input
    try:
        if arguments.input == "-":
            chunks = []
            while chunk := sys.stdin.buffer.read(65536):
                chunks.append(chunk)
            text = b"".join(chunks).decode("utf-8", errors="strict")
            result = _count_selected(text, arguments.lines, strip_bom=not arguments.keep_bom)
        elif arguments.lines is None:
            result = count_file(arguments.input, strip_bom=not arguments.keep_bom)
        else:
            result = _count_file_selected(
                arguments.input, arguments.lines, strip_bom=not arguments.keep_bom
            )
    except (OSError, UnicodeDecodeError) as error:
        print(f"textstats: {source}: {error}", file=sys.stderr)
        return 1
    print(f"lines={result.lines} words={result.words}")
    return 0

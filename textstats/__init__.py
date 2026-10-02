"""Public text statistics API: TextStats, count_text and count_file."""

from .counting import TextStats, count_text
from .files import count_file

__all__ = ["TextStats", "count_text", "count_file"]

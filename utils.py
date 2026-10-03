"""Reusable helper functions for common text-processing tasks."""

from collections import Counter
import re
import unicodedata


def normalize_whitespace(text: str, *, preserve_newlines: bool = False) -> str:
    """Normalize whitespace and remove leading or trailing whitespace.

    Args:
        text: The text to normalize.
        preserve_newlines: Keep line boundaries while normalizing whitespace
            within each line. Blank lines are removed.

    Returns:
        The normalized text.
    """
    if preserve_newlines:
        lines = (" ".join(line.split()) for line in text.splitlines())
        return "\n".join(line for line in lines if line)
    return " ".join(text.split())


def truncate_text(text: str, max_length: int, *, suffix: str = "…") -> str:
    """Shorten text to a maximum length without splitting the suffix.

    Args:
        text: The text to shorten.
        max_length: Maximum length of the returned string.
        suffix: Text appended when truncation occurs.

    Returns:
        The original text if it fits, otherwise a truncated string ending with
        the suffix.

    Raises:
        ValueError: If ``max_length`` is negative or shorter than the suffix.
    """
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if len(text) <= max_length:
        return text
    if len(suffix) > max_length:
        raise ValueError("max_length must be at least the length of suffix")
    return text[: max_length - len(suffix)].rstrip() + suffix


def word_frequencies(
    text: str, *, case_sensitive: bool = False
) -> dict[str, int]:
    """Count words in text using Unicode-aware character matching.

    Words may contain internal apostrophes, such as in ``don't``. Leading and
    trailing underscores are excluded.

    Args:
        text: The text whose words will be counted.
        case_sensitive: Preserve case distinctions when true.

    Returns:
        A dictionary mapping each word to its occurrence count.
    """
    source = text if case_sensitive else text.casefold()
    words = re.findall(r"[^\W_]+(?:['’][^\W_]+)*", source, flags=re.UNICODE)
    return dict(Counter(words))


def slugify(text: str, *, separator: str = "-") -> str:
    """Convert text into a lowercase ASCII slug.

    Accented characters are transliterated where Unicode decomposition permits,
    punctuation is removed, and runs of non-alphanumeric characters are
    replaced by one separator.

    Args:
        text: The text to convert.
        separator: String placed between normalized word groups.

    Returns:
        A lowercase slug, or an empty string when no ASCII letters or digits
        remain.

    Raises:
        ValueError: If ``separator`` is empty or contains alphanumeric
            characters.
    """
    if not separator:
        raise ValueError("separator must not be empty")
    if any(character.isalnum() for character in separator):
        raise ValueError("separator must not contain alphanumeric characters")

    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii").lower()
    groups = re.findall(r"[a-z0-9]+", ascii_text)
    return separator.join(groups)
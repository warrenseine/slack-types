"""Lock the exhaustive type-hardening pass in scripts/build.py.

Real Slack payloads ship File dimension fields as integers and inline raw
strings where Block Kit text/title objects are expected. The build pass widens
those families across every generated module; these tests fail if a
regeneration ever drops the pass and reintroduces the narrow declarations.
"""

import re
from pathlib import Path

GENERATED_ROOT = Path(__file__).resolve().parent.parent / "python" / "slack_types"

_STR_ONLY_DIMENSION = re.compile(
    r"(?:thumb_(?:\d+|pdf|video)|original)_[wh]: str \| None = None"
)
_OBJECT_ONLY_TEXTLIKE = re.compile(
    r"^\s+(?:text|title): [A-Z][A-Za-z0-9]* \| None = None$", re.MULTILINE
)


def _offenders(pattern: re.Pattern[str]) -> list[str]:
    return [
        str(path.relative_to(GENERATED_ROOT))
        for path in GENERATED_ROOT.rglob("*.py")
        if pattern.search(path.read_text())
    ]


def test_no_str_only_file_dimension_fields() -> None:
    assert _offenders(_STR_ONLY_DIMENSION) == []


def test_no_object_only_block_kit_textlike_fields() -> None:
    assert _offenders(_OBJECT_ONLY_TEXTLIKE) == []

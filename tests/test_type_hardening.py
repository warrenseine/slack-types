"""Lock the exhaustive type-hardening pass in scripts/build.py.

Real Slack payloads ship File dimension fields as integers, inline raw strings
where Block Kit text/title objects are expected, and put booleans, epoch
integers or a list of linked messages in Slack List record cells. The build
pass widens those families across every generated module; these tests fail if a
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

_CLASS_BLOCK = re.compile(r"^class \w+\(BaseModel\):\n(?:(?: +.*)?\n)*", re.MULTILINE)
_CELL_MARKER = "    column_id: str | None = None\n"
_NARROW_CELL_VALUE = re.compile(
    r"^ +value: (?:bool \| )?str \| None = None$", re.MULTILINE
)
_OBJECT_ONLY_CELL_MESSAGE = re.compile(
    r"^ +message: [A-Z][A-Za-z0-9]* \| None = None$", re.MULTILINE
)


def _offenders(pattern: re.Pattern[str]) -> list[str]:
    return [
        str(path.relative_to(GENERATED_ROOT))
        for path in GENERATED_ROOT.rglob("*.py")
        if pattern.search(path.read_text())
    ]


def _cell_offenders(pattern: re.Pattern[str]) -> list[str]:
    """Offenders limited to Slack List cell classes, keyed off ``column_id``."""
    offenders = []
    for path in sorted(GENERATED_ROOT.rglob("*.py")):
        for block in _CLASS_BLOCK.finditer(path.read_text()):
            body = block.group(0)
            if _CELL_MARKER in body and pattern.search(body):
                offenders.append(str(path.relative_to(GENERATED_ROOT)))
                break
    return offenders


def test_no_str_only_file_dimension_fields() -> None:
    assert _offenders(_STR_ONLY_DIMENSION) == []


def test_no_object_only_block_kit_textlike_fields() -> None:
    assert _offenders(_OBJECT_ONLY_TEXTLIKE) == []


def test_no_narrow_list_record_cell_values() -> None:
    assert _cell_offenders(_NARROW_CELL_VALUE) == []


def test_no_object_only_list_record_cell_messages() -> None:
    assert _cell_offenders(_OBJECT_ONLY_CELL_MESSAGE) == []


def test_cell_guards_actually_match_the_narrow_declarations() -> None:
    """Guard the guards: a regex that matches nothing would pass vacuously."""
    assert _NARROW_CELL_VALUE.search("    value: str | None = None")
    assert _NARROW_CELL_VALUE.search("    value: bool | str | None = None")
    assert not _NARROW_CELL_VALUE.search("    value: bool | int | str | None = None")
    assert _OBJECT_ONLY_CELL_MESSAGE.search("    message: Message3 | None = None")
    assert not _OBJECT_ONLY_CELL_MESSAGE.search(
        "    message: List[Message3] | Message3 | None = None"
    )

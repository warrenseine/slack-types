"""Build all slack_types Python modules from java-slack-sdk JSON samples.

Pipeline per sample: JSON -> genson-inferred JSON Schema ->
datamodel-code-generator -> Pydantic v2 module. Pre-computing the schema is
orders of magnitude faster on deeply-nested Slack samples than letting
datamodel-code-generator infer directly.

Run via `uv run python scripts/build.py` (with the dev dependency group
synced: `uv sync --group dev`).
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

import genson

REPO = Path(__file__).resolve().parent.parent
JAVA_SDK = REPO / "java-slack-sdk"
JSON_ROOT = REPO / "json"
OUT_ROOT = REPO / "python" / "slack_types"

JAVA_SDK_REPO = "git@github.com:slackapi/java-slack-sdk.git"

# Map: source dir under java-slack-sdk/json-logs/samples/ -> local json/ dir.
COPY_MAP = {
    "audit": JSON_ROOT / "audit-api",
    "api": JSON_ROOT / "web-api",
    "events": JSON_ROOT / "events-api",
    "rtm": JSON_ROOT / "rtm-api",
    "scim": JSON_ROOT / "scim-api",
    "app-backend/dialogs": JSON_ROOT / "app-backend" / "dialogs",
    "app-backend/interactive-components": JSON_ROOT / "app-backend" / "interactive-components",
    "app-backend/slash-commands": JSON_ROOT / "app-backend" / "slash-commands",
    "app-backend/views": JSON_ROOT / "app-backend" / "views",
}

SUBSAMPLE_THRESHOLD_BYTES = 100 * 1024
SUBSAMPLE_ARRAY_LIMIT = 2


def ensure_java_sdk() -> None:
    if (JAVA_SDK / "pom.xml").exists():
        return
    subprocess.run(
        ["git", "clone", "--depth", "1", JAVA_SDK_REPO, str(JAVA_SDK)],
        check=True,
    )


def copy_samples() -> None:
    for src, dst in COPY_MAP.items():
        src_dir = JAVA_SDK / "json-logs" / "samples" / src
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src_dir, dst)

    # Slack's BlockActionPayload sample is missing `selected_options`.
    # Backfill from `selected_option` so the inferred schema has the field.
    block_action = JSON_ROOT / "app-backend" / "interactive-components" / "BlockActionPayload.json"
    data = json.loads(block_action.read_text())
    data["actions"][0]["selected_options"] = [data["actions"][0]["selected_option"]]
    block_action.write_text(json.dumps(data, indent=2))

    for sample in JSON_ROOT.rglob("*.json"):
        if sample.stat().st_size <= SUBSAMPLE_THRESHOLD_BYTES:
            continue
        trimmed = _truncate_arrays(json.loads(sample.read_text()), SUBSAMPLE_ARRAY_LIMIT)
        sample.write_text(json.dumps(trimmed))


def _truncate_arrays(value: Any, limit: int) -> Any:
    if isinstance(value, list):
        return [_truncate_arrays(v, limit) for v in value[:limit]]
    if isinstance(value, dict):
        return {k: _truncate_arrays(v, limit) for k, v in value.items()}
    return value


def snake_case(name: str) -> str:
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    s = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", s)
    return s.replace("-", "_").lower()


def title_case_dotted(name: str) -> str:
    return "".join(part[:1].upper() + part[1:] for part in name.split("."))


def generate_module(json_path: Path, root_class: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    builder = genson.SchemaBuilder()
    builder.add_object(json.loads(json_path.read_text()))
    schema = builder.to_schema()

    with tempfile.NamedTemporaryFile(
        "w", suffix=".schema.json", delete=False
    ) as tmp:
        json.dump(schema, tmp)
        schema_path = Path(tmp.name)
    try:
        print(f"  {root_class:<55s}  ({json_path.relative_to(REPO)})")
        subprocess.run(
            [
                "datamodel-codegen",
                "--input", str(schema_path),
                "--input-file-type", "jsonschema",
                "--output-model-type", "pydantic_v2.BaseModel",
                "--target-python-version", "3.12",
                "--no-use-standard-collections",
                "--use-union-operator",
                "--use-schema-description",
                "--force-optional",
                "--snake-case-field",
                "--class-name", root_class,
                "--output", str(out_path),
                "--disable-timestamp",
                "--disable-future-imports",
                "--formatters", "ruff-format",
                "--formatters", "ruff-check",
            ],
            check=True,
        )
    finally:
        schema_path.unlink(missing_ok=True)


def gen_dir(
    src: Path,
    out: Path,
    *,
    response_suffix: bool,
    dotted_to_class: bool,
) -> None:
    for json_file in sorted(src.glob("*.json")):
        stem = json_file.stem
        root = title_case_dotted(stem) if dotted_to_class else stem
        if response_suffix:
            root += "Response"
        generate_module(json_file, root, out / f"{snake_case(root)}.py")


def gen_scim() -> None:
    for version in ("v1", "v2"):
        scim_dir = JSON_ROOT / "scim-api" / version
        out_dir = OUT_ROOT / "scim_api" / version
        targets: list[tuple[Path, str]] = [
            (scim_dir / "Users.json", "UsersResponse"),
            (scim_dir / "Groups.json", "GroupsResponse"),
            (scim_dir / "ServiceProviderConfigs.json", "ServiceProviderConfigsResponse"),
            (scim_dir / "Users" / "00000000000.json", "UserResponse"),
            (scim_dir / "Groups" / "00000000000.json", "GroupResponse"),
        ]
        if version == "v2":
            targets.append((scim_dir / "ResourceTypes.json", "ResourceTypesResponse"))
        for json_file, class_name in targets:
            generate_module(json_file, class_name, out_dir / f"{snake_case(class_name)}.py")


def write_init_files() -> None:
    for path in OUT_ROOT.rglob("*"):
        if path.is_dir():
            (path / "__init__.py").touch()
    OUT_ROOT.joinpath("__init__.py").touch()


def main() -> int:
    ensure_java_sdk()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    copy_samples()

    print("Generating app_backend...")
    for sub in ("dialogs", "interactive-components", "slash-commands", "views"):
        gen_dir(
            JSON_ROOT / "app-backend" / sub,
            OUT_ROOT / "app_backend" / sub.replace("-", "_"),
            response_suffix=False,
            dotted_to_class=False,
        )

    print("Generating events_api...")
    gen_dir(JSON_ROOT / "events-api", OUT_ROOT / "events_api", response_suffix=False, dotted_to_class=False)

    print("Generating rtm_api...")
    gen_dir(JSON_ROOT / "rtm-api", OUT_ROOT / "rtm_api", response_suffix=False, dotted_to_class=False)

    print("Generating audit_api...")
    gen_dir(JSON_ROOT / "audit-api" / "v1", OUT_ROOT / "audit_api" / "v1", response_suffix=True, dotted_to_class=True)

    print("Generating scim_api...")
    gen_scim()

    print("Generating web_api...")
    gen_dir(JSON_ROOT / "web-api", OUT_ROOT / "web_api", response_suffix=True, dotted_to_class=True)

    write_init_files()
    return 0


if __name__ == "__main__":
    sys.exit(main())

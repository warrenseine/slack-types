"""Generate a Pydantic v2 module from a JSON sample.

Pipeline: JSON sample -> genson-inferred JSON Schema -> datamodel-codegen
-> Pydantic v2 module. Pre-computing the schema with genson is orders of
magnitude faster on deeply-nested Slack samples than letting
datamodel-codegen infer directly from the JSON.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--class-name", required=True)
    args = parser.parse_args()

    import genson

    with args.input.open() as f:
        data = json.load(f)
    builder = genson.SchemaBuilder()
    builder.add_object(data)
    schema = builder.to_schema()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", suffix=".schema.json", delete=False
    ) as tmp:
        json.dump(schema, tmp)
        schema_path = Path(tmp.name)

    try:
        result = subprocess.run(
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
                "--class-name", args.class_name,
                "--output", str(args.output),
                "--disable-timestamp",
                "--disable-future-imports",
                "--formatters", "ruff-format",
                "--formatters", "ruff-check",
            ],
        )
    finally:
        schema_path.unlink(missing_ok=True)

    return result.returncode


if __name__ == "__main__":
    sys.exit(main())

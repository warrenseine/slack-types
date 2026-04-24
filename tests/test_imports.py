"""Smoke test: every generated module imports cleanly."""

import importlib
import pkgutil

import slack_types


def test_all_submodules_import() -> None:
    failures: list[tuple[str, Exception]] = []
    for module_info in pkgutil.walk_packages(
        slack_types.__path__, prefix="slack_types."
    ):
        try:
            importlib.import_module(module_info.name)
        except Exception as exc:
            failures.append((module_info.name, exc))
    assert not failures, "\n".join(f"{m}: {e}" for m, e in failures)

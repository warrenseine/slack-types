# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = slack_lists_create_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Choice:
    value: Optional[str] = None
    label: Optional[str] = None
    color: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Choice':
        assert isinstance(obj, dict)
        value = from_union([from_str, from_none], obj.get("value"))
        label = from_union([from_str, from_none], obj.get("label"))
        color = from_union([from_str, from_none], obj.get("color"))
        return Choice(value, label, color)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_str, from_none], self.value)
        result["label"] = from_union([from_str, from_none], self.label)
        result["color"] = from_union([from_str, from_none], self.color)
        return result


@dataclass
class SchemaOptions:
    format: Optional[str] = None
    show_member_name: Optional[bool] = None
    choices: Optional[List[Choice]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SchemaOptions':
        assert isinstance(obj, dict)
        format = from_union([from_str, from_none], obj.get("format"))
        show_member_name = from_union([from_bool, from_none], obj.get("show_member_name"))
        choices = from_union([lambda x: from_list(Choice.from_dict, x), from_none], obj.get("choices"))
        return SchemaOptions(format, show_member_name, choices)

    def to_dict(self) -> dict:
        result: dict = {}
        result["format"] = from_union([from_str, from_none], self.format)
        result["show_member_name"] = from_union([from_bool, from_none], self.show_member_name)
        result["choices"] = from_union([lambda x: from_list(lambda x: to_class(Choice, x), x), from_none], self.choices)
        return result


@dataclass
class Schema:
    key: Optional[str] = None
    name: Optional[str] = None
    is_primary_column: Optional[bool] = None
    type: Optional[str] = None
    id: Optional[str] = None
    options: Optional[SchemaOptions] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Schema':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        name = from_union([from_str, from_none], obj.get("name"))
        is_primary_column = from_union([from_bool, from_none], obj.get("is_primary_column"))
        type = from_union([from_str, from_none], obj.get("type"))
        id = from_union([from_str, from_none], obj.get("id"))
        options = from_union([SchemaOptions.from_dict, from_none], obj.get("options"))
        return Schema(key, name, is_primary_column, type, id, options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["key"] = from_union([from_str, from_none], self.key)
        result["name"] = from_union([from_str, from_none], self.name)
        result["is_primary_column"] = from_union([from_bool, from_none], self.is_primary_column)
        result["type"] = from_union([from_str, from_none], self.type)
        result["id"] = from_union([from_str, from_none], self.id)
        result["options"] = from_union([lambda x: to_class(SchemaOptions, x), from_none], self.options)
        return result


@dataclass
class SubtaskSchemaOptions:
    format: Optional[str] = None
    show_member_name: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SubtaskSchemaOptions':
        assert isinstance(obj, dict)
        format = from_union([from_str, from_none], obj.get("format"))
        show_member_name = from_union([from_bool, from_none], obj.get("show_member_name"))
        return SubtaskSchemaOptions(format, show_member_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["format"] = from_union([from_str, from_none], self.format)
        result["show_member_name"] = from_union([from_bool, from_none], self.show_member_name)
        return result


@dataclass
class SubtaskSchema:
    key: Optional[str] = None
    name: Optional[str] = None
    is_primary_column: Optional[bool] = None
    type: Optional[str] = None
    id: Optional[str] = None
    options: Optional[SubtaskSchemaOptions] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SubtaskSchema':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        name = from_union([from_str, from_none], obj.get("name"))
        is_primary_column = from_union([from_bool, from_none], obj.get("is_primary_column"))
        type = from_union([from_str, from_none], obj.get("type"))
        id = from_union([from_str, from_none], obj.get("id"))
        options = from_union([SubtaskSchemaOptions.from_dict, from_none], obj.get("options"))
        return SubtaskSchema(key, name, is_primary_column, type, id, options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["key"] = from_union([from_str, from_none], self.key)
        result["name"] = from_union([from_str, from_none], self.name)
        result["is_primary_column"] = from_union([from_bool, from_none], self.is_primary_column)
        result["type"] = from_union([from_str, from_none], self.type)
        result["id"] = from_union([from_str, from_none], self.id)
        result["options"] = from_union([lambda x: to_class(SubtaskSchemaOptions, x), from_none], self.options)
        return result


@dataclass
class View:
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    is_locked: Optional[bool] = None
    position: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'View':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([from_str, from_none], obj.get("type"))
        is_locked = from_union([from_bool, from_none], obj.get("is_locked"))
        position = from_union([from_str, from_none], obj.get("position"))
        return View(id, name, type, is_locked, position)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["type"] = from_union([from_str, from_none], self.type)
        result["is_locked"] = from_union([from_bool, from_none], self.is_locked)
        result["position"] = from_union([from_str, from_none], self.position)
        return result


@dataclass
class ListMetadata:
    schema: Optional[List[Schema]] = None
    subtask_schema: Optional[List[SubtaskSchema]] = None
    views: Optional[List[View]] = None
    integrations: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ListMetadata':
        assert isinstance(obj, dict)
        schema = from_union([lambda x: from_list(Schema.from_dict, x), from_none], obj.get("schema"))
        subtask_schema = from_union([lambda x: from_list(SubtaskSchema.from_dict, x), from_none], obj.get("subtask_schema"))
        views = from_union([lambda x: from_list(View.from_dict, x), from_none], obj.get("views"))
        integrations = from_union([lambda x: from_list(from_str, x), from_none], obj.get("integrations"))
        return ListMetadata(schema, subtask_schema, views, integrations)

    def to_dict(self) -> dict:
        result: dict = {}
        result["schema"] = from_union([lambda x: from_list(lambda x: to_class(Schema, x), x), from_none], self.schema)
        result["subtask_schema"] = from_union([lambda x: from_list(lambda x: to_class(SubtaskSchema, x), x), from_none], self.subtask_schema)
        result["views"] = from_union([lambda x: from_list(lambda x: to_class(View, x), x), from_none], self.views)
        result["integrations"] = from_union([lambda x: from_list(from_str, x), from_none], self.integrations)
        return result


@dataclass
class SlackListsCreateResponse:
    ok: Optional[bool] = None
    list_id: Optional[str] = None
    list_metadata: Optional[ListMetadata] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SlackListsCreateResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        list_id = from_union([from_str, from_none], obj.get("list_id"))
        list_metadata = from_union([ListMetadata.from_dict, from_none], obj.get("list_metadata"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return SlackListsCreateResponse(ok, list_id, list_metadata, error, needed, provided, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["list_id"] = from_union([from_str, from_none], self.list_id)
        result["list_metadata"] = from_union([lambda x: to_class(ListMetadata, x), from_none], self.list_metadata)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def slack_lists_create_response_from_dict(s: Any) -> SlackListsCreateResponse:
    return SlackListsCreateResponse.from_dict(s)


def slack_lists_create_response_to_dict(x: SlackListsCreateResponse) -> Any:
    return to_class(SlackListsCreateResponse, x)

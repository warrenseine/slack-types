# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = slack_lists_items_list_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, Union, TypeVar, Callable, Type, cast


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


@dataclass
class ElementElementClass:
    text: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ElementElementClass':
        assert isinstance(obj, dict)
        text = from_union([from_str, from_none], obj.get("text"))
        type = from_union([from_str, from_none], obj.get("type"))
        return ElementElementClass(text, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([from_str, from_none], self.text)
        result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class RichTextElement:
    type: Optional[str] = None
    elements: Optional[List[ElementElementClass]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RichTextElement':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        elements = from_union([lambda x: from_list(ElementElementClass.from_dict, x), from_none], obj.get("elements"))
        return RichTextElement(type, elements)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(ElementElementClass, x), x), from_none], self.elements)
        return result


@dataclass
class RichText:
    type: Optional[str] = None
    block_id: Optional[str] = None
    elements: Optional[List[RichTextElement]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RichText':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        block_id = from_union([from_str, from_none], obj.get("block_id"))
        elements = from_union([lambda x: from_list(RichTextElement.from_dict, x), from_none], obj.get("elements"))
        return RichText(type, block_id, elements)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["block_id"] = from_union([from_str, from_none], self.block_id)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(RichTextElement, x), x), from_none], self.elements)
        return result


@dataclass
class Field:
    value: Union[bool, None, str]
    key: Optional[str] = None
    column_id: Optional[str] = None
    rich_text: Optional[List[RichText]] = None
    checkbox: Optional[bool] = None
    text: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Field':
        assert isinstance(obj, dict)
        value = from_union([from_bool, from_str, from_none], obj.get("value"))
        key = from_union([from_str, from_none], obj.get("key"))
        column_id = from_union([from_str, from_none], obj.get("column_id"))
        rich_text = from_union([lambda x: from_list(RichText.from_dict, x), from_none], obj.get("rich_text"))
        checkbox = from_union([from_bool, from_none], obj.get("checkbox"))
        text = from_union([from_str, from_none], obj.get("text"))
        return Field(value, key, column_id, rich_text, checkbox, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_bool, from_str, from_none], self.value)
        result["key"] = from_union([from_str, from_none], self.key)
        result["column_id"] = from_union([from_str, from_none], self.column_id)
        result["rich_text"] = from_union([lambda x: from_list(lambda x: to_class(RichText, x), x), from_none], self.rich_text)
        result["checkbox"] = from_union([from_bool, from_none], self.checkbox)
        result["text"] = from_union([from_str, from_none], self.text)
        return result


@dataclass
class Item:
    id: Optional[str] = None
    list_id: Optional[str] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    fields: Optional[List[Field]] = None
    updated_timestamp: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        list_id = from_union([from_str, from_none], obj.get("list_id"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        updated_by = from_union([from_str, from_none], obj.get("updated_by"))
        fields = from_union([lambda x: from_list(Field.from_dict, x), from_none], obj.get("fields"))
        updated_timestamp = from_union([from_str, from_none], obj.get("updated_timestamp"))
        return Item(id, list_id, date_created, created_by, updated_by, fields, updated_timestamp)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["list_id"] = from_union([from_str, from_none], self.list_id)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["created_by"] = from_union([from_str, from_none], self.created_by)
        result["updated_by"] = from_union([from_str, from_none], self.updated_by)
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(Field, x), x), from_none], self.fields)
        result["updated_timestamp"] = from_union([from_str, from_none], self.updated_timestamp)
        return result


@dataclass
class ResponseMetadata:
    next_cursor: Optional[str] = None
    messages: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        next_cursor = from_union([from_str, from_none], obj.get("next_cursor"))
        messages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("messages"))
        return ResponseMetadata(next_cursor, messages)

    def to_dict(self) -> dict:
        result: dict = {}
        result["next_cursor"] = from_union([from_str, from_none], self.next_cursor)
        result["messages"] = from_union([lambda x: from_list(from_str, x), from_none], self.messages)
        return result


@dataclass
class SlackListsItemsListResponse:
    ok: Optional[bool] = None
    items: Optional[List[Item]] = None
    response_metadata: Optional[ResponseMetadata] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SlackListsItemsListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        items = from_union([lambda x: from_list(Item.from_dict, x), from_none], obj.get("items"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return SlackListsItemsListResponse(ok, items, response_metadata, error, needed, provided, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["items"] = from_union([lambda x: from_list(lambda x: to_class(Item, x), x), from_none], self.items)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def slack_lists_items_list_response_from_dict(s: Any) -> SlackListsItemsListResponse:
    return SlackListsItemsListResponse.from_dict(s)


def slack_lists_items_list_response_to_dict(x: SlackListsItemsListResponse) -> Any:
    return to_class(SlackListsItemsListResponse, x)

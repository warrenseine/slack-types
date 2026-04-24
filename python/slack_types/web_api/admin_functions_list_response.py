# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_functions_list_response_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class PutParameter:
    type: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    is_required: Optional[bool] = None
    description: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PutParameter':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        name = from_union([from_str, from_none], obj.get("name"))
        title = from_union([from_str, from_none], obj.get("title"))
        is_required = from_union([from_bool, from_none], obj.get("is_required"))
        description = from_union([from_str, from_none], obj.get("description"))
        return PutParameter(type, name, title, is_required, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["name"] = from_union([from_str, from_none], self.name)
        result["title"] = from_union([from_str, from_none], self.title)
        result["is_required"] = from_union([from_bool, from_none], self.is_required)
        result["description"] = from_union([from_str, from_none], self.description)
        return result


@dataclass
class ProductLevelAvailability:
    is_available: Optional[bool] = None
    available_to: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ProductLevelAvailability':
        assert isinstance(obj, dict)
        is_available = from_union([from_bool, from_none], obj.get("is_available"))
        available_to = from_union([from_str, from_none], obj.get("available_to"))
        return ProductLevelAvailability(is_available, available_to)

    def to_dict(self) -> dict:
        result: dict = {}
        result["is_available"] = from_union([from_bool, from_none], self.is_available)
        result["available_to"] = from_union([from_str, from_none], self.available_to)
        return result


@dataclass
class Function:
    id: Optional[str] = None
    callback_id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    input_parameters: Optional[List[PutParameter]] = None
    output_parameters: Optional[List[PutParameter]] = None
    app_id: Optional[str] = None
    date_created: Optional[int] = None
    date_updated: Optional[int] = None
    date_deleted: Optional[int] = None
    form_enabled: Optional[bool] = None
    date_released: Optional[int] = None
    category_id: Optional[str] = None
    category_label: Optional[str] = None
    product_level_availability: Optional[ProductLevelAvailability] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Function':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        callback_id = from_union([from_str, from_none], obj.get("callback_id"))
        title = from_union([from_str, from_none], obj.get("title"))
        description = from_union([from_str, from_none], obj.get("description"))
        type = from_union([from_str, from_none], obj.get("type"))
        input_parameters = from_union([lambda x: from_list(PutParameter.from_dict, x), from_none], obj.get("input_parameters"))
        output_parameters = from_union([lambda x: from_list(PutParameter.from_dict, x), from_none], obj.get("output_parameters"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        date_updated = from_union([from_int, from_none], obj.get("date_updated"))
        date_deleted = from_union([from_int, from_none], obj.get("date_deleted"))
        form_enabled = from_union([from_bool, from_none], obj.get("form_enabled"))
        date_released = from_union([from_int, from_none], obj.get("date_released"))
        category_id = from_union([from_str, from_none], obj.get("category_id"))
        category_label = from_union([from_str, from_none], obj.get("category_label"))
        product_level_availability = from_union([ProductLevelAvailability.from_dict, from_none], obj.get("product_level_availability"))
        return Function(id, callback_id, title, description, type, input_parameters, output_parameters, app_id, date_created, date_updated, date_deleted, form_enabled, date_released, category_id, category_label, product_level_availability)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["callback_id"] = from_union([from_str, from_none], self.callback_id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["description"] = from_union([from_str, from_none], self.description)
        result["type"] = from_union([from_str, from_none], self.type)
        result["input_parameters"] = from_union([lambda x: from_list(lambda x: to_class(PutParameter, x), x), from_none], self.input_parameters)
        result["output_parameters"] = from_union([lambda x: from_list(lambda x: to_class(PutParameter, x), x), from_none], self.output_parameters)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["date_updated"] = from_union([from_int, from_none], self.date_updated)
        result["date_deleted"] = from_union([from_int, from_none], self.date_deleted)
        result["form_enabled"] = from_union([from_bool, from_none], self.form_enabled)
        result["date_released"] = from_union([from_int, from_none], self.date_released)
        result["category_id"] = from_union([from_str, from_none], self.category_id)
        result["category_label"] = from_union([from_str, from_none], self.category_label)
        result["product_level_availability"] = from_union([lambda x: to_class(ProductLevelAvailability, x), from_none], self.product_level_availability)
        return result


@dataclass
class ResponseMetadata:
    messages: Optional[List[str]] = None
    next_cursor: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        messages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("messages"))
        next_cursor = from_union([from_str, from_none], obj.get("next_cursor"))
        return ResponseMetadata(messages, next_cursor)

    def to_dict(self) -> dict:
        result: dict = {}
        result["messages"] = from_union([lambda x: from_list(from_str, x), from_none], self.messages)
        result["next_cursor"] = from_union([from_str, from_none], self.next_cursor)
        return result


@dataclass
class AdminFunctionsListResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    functions: Optional[List[Function]] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminFunctionsListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        functions = from_union([lambda x: from_list(Function.from_dict, x), from_none], obj.get("functions"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return AdminFunctionsListResponse(ok, error, response_metadata, needed, provided, functions, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["functions"] = from_union([lambda x: from_list(lambda x: to_class(Function, x), x), from_none], self.functions)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def admin_functions_list_response_from_dict(s: Any) -> AdminFunctionsListResponse:
    return AdminFunctionsListResponse.from_dict(s)


def admin_functions_list_response_to_dict(x: AdminFunctionsListResponse) -> Any:
    return to_class(AdminFunctionsListResponse, x)

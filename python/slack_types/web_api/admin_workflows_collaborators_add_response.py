# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_workflows_collaborators_add_response_from_dict(json.loads(json_string))

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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Error:
    message: Optional[str] = None
    user: Optional[str] = None
    workflow: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Error':
        assert isinstance(obj, dict)
        message = from_union([from_str, from_none], obj.get("message"))
        user = from_union([from_str, from_none], obj.get("user"))
        workflow = from_union([from_str, from_none], obj.get("workflow"))
        return Error(message, user, workflow)

    def to_dict(self) -> dict:
        result: dict = {}
        result["message"] = from_union([from_str, from_none], self.message)
        result["user"] = from_union([from_str, from_none], self.user)
        result["workflow"] = from_union([from_str, from_none], self.workflow)
        return result


@dataclass
class ResponseMetadata:
    messages: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        messages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("messages"))
        return ResponseMetadata(messages)

    def to_dict(self) -> dict:
        result: dict = {}
        result["messages"] = from_union([lambda x: from_list(from_str, x), from_none], self.messages)
        return result


@dataclass
class AdminWorkflowsCollaboratorsAddResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminWorkflowsCollaboratorsAddResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return AdminWorkflowsCollaboratorsAddResponse(ok, error, response_metadata, needed, provided, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        return result


def admin_workflows_collaborators_add_response_from_dict(s: Any) -> AdminWorkflowsCollaboratorsAddResponse:
    return AdminWorkflowsCollaboratorsAddResponse.from_dict(s)


def admin_workflows_collaborators_add_response_to_dict(x: AdminWorkflowsCollaboratorsAddResponse) -> Any:
    return to_class(AdminWorkflowsCollaboratorsAddResponse, x)

# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_workflows_collaborators_remove_response_from_dict(json.loads(json_string))

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
class Error:
    user: Optional[str] = None
    workflow: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Error':
        assert isinstance(obj, dict)
        user = from_union([from_str, from_none], obj.get("user"))
        workflow = from_union([from_str, from_none], obj.get("workflow"))
        message = from_union([from_str, from_none], obj.get("message"))
        return Error(user, workflow, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user"] = from_union([from_str, from_none], self.user)
        result["workflow"] = from_union([from_str, from_none], self.workflow)
        result["message"] = from_union([from_str, from_none], self.message)
        return result


@dataclass
class AdminWorkflowsCollaboratorsRemoveResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    errors: Optional[List[Error]] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminWorkflowsCollaboratorsRemoveResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AdminWorkflowsCollaboratorsRemoveResponse(ok, error, errors, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def admin_workflows_collaborators_remove_response_from_dict(s: Any) -> AdminWorkflowsCollaboratorsRemoveResponse:
    return AdminWorkflowsCollaboratorsRemoveResponse.from_dict(s)


def admin_workflows_collaborators_remove_response_to_dict(x: AdminWorkflowsCollaboratorsRemoveResponse) -> Any:
    return to_class(AdminWorkflowsCollaboratorsRemoveResponse, x)

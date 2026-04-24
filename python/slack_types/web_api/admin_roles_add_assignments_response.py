# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_roles_add_assignments_response_from_dict(json.loads(json_string))

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
class RejectedUser:
    id: Optional[str] = None
    error: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RejectedUser':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        error = from_union([from_str, from_none], obj.get("error"))
        return RejectedUser(id, error)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["error"] = from_union([from_str, from_none], self.error)
        return result


@dataclass
class AdminRolesAddAssignmentsResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    rejected_users: Optional[List[RejectedUser]] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminRolesAddAssignmentsResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        rejected_users = from_union([lambda x: from_list(RejectedUser.from_dict, x), from_none], obj.get("rejected_users"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AdminRolesAddAssignmentsResponse(ok, error, rejected_users, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["rejected_users"] = from_union([lambda x: from_list(lambda x: to_class(RejectedUser, x), x), from_none], self.rejected_users)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def admin_roles_add_assignments_response_from_dict(s: Any) -> AdminRolesAddAssignmentsResponse:
    return AdminRolesAddAssignmentsResponse.from_dict(s)


def admin_roles_add_assignments_response_to_dict(x: AdminRolesAddAssignmentsResponse) -> Any:
    return to_class(AdminRolesAddAssignmentsResponse, x)

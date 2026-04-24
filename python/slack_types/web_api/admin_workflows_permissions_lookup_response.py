# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_workflows_permissions_lookup_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, Dict, TypeVar, Callable, Type, cast


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


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


@dataclass
class WhoCanRun:
    permission_type: Optional[str] = None
    user_ids: Optional[List[str]] = None
    channel_ids: Optional[List[str]] = None
    team_ids: Optional[List[str]] = None
    org_ids: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'WhoCanRun':
        assert isinstance(obj, dict)
        permission_type = from_union([from_str, from_none], obj.get("permission_type"))
        user_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("user_ids"))
        channel_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channel_ids"))
        team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("team_ids"))
        org_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("org_ids"))
        return WhoCanRun(permission_type, user_ids, channel_ids, team_ids, org_ids)

    def to_dict(self) -> dict:
        result: dict = {}
        result["permission_type"] = from_union([from_str, from_none], self.permission_type)
        result["user_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.user_ids)
        result["channel_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.channel_ids)
        result["team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.team_ids)
        result["org_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.org_ids)
        return result


@dataclass
class Permission:
    complete: Optional[bool] = None
    who_can_run: Optional[WhoCanRun] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Permission':
        assert isinstance(obj, dict)
        complete = from_union([from_bool, from_none], obj.get("complete"))
        who_can_run = from_union([WhoCanRun.from_dict, from_none], obj.get("who_can_run"))
        return Permission(complete, who_can_run)

    def to_dict(self) -> dict:
        result: dict = {}
        result["complete"] = from_union([from_bool, from_none], self.complete)
        result["who_can_run"] = from_union([lambda x: to_class(WhoCanRun, x), from_none], self.who_can_run)
        return result


@dataclass
class AdminWorkflowsPermissionsLookupResponse:
    ok: Optional[bool] = None
    permissions: Optional[Dict[str, Permission]] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminWorkflowsPermissionsLookupResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        permissions = from_union([lambda x: from_dict(Permission.from_dict, x), from_none], obj.get("permissions"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AdminWorkflowsPermissionsLookupResponse(ok, permissions, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["permissions"] = from_union([lambda x: from_dict(lambda x: to_class(Permission, x), x), from_none], self.permissions)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def admin_workflows_permissions_lookup_response_from_dict(s: Any) -> AdminWorkflowsPermissionsLookupResponse:
    return AdminWorkflowsPermissionsLookupResponse.from_dict(s)


def admin_workflows_permissions_lookup_response_to_dict(x: AdminWorkflowsPermissionsLookupResponse) -> Any:
    return to_class(AdminWorkflowsPermissionsLookupResponse, x)

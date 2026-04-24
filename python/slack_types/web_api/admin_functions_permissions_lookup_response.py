# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_functions_permissions_lookup_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, Optional, List, Dict, TypeVar, Callable, Type, cast


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


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


@dataclass
class Errors:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'Errors':
        assert isinstance(obj, dict)
        return Errors()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class AllowedByAdmin:
    type: Optional[str] = None
    user_ids: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AllowedByAdmin':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("user_ids"))
        return AllowedByAdmin(type, user_ids)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.user_ids)
        return result


@dataclass
class AllowedEntities:
    type: Optional[str] = None
    user_ids: Optional[List[str]] = None
    team_ids: Optional[List[str]] = None
    org_ids: Optional[List[str]] = None
    channel_ids: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AllowedEntities':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("user_ids"))
        team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("team_ids"))
        org_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("org_ids"))
        channel_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channel_ids"))
        return AllowedEntities(type, user_ids, team_ids, org_ids, channel_ids)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.user_ids)
        result["team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.team_ids)
        result["org_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.org_ids)
        result["channel_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.channel_ids)
        return result


@dataclass
class Permission:
    distribution: Optional[AllowedByAdmin] = None
    allowed_entities: Optional[AllowedEntities] = None
    allowed_by_admin: Optional[AllowedByAdmin] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Permission':
        assert isinstance(obj, dict)
        distribution = from_union([AllowedByAdmin.from_dict, from_none], obj.get("distribution"))
        allowed_entities = from_union([AllowedEntities.from_dict, from_none], obj.get("allowed_entities"))
        allowed_by_admin = from_union([AllowedByAdmin.from_dict, from_none], obj.get("allowed_by_admin"))
        return Permission(distribution, allowed_entities, allowed_by_admin)

    def to_dict(self) -> dict:
        result: dict = {}
        result["distribution"] = from_union([lambda x: to_class(AllowedByAdmin, x), from_none], self.distribution)
        result["allowed_entities"] = from_union([lambda x: to_class(AllowedEntities, x), from_none], self.allowed_entities)
        result["allowed_by_admin"] = from_union([lambda x: to_class(AllowedByAdmin, x), from_none], self.allowed_by_admin)
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
class AdminFunctionsPermissionsLookupResponse:
    ok: Optional[bool] = None
    permissions: Optional[Dict[str, Permission]] = None
    errors: Optional[Errors] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    metadata: Optional[Dict[str, Errors]] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminFunctionsPermissionsLookupResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        permissions = from_union([lambda x: from_dict(Permission.from_dict, x), from_none], obj.get("permissions"))
        errors = from_union([Errors.from_dict, from_none], obj.get("errors"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        metadata = from_union([lambda x: from_dict(Errors.from_dict, x), from_none], obj.get("metadata"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return AdminFunctionsPermissionsLookupResponse(ok, permissions, errors, error, needed, provided, response_metadata, metadata, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["permissions"] = from_union([lambda x: from_dict(lambda x: to_class(Permission, x), x), from_none], self.permissions)
        result["errors"] = from_union([lambda x: to_class(Errors, x), from_none], self.errors)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["metadata"] = from_union([lambda x: from_dict(lambda x: to_class(Errors, x), x), from_none], self.metadata)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def admin_functions_permissions_lookup_response_from_dict(s: Any) -> AdminFunctionsPermissionsLookupResponse:
    return AdminFunctionsPermissionsLookupResponse.from_dict(s)


def admin_functions_permissions_lookup_response_to_dict(x: AdminFunctionsPermissionsLookupResponse) -> Any:
    return to_class(AdminFunctionsPermissionsLookupResponse, x)

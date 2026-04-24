# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_users_list_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


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
class User:
    id: Optional[str] = None
    email: Optional[str] = None
    is_admin: Optional[bool] = None
    is_owner: Optional[bool] = None
    is_primary_owner: Optional[bool] = None
    is_restricted: Optional[bool] = None
    is_ultra_restricted: Optional[bool] = None
    is_bot: Optional[bool] = None
    expiration_ts: Optional[int] = None
    username: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    date_created: Optional[int] = None
    roles: Optional[List[str]] = None
    workspaces: Optional[List[str]] = None
    has_2_fa: Optional[bool] = None
    has_sso: Optional[bool] = None
    last_active_ts: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        email = from_union([from_str, from_none], obj.get("email"))
        is_admin = from_union([from_bool, from_none], obj.get("is_admin"))
        is_owner = from_union([from_bool, from_none], obj.get("is_owner"))
        is_primary_owner = from_union([from_bool, from_none], obj.get("is_primary_owner"))
        is_restricted = from_union([from_bool, from_none], obj.get("is_restricted"))
        is_ultra_restricted = from_union([from_bool, from_none], obj.get("is_ultra_restricted"))
        is_bot = from_union([from_bool, from_none], obj.get("is_bot"))
        expiration_ts = from_union([from_int, from_none], obj.get("expiration_ts"))
        username = from_union([from_str, from_none], obj.get("username"))
        full_name = from_union([from_str, from_none], obj.get("full_name"))
        is_active = from_union([from_bool, from_none], obj.get("is_active"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        roles = from_union([lambda x: from_list(from_str, x), from_none], obj.get("roles"))
        workspaces = from_union([lambda x: from_list(from_str, x), from_none], obj.get("workspaces"))
        has_2_fa = from_union([from_bool, from_none], obj.get("has_2fa"))
        has_sso = from_union([from_bool, from_none], obj.get("has_sso"))
        last_active_ts = from_union([from_int, from_none], obj.get("last_active_ts"))
        return User(id, email, is_admin, is_owner, is_primary_owner, is_restricted, is_ultra_restricted, is_bot, expiration_ts, username, full_name, is_active, date_created, roles, workspaces, has_2_fa, has_sso, last_active_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["email"] = from_union([from_str, from_none], self.email)
        result["is_admin"] = from_union([from_bool, from_none], self.is_admin)
        result["is_owner"] = from_union([from_bool, from_none], self.is_owner)
        result["is_primary_owner"] = from_union([from_bool, from_none], self.is_primary_owner)
        result["is_restricted"] = from_union([from_bool, from_none], self.is_restricted)
        result["is_ultra_restricted"] = from_union([from_bool, from_none], self.is_ultra_restricted)
        result["is_bot"] = from_union([from_bool, from_none], self.is_bot)
        result["expiration_ts"] = from_union([from_int, from_none], self.expiration_ts)
        result["username"] = from_union([from_str, from_none], self.username)
        result["full_name"] = from_union([from_str, from_none], self.full_name)
        result["is_active"] = from_union([from_bool, from_none], self.is_active)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["roles"] = from_union([lambda x: from_list(from_str, x), from_none], self.roles)
        result["workspaces"] = from_union([lambda x: from_list(from_str, x), from_none], self.workspaces)
        result["has_2fa"] = from_union([from_bool, from_none], self.has_2_fa)
        result["has_sso"] = from_union([from_bool, from_none], self.has_sso)
        result["last_active_ts"] = from_union([from_int, from_none], self.last_active_ts)
        return result


@dataclass
class AdminUsersListResponse:
    ok: Optional[bool] = None
    users: Optional[List[User]] = None
    response_metadata: Optional[ResponseMetadata] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminUsersListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        users = from_union([lambda x: from_list(User.from_dict, x), from_none], obj.get("users"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return AdminUsersListResponse(ok, users, response_metadata, error, needed, provided, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["users"] = from_union([lambda x: from_list(lambda x: to_class(User, x), x), from_none], self.users)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def admin_users_list_response_from_dict(s: Any) -> AdminUsersListResponse:
    return AdminUsersListResponse.from_dict(s)


def admin_users_list_response_to_dict(x: AdminUsersListResponse) -> Any:
    return to_class(AdminUsersListResponse, x)

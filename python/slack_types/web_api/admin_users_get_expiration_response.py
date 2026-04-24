# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_users_get_expiration_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class User:
    id: Optional[str] = None
    email: Optional[str] = None
    is_restricted: Optional[bool] = None
    is_ultra_restricted: Optional[bool] = None
    expiration_ts: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        email = from_union([from_str, from_none], obj.get("email"))
        is_restricted = from_union([from_bool, from_none], obj.get("is_restricted"))
        is_ultra_restricted = from_union([from_bool, from_none], obj.get("is_ultra_restricted"))
        expiration_ts = from_union([from_int, from_none], obj.get("expiration_ts"))
        return User(id, email, is_restricted, is_ultra_restricted, expiration_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["email"] = from_union([from_str, from_none], self.email)
        result["is_restricted"] = from_union([from_bool, from_none], self.is_restricted)
        result["is_ultra_restricted"] = from_union([from_bool, from_none], self.is_ultra_restricted)
        result["expiration_ts"] = from_union([from_int, from_none], self.expiration_ts)
        return result


@dataclass
class AdminUsersGetExpirationResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    user: Optional[User] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminUsersGetExpirationResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        return AdminUsersGetExpirationResponse(ok, error, needed, provided, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        return result


def admin_users_get_expiration_response_from_dict(s: Any) -> AdminUsersGetExpirationResponse:
    return AdminUsersGetExpirationResponse.from_dict(s)


def admin_users_get_expiration_response_to_dict(x: AdminUsersGetExpirationResponse) -> Any:
    return to_class(AdminUsersGetExpirationResponse, x)

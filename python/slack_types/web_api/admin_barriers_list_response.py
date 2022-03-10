# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_barriers_list_response_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


@dataclass
class Usergroup:
    id: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Usergroup':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return Usergroup(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class Barrier:
    id: Optional[str] = None
    enterprise_id: Optional[str] = None
    primary_usergroup: Optional[Usergroup] = None
    barriered_from_usergroups: Optional[List[Usergroup]] = None
    restricted_subjects: Optional[List[str]] = None
    date_update: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Barrier':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        primary_usergroup = from_union([Usergroup.from_dict, from_none], obj.get("primary_usergroup"))
        barriered_from_usergroups = from_union([lambda x: from_list(Usergroup.from_dict, x), from_none], obj.get("barriered_from_usergroups"))
        restricted_subjects = from_union([lambda x: from_list(from_str, x), from_none], obj.get("restricted_subjects"))
        date_update = from_union([from_int, from_none], obj.get("date_update"))
        return Barrier(id, enterprise_id, primary_usergroup, barriered_from_usergroups, restricted_subjects, date_update)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["primary_usergroup"] = from_union([lambda x: to_class(Usergroup, x), from_none], self.primary_usergroup)
        result["barriered_from_usergroups"] = from_union([lambda x: from_list(lambda x: to_class(Usergroup, x), x), from_none], self.barriered_from_usergroups)
        result["restricted_subjects"] = from_union([lambda x: from_list(from_str, x), from_none], self.restricted_subjects)
        result["date_update"] = from_union([from_int, from_none], self.date_update)
        return result


@dataclass
class AdminBarriersListResponse:
    ok: Optional[bool] = None
    barriers: Optional[List[Barrier]] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminBarriersListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        barriers = from_union([lambda x: from_list(Barrier.from_dict, x), from_none], obj.get("barriers"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AdminBarriersListResponse(ok, barriers, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["barriers"] = from_union([lambda x: from_list(lambda x: to_class(Barrier, x), x), from_none], self.barriers)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def admin_barriers_list_response_from_dict(s: Any) -> AdminBarriersListResponse:
    return AdminBarriersListResponse.from_dict(s)


def admin_barriers_list_response_to_dict(x: AdminBarriersListResponse) -> Any:
    return to_class(AdminBarriersListResponse, x)
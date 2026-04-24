# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = team_profile_get_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Options:
    is_scim: Optional[bool] = None
    is_protected: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Options':
        assert isinstance(obj, dict)
        is_scim = from_union([from_bool, from_none], obj.get("is_scim"))
        is_protected = from_union([from_bool, from_none], obj.get("is_protected"))
        return Options(is_scim, is_protected)

    def to_dict(self) -> dict:
        result: dict = {}
        result["is_scim"] = from_union([from_bool, from_none], self.is_scim)
        result["is_protected"] = from_union([from_bool, from_none], self.is_protected)
        return result


@dataclass
class Permissions:
    api: Optional[List[str]] = None
    ui: Optional[bool] = None
    scim: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Permissions':
        assert isinstance(obj, dict)
        api = from_union([lambda x: from_list(from_str, x), from_none], obj.get("api"))
        ui = from_union([from_bool, from_none], obj.get("ui"))
        scim = from_union([from_bool, from_none], obj.get("scim"))
        return Permissions(api, ui, scim)

    def to_dict(self) -> dict:
        result: dict = {}
        result["api"] = from_union([lambda x: from_list(from_str, x), from_none], self.api)
        result["ui"] = from_union([from_bool, from_none], self.ui)
        result["scim"] = from_union([from_bool, from_none], self.scim)
        return result


@dataclass
class Field:
    id: Optional[str] = None
    ordering: Optional[int] = None
    field_name: Optional[str] = None
    label: Optional[str] = None
    hint: Optional[str] = None
    type: Optional[str] = None
    is_hidden: Optional[bool] = None
    options: Optional[Options] = None
    section_id: Optional[str] = None
    permissions: Optional[Permissions] = None
    is_inverse: Optional[bool] = None
    possible_values: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Field':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        ordering = from_union([from_int, from_none], obj.get("ordering"))
        field_name = from_union([from_str, from_none], obj.get("field_name"))
        label = from_union([from_str, from_none], obj.get("label"))
        hint = from_union([from_str, from_none], obj.get("hint"))
        type = from_union([from_str, from_none], obj.get("type"))
        is_hidden = from_union([from_bool, from_none], obj.get("is_hidden"))
        options = from_union([Options.from_dict, from_none], obj.get("options"))
        section_id = from_union([from_str, from_none], obj.get("section_id"))
        permissions = from_union([Permissions.from_dict, from_none], obj.get("permissions"))
        is_inverse = from_union([from_bool, from_none], obj.get("is_inverse"))
        possible_values = from_union([lambda x: from_list(from_str, x), from_none], obj.get("possible_values"))
        return Field(id, ordering, field_name, label, hint, type, is_hidden, options, section_id, permissions, is_inverse, possible_values)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["ordering"] = from_union([from_int, from_none], self.ordering)
        result["field_name"] = from_union([from_str, from_none], self.field_name)
        result["label"] = from_union([from_str, from_none], self.label)
        result["hint"] = from_union([from_str, from_none], self.hint)
        result["type"] = from_union([from_str, from_none], self.type)
        result["is_hidden"] = from_union([from_bool, from_none], self.is_hidden)
        result["options"] = from_union([lambda x: to_class(Options, x), from_none], self.options)
        result["section_id"] = from_union([from_str, from_none], self.section_id)
        result["permissions"] = from_union([lambda x: to_class(Permissions, x), from_none], self.permissions)
        result["is_inverse"] = from_union([from_bool, from_none], self.is_inverse)
        result["possible_values"] = from_union([lambda x: from_list(from_str, x), from_none], self.possible_values)
        return result


@dataclass
class Section:
    id: Optional[str] = None
    team_id: Optional[str] = None
    section_type: Optional[str] = None
    label: Optional[str] = None
    order: Optional[int] = None
    is_hidden: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Section':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        section_type = from_union([from_str, from_none], obj.get("section_type"))
        label = from_union([from_str, from_none], obj.get("label"))
        order = from_union([from_int, from_none], obj.get("order"))
        is_hidden = from_union([from_bool, from_none], obj.get("is_hidden"))
        return Section(id, team_id, section_type, label, order, is_hidden)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["section_type"] = from_union([from_str, from_none], self.section_type)
        result["label"] = from_union([from_str, from_none], self.label)
        result["order"] = from_union([from_int, from_none], self.order)
        result["is_hidden"] = from_union([from_bool, from_none], self.is_hidden)
        return result


@dataclass
class Profile:
    fields: Optional[List[Field]] = None
    sections: Optional[List[Section]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        assert isinstance(obj, dict)
        fields = from_union([lambda x: from_list(Field.from_dict, x), from_none], obj.get("fields"))
        sections = from_union([lambda x: from_list(Section.from_dict, x), from_none], obj.get("sections"))
        return Profile(fields, sections)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(Field, x), x), from_none], self.fields)
        result["sections"] = from_union([lambda x: from_list(lambda x: to_class(Section, x), x), from_none], self.sections)
        return result


@dataclass
class TeamProfileGetResponse:
    ok: Optional[bool] = None
    profile: Optional[Profile] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TeamProfileGetResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        profile = from_union([Profile.from_dict, from_none], obj.get("profile"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return TeamProfileGetResponse(ok, profile, error, needed, provided, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["profile"] = from_union([lambda x: to_class(Profile, x), from_none], self.profile)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def team_profile_get_response_from_dict(s: Any) -> TeamProfileGetResponse:
    return TeamProfileGetResponse.from_dict(s)


def team_profile_get_response_to_dict(x: TeamProfileGetResponse) -> Any:
    return to_class(TeamProfileGetResponse, x)

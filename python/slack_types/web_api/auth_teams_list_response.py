# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = auth_teams_list_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class ResponseMetadata:
    next_cursor: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        next_cursor = from_union([from_str, from_none], obj.get("next_cursor"))
        return ResponseMetadata(next_cursor)

    def to_dict(self) -> dict:
        result: dict = {}
        result["next_cursor"] = from_union([from_str, from_none], self.next_cursor)
        return result


@dataclass
class Icon:
    image_default: Optional[bool] = None
    image_34: Optional[str] = None
    image_44: Optional[str] = None
    image_68: Optional[str] = None
    image_88: Optional[str] = None
    image_102: Optional[str] = None
    image_230: Optional[str] = None
    image_132: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Icon':
        assert isinstance(obj, dict)
        image_default = from_union([from_bool, from_none], obj.get("image_default"))
        image_34 = from_union([from_str, from_none], obj.get("image_34"))
        image_44 = from_union([from_str, from_none], obj.get("image_44"))
        image_68 = from_union([from_str, from_none], obj.get("image_68"))
        image_88 = from_union([from_str, from_none], obj.get("image_88"))
        image_102 = from_union([from_str, from_none], obj.get("image_102"))
        image_230 = from_union([from_str, from_none], obj.get("image_230"))
        image_132 = from_union([from_str, from_none], obj.get("image_132"))
        return Icon(image_default, image_34, image_44, image_68, image_88, image_102, image_230, image_132)

    def to_dict(self) -> dict:
        result: dict = {}
        result["image_default"] = from_union([from_bool, from_none], self.image_default)
        result["image_34"] = from_union([from_str, from_none], self.image_34)
        result["image_44"] = from_union([from_str, from_none], self.image_44)
        result["image_68"] = from_union([from_str, from_none], self.image_68)
        result["image_88"] = from_union([from_str, from_none], self.image_88)
        result["image_102"] = from_union([from_str, from_none], self.image_102)
        result["image_230"] = from_union([from_str, from_none], self.image_230)
        result["image_132"] = from_union([from_str, from_none], self.image_132)
        return result


@dataclass
class Team:
    id: Optional[str] = None
    name: Optional[str] = None
    icon: Optional[Icon] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Team':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        icon = from_union([Icon.from_dict, from_none], obj.get("icon"))
        return Team(id, name, icon)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["icon"] = from_union([lambda x: to_class(Icon, x), from_none], self.icon)
        return result


@dataclass
class AuthTeamsListResponse:
    ok: Optional[bool] = None
    teams: Optional[List[Team]] = None
    error: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AuthTeamsListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        teams = from_union([lambda x: from_list(Team.from_dict, x), from_none], obj.get("teams"))
        error = from_union([from_str, from_none], obj.get("error"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return AuthTeamsListResponse(ok, teams, error, response_metadata, needed, provided, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["teams"] = from_union([lambda x: from_list(lambda x: to_class(Team, x), x), from_none], self.teams)
        result["error"] = from_union([from_str, from_none], self.error)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def auth_teams_list_response_from_dict(s: Any) -> AuthTeamsListResponse:
    return AuthTeamsListResponse.from_dict(s)


def auth_teams_list_response_to_dict(x: AuthTeamsListResponse) -> Any:
    return to_class(AuthTeamsListResponse, x)

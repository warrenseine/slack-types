# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_teams_list_response_from_dict(json.loads(json_string))

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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


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
class PrimaryOwner:
    user_id: Optional[str] = None
    email: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PrimaryOwner':
        assert isinstance(obj, dict)
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        email = from_union([from_str, from_none], obj.get("email"))
        return PrimaryOwner(user_id, email)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["email"] = from_union([from_str, from_none], self.email)
        return result


@dataclass
class Team:
    id: Optional[str] = None
    name: Optional[str] = None
    discoverability: Optional[str] = None
    primary_owner: Optional[PrimaryOwner] = None
    team_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Team':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        discoverability = from_union([from_str, from_none], obj.get("discoverability"))
        primary_owner = from_union([PrimaryOwner.from_dict, from_none], obj.get("primary_owner"))
        team_url = from_union([from_str, from_none], obj.get("team_url"))
        return Team(id, name, discoverability, primary_owner, team_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["discoverability"] = from_union([from_str, from_none], self.discoverability)
        result["primary_owner"] = from_union([lambda x: to_class(PrimaryOwner, x), from_none], self.primary_owner)
        result["team_url"] = from_union([from_str, from_none], self.team_url)
        return result


@dataclass
class AdminTeamsListResponse:
    ok: Optional[bool] = None
    teams: Optional[List[Team]] = None
    response_metadata: Optional[ResponseMetadata] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminTeamsListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        teams = from_union([lambda x: from_list(Team.from_dict, x), from_none], obj.get("teams"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AdminTeamsListResponse(ok, teams, response_metadata, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["teams"] = from_union([lambda x: from_list(lambda x: to_class(Team, x), x), from_none], self.teams)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def admin_teams_list_response_from_dict(s: Any) -> AdminTeamsListResponse:
    return AdminTeamsListResponse.from_dict(s)


def admin_teams_list_response_to_dict(x: AdminTeamsListResponse) -> Any:
    return to_class(AdminTeamsListResponse, x)
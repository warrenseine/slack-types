# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = conversations_request_shared_invite_list_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


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
    avatar_base_url: Optional[str] = None
    is_verified: Optional[bool] = None
    domain: Optional[str] = None
    date_created: Optional[int] = None
    requires_sponsorship: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Team':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        icon = from_union([Icon.from_dict, from_none], obj.get("icon"))
        avatar_base_url = from_union([from_str, from_none], obj.get("avatar_base_url"))
        is_verified = from_union([from_bool, from_none], obj.get("is_verified"))
        domain = from_union([from_str, from_none], obj.get("domain"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        requires_sponsorship = from_union([from_bool, from_none], obj.get("requires_sponsorship"))
        return Team(id, name, icon, avatar_base_url, is_verified, domain, date_created, requires_sponsorship)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["icon"] = from_union([lambda x: to_class(Icon, x), from_none], self.icon)
        result["avatar_base_url"] = from_union([from_str, from_none], self.avatar_base_url)
        result["is_verified"] = from_union([from_bool, from_none], self.is_verified)
        result["domain"] = from_union([from_str, from_none], self.domain)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["requires_sponsorship"] = from_union([from_bool, from_none], self.requires_sponsorship)
        return result


@dataclass
class Connection:
    team: Optional[Team] = None
    is_private: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Connection':
        assert isinstance(obj, dict)
        team = from_union([Team.from_dict, from_none], obj.get("team"))
        is_private = from_union([from_bool, from_none], obj.get("is_private"))
        return Connection(team, is_private)

    def to_dict(self) -> dict:
        result: dict = {}
        result["team"] = from_union([lambda x: to_class(Team, x), from_none], self.team)
        result["is_private"] = from_union([from_bool, from_none], self.is_private)
        return result


@dataclass
class Channel:
    id: Optional[str] = None
    is_im: Optional[bool] = None
    is_private: Optional[bool] = None
    date_created: Optional[int] = None
    name: Optional[str] = None
    connections: Optional[List[Connection]] = None
    pending_connections: Optional[List[Connection]] = None
    previous_connections: Optional[List[Connection]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        is_im = from_union([from_bool, from_none], obj.get("is_im"))
        is_private = from_union([from_bool, from_none], obj.get("is_private"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        name = from_union([from_str, from_none], obj.get("name"))
        connections = from_union([lambda x: from_list(Connection.from_dict, x), from_none], obj.get("connections"))
        pending_connections = from_union([lambda x: from_list(Connection.from_dict, x), from_none], obj.get("pending_connections"))
        previous_connections = from_union([lambda x: from_list(Connection.from_dict, x), from_none], obj.get("previous_connections"))
        return Channel(id, is_im, is_private, date_created, name, connections, pending_connections, previous_connections)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["is_im"] = from_union([from_bool, from_none], self.is_im)
        result["is_private"] = from_union([from_bool, from_none], self.is_private)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["name"] = from_union([from_str, from_none], self.name)
        result["connections"] = from_union([lambda x: from_list(lambda x: to_class(Connection, x), x), from_none], self.connections)
        result["pending_connections"] = from_union([lambda x: from_list(lambda x: to_class(Connection, x), x), from_none], self.pending_connections)
        result["previous_connections"] = from_union([lambda x: from_list(lambda x: to_class(Connection, x), x), from_none], self.previous_connections)
        return result


@dataclass
class Profile:
    real_name: Optional[str] = None
    display_name: Optional[str] = None
    real_name_normalized: Optional[str] = None
    display_name_normalized: Optional[str] = None
    team: Optional[str] = None
    avatar_hash: Optional[str] = None
    email: Optional[str] = None
    image_24: Optional[str] = None
    image_32: Optional[str] = None
    image_48: Optional[str] = None
    image_72: Optional[str] = None
    image_192: Optional[str] = None
    image_512: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        assert isinstance(obj, dict)
        real_name = from_union([from_str, from_none], obj.get("real_name"))
        display_name = from_union([from_str, from_none], obj.get("display_name"))
        real_name_normalized = from_union([from_str, from_none], obj.get("real_name_normalized"))
        display_name_normalized = from_union([from_str, from_none], obj.get("display_name_normalized"))
        team = from_union([from_str, from_none], obj.get("team"))
        avatar_hash = from_union([from_str, from_none], obj.get("avatar_hash"))
        email = from_union([from_str, from_none], obj.get("email"))
        image_24 = from_union([from_str, from_none], obj.get("image_24"))
        image_32 = from_union([from_str, from_none], obj.get("image_32"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        image_192 = from_union([from_str, from_none], obj.get("image_192"))
        image_512 = from_union([from_str, from_none], obj.get("image_512"))
        return Profile(real_name, display_name, real_name_normalized, display_name_normalized, team, avatar_hash, email, image_24, image_32, image_48, image_72, image_192, image_512)

    def to_dict(self) -> dict:
        result: dict = {}
        result["real_name"] = from_union([from_str, from_none], self.real_name)
        result["display_name"] = from_union([from_str, from_none], self.display_name)
        result["real_name_normalized"] = from_union([from_str, from_none], self.real_name_normalized)
        result["display_name_normalized"] = from_union([from_str, from_none], self.display_name_normalized)
        result["team"] = from_union([from_str, from_none], self.team)
        result["avatar_hash"] = from_union([from_str, from_none], self.avatar_hash)
        result["email"] = from_union([from_str, from_none], self.email)
        result["image_24"] = from_union([from_str, from_none], self.image_24)
        result["image_32"] = from_union([from_str, from_none], self.image_32)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        result["image_192"] = from_union([from_str, from_none], self.image_192)
        result["image_512"] = from_union([from_str, from_none], self.image_512)
        return result


@dataclass
class InvitingUser:
    team_id: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    updated: Optional[int] = None
    who_can_share_contact_card: Optional[str] = None
    profile: Optional[Profile] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InvitingUser':
        assert isinstance(obj, dict)
        team_id = from_union([from_none, lambda x: int(from_str(x))], obj.get("team_id"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        who_can_share_contact_card = from_union([from_str, from_none], obj.get("who_can_share_contact_card"))
        profile = from_union([Profile.from_dict, from_none], obj.get("profile"))
        return InvitingUser(team_id, id, name, updated, who_can_share_contact_card, profile)

    def to_dict(self) -> dict:
        result: dict = {}
        result["team_id"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.team_id)
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["who_can_share_contact_card"] = from_union([from_str, from_none], self.who_can_share_contact_card)
        result["profile"] = from_union([lambda x: to_class(Profile, x), from_none], self.profile)
        return result


@dataclass
class TargetUser:
    recipient_email: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TargetUser':
        assert isinstance(obj, dict)
        recipient_email = from_union([from_str, from_none], obj.get("recipient_email"))
        return TargetUser(recipient_email)

    def to_dict(self) -> dict:
        result: dict = {}
        result["recipient_email"] = from_union([from_str, from_none], self.recipient_email)
        return result


@dataclass
class InviteRequest:
    id: Optional[str] = None
    date_created: Optional[int] = None
    expires_at: Optional[int] = None
    inviting_team: Optional[Team] = None
    inviting_user: Optional[InvitingUser] = None
    channel: Optional[Channel] = None
    is_external_limited: Optional[bool] = None
    date_last_updated: Optional[int] = None
    target_user: Optional[TargetUser] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InviteRequest':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        expires_at = from_union([from_int, from_none], obj.get("expires_at"))
        inviting_team = from_union([Team.from_dict, from_none], obj.get("inviting_team"))
        inviting_user = from_union([InvitingUser.from_dict, from_none], obj.get("inviting_user"))
        channel = from_union([Channel.from_dict, from_none], obj.get("channel"))
        is_external_limited = from_union([from_bool, from_none], obj.get("is_external_limited"))
        date_last_updated = from_union([from_int, from_none], obj.get("date_last_updated"))
        target_user = from_union([TargetUser.from_dict, from_none], obj.get("target_user"))
        return InviteRequest(id, date_created, expires_at, inviting_team, inviting_user, channel, is_external_limited, date_last_updated, target_user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["expires_at"] = from_union([from_int, from_none], self.expires_at)
        result["inviting_team"] = from_union([lambda x: to_class(Team, x), from_none], self.inviting_team)
        result["inviting_user"] = from_union([lambda x: to_class(InvitingUser, x), from_none], self.inviting_user)
        result["channel"] = from_union([lambda x: to_class(Channel, x), from_none], self.channel)
        result["is_external_limited"] = from_union([from_bool, from_none], self.is_external_limited)
        result["date_last_updated"] = from_union([from_int, from_none], self.date_last_updated)
        result["target_user"] = from_union([lambda x: to_class(TargetUser, x), from_none], self.target_user)
        return result


@dataclass
class ConversationsRequestSharedInviteListResponse:
    ok: Optional[bool] = None
    invite_requests: Optional[List[InviteRequest]] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ConversationsRequestSharedInviteListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        invite_requests = from_union([lambda x: from_list(InviteRequest.from_dict, x), from_none], obj.get("invite_requests"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return ConversationsRequestSharedInviteListResponse(ok, invite_requests, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["invite_requests"] = from_union([lambda x: from_list(lambda x: to_class(InviteRequest, x), x), from_none], self.invite_requests)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def conversations_request_shared_invite_list_response_from_dict(s: Any) -> ConversationsRequestSharedInviteListResponse:
    return ConversationsRequestSharedInviteListResponse.from_dict(s)


def conversations_request_shared_invite_list_response_to_dict(x: ConversationsRequestSharedInviteListResponse) -> Any:
    return to_class(ConversationsRequestSharedInviteListResponse, x)

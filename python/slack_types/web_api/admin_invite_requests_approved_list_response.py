# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_invite_requests_approved_list_response_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ApprovedBy:
    actor_type: Optional[str] = None
    actor_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ApprovedBy':
        assert isinstance(obj, dict)
        actor_type = from_union([from_str, from_none], obj.get("actor_type"))
        actor_id = from_union([from_str, from_none], obj.get("actor_id"))
        return ApprovedBy(actor_type, actor_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["actor_type"] = from_union([from_str, from_none], self.actor_type)
        result["actor_id"] = from_union([from_str, from_none], self.actor_id)
        return result


@dataclass
class InvitePreferences:
    is_restricted: Optional[bool] = None
    is_ultra_restricted: Optional[bool] = None
    channel_ids: Optional[List[str]] = None
    is_domain_matched: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InvitePreferences':
        assert isinstance(obj, dict)
        is_restricted = from_union([from_bool, from_none], obj.get("is_restricted"))
        is_ultra_restricted = from_union([from_bool, from_none], obj.get("is_ultra_restricted"))
        channel_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channel_ids"))
        is_domain_matched = from_union([from_bool, from_none], obj.get("is_domain_matched"))
        return InvitePreferences(is_restricted, is_ultra_restricted, channel_ids, is_domain_matched)

    def to_dict(self) -> dict:
        result: dict = {}
        result["is_restricted"] = from_union([from_bool, from_none], self.is_restricted)
        result["is_ultra_restricted"] = from_union([from_bool, from_none], self.is_ultra_restricted)
        result["channel_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.channel_ids)
        result["is_domain_matched"] = from_union([from_bool, from_none], self.is_domain_matched)
        return result


@dataclass
class Invite:
    id: Optional[str] = None
    email: Optional[str] = None
    inviter_id: Optional[str] = None
    date_created: Optional[int] = None
    is_bouncing: Optional[bool] = None
    invite_preferences: Optional[InvitePreferences] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Invite':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        email = from_union([from_str, from_none], obj.get("email"))
        inviter_id = from_union([from_str, from_none], obj.get("inviter_id"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        is_bouncing = from_union([from_bool, from_none], obj.get("is_bouncing"))
        invite_preferences = from_union([InvitePreferences.from_dict, from_none], obj.get("invite_preferences"))
        return Invite(id, email, inviter_id, date_created, is_bouncing, invite_preferences)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["email"] = from_union([from_str, from_none], self.email)
        result["inviter_id"] = from_union([from_str, from_none], self.inviter_id)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["is_bouncing"] = from_union([from_bool, from_none], self.is_bouncing)
        result["invite_preferences"] = from_union([lambda x: to_class(InvitePreferences, x), from_none], self.invite_preferences)
        return result


@dataclass
class InviteRequest:
    id: Optional[str] = None
    email: Optional[str] = None
    date_created: Optional[int] = None
    requester_ids: Optional[List[str]] = None
    channel_ids: Optional[List[str]] = None
    invite_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InviteRequest':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        email = from_union([from_str, from_none], obj.get("email"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        requester_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("requester_ids"))
        channel_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channel_ids"))
        invite_type = from_union([from_str, from_none], obj.get("invite_type"))
        return InviteRequest(id, email, date_created, requester_ids, channel_ids, invite_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["email"] = from_union([from_str, from_none], self.email)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["requester_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.requester_ids)
        result["channel_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.channel_ids)
        result["invite_type"] = from_union([from_str, from_none], self.invite_type)
        return result


@dataclass
class ApprovedRequest:
    invite_request: Optional[InviteRequest] = None
    approved_by: Optional[ApprovedBy] = None
    invite: Optional[Invite] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ApprovedRequest':
        assert isinstance(obj, dict)
        invite_request = from_union([InviteRequest.from_dict, from_none], obj.get("invite_request"))
        approved_by = from_union([ApprovedBy.from_dict, from_none], obj.get("approved_by"))
        invite = from_union([Invite.from_dict, from_none], obj.get("invite"))
        return ApprovedRequest(invite_request, approved_by, invite)

    def to_dict(self) -> dict:
        result: dict = {}
        result["invite_request"] = from_union([lambda x: to_class(InviteRequest, x), from_none], self.invite_request)
        result["approved_by"] = from_union([lambda x: to_class(ApprovedBy, x), from_none], self.approved_by)
        result["invite"] = from_union([lambda x: to_class(Invite, x), from_none], self.invite)
        return result


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
class AdminInviteRequestsApprovedListResponse:
    ok: Optional[bool] = None
    approved_requests: Optional[List[ApprovedRequest]] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminInviteRequestsApprovedListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        approved_requests = from_union([lambda x: from_list(ApprovedRequest.from_dict, x), from_none], obj.get("approved_requests"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return AdminInviteRequestsApprovedListResponse(ok, approved_requests, error, needed, provided, response_metadata, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["approved_requests"] = from_union([lambda x: from_list(lambda x: to_class(ApprovedRequest, x), x), from_none], self.approved_requests)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def admin_invite_requests_approved_list_response_from_dict(s: Any) -> AdminInviteRequestsApprovedListResponse:
    return AdminInviteRequestsApprovedListResponse.from_dict(s)


def admin_invite_requests_approved_list_response_to_dict(x: AdminInviteRequestsApprovedListResponse) -> Any:
    return to_class(AdminInviteRequestsApprovedListResponse, x)

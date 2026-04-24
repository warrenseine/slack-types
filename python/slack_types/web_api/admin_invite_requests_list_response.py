# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_invite_requests_list_response_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class InviteRequest:
    id: Optional[str] = None
    email: Optional[str] = None
    date_created: Optional[int] = None
    requester_ids: Optional[List[str]] = None
    channel_ids: Optional[List[str]] = None
    invite_type: Optional[str] = None
    request_reason: Optional[str] = None
    date_expire: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InviteRequest':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        email = from_union([from_str, from_none], obj.get("email"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        requester_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("requester_ids"))
        channel_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channel_ids"))
        invite_type = from_union([from_str, from_none], obj.get("invite_type"))
        request_reason = from_union([from_str, from_none], obj.get("request_reason"))
        date_expire = from_union([from_int, from_none], obj.get("date_expire"))
        return InviteRequest(id, email, date_created, requester_ids, channel_ids, invite_type, request_reason, date_expire)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["email"] = from_union([from_str, from_none], self.email)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["requester_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.requester_ids)
        result["channel_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.channel_ids)
        result["invite_type"] = from_union([from_str, from_none], self.invite_type)
        result["request_reason"] = from_union([from_str, from_none], self.request_reason)
        result["date_expire"] = from_union([from_int, from_none], self.date_expire)
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
class AdminInviteRequestsListResponse:
    ok: Optional[bool] = None
    invite_requests: Optional[List[InviteRequest]] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminInviteRequestsListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        invite_requests = from_union([lambda x: from_list(InviteRequest.from_dict, x), from_none], obj.get("invite_requests"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return AdminInviteRequestsListResponse(ok, invite_requests, error, needed, provided, response_metadata, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["invite_requests"] = from_union([lambda x: from_list(lambda x: to_class(InviteRequest, x), x), from_none], self.invite_requests)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def admin_invite_requests_list_response_from_dict(s: Any) -> AdminInviteRequestsListResponse:
    return AdminInviteRequestsListResponse.from_dict(s)


def admin_invite_requests_list_response_to_dict(x: AdminInviteRequestsListResponse) -> Any:
    return to_class(AdminInviteRequestsListResponse, x)

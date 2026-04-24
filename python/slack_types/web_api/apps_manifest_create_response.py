# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = apps_manifest_create_response_from_dict(json.loads(json_string))

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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Credentials:
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    verification_token: Optional[str] = None
    signing_secret: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Credentials':
        assert isinstance(obj, dict)
        client_id = from_union([from_str, from_none], obj.get("client_id"))
        client_secret = from_union([from_str, from_none], obj.get("client_secret"))
        verification_token = from_union([from_str, from_none], obj.get("verification_token"))
        signing_secret = from_union([from_str, from_none], obj.get("signing_secret"))
        return Credentials(client_id, client_secret, verification_token, signing_secret)

    def to_dict(self) -> dict:
        result: dict = {}
        result["client_id"] = from_union([from_str, from_none], self.client_id)
        result["client_secret"] = from_union([from_str, from_none], self.client_secret)
        result["verification_token"] = from_union([from_str, from_none], self.verification_token)
        result["signing_secret"] = from_union([from_str, from_none], self.signing_secret)
        return result


@dataclass
class Error:
    code: Optional[str] = None
    message: Optional[str] = None
    pointer: Optional[str] = None
    related_component: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Error':
        assert isinstance(obj, dict)
        code = from_union([from_str, from_none], obj.get("code"))
        message = from_union([from_str, from_none], obj.get("message"))
        pointer = from_union([from_str, from_none], obj.get("pointer"))
        related_component = from_union([from_str, from_none], obj.get("related_component"))
        return Error(code, message, pointer, related_component)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_union([from_str, from_none], self.code)
        result["message"] = from_union([from_str, from_none], self.message)
        result["pointer"] = from_union([from_str, from_none], self.pointer)
        result["related_component"] = from_union([from_str, from_none], self.related_component)
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
class AppsManifestCreateResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    errors: Optional[List[Error]] = None
    app_id: Optional[str] = None
    credentials: Optional[Credentials] = None
    oauth_authorize_url: Optional[str] = None
    team_id: Optional[str] = None
    team_domain: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AppsManifestCreateResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        credentials = from_union([Credentials.from_dict, from_none], obj.get("credentials"))
        oauth_authorize_url = from_union([from_str, from_none], obj.get("oauth_authorize_url"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        team_domain = from_union([from_str, from_none], obj.get("team_domain"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return AppsManifestCreateResponse(ok, error, response_metadata, needed, provided, errors, app_id, credentials, oauth_authorize_url, team_id, team_domain, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["errors"] = from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none], self.errors)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["credentials"] = from_union([lambda x: to_class(Credentials, x), from_none], self.credentials)
        result["oauth_authorize_url"] = from_union([from_str, from_none], self.oauth_authorize_url)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["team_domain"] = from_union([from_str, from_none], self.team_domain)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def apps_manifest_create_response_from_dict(s: Any) -> AppsManifestCreateResponse:
    return AppsManifestCreateResponse.from_dict(s)


def apps_manifest_create_response_to_dict(x: AppsManifestCreateResponse) -> Any:
    return to_class(AppsManifestCreateResponse, x)

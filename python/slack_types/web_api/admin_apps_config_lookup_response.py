# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_apps_config_lookup_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


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


@dataclass
class DomainRestrictions:
    emails: Optional[List[str]] = None
    urls: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DomainRestrictions':
        assert isinstance(obj, dict)
        emails = from_union([lambda x: from_list(from_str, x), from_none], obj.get("emails"))
        urls = from_union([lambda x: from_list(from_str, x), from_none], obj.get("urls"))
        return DomainRestrictions(emails, urls)

    def to_dict(self) -> dict:
        result: dict = {}
        result["emails"] = from_union([lambda x: from_list(from_str, x), from_none], self.emails)
        result["urls"] = from_union([lambda x: from_list(from_str, x), from_none], self.urls)
        return result


@dataclass
class Config:
    app_id: Optional[str] = None
    workflow_auth_strategy: Optional[str] = None
    domain_restrictions: Optional[DomainRestrictions] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Config':
        assert isinstance(obj, dict)
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        workflow_auth_strategy = from_union([from_str, from_none], obj.get("workflow_auth_strategy"))
        domain_restrictions = from_union([DomainRestrictions.from_dict, from_none], obj.get("domain_restrictions"))
        return Config(app_id, workflow_auth_strategy, domain_restrictions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["workflow_auth_strategy"] = from_union([from_str, from_none], self.workflow_auth_strategy)
        result["domain_restrictions"] = from_union([lambda x: to_class(DomainRestrictions, x), from_none], self.domain_restrictions)
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
class AdminAppsConfigLookupResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    configs: Optional[List[Config]] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminAppsConfigLookupResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        configs = from_union([lambda x: from_list(Config.from_dict, x), from_none], obj.get("configs"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return AdminAppsConfigLookupResponse(ok, error, response_metadata, needed, provided, configs, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["configs"] = from_union([lambda x: from_list(lambda x: to_class(Config, x), x), from_none], self.configs)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def admin_apps_config_lookup_response_from_dict(s: Any) -> AdminAppsConfigLookupResponse:
    return AdminAppsConfigLookupResponse.from_dict(s)


def admin_apps_config_lookup_response_to_dict(x: AdminAppsConfigLookupResponse) -> Any:
    return to_class(AdminAppsConfigLookupResponse, x)

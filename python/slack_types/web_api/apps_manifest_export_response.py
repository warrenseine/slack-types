# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = apps_manifest_export_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, Dict, TypeVar, Callable, Type, cast


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


@dataclass
class DisplayInformation:
    name: Optional[str] = None
    long_description: Optional[str] = None
    description: Optional[str] = None
    background_color: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DisplayInformation':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        long_description = from_union([from_str, from_none], obj.get("long_description"))
        description = from_union([from_str, from_none], obj.get("description"))
        background_color = from_union([from_str, from_none], obj.get("background_color"))
        return DisplayInformation(name, long_description, description, background_color)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["long_description"] = from_union([from_str, from_none], self.long_description)
        result["description"] = from_union([from_str, from_none], self.description)
        result["background_color"] = from_union([from_str, from_none], self.background_color)
        return result


@dataclass
class AppHome:
    home_tab_enabled: Optional[bool] = None
    messages_tab_enabled: Optional[bool] = None
    messages_tab_read_only_enabled: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AppHome':
        assert isinstance(obj, dict)
        home_tab_enabled = from_union([from_bool, from_none], obj.get("home_tab_enabled"))
        messages_tab_enabled = from_union([from_bool, from_none], obj.get("messages_tab_enabled"))
        messages_tab_read_only_enabled = from_union([from_bool, from_none], obj.get("messages_tab_read_only_enabled"))
        return AppHome(home_tab_enabled, messages_tab_enabled, messages_tab_read_only_enabled)

    def to_dict(self) -> dict:
        result: dict = {}
        result["home_tab_enabled"] = from_union([from_bool, from_none], self.home_tab_enabled)
        result["messages_tab_enabled"] = from_union([from_bool, from_none], self.messages_tab_enabled)
        result["messages_tab_read_only_enabled"] = from_union([from_bool, from_none], self.messages_tab_read_only_enabled)
        return result


@dataclass
class BotUser:
    display_name: Optional[str] = None
    always_online: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BotUser':
        assert isinstance(obj, dict)
        display_name = from_union([from_str, from_none], obj.get("display_name"))
        always_online = from_union([from_bool, from_none], obj.get("always_online"))
        return BotUser(display_name, always_online)

    def to_dict(self) -> dict:
        result: dict = {}
        result["display_name"] = from_union([from_str, from_none], self.display_name)
        result["always_online"] = from_union([from_bool, from_none], self.always_online)
        return result


@dataclass
class Shortcut:
    type: Optional[str] = None
    callback_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Shortcut':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        callback_id = from_union([from_str, from_none], obj.get("callback_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        description = from_union([from_str, from_none], obj.get("description"))
        return Shortcut(type, callback_id, name, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["callback_id"] = from_union([from_str, from_none], self.callback_id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["description"] = from_union([from_str, from_none], self.description)
        return result


@dataclass
class SlashCommand:
    command: Optional[str] = None
    description: Optional[str] = None
    usage_hint: Optional[str] = None
    url: Optional[str] = None
    should_escape: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SlashCommand':
        assert isinstance(obj, dict)
        command = from_union([from_str, from_none], obj.get("command"))
        description = from_union([from_str, from_none], obj.get("description"))
        usage_hint = from_union([from_str, from_none], obj.get("usage_hint"))
        url = from_union([from_str, from_none], obj.get("url"))
        should_escape = from_union([from_bool, from_none], obj.get("should_escape"))
        return SlashCommand(command, description, usage_hint, url, should_escape)

    def to_dict(self) -> dict:
        result: dict = {}
        result["command"] = from_union([from_str, from_none], self.command)
        result["description"] = from_union([from_str, from_none], self.description)
        result["usage_hint"] = from_union([from_str, from_none], self.usage_hint)
        result["url"] = from_union([from_str, from_none], self.url)
        result["should_escape"] = from_union([from_bool, from_none], self.should_escape)
        return result


@dataclass
class Features:
    app_home: Optional[AppHome] = None
    bot_user: Optional[BotUser] = None
    shortcuts: Optional[List[Shortcut]] = None
    slash_commands: Optional[List[SlashCommand]] = None
    unfurl_domains: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Features':
        assert isinstance(obj, dict)
        app_home = from_union([AppHome.from_dict, from_none], obj.get("app_home"))
        bot_user = from_union([BotUser.from_dict, from_none], obj.get("bot_user"))
        shortcuts = from_union([lambda x: from_list(Shortcut.from_dict, x), from_none], obj.get("shortcuts"))
        slash_commands = from_union([lambda x: from_list(SlashCommand.from_dict, x), from_none], obj.get("slash_commands"))
        unfurl_domains = from_union([lambda x: from_list(from_str, x), from_none], obj.get("unfurl_domains"))
        return Features(app_home, bot_user, shortcuts, slash_commands, unfurl_domains)

    def to_dict(self) -> dict:
        result: dict = {}
        result["app_home"] = from_union([lambda x: to_class(AppHome, x), from_none], self.app_home)
        result["bot_user"] = from_union([lambda x: to_class(BotUser, x), from_none], self.bot_user)
        result["shortcuts"] = from_union([lambda x: from_list(lambda x: to_class(Shortcut, x), x), from_none], self.shortcuts)
        result["slash_commands"] = from_union([lambda x: from_list(lambda x: to_class(SlashCommand, x), x), from_none], self.slash_commands)
        result["unfurl_domains"] = from_union([lambda x: from_list(from_str, x), from_none], self.unfurl_domains)
        return result


@dataclass
class PutParameter:
    type: Optional[str] = None
    name: Optional[str] = None
    is_required: Optional[bool] = None
    description: Optional[str] = None
    title: Optional[str] = None
    hint: Optional[str] = None
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    minimum: Optional[int] = None
    maximum: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PutParameter':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        name = from_union([from_str, from_none], obj.get("name"))
        is_required = from_union([from_bool, from_none], obj.get("is_required"))
        description = from_union([from_str, from_none], obj.get("description"))
        title = from_union([from_str, from_none], obj.get("title"))
        hint = from_union([from_str, from_none], obj.get("hint"))
        min_length = from_union([from_int, from_none], obj.get("minLength"))
        max_length = from_union([from_int, from_none], obj.get("maxLength"))
        minimum = from_union([from_int, from_none], obj.get("minimum"))
        maximum = from_union([from_int, from_none], obj.get("maximum"))
        return PutParameter(type, name, is_required, description, title, hint, min_length, max_length, minimum, maximum)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["name"] = from_union([from_str, from_none], self.name)
        result["is_required"] = from_union([from_bool, from_none], self.is_required)
        result["description"] = from_union([from_str, from_none], self.description)
        result["title"] = from_union([from_str, from_none], self.title)
        result["hint"] = from_union([from_str, from_none], self.hint)
        result["minLength"] = from_union([from_int, from_none], self.min_length)
        result["maxLength"] = from_union([from_int, from_none], self.max_length)
        result["minimum"] = from_union([from_int, from_none], self.minimum)
        result["maximum"] = from_union([from_int, from_none], self.maximum)
        return result


@dataclass
class Function:
    title: Optional[str] = None
    description: Optional[str] = None
    input_parameters: Optional[Dict[str, PutParameter]] = None
    output_parameters: Optional[Dict[str, PutParameter]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Function':
        assert isinstance(obj, dict)
        title = from_union([from_str, from_none], obj.get("title"))
        description = from_union([from_str, from_none], obj.get("description"))
        input_parameters = from_union([lambda x: from_dict(PutParameter.from_dict, x), from_none], obj.get("input_parameters"))
        output_parameters = from_union([lambda x: from_dict(PutParameter.from_dict, x), from_none], obj.get("output_parameters"))
        return Function(title, description, input_parameters, output_parameters)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([from_str, from_none], self.title)
        result["description"] = from_union([from_str, from_none], self.description)
        result["input_parameters"] = from_union([lambda x: from_dict(lambda x: to_class(PutParameter, x), x), from_none], self.input_parameters)
        result["output_parameters"] = from_union([lambda x: from_dict(lambda x: to_class(PutParameter, x), x), from_none], self.output_parameters)
        return result


@dataclass
class Metadata:
    major_version: Optional[int] = None
    minor_version: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Metadata':
        assert isinstance(obj, dict)
        major_version = from_union([from_int, from_none], obj.get("major_version"))
        minor_version = from_union([from_int, from_none], obj.get("minor_version"))
        return Metadata(major_version, minor_version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["major_version"] = from_union([from_int, from_none], self.major_version)
        result["minor_version"] = from_union([from_int, from_none], self.minor_version)
        return result


@dataclass
class Scopes:
    bot: Optional[List[str]] = None
    user: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Scopes':
        assert isinstance(obj, dict)
        bot = from_union([lambda x: from_list(from_str, x), from_none], obj.get("bot"))
        user = from_union([lambda x: from_list(from_str, x), from_none], obj.get("user"))
        return Scopes(bot, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bot"] = from_union([lambda x: from_list(from_str, x), from_none], self.bot)
        result["user"] = from_union([lambda x: from_list(from_str, x), from_none], self.user)
        return result


@dataclass
class OauthConfig:
    scopes: Optional[Scopes] = None
    redirect_urls: Optional[List[str]] = None
    token_management_enabled: Optional[bool] = None
    pkce_enabled: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OauthConfig':
        assert isinstance(obj, dict)
        scopes = from_union([Scopes.from_dict, from_none], obj.get("scopes"))
        redirect_urls = from_union([lambda x: from_list(from_str, x), from_none], obj.get("redirect_urls"))
        token_management_enabled = from_union([from_bool, from_none], obj.get("token_management_enabled"))
        pkce_enabled = from_union([from_bool, from_none], obj.get("pkce_enabled"))
        return OauthConfig(scopes, redirect_urls, token_management_enabled, pkce_enabled)

    def to_dict(self) -> dict:
        result: dict = {}
        result["scopes"] = from_union([lambda x: to_class(Scopes, x), from_none], self.scopes)
        result["redirect_urls"] = from_union([lambda x: from_list(from_str, x), from_none], self.redirect_urls)
        result["token_management_enabled"] = from_union([from_bool, from_none], self.token_management_enabled)
        result["pkce_enabled"] = from_union([from_bool, from_none], self.pkce_enabled)
        return result


@dataclass
class EventSubscriptions:
    bot_events: Optional[List[str]] = None
    user_events: Optional[List[str]] = None
    request_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EventSubscriptions':
        assert isinstance(obj, dict)
        bot_events = from_union([lambda x: from_list(from_str, x), from_none], obj.get("bot_events"))
        user_events = from_union([lambda x: from_list(from_str, x), from_none], obj.get("user_events"))
        request_url = from_union([from_str, from_none], obj.get("request_url"))
        return EventSubscriptions(bot_events, user_events, request_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bot_events"] = from_union([lambda x: from_list(from_str, x), from_none], self.bot_events)
        result["user_events"] = from_union([lambda x: from_list(from_str, x), from_none], self.user_events)
        result["request_url"] = from_union([from_str, from_none], self.request_url)
        return result


@dataclass
class Interactivity:
    is_enabled: Optional[bool] = None
    request_url: Optional[str] = None
    message_menu_options_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Interactivity':
        assert isinstance(obj, dict)
        is_enabled = from_union([from_bool, from_none], obj.get("is_enabled"))
        request_url = from_union([from_str, from_none], obj.get("request_url"))
        message_menu_options_url = from_union([from_str, from_none], obj.get("message_menu_options_url"))
        return Interactivity(is_enabled, request_url, message_menu_options_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["is_enabled"] = from_union([from_bool, from_none], self.is_enabled)
        result["request_url"] = from_union([from_str, from_none], self.request_url)
        result["message_menu_options_url"] = from_union([from_str, from_none], self.message_menu_options_url)
        return result


@dataclass
class Settings:
    description: Optional[str] = None
    long_description: Optional[str] = None
    background_color: Optional[str] = None
    event_subscriptions: Optional[EventSubscriptions] = None
    interactivity: Optional[Interactivity] = None
    allowed_ip_address_ranges: Optional[List[str]] = None
    org_deploy_enabled: Optional[bool] = None
    socket_mode_enabled: Optional[bool] = None
    token_rotation_enabled: Optional[bool] = None
    hermes_app_type: Optional[str] = None
    function_runtime: Optional[str] = None
    is_mcp_enabled: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Settings':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("description"))
        long_description = from_union([from_str, from_none], obj.get("long_description"))
        background_color = from_union([from_str, from_none], obj.get("background_color"))
        event_subscriptions = from_union([EventSubscriptions.from_dict, from_none], obj.get("event_subscriptions"))
        interactivity = from_union([Interactivity.from_dict, from_none], obj.get("interactivity"))
        allowed_ip_address_ranges = from_union([lambda x: from_list(from_str, x), from_none], obj.get("allowed_ip_address_ranges"))
        org_deploy_enabled = from_union([from_bool, from_none], obj.get("org_deploy_enabled"))
        socket_mode_enabled = from_union([from_bool, from_none], obj.get("socket_mode_enabled"))
        token_rotation_enabled = from_union([from_bool, from_none], obj.get("token_rotation_enabled"))
        hermes_app_type = from_union([from_str, from_none], obj.get("hermes_app_type"))
        function_runtime = from_union([from_str, from_none], obj.get("function_runtime"))
        is_mcp_enabled = from_union([from_bool, from_none], obj.get("is_mcp_enabled"))
        return Settings(description, long_description, background_color, event_subscriptions, interactivity, allowed_ip_address_ranges, org_deploy_enabled, socket_mode_enabled, token_rotation_enabled, hermes_app_type, function_runtime, is_mcp_enabled)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_union([from_str, from_none], self.description)
        result["long_description"] = from_union([from_str, from_none], self.long_description)
        result["background_color"] = from_union([from_str, from_none], self.background_color)
        result["event_subscriptions"] = from_union([lambda x: to_class(EventSubscriptions, x), from_none], self.event_subscriptions)
        result["interactivity"] = from_union([lambda x: to_class(Interactivity, x), from_none], self.interactivity)
        result["allowed_ip_address_ranges"] = from_union([lambda x: from_list(from_str, x), from_none], self.allowed_ip_address_ranges)
        result["org_deploy_enabled"] = from_union([from_bool, from_none], self.org_deploy_enabled)
        result["socket_mode_enabled"] = from_union([from_bool, from_none], self.socket_mode_enabled)
        result["token_rotation_enabled"] = from_union([from_bool, from_none], self.token_rotation_enabled)
        result["hermes_app_type"] = from_union([from_str, from_none], self.hermes_app_type)
        result["function_runtime"] = from_union([from_str, from_none], self.function_runtime)
        result["is_mcp_enabled"] = from_union([from_bool, from_none], self.is_mcp_enabled)
        return result


@dataclass
class Manifest:
    metadata: Optional[Metadata] = None
    display_information: Optional[DisplayInformation] = None
    settings: Optional[Settings] = None
    features: Optional[Features] = None
    oauth_config: Optional[OauthConfig] = None
    functions: Optional[Dict[str, Function]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Manifest':
        assert isinstance(obj, dict)
        metadata = from_union([Metadata.from_dict, from_none], obj.get("_metadata"))
        display_information = from_union([DisplayInformation.from_dict, from_none], obj.get("display_information"))
        settings = from_union([Settings.from_dict, from_none], obj.get("settings"))
        features = from_union([Features.from_dict, from_none], obj.get("features"))
        oauth_config = from_union([OauthConfig.from_dict, from_none], obj.get("oauth_config"))
        functions = from_union([lambda x: from_dict(Function.from_dict, x), from_none], obj.get("functions"))
        return Manifest(metadata, display_information, settings, features, oauth_config, functions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_metadata"] = from_union([lambda x: to_class(Metadata, x), from_none], self.metadata)
        result["display_information"] = from_union([lambda x: to_class(DisplayInformation, x), from_none], self.display_information)
        result["settings"] = from_union([lambda x: to_class(Settings, x), from_none], self.settings)
        result["features"] = from_union([lambda x: to_class(Features, x), from_none], self.features)
        result["oauth_config"] = from_union([lambda x: to_class(OauthConfig, x), from_none], self.oauth_config)
        result["functions"] = from_union([lambda x: from_dict(lambda x: to_class(Function, x), x), from_none], self.functions)
        return result


@dataclass
class AppsManifestExportResponse:
    ok: Optional[bool] = None
    manifest: Optional[Manifest] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AppsManifestExportResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        manifest = from_union([Manifest.from_dict, from_none], obj.get("manifest"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return AppsManifestExportResponse(ok, manifest, error, needed, provided, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["manifest"] = from_union([lambda x: to_class(Manifest, x), from_none], self.manifest)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def apps_manifest_export_response_from_dict(s: Any) -> AppsManifestExportResponse:
    return AppsManifestExportResponse.from_dict(s)


def apps_manifest_export_response_to_dict(x: AppsManifestExportResponse) -> Any:
    return to_class(AppsManifestExportResponse, x)

# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = views_publish_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, Union, TypeVar, Callable, Type, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


@dataclass
class ResponseMetadata:
    messages: Optional[List[str]] = None
    warnings: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        messages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("messages"))
        warnings = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("warnings"))
        return ResponseMetadata(messages, warnings)

    def to_dict(self) -> dict:
        result: dict = {}
        result["messages"] = from_union([lambda x: from_list(from_str, x), from_none], self.messages)
        result["warnings"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.warnings)
        return result


@dataclass
class SlackFile:
    id: Optional[str] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SlackFile':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        url = from_union([from_str, from_none], obj.get("url"))
        return SlackFile(id, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class Accessory:
    type: Optional[str] = None
    image_url: Optional[str] = None
    alt_text: Optional[str] = None
    fallback: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    slack_file: Optional[SlackFile] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Accessory':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        slack_file = from_union([SlackFile.from_dict, from_none], obj.get("slack_file"))
        return Accessory(type, image_url, alt_text, fallback, image_width, image_height, image_bytes, slack_file)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["slack_file"] = from_union([lambda x: to_class(SlackFile, x), from_none], self.slack_file)
        return result


class CloseType(Enum):
    EMPTY = ""
    MRKDWN = "mrkdwn"
    PLAIN_TEXT = "plain_text"


@dataclass
class Close:
    type: Optional[CloseType] = None
    text: Optional[str] = None
    emoji: Optional[bool] = None
    verbatim: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Close':
        assert isinstance(obj, dict)
        type = from_union([CloseType, from_none], obj.get("type"))
        text = from_union([from_str, from_none], obj.get("text"))
        emoji = from_union([from_bool, from_none], obj.get("emoji"))
        verbatim = from_union([from_bool, from_none], obj.get("verbatim"))
        return Close(type, text, emoji, verbatim)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: to_enum(CloseType, x), from_none], self.type)
        result["text"] = from_union([from_str, from_none], self.text)
        result["emoji"] = from_union([from_bool, from_none], self.emoji)
        result["verbatim"] = from_union([from_bool, from_none], self.verbatim)
        return result


@dataclass
class Confirm:
    title: Optional[Close] = None
    text: Optional[Close] = None
    confirm: Optional[Close] = None
    deny: Optional[Close] = None
    style: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Confirm':
        assert isinstance(obj, dict)
        title = from_union([Close.from_dict, from_none], obj.get("title"))
        text = from_union([Close.from_dict, from_none], obj.get("text"))
        confirm = from_union([Close.from_dict, from_none], obj.get("confirm"))
        deny = from_union([Close.from_dict, from_none], obj.get("deny"))
        style = from_union([from_str, from_none], obj.get("style"))
        return Confirm(title, text, confirm, deny, style)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([lambda x: to_class(Close, x), from_none], self.title)
        result["text"] = from_union([lambda x: to_class(Close, x), from_none], self.text)
        result["confirm"] = from_union([lambda x: to_class(Close, x), from_none], self.confirm)
        result["deny"] = from_union([lambda x: to_class(Close, x), from_none], self.deny)
        result["style"] = from_union([from_str, from_none], self.style)
        return result


@dataclass
class DispatchActionConfig:
    trigger_actions_on: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DispatchActionConfig':
        assert isinstance(obj, dict)
        trigger_actions_on = from_union([lambda x: from_list(from_str, x), from_none], obj.get("trigger_actions_on"))
        return DispatchActionConfig(trigger_actions_on)

    def to_dict(self) -> dict:
        result: dict = {}
        result["trigger_actions_on"] = from_union([lambda x: from_list(from_str, x), from_none], self.trigger_actions_on)
        return result


@dataclass
class Filter:
    include: Optional[List[Any]] = None
    exclude_external_shared_channels: Optional[bool] = None
    exclude_bot_users: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Filter':
        assert isinstance(obj, dict)
        include = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("include"))
        exclude_external_shared_channels = from_union([from_bool, from_none], obj.get("exclude_external_shared_channels"))
        exclude_bot_users = from_union([from_bool, from_none], obj.get("exclude_bot_users"))
        return Filter(include, exclude_external_shared_channels, exclude_bot_users)

    def to_dict(self) -> dict:
        result: dict = {}
        result["include"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.include)
        result["exclude_external_shared_channels"] = from_union([from_bool, from_none], self.exclude_external_shared_channels)
        result["exclude_bot_users"] = from_union([from_bool, from_none], self.exclude_bot_users)
        return result


@dataclass
class Option:
    text: Optional[Close] = None
    value: Optional[str] = None
    description: Optional[Close] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Option':
        assert isinstance(obj, dict)
        text = from_union([Close.from_dict, from_none], obj.get("text"))
        value = from_union([from_str, from_none], obj.get("value"))
        description = from_union([Close.from_dict, from_none], obj.get("description"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Option(text, value, description, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([lambda x: to_class(Close, x), from_none], self.text)
        result["value"] = from_union([from_str, from_none], self.value)
        result["description"] = from_union([lambda x: to_class(Close, x), from_none], self.description)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class Style:
    bold: Optional[bool] = None
    italic: Optional[bool] = None
    strike: Optional[bool] = None
    highlight: Optional[bool] = None
    client_highlight: Optional[bool] = None
    underline: Optional[bool] = None
    unlink: Optional[bool] = None
    code: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Style':
        assert isinstance(obj, dict)
        bold = from_union([from_bool, from_none], obj.get("bold"))
        italic = from_union([from_bool, from_none], obj.get("italic"))
        strike = from_union([from_bool, from_none], obj.get("strike"))
        highlight = from_union([from_bool, from_none], obj.get("highlight"))
        client_highlight = from_union([from_bool, from_none], obj.get("client_highlight"))
        underline = from_union([from_bool, from_none], obj.get("underline"))
        unlink = from_union([from_bool, from_none], obj.get("unlink"))
        code = from_union([from_bool, from_none], obj.get("code"))
        return Style(bold, italic, strike, highlight, client_highlight, underline, unlink, code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bold"] = from_union([from_bool, from_none], self.bold)
        result["italic"] = from_union([from_bool, from_none], self.italic)
        result["strike"] = from_union([from_bool, from_none], self.strike)
        result["highlight"] = from_union([from_bool, from_none], self.highlight)
        result["client_highlight"] = from_union([from_bool, from_none], self.client_highlight)
        result["underline"] = from_union([from_bool, from_none], self.underline)
        result["unlink"] = from_union([from_bool, from_none], self.unlink)
        result["code"] = from_union([from_bool, from_none], self.code)
        return result


class ElementType(Enum):
    BROADCAST = "broadcast"
    CHANNEL = "channel"
    COLOR = "color"
    DATE = "date"
    EMOJI = "emoji"
    LINK = "link"
    TEAM = "team"
    TEXT = "text"
    USER = "user"
    USERGROUP = "usergroup"


@dataclass
class TentacledElement:
    type: Optional[ElementType] = None
    range: Optional[str] = None
    style: Optional[Style] = None
    text: Optional[str] = None
    channel_id: Optional[str] = None
    value: Optional[str] = None
    timestamp: Optional[int] = None
    format: Optional[str] = None
    url: Optional[str] = None
    fallback: Optional[str] = None
    unsafe: Optional[bool] = None
    team_id: Optional[str] = None
    user_id: Optional[str] = None
    usergroup_id: Optional[str] = None
    name: Optional[str] = None
    skin_tone: Optional[int] = None
    unicode: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledElement':
        assert isinstance(obj, dict)
        type = from_union([ElementType, from_none], obj.get("type"))
        range = from_union([from_str, from_none], obj.get("range"))
        style = from_union([Style.from_dict, from_none], obj.get("style"))
        text = from_union([from_str, from_none], obj.get("text"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        value = from_union([from_str, from_none], obj.get("value"))
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        format = from_union([from_str, from_none], obj.get("format"))
        url = from_union([from_str, from_none], obj.get("url"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        unsafe = from_union([from_bool, from_none], obj.get("unsafe"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        usergroup_id = from_union([from_str, from_none], obj.get("usergroup_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        skin_tone = from_union([from_int, from_none], obj.get("skin_tone"))
        unicode = from_union([from_str, from_none], obj.get("unicode"))
        return TentacledElement(type, range, style, text, channel_id, value, timestamp, format, url, fallback, unsafe, team_id, user_id, usergroup_id, name, skin_tone, unicode)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: to_enum(ElementType, x), from_none], self.type)
        result["range"] = from_union([from_str, from_none], self.range)
        result["style"] = from_union([lambda x: to_class(Style, x), from_none], self.style)
        result["text"] = from_union([from_str, from_none], self.text)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["value"] = from_union([from_str, from_none], self.value)
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        result["format"] = from_union([from_str, from_none], self.format)
        result["url"] = from_union([from_str, from_none], self.url)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["unsafe"] = from_union([from_bool, from_none], self.unsafe)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["usergroup_id"] = from_union([from_str, from_none], self.usergroup_id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["skin_tone"] = from_union([from_int, from_none], self.skin_tone)
        result["unicode"] = from_union([from_str, from_none], self.unicode)
        return result


@dataclass
class FluffyElement:
    type: Optional[str] = None
    elements: Optional[List[TentacledElement]] = None
    style: Optional[str] = None
    indent: Optional[int] = None
    offset: Optional[int] = None
    border: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyElement':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        elements = from_union([lambda x: from_list(TentacledElement.from_dict, x), from_none], obj.get("elements"))
        style = from_union([from_str, from_none], obj.get("style"))
        indent = from_union([from_int, from_none], obj.get("indent"))
        offset = from_union([from_int, from_none], obj.get("offset"))
        border = from_union([from_int, from_none], obj.get("border"))
        return FluffyElement(type, elements, style, indent, offset, border)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(TentacledElement, x), x), from_none], self.elements)
        result["style"] = from_union([from_str, from_none], self.style)
        result["indent"] = from_union([from_int, from_none], self.indent)
        result["offset"] = from_union([from_int, from_none], self.offset)
        result["border"] = from_union([from_int, from_none], self.border)
        return result


@dataclass
class InitialValueElement:
    type: Optional[str] = None
    elements: Optional[List[FluffyElement]] = None
    style: Optional[str] = None
    indent: Optional[int] = None
    offset: Optional[int] = None
    border: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InitialValueElement':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        elements = from_union([lambda x: from_list(FluffyElement.from_dict, x), from_none], obj.get("elements"))
        style = from_union([from_str, from_none], obj.get("style"))
        indent = from_union([from_int, from_none], obj.get("indent"))
        offset = from_union([from_int, from_none], obj.get("offset"))
        border = from_union([from_int, from_none], obj.get("border"))
        return InitialValueElement(type, elements, style, indent, offset, border)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(FluffyElement, x), x), from_none], self.elements)
        result["style"] = from_union([from_str, from_none], self.style)
        result["indent"] = from_union([from_int, from_none], self.indent)
        result["offset"] = from_union([from_int, from_none], self.offset)
        result["border"] = from_union([from_int, from_none], self.border)
        return result


@dataclass
class InitialValueClass:
    type: Optional[str] = None
    elements: Optional[List[InitialValueElement]] = None
    block_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InitialValueClass':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        elements = from_union([lambda x: from_list(InitialValueElement.from_dict, x), from_none], obj.get("elements"))
        block_id = from_union([from_str, from_none], obj.get("block_id"))
        return InitialValueClass(type, elements, block_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(InitialValueElement, x), x), from_none], self.elements)
        result["block_id"] = from_union([from_str, from_none], self.block_id)
        return result


@dataclass
class OptionGroup:
    label: Optional[Close] = None
    options: Optional[List[Option]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OptionGroup':
        assert isinstance(obj, dict)
        label = from_union([Close.from_dict, from_none], obj.get("label"))
        options = from_union([lambda x: from_list(Option.from_dict, x), from_none], obj.get("options"))
        return OptionGroup(label, options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["label"] = from_union([lambda x: to_class(Close, x), from_none], self.label)
        result["options"] = from_union([lambda x: from_list(lambda x: to_class(Option, x), x), from_none], self.options)
        return result


@dataclass
class PurpleElement:
    initial_value: Union[InitialValueClass, None, str]
    type: Optional[str] = None
    action_id: Optional[str] = None
    dispatch_action_config: Optional[DispatchActionConfig] = None
    focus_on_load: Optional[bool] = None
    placeholder: Optional[Close] = None
    multiline: Optional[bool] = None
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    options: Optional[List[Option]] = None
    initial_option: Optional[Option] = None
    confirm: Optional[Confirm] = None
    text: Optional[Close] = None
    url: Optional[str] = None
    value: Optional[str] = None
    style: Optional[str] = None
    accessibility_label: Optional[str] = None
    initial_channel: Optional[str] = None
    response_url_enabled: Optional[bool] = None
    initial_conversation: Optional[str] = None
    default_to_current_conversation: Optional[bool] = None
    filter: Optional[Filter] = None
    initial_date: Optional[str] = None
    initial_time: Optional[str] = None
    timezone: Optional[str] = None
    initial_date_time: Optional[int] = None
    min_query_length: Optional[int] = None
    image_url: Optional[str] = None
    alt_text: Optional[str] = None
    fallback: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    slack_file: Optional[SlackFile] = None
    option_groups: Optional[List[OptionGroup]] = None
    initial_user: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleElement':
        assert isinstance(obj, dict)
        initial_value = from_union([InitialValueClass.from_dict, from_str, from_none], obj.get("initial_value"))
        type = from_union([from_str, from_none], obj.get("type"))
        action_id = from_union([from_str, from_none], obj.get("action_id"))
        dispatch_action_config = from_union([DispatchActionConfig.from_dict, from_none], obj.get("dispatch_action_config"))
        focus_on_load = from_union([from_bool, from_none], obj.get("focus_on_load"))
        placeholder = from_union([Close.from_dict, from_none], obj.get("placeholder"))
        multiline = from_union([from_bool, from_none], obj.get("multiline"))
        min_length = from_union([from_int, from_none], obj.get("min_length"))
        max_length = from_union([from_int, from_none], obj.get("max_length"))
        options = from_union([lambda x: from_list(Option.from_dict, x), from_none], obj.get("options"))
        initial_option = from_union([Option.from_dict, from_none], obj.get("initial_option"))
        confirm = from_union([Confirm.from_dict, from_none], obj.get("confirm"))
        text = from_union([Close.from_dict, from_none], obj.get("text"))
        url = from_union([from_str, from_none], obj.get("url"))
        value = from_union([from_str, from_none], obj.get("value"))
        style = from_union([from_str, from_none], obj.get("style"))
        accessibility_label = from_union([from_str, from_none], obj.get("accessibility_label"))
        initial_channel = from_union([from_str, from_none], obj.get("initial_channel"))
        response_url_enabled = from_union([from_bool, from_none], obj.get("response_url_enabled"))
        initial_conversation = from_union([from_str, from_none], obj.get("initial_conversation"))
        default_to_current_conversation = from_union([from_bool, from_none], obj.get("default_to_current_conversation"))
        filter = from_union([Filter.from_dict, from_none], obj.get("filter"))
        initial_date = from_union([from_str, from_none], obj.get("initial_date"))
        initial_time = from_union([from_str, from_none], obj.get("initial_time"))
        timezone = from_union([from_str, from_none], obj.get("timezone"))
        initial_date_time = from_union([from_int, from_none], obj.get("initial_date_time"))
        min_query_length = from_union([from_int, from_none], obj.get("min_query_length"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        slack_file = from_union([SlackFile.from_dict, from_none], obj.get("slack_file"))
        option_groups = from_union([lambda x: from_list(OptionGroup.from_dict, x), from_none], obj.get("option_groups"))
        initial_user = from_union([from_str, from_none], obj.get("initial_user"))
        return PurpleElement(initial_value, type, action_id, dispatch_action_config, focus_on_load, placeholder, multiline, min_length, max_length, options, initial_option, confirm, text, url, value, style, accessibility_label, initial_channel, response_url_enabled, initial_conversation, default_to_current_conversation, filter, initial_date, initial_time, timezone, initial_date_time, min_query_length, image_url, alt_text, fallback, image_width, image_height, image_bytes, slack_file, option_groups, initial_user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["initial_value"] = from_union([lambda x: to_class(InitialValueClass, x), from_str, from_none], self.initial_value)
        result["type"] = from_union([from_str, from_none], self.type)
        result["action_id"] = from_union([from_str, from_none], self.action_id)
        result["dispatch_action_config"] = from_union([lambda x: to_class(DispatchActionConfig, x), from_none], self.dispatch_action_config)
        result["focus_on_load"] = from_union([from_bool, from_none], self.focus_on_load)
        result["placeholder"] = from_union([lambda x: to_class(Close, x), from_none], self.placeholder)
        result["multiline"] = from_union([from_bool, from_none], self.multiline)
        result["min_length"] = from_union([from_int, from_none], self.min_length)
        result["max_length"] = from_union([from_int, from_none], self.max_length)
        result["options"] = from_union([lambda x: from_list(lambda x: to_class(Option, x), x), from_none], self.options)
        result["initial_option"] = from_union([lambda x: to_class(Option, x), from_none], self.initial_option)
        result["confirm"] = from_union([lambda x: to_class(Confirm, x), from_none], self.confirm)
        result["text"] = from_union([lambda x: to_class(Close, x), from_none], self.text)
        result["url"] = from_union([from_str, from_none], self.url)
        result["value"] = from_union([from_str, from_none], self.value)
        result["style"] = from_union([from_str, from_none], self.style)
        result["accessibility_label"] = from_union([from_str, from_none], self.accessibility_label)
        result["initial_channel"] = from_union([from_str, from_none], self.initial_channel)
        result["response_url_enabled"] = from_union([from_bool, from_none], self.response_url_enabled)
        result["initial_conversation"] = from_union([from_str, from_none], self.initial_conversation)
        result["default_to_current_conversation"] = from_union([from_bool, from_none], self.default_to_current_conversation)
        result["filter"] = from_union([lambda x: to_class(Filter, x), from_none], self.filter)
        result["initial_date"] = from_union([from_str, from_none], self.initial_date)
        result["initial_time"] = from_union([from_str, from_none], self.initial_time)
        result["timezone"] = from_union([from_str, from_none], self.timezone)
        result["initial_date_time"] = from_union([from_int, from_none], self.initial_date_time)
        result["min_query_length"] = from_union([from_int, from_none], self.min_query_length)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["slack_file"] = from_union([lambda x: to_class(SlackFile, x), from_none], self.slack_file)
        result["option_groups"] = from_union([lambda x: from_list(lambda x: to_class(OptionGroup, x), x), from_none], self.option_groups)
        result["initial_user"] = from_union([from_str, from_none], self.initial_user)
        return result


@dataclass
class CustomizableInputParameter:
    name: Optional[str] = None
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CustomizableInputParameter':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        value = from_union([from_str, from_none], obj.get("value"))
        return CustomizableInputParameter(name, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["value"] = from_union([from_str, from_none], self.value)
        return result


@dataclass
class Trigger:
    url: Optional[str] = None
    customizable_input_parameters: Optional[List[CustomizableInputParameter]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Trigger':
        assert isinstance(obj, dict)
        url = from_union([from_str, from_none], obj.get("url"))
        customizable_input_parameters = from_union([lambda x: from_list(CustomizableInputParameter.from_dict, x), from_none], obj.get("customizable_input_parameters"))
        return Trigger(url, customizable_input_parameters)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_union([from_str, from_none], self.url)
        result["customizable_input_parameters"] = from_union([lambda x: from_list(lambda x: to_class(CustomizableInputParameter, x), x), from_none], self.customizable_input_parameters)
        return result


@dataclass
class Workflow:
    trigger: Optional[Trigger] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Workflow':
        assert isinstance(obj, dict)
        trigger = from_union([Trigger.from_dict, from_none], obj.get("trigger"))
        return Workflow(trigger)

    def to_dict(self) -> dict:
        result: dict = {}
        result["trigger"] = from_union([lambda x: to_class(Trigger, x), from_none], self.trigger)
        return result


@dataclass
class StickyElement:
    type: Optional[str] = None
    text: Optional[Close] = None
    action_id: Optional[str] = None
    url: Optional[str] = None
    value: Optional[str] = None
    style: Optional[str] = None
    confirm: Optional[Confirm] = None
    accessibility_label: Optional[str] = None
    workflow: Optional[Workflow] = None
    options: Optional[List[Option]] = None
    initial_options: Optional[List[Option]] = None
    focus_on_load: Optional[bool] = None
    initial_option: Optional[Option] = None
    placeholder: Optional[Close] = None
    initial_channel: Optional[str] = None
    response_url_enabled: Optional[bool] = None
    initial_channels: Optional[List[str]] = None
    max_selected_items: Optional[int] = None
    initial_conversation: Optional[str] = None
    default_to_current_conversation: Optional[bool] = None
    filter: Optional[Filter] = None
    initial_conversations: Optional[List[str]] = None
    initial_date: Optional[str] = None
    initial_time: Optional[str] = None
    timezone: Optional[str] = None
    initial_date_time: Optional[int] = None
    min_query_length: Optional[int] = None
    image_url: Optional[str] = None
    alt_text: Optional[str] = None
    fallback: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    slack_file: Optional[SlackFile] = None
    option_groups: Optional[List[OptionGroup]] = None
    initial_user: Optional[str] = None
    initial_users: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StickyElement':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        text = from_union([Close.from_dict, from_none], obj.get("text"))
        action_id = from_union([from_str, from_none], obj.get("action_id"))
        url = from_union([from_str, from_none], obj.get("url"))
        value = from_union([from_str, from_none], obj.get("value"))
        style = from_union([from_str, from_none], obj.get("style"))
        confirm = from_union([Confirm.from_dict, from_none], obj.get("confirm"))
        accessibility_label = from_union([from_str, from_none], obj.get("accessibility_label"))
        workflow = from_union([Workflow.from_dict, from_none], obj.get("workflow"))
        options = from_union([lambda x: from_list(Option.from_dict, x), from_none], obj.get("options"))
        initial_options = from_union([lambda x: from_list(Option.from_dict, x), from_none], obj.get("initial_options"))
        focus_on_load = from_union([from_bool, from_none], obj.get("focus_on_load"))
        initial_option = from_union([Option.from_dict, from_none], obj.get("initial_option"))
        placeholder = from_union([Close.from_dict, from_none], obj.get("placeholder"))
        initial_channel = from_union([from_str, from_none], obj.get("initial_channel"))
        response_url_enabled = from_union([from_bool, from_none], obj.get("response_url_enabled"))
        initial_channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("initial_channels"))
        max_selected_items = from_union([from_int, from_none], obj.get("max_selected_items"))
        initial_conversation = from_union([from_str, from_none], obj.get("initial_conversation"))
        default_to_current_conversation = from_union([from_bool, from_none], obj.get("default_to_current_conversation"))
        filter = from_union([Filter.from_dict, from_none], obj.get("filter"))
        initial_conversations = from_union([lambda x: from_list(from_str, x), from_none], obj.get("initial_conversations"))
        initial_date = from_union([from_str, from_none], obj.get("initial_date"))
        initial_time = from_union([from_str, from_none], obj.get("initial_time"))
        timezone = from_union([from_str, from_none], obj.get("timezone"))
        initial_date_time = from_union([from_int, from_none], obj.get("initial_date_time"))
        min_query_length = from_union([from_int, from_none], obj.get("min_query_length"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        slack_file = from_union([SlackFile.from_dict, from_none], obj.get("slack_file"))
        option_groups = from_union([lambda x: from_list(OptionGroup.from_dict, x), from_none], obj.get("option_groups"))
        initial_user = from_union([from_str, from_none], obj.get("initial_user"))
        initial_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("initial_users"))
        return StickyElement(type, text, action_id, url, value, style, confirm, accessibility_label, workflow, options, initial_options, focus_on_load, initial_option, placeholder, initial_channel, response_url_enabled, initial_channels, max_selected_items, initial_conversation, default_to_current_conversation, filter, initial_conversations, initial_date, initial_time, timezone, initial_date_time, min_query_length, image_url, alt_text, fallback, image_width, image_height, image_bytes, slack_file, option_groups, initial_user, initial_users)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["text"] = from_union([lambda x: to_class(Close, x), from_none], self.text)
        result["action_id"] = from_union([from_str, from_none], self.action_id)
        result["url"] = from_union([from_str, from_none], self.url)
        result["value"] = from_union([from_str, from_none], self.value)
        result["style"] = from_union([from_str, from_none], self.style)
        result["confirm"] = from_union([lambda x: to_class(Confirm, x), from_none], self.confirm)
        result["accessibility_label"] = from_union([from_str, from_none], self.accessibility_label)
        result["workflow"] = from_union([lambda x: to_class(Workflow, x), from_none], self.workflow)
        result["options"] = from_union([lambda x: from_list(lambda x: to_class(Option, x), x), from_none], self.options)
        result["initial_options"] = from_union([lambda x: from_list(lambda x: to_class(Option, x), x), from_none], self.initial_options)
        result["focus_on_load"] = from_union([from_bool, from_none], self.focus_on_load)
        result["initial_option"] = from_union([lambda x: to_class(Option, x), from_none], self.initial_option)
        result["placeholder"] = from_union([lambda x: to_class(Close, x), from_none], self.placeholder)
        result["initial_channel"] = from_union([from_str, from_none], self.initial_channel)
        result["response_url_enabled"] = from_union([from_bool, from_none], self.response_url_enabled)
        result["initial_channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.initial_channels)
        result["max_selected_items"] = from_union([from_int, from_none], self.max_selected_items)
        result["initial_conversation"] = from_union([from_str, from_none], self.initial_conversation)
        result["default_to_current_conversation"] = from_union([from_bool, from_none], self.default_to_current_conversation)
        result["filter"] = from_union([lambda x: to_class(Filter, x), from_none], self.filter)
        result["initial_conversations"] = from_union([lambda x: from_list(from_str, x), from_none], self.initial_conversations)
        result["initial_date"] = from_union([from_str, from_none], self.initial_date)
        result["initial_time"] = from_union([from_str, from_none], self.initial_time)
        result["timezone"] = from_union([from_str, from_none], self.timezone)
        result["initial_date_time"] = from_union([from_int, from_none], self.initial_date_time)
        result["min_query_length"] = from_union([from_int, from_none], self.min_query_length)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["slack_file"] = from_union([lambda x: to_class(SlackFile, x), from_none], self.slack_file)
        result["option_groups"] = from_union([lambda x: from_list(lambda x: to_class(OptionGroup, x), x), from_none], self.option_groups)
        result["initial_user"] = from_union([from_str, from_none], self.initial_user)
        result["initial_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.initial_users)
        return result


@dataclass
class Block:
    type: Optional[str] = None
    block_id: Optional[str] = None
    label: Optional[Close] = None
    element: Optional[PurpleElement] = None
    dispatch_action: Optional[bool] = None
    hint: Optional[Close] = None
    optional: Optional[bool] = None
    elements: Optional[List[StickyElement]] = None
    fallback: Optional[str] = None
    image_url: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    is_animated: Optional[bool] = None
    slack_file: Optional[SlackFile] = None
    alt_text: Optional[str] = None
    title: Optional[Close] = None
    title_url: Optional[str] = None
    description: Optional[Close] = None
    video_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    author_name: Optional[str] = None
    provider_name: Optional[str] = None
    provider_icon_url: Optional[str] = None
    text: Optional[Close] = None
    fields: Optional[List[Close]] = None
    accessory: Optional[Accessory] = None
    expand: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Block':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        block_id = from_union([from_str, from_none], obj.get("block_id"))
        label = from_union([Close.from_dict, from_none], obj.get("label"))
        element = from_union([PurpleElement.from_dict, from_none], obj.get("element"))
        dispatch_action = from_union([from_bool, from_none], obj.get("dispatch_action"))
        hint = from_union([Close.from_dict, from_none], obj.get("hint"))
        optional = from_union([from_bool, from_none], obj.get("optional"))
        elements = from_union([lambda x: from_list(StickyElement.from_dict, x), from_none], obj.get("elements"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        is_animated = from_union([from_bool, from_none], obj.get("is_animated"))
        slack_file = from_union([SlackFile.from_dict, from_none], obj.get("slack_file"))
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        title = from_union([Close.from_dict, from_none], obj.get("title"))
        title_url = from_union([from_str, from_none], obj.get("title_url"))
        description = from_union([Close.from_dict, from_none], obj.get("description"))
        video_url = from_union([from_str, from_none], obj.get("video_url"))
        thumbnail_url = from_union([from_str, from_none], obj.get("thumbnail_url"))
        author_name = from_union([from_str, from_none], obj.get("author_name"))
        provider_name = from_union([from_str, from_none], obj.get("provider_name"))
        provider_icon_url = from_union([from_str, from_none], obj.get("provider_icon_url"))
        text = from_union([Close.from_dict, from_none], obj.get("text"))
        fields = from_union([lambda x: from_list(Close.from_dict, x), from_none], obj.get("fields"))
        accessory = from_union([Accessory.from_dict, from_none], obj.get("accessory"))
        expand = from_union([from_bool, from_none], obj.get("expand"))
        return Block(type, block_id, label, element, dispatch_action, hint, optional, elements, fallback, image_url, image_width, image_height, image_bytes, is_animated, slack_file, alt_text, title, title_url, description, video_url, thumbnail_url, author_name, provider_name, provider_icon_url, text, fields, accessory, expand)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["block_id"] = from_union([from_str, from_none], self.block_id)
        result["label"] = from_union([lambda x: to_class(Close, x), from_none], self.label)
        result["element"] = from_union([lambda x: to_class(PurpleElement, x), from_none], self.element)
        result["dispatch_action"] = from_union([from_bool, from_none], self.dispatch_action)
        result["hint"] = from_union([lambda x: to_class(Close, x), from_none], self.hint)
        result["optional"] = from_union([from_bool, from_none], self.optional)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(StickyElement, x), x), from_none], self.elements)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["is_animated"] = from_union([from_bool, from_none], self.is_animated)
        result["slack_file"] = from_union([lambda x: to_class(SlackFile, x), from_none], self.slack_file)
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["title"] = from_union([lambda x: to_class(Close, x), from_none], self.title)
        result["title_url"] = from_union([from_str, from_none], self.title_url)
        result["description"] = from_union([lambda x: to_class(Close, x), from_none], self.description)
        result["video_url"] = from_union([from_str, from_none], self.video_url)
        result["thumbnail_url"] = from_union([from_str, from_none], self.thumbnail_url)
        result["author_name"] = from_union([from_str, from_none], self.author_name)
        result["provider_name"] = from_union([from_str, from_none], self.provider_name)
        result["provider_icon_url"] = from_union([from_str, from_none], self.provider_icon_url)
        result["text"] = from_union([lambda x: to_class(Close, x), from_none], self.text)
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(Close, x), x), from_none], self.fields)
        result["accessory"] = from_union([lambda x: to_class(Accessory, x), from_none], self.accessory)
        result["expand"] = from_union([from_bool, from_none], self.expand)
        return result


@dataclass
class ExternalRef:
    id: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ExternalRef':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        type = from_union([from_str, from_none], obj.get("type"))
        return ExternalRef(id, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class State:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'State':
        assert isinstance(obj, dict)
        return State()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class View:
    id: Optional[str] = None
    team_id: Optional[str] = None
    type: Optional[str] = None
    title: Optional[Close] = None
    submit: Optional[Close] = None
    close: Optional[Close] = None
    blocks: Optional[List[Block]] = None
    private_metadata: Optional[str] = None
    callback_id: Optional[str] = None
    external_id: Optional[str] = None
    state: Optional[State] = None
    hash: Optional[str] = None
    clear_on_close: Optional[bool] = None
    notify_on_close: Optional[bool] = None
    submit_disabled: Optional[bool] = None
    root_view_id: Optional[str] = None
    previous_view_id: Optional[str] = None
    app_id: Optional[str] = None
    app_installed_team_id: Optional[str] = None
    bot_id: Optional[str] = None
    entity_url: Optional[str] = None
    external_ref: Optional[ExternalRef] = None
    app_unfurl_url: Optional[str] = None
    message_ts: Optional[str] = None
    thread_ts: Optional[str] = None
    channel: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'View':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        title = from_union([Close.from_dict, from_none], obj.get("title"))
        submit = from_union([Close.from_dict, from_none], obj.get("submit"))
        close = from_union([Close.from_dict, from_none], obj.get("close"))
        blocks = from_union([lambda x: from_list(Block.from_dict, x), from_none], obj.get("blocks"))
        private_metadata = from_union([from_str, from_none], obj.get("private_metadata"))
        callback_id = from_union([from_str, from_none], obj.get("callback_id"))
        external_id = from_union([from_str, from_none], obj.get("external_id"))
        state = from_union([State.from_dict, from_none], obj.get("state"))
        hash = from_union([from_str, from_none], obj.get("hash"))
        clear_on_close = from_union([from_bool, from_none], obj.get("clear_on_close"))
        notify_on_close = from_union([from_bool, from_none], obj.get("notify_on_close"))
        submit_disabled = from_union([from_bool, from_none], obj.get("submit_disabled"))
        root_view_id = from_union([from_str, from_none], obj.get("root_view_id"))
        previous_view_id = from_union([from_str, from_none], obj.get("previous_view_id"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        app_installed_team_id = from_union([from_str, from_none], obj.get("app_installed_team_id"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        entity_url = from_union([from_str, from_none], obj.get("entity_url"))
        external_ref = from_union([ExternalRef.from_dict, from_none], obj.get("external_ref"))
        app_unfurl_url = from_union([from_str, from_none], obj.get("app_unfurl_url"))
        message_ts = from_union([from_str, from_none], obj.get("message_ts"))
        thread_ts = from_union([from_str, from_none], obj.get("thread_ts"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        return View(id, team_id, type, title, submit, close, blocks, private_metadata, callback_id, external_id, state, hash, clear_on_close, notify_on_close, submit_disabled, root_view_id, previous_view_id, app_id, app_installed_team_id, bot_id, entity_url, external_ref, app_unfurl_url, message_ts, thread_ts, channel)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["title"] = from_union([lambda x: to_class(Close, x), from_none], self.title)
        result["submit"] = from_union([lambda x: to_class(Close, x), from_none], self.submit)
        result["close"] = from_union([lambda x: to_class(Close, x), from_none], self.close)
        result["blocks"] = from_union([lambda x: from_list(lambda x: to_class(Block, x), x), from_none], self.blocks)
        result["private_metadata"] = from_union([from_str, from_none], self.private_metadata)
        result["callback_id"] = from_union([from_str, from_none], self.callback_id)
        result["external_id"] = from_union([from_str, from_none], self.external_id)
        result["state"] = from_union([lambda x: to_class(State, x), from_none], self.state)
        result["hash"] = from_union([from_str, from_none], self.hash)
        result["clear_on_close"] = from_union([from_bool, from_none], self.clear_on_close)
        result["notify_on_close"] = from_union([from_bool, from_none], self.notify_on_close)
        result["submit_disabled"] = from_union([from_bool, from_none], self.submit_disabled)
        result["root_view_id"] = from_union([from_str, from_none], self.root_view_id)
        result["previous_view_id"] = from_union([from_str, from_none], self.previous_view_id)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["app_installed_team_id"] = from_union([from_str, from_none], self.app_installed_team_id)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["entity_url"] = from_union([from_str, from_none], self.entity_url)
        result["external_ref"] = from_union([lambda x: to_class(ExternalRef, x), from_none], self.external_ref)
        result["app_unfurl_url"] = from_union([from_str, from_none], self.app_unfurl_url)
        result["message_ts"] = from_union([from_str, from_none], self.message_ts)
        result["thread_ts"] = from_union([from_str, from_none], self.thread_ts)
        result["channel"] = from_union([from_str, from_none], self.channel)
        return result


@dataclass
class ViewsPublishResponse:
    ok: Optional[bool] = None
    warning: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    view: Optional[View] = None
    response_metadata: Optional[ResponseMetadata] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ViewsPublishResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        view = from_union([View.from_dict, from_none], obj.get("view"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        return ViewsPublishResponse(ok, warning, error, needed, provided, view, response_metadata)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["warning"] = from_union([from_str, from_none], self.warning)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["view"] = from_union([lambda x: to_class(View, x), from_none], self.view)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        return result


def views_publish_response_from_dict(s: Any) -> ViewsPublishResponse:
    return ViewsPublishResponse.from_dict(s)


def views_publish_response_to_dict(x: ViewsPublishResponse) -> Any:
    return to_class(ViewsPublishResponse, x)

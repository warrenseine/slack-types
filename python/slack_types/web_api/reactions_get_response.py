# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = reactions_get_response_from_dict(json.loads(json_string))

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, Union, Dict, TypeVar, Type, cast, Callable


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


class DescriptionType(Enum):
    MRKDWN = "mrkdwn"
    PLAIN_TEXT = "plain_text"


@dataclass
class DescriptionElement:
    type: Optional[DescriptionType] = None
    text: Optional[str] = None
    emoji: Optional[bool] = None
    verbatim: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DescriptionElement':
        assert isinstance(obj, dict)
        type = from_union([DescriptionType, from_none], obj.get("type"))
        text = from_union([from_str, from_none], obj.get("text"))
        emoji = from_union([from_bool, from_none], obj.get("emoji"))
        verbatim = from_union([from_bool, from_none], obj.get("verbatim"))
        return DescriptionElement(type, text, emoji, verbatim)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: to_enum(DescriptionType, x), from_none], self.type)
        result["text"] = from_union([from_str, from_none], self.text)
        result["emoji"] = from_union([from_bool, from_none], self.emoji)
        result["verbatim"] = from_union([from_bool, from_none], self.verbatim)
        return result


@dataclass
class Confirm:
    title: Optional[DescriptionElement] = None
    text: Optional[DescriptionElement] = None
    confirm: Optional[DescriptionElement] = None
    deny: Optional[DescriptionElement] = None
    style: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Confirm':
        assert isinstance(obj, dict)
        title = from_union([DescriptionElement.from_dict, from_none], obj.get("title"))
        text = from_union([DescriptionElement.from_dict, from_none], obj.get("text"))
        confirm = from_union([DescriptionElement.from_dict, from_none], obj.get("confirm"))
        deny = from_union([DescriptionElement.from_dict, from_none], obj.get("deny"))
        style = from_union([from_str, from_none], obj.get("style"))
        return Confirm(title, text, confirm, deny, style)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.title)
        result["text"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.text)
        result["confirm"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.confirm)
        result["deny"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.deny)
        result["style"] = from_union([from_str, from_none], self.style)
        return result


@dataclass
class Style:
    bold: Optional[bool] = None
    italic: Optional[bool] = None
    strike: Optional[bool] = None
    highlight: Optional[bool] = None
    client_highlight: Optional[bool] = None
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
        unlink = from_union([from_bool, from_none], obj.get("unlink"))
        code = from_union([from_bool, from_none], obj.get("code"))
        return Style(bold, italic, strike, highlight, client_highlight, unlink, code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bold"] = from_union([from_bool, from_none], self.bold)
        result["italic"] = from_union([from_bool, from_none], self.italic)
        result["strike"] = from_union([from_bool, from_none], self.strike)
        result["highlight"] = from_union([from_bool, from_none], self.highlight)
        result["client_highlight"] = from_union([from_bool, from_none], self.client_highlight)
        result["unlink"] = from_union([from_bool, from_none], self.unlink)
        result["code"] = from_union([from_bool, from_none], self.code)
        return result


class PurpleType(Enum):
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
class PurpleElement:
    type: Optional[PurpleType] = None
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
    def from_dict(obj: Any) -> 'PurpleElement':
        assert isinstance(obj, dict)
        type = from_union([PurpleType, from_none], obj.get("type"))
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
        return PurpleElement(type, range, style, text, channel_id, value, timestamp, format, url, fallback, unsafe, team_id, user_id, usergroup_id, name, skin_tone, unicode)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: to_enum(PurpleType, x), from_none], self.type)
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


class FluffyType(Enum):
    RICH_TEXT_LIST = "rich_text_list"
    RICH_TEXT_PREFORMATTED = "rich_text_preformatted"
    RICH_TEXT_QUOTE = "rich_text_quote"
    RICH_TEXT_SECTION = "rich_text_section"


@dataclass
class AccessoryElement:
    type: Optional[FluffyType] = None
    elements: Optional[List[PurpleElement]] = None
    style: Optional[str] = None
    indent: Optional[int] = None
    offset: Optional[int] = None
    border: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AccessoryElement':
        assert isinstance(obj, dict)
        type = from_union([FluffyType, from_none], obj.get("type"))
        elements = from_union([lambda x: from_list(PurpleElement.from_dict, x), from_none], obj.get("elements"))
        style = from_union([from_str, from_none], obj.get("style"))
        indent = from_union([from_int, from_none], obj.get("indent"))
        offset = from_union([from_int, from_none], obj.get("offset"))
        border = from_union([from_int, from_none], obj.get("border"))
        return AccessoryElement(type, elements, style, indent, offset, border)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: to_enum(FluffyType, x), from_none], self.type)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(PurpleElement, x), x), from_none], self.elements)
        result["style"] = from_union([from_str, from_none], self.style)
        result["indent"] = from_union([from_int, from_none], self.indent)
        result["offset"] = from_union([from_int, from_none], self.offset)
        result["border"] = from_union([from_int, from_none], self.border)
        return result


@dataclass
class AccessoryFilter:
    include: Optional[List[Any]] = None
    exclude_external_shared_channels: Optional[bool] = None
    exclude_bot_users: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AccessoryFilter':
        assert isinstance(obj, dict)
        include = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("include"))
        exclude_external_shared_channels = from_union([from_bool, from_none], obj.get("exclude_external_shared_channels"))
        exclude_bot_users = from_union([from_bool, from_none], obj.get("exclude_bot_users"))
        return AccessoryFilter(include, exclude_external_shared_channels, exclude_bot_users)

    def to_dict(self) -> dict:
        result: dict = {}
        result["include"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.include)
        result["exclude_external_shared_channels"] = from_union([from_bool, from_none], self.exclude_external_shared_channels)
        result["exclude_bot_users"] = from_union([from_bool, from_none], self.exclude_bot_users)
        return result


@dataclass
class Option:
    text: Optional[DescriptionElement] = None
    value: Optional[str] = None
    description: Optional[DescriptionElement] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Option':
        assert isinstance(obj, dict)
        text = from_union([DescriptionElement.from_dict, from_none], obj.get("text"))
        value = from_union([from_str, from_none], obj.get("value"))
        description = from_union([DescriptionElement.from_dict, from_none], obj.get("description"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Option(text, value, description, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.text)
        result["value"] = from_union([from_str, from_none], self.value)
        result["description"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.description)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class OptionGroup:
    label: Optional[DescriptionElement] = None
    options: Optional[List[Option]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OptionGroup':
        assert isinstance(obj, dict)
        label = from_union([DescriptionElement.from_dict, from_none], obj.get("label"))
        options = from_union([lambda x: from_list(Option.from_dict, x), from_none], obj.get("options"))
        return OptionGroup(label, options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["label"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.label)
        result["options"] = from_union([lambda x: from_list(lambda x: to_class(Option, x), x), from_none], self.options)
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
class Accessory:
    type: Optional[str] = None
    text: Optional[DescriptionElement] = None
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
    placeholder: Optional[DescriptionElement] = None
    initial_channel: Optional[str] = None
    response_url_enabled: Optional[bool] = None
    initial_channels: Optional[List[str]] = None
    max_selected_items: Optional[int] = None
    initial_conversation: Optional[str] = None
    default_to_current_conversation: Optional[bool] = None
    filter: Optional[AccessoryFilter] = None
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
    elements: Optional[List[AccessoryElement]] = None
    indent: Optional[int] = None
    offset: Optional[int] = None
    border: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Accessory':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        text = from_union([DescriptionElement.from_dict, from_none], obj.get("text"))
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
        placeholder = from_union([DescriptionElement.from_dict, from_none], obj.get("placeholder"))
        initial_channel = from_union([from_str, from_none], obj.get("initial_channel"))
        response_url_enabled = from_union([from_bool, from_none], obj.get("response_url_enabled"))
        initial_channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("initial_channels"))
        max_selected_items = from_union([from_int, from_none], obj.get("max_selected_items"))
        initial_conversation = from_union([from_str, from_none], obj.get("initial_conversation"))
        default_to_current_conversation = from_union([from_bool, from_none], obj.get("default_to_current_conversation"))
        filter = from_union([AccessoryFilter.from_dict, from_none], obj.get("filter"))
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
        elements = from_union([lambda x: from_list(AccessoryElement.from_dict, x), from_none], obj.get("elements"))
        indent = from_union([from_int, from_none], obj.get("indent"))
        offset = from_union([from_int, from_none], obj.get("offset"))
        border = from_union([from_int, from_none], obj.get("border"))
        return Accessory(type, text, action_id, url, value, style, confirm, accessibility_label, workflow, options, initial_options, focus_on_load, initial_option, placeholder, initial_channel, response_url_enabled, initial_channels, max_selected_items, initial_conversation, default_to_current_conversation, filter, initial_conversations, initial_date, initial_time, timezone, initial_date_time, min_query_length, image_url, alt_text, fallback, image_width, image_height, image_bytes, slack_file, option_groups, initial_user, initial_users, elements, indent, offset, border)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["text"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.text)
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
        result["placeholder"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.placeholder)
        result["initial_channel"] = from_union([from_str, from_none], self.initial_channel)
        result["response_url_enabled"] = from_union([from_bool, from_none], self.response_url_enabled)
        result["initial_channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.initial_channels)
        result["max_selected_items"] = from_union([from_int, from_none], self.max_selected_items)
        result["initial_conversation"] = from_union([from_str, from_none], self.initial_conversation)
        result["default_to_current_conversation"] = from_union([from_bool, from_none], self.default_to_current_conversation)
        result["filter"] = from_union([lambda x: to_class(AccessoryFilter, x), from_none], self.filter)
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
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(AccessoryElement, x), x), from_none], self.elements)
        result["indent"] = from_union([from_int, from_none], self.indent)
        result["offset"] = from_union([from_int, from_none], self.offset)
        result["border"] = from_union([from_int, from_none], self.border)
        return result


@dataclass
class Participant:
    slack_id: Optional[str] = None
    external_id: Optional[str] = None
    display_name: Optional[str] = None
    avatar_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Participant':
        assert isinstance(obj, dict)
        slack_id = from_union([from_str, from_none], obj.get("slack_id"))
        external_id = from_union([from_str, from_none], obj.get("external_id"))
        display_name = from_union([from_str, from_none], obj.get("display_name"))
        avatar_url = from_union([from_str, from_none], obj.get("avatar_url"))
        return Participant(slack_id, external_id, display_name, avatar_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["slack_id"] = from_union([from_str, from_none], self.slack_id)
        result["external_id"] = from_union([from_str, from_none], self.external_id)
        result["display_name"] = from_union([from_str, from_none], self.display_name)
        result["avatar_url"] = from_union([from_str, from_none], self.avatar_url)
        return result


@dataclass
class AppIconUrls:
    image_32: Optional[str] = None
    image_36: Optional[str] = None
    image_48: Optional[str] = None
    image_64: Optional[str] = None
    image_72: Optional[str] = None
    image_96: Optional[str] = None
    image_128: Optional[str] = None
    image_192: Optional[str] = None
    image_512: Optional[str] = None
    image_1024: Optional[str] = None
    image_original: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AppIconUrls':
        assert isinstance(obj, dict)
        image_32 = from_union([from_str, from_none], obj.get("image_32"))
        image_36 = from_union([from_str, from_none], obj.get("image_36"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_64 = from_union([from_str, from_none], obj.get("image_64"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        image_96 = from_union([from_str, from_none], obj.get("image_96"))
        image_128 = from_union([from_str, from_none], obj.get("image_128"))
        image_192 = from_union([from_str, from_none], obj.get("image_192"))
        image_512 = from_union([from_str, from_none], obj.get("image_512"))
        image_1024 = from_union([from_str, from_none], obj.get("image_1024"))
        image_original = from_union([from_str, from_none], obj.get("image_original"))
        return AppIconUrls(image_32, image_36, image_48, image_64, image_72, image_96, image_128, image_192, image_512, image_1024, image_original)

    def to_dict(self) -> dict:
        result: dict = {}
        result["image_32"] = from_union([from_str, from_none], self.image_32)
        result["image_36"] = from_union([from_str, from_none], self.image_36)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_64"] = from_union([from_str, from_none], self.image_64)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        result["image_96"] = from_union([from_str, from_none], self.image_96)
        result["image_128"] = from_union([from_str, from_none], self.image_128)
        result["image_192"] = from_union([from_str, from_none], self.image_192)
        result["image_512"] = from_union([from_str, from_none], self.image_512)
        result["image_1024"] = from_union([from_str, from_none], self.image_1024)
        result["image_original"] = from_union([from_str, from_none], self.image_original)
        return result


@dataclass
class V1:
    id: Optional[str] = None
    app_id: Optional[str] = None
    app_icon_urls: Optional[AppIconUrls] = None
    date_start: Optional[int] = None
    active_participants: Optional[List[Participant]] = None
    all_participants: Optional[List[Participant]] = None
    display_id: Optional[str] = None
    join_url: Optional[str] = None
    desktop_app_join_url: Optional[str] = None
    name: Optional[str] = None
    created_by: Optional[str] = None
    date_end: Optional[int] = None
    channels: Optional[List[str]] = None
    is_dm_call: Optional[bool] = None
    was_rejected: Optional[bool] = None
    was_missed: Optional[bool] = None
    was_accepted: Optional[bool] = None
    has_ended: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'V1':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        app_icon_urls = from_union([AppIconUrls.from_dict, from_none], obj.get("app_icon_urls"))
        date_start = from_union([from_int, from_none], obj.get("date_start"))
        active_participants = from_union([lambda x: from_list(Participant.from_dict, x), from_none], obj.get("active_participants"))
        all_participants = from_union([lambda x: from_list(Participant.from_dict, x), from_none], obj.get("all_participants"))
        display_id = from_union([from_str, from_none], obj.get("display_id"))
        join_url = from_union([from_str, from_none], obj.get("join_url"))
        desktop_app_join_url = from_union([from_str, from_none], obj.get("desktop_app_join_url"))
        name = from_union([from_str, from_none], obj.get("name"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        date_end = from_union([from_int, from_none], obj.get("date_end"))
        channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channels"))
        is_dm_call = from_union([from_bool, from_none], obj.get("is_dm_call"))
        was_rejected = from_union([from_bool, from_none], obj.get("was_rejected"))
        was_missed = from_union([from_bool, from_none], obj.get("was_missed"))
        was_accepted = from_union([from_bool, from_none], obj.get("was_accepted"))
        has_ended = from_union([from_bool, from_none], obj.get("has_ended"))
        return V1(id, app_id, app_icon_urls, date_start, active_participants, all_participants, display_id, join_url, desktop_app_join_url, name, created_by, date_end, channels, is_dm_call, was_rejected, was_missed, was_accepted, has_ended)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["app_icon_urls"] = from_union([lambda x: to_class(AppIconUrls, x), from_none], self.app_icon_urls)
        result["date_start"] = from_union([from_int, from_none], self.date_start)
        result["active_participants"] = from_union([lambda x: from_list(lambda x: to_class(Participant, x), x), from_none], self.active_participants)
        result["all_participants"] = from_union([lambda x: from_list(lambda x: to_class(Participant, x), x), from_none], self.all_participants)
        result["display_id"] = from_union([from_str, from_none], self.display_id)
        result["join_url"] = from_union([from_str, from_none], self.join_url)
        result["desktop_app_join_url"] = from_union([from_str, from_none], self.desktop_app_join_url)
        result["name"] = from_union([from_str, from_none], self.name)
        result["created_by"] = from_union([from_str, from_none], self.created_by)
        result["date_end"] = from_union([from_int, from_none], self.date_end)
        result["channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.channels)
        result["is_dm_call"] = from_union([from_bool, from_none], self.is_dm_call)
        result["was_rejected"] = from_union([from_bool, from_none], self.was_rejected)
        result["was_missed"] = from_union([from_bool, from_none], self.was_missed)
        result["was_accepted"] = from_union([from_bool, from_none], self.was_accepted)
        result["has_ended"] = from_union([from_bool, from_none], self.has_ended)
        return result


@dataclass
class Call:
    v1: Optional[V1] = None
    media_backend_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Call':
        assert isinstance(obj, dict)
        v1 = from_union([V1.from_dict, from_none], obj.get("v1"))
        media_backend_type = from_union([from_str, from_none], obj.get("media_backend_type"))
        return Call(v1, media_backend_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["v1"] = from_union([lambda x: to_class(V1, x), from_none], self.v1)
        result["media_backend_type"] = from_union([from_str, from_none], self.media_backend_type)
        return result


class BlockType(Enum):
    ACTIONS = "actions"
    CONTEXT = "context"
    DIVIDER = "divider"
    IMAGE = "image"
    RICH_TEXT = "rich_text"
    SECTION = "section"
    SHARE_SHORTCUT = "share_shortcut"
    VIDEO = "video"


@dataclass
class DescriptionBlockElement:
    title: Union[DescriptionElement, None, str]
    description: Union[DescriptionElement, None, str]
    type: Optional[BlockType] = None
    elements: Optional[List[Accessory]] = None
    block_id: Optional[str] = None
    fallback: Optional[str] = None
    image_url: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    is_animated: Optional[bool] = None
    slack_file: Optional[SlackFile] = None
    alt_text: Optional[str] = None
    text: Optional[DescriptionElement] = None
    fields: Optional[List[DescriptionElement]] = None
    accessory: Optional[Accessory] = None
    expand: Optional[bool] = None
    title_url: Optional[str] = None
    video_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    author_name: Optional[str] = None
    provider_name: Optional[str] = None
    provider_icon_url: Optional[str] = None
    function_trigger_id: Optional[str] = None
    app_id: Optional[str] = None
    is_workflow_app: Optional[bool] = None
    sales_home_workflow_app_type: Optional[int] = None
    app_collaborators: Optional[List[str]] = None
    button_label: Optional[str] = None
    bot_user_id: Optional[str] = None
    url: Optional[str] = None
    owning_team_id: Optional[str] = None
    workflow_id: Optional[str] = None
    developer_trace_id: Optional[str] = None
    trigger_type: Optional[str] = None
    trigger_subtype: Optional[str] = None
    share_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DescriptionBlockElement':
        assert isinstance(obj, dict)
        title = from_union([DescriptionElement.from_dict, from_str, from_none], obj.get("title"))
        description = from_union([DescriptionElement.from_dict, from_str, from_none], obj.get("description"))
        type = from_union([BlockType, from_none], obj.get("type"))
        elements = from_union([lambda x: from_list(Accessory.from_dict, x), from_none], obj.get("elements"))
        block_id = from_union([from_str, from_none], obj.get("block_id"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        is_animated = from_union([from_bool, from_none], obj.get("is_animated"))
        slack_file = from_union([SlackFile.from_dict, from_none], obj.get("slack_file"))
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        text = from_union([DescriptionElement.from_dict, from_none], obj.get("text"))
        fields = from_union([lambda x: from_list(DescriptionElement.from_dict, x), from_none], obj.get("fields"))
        accessory = from_union([Accessory.from_dict, from_none], obj.get("accessory"))
        expand = from_union([from_bool, from_none], obj.get("expand"))
        title_url = from_union([from_str, from_none], obj.get("title_url"))
        video_url = from_union([from_str, from_none], obj.get("video_url"))
        thumbnail_url = from_union([from_str, from_none], obj.get("thumbnail_url"))
        author_name = from_union([from_str, from_none], obj.get("author_name"))
        provider_name = from_union([from_str, from_none], obj.get("provider_name"))
        provider_icon_url = from_union([from_str, from_none], obj.get("provider_icon_url"))
        function_trigger_id = from_union([from_str, from_none], obj.get("function_trigger_id"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        is_workflow_app = from_union([from_bool, from_none], obj.get("is_workflow_app"))
        sales_home_workflow_app_type = from_union([from_int, from_none], obj.get("sales_home_workflow_app_type"))
        app_collaborators = from_union([lambda x: from_list(from_str, x), from_none], obj.get("app_collaborators"))
        button_label = from_union([from_str, from_none], obj.get("button_label"))
        bot_user_id = from_union([from_str, from_none], obj.get("bot_user_id"))
        url = from_union([from_str, from_none], obj.get("url"))
        owning_team_id = from_union([from_str, from_none], obj.get("owning_team_id"))
        workflow_id = from_union([from_str, from_none], obj.get("workflow_id"))
        developer_trace_id = from_union([from_str, from_none], obj.get("developer_trace_id"))
        trigger_type = from_union([from_str, from_none], obj.get("trigger_type"))
        trigger_subtype = from_union([from_str, from_none], obj.get("trigger_subtype"))
        share_url = from_union([from_str, from_none], obj.get("share_url"))
        return DescriptionBlockElement(title, description, type, elements, block_id, fallback, image_url, image_width, image_height, image_bytes, is_animated, slack_file, alt_text, text, fields, accessory, expand, title_url, video_url, thumbnail_url, author_name, provider_name, provider_icon_url, function_trigger_id, app_id, is_workflow_app, sales_home_workflow_app_type, app_collaborators, button_label, bot_user_id, url, owning_team_id, workflow_id, developer_trace_id, trigger_type, trigger_subtype, share_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([lambda x: to_class(DescriptionElement, x), from_str, from_none], self.title)
        result["description"] = from_union([lambda x: to_class(DescriptionElement, x), from_str, from_none], self.description)
        result["type"] = from_union([lambda x: to_enum(BlockType, x), from_none], self.type)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(Accessory, x), x), from_none], self.elements)
        result["block_id"] = from_union([from_str, from_none], self.block_id)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["is_animated"] = from_union([from_bool, from_none], self.is_animated)
        result["slack_file"] = from_union([lambda x: to_class(SlackFile, x), from_none], self.slack_file)
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["text"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.text)
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(DescriptionElement, x), x), from_none], self.fields)
        result["accessory"] = from_union([lambda x: to_class(Accessory, x), from_none], self.accessory)
        result["expand"] = from_union([from_bool, from_none], self.expand)
        result["title_url"] = from_union([from_str, from_none], self.title_url)
        result["video_url"] = from_union([from_str, from_none], self.video_url)
        result["thumbnail_url"] = from_union([from_str, from_none], self.thumbnail_url)
        result["author_name"] = from_union([from_str, from_none], self.author_name)
        result["provider_name"] = from_union([from_str, from_none], self.provider_name)
        result["provider_icon_url"] = from_union([from_str, from_none], self.provider_icon_url)
        result["function_trigger_id"] = from_union([from_str, from_none], self.function_trigger_id)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["is_workflow_app"] = from_union([from_bool, from_none], self.is_workflow_app)
        result["sales_home_workflow_app_type"] = from_union([from_int, from_none], self.sales_home_workflow_app_type)
        result["app_collaborators"] = from_union([lambda x: from_list(from_str, x), from_none], self.app_collaborators)
        result["button_label"] = from_union([from_str, from_none], self.button_label)
        result["bot_user_id"] = from_union([from_str, from_none], self.bot_user_id)
        result["url"] = from_union([from_str, from_none], self.url)
        result["owning_team_id"] = from_union([from_str, from_none], self.owning_team_id)
        result["workflow_id"] = from_union([from_str, from_none], self.workflow_id)
        result["developer_trace_id"] = from_union([from_str, from_none], self.developer_trace_id)
        result["trigger_type"] = from_union([from_str, from_none], self.trigger_type)
        result["trigger_subtype"] = from_union([from_str, from_none], self.trigger_subtype)
        result["share_url"] = from_union([from_str, from_none], self.share_url)
        return result


@dataclass
class Cc:
    address: Optional[str] = None
    name: Optional[str] = None
    original: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Cc':
        assert isinstance(obj, dict)
        address = from_union([from_str, from_none], obj.get("address"))
        name = from_union([from_str, from_none], obj.get("name"))
        original = from_union([from_str, from_none], obj.get("original"))
        return Cc(address, name, original)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_union([from_str, from_none], self.address)
        result["name"] = from_union([from_str, from_none], self.name)
        result["original"] = from_union([from_str, from_none], self.original)
        return result


@dataclass
class DmMpdmUsersWithFileAccess:
    user_id: Optional[str] = None
    access: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DmMpdmUsersWithFileAccess':
        assert isinstance(obj, dict)
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        access = from_union([from_str, from_none], obj.get("access"))
        return DmMpdmUsersWithFileAccess(user_id, access)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["access"] = from_union([from_str, from_none], self.access)
        return result


@dataclass
class Favorite:
    collection_id: Optional[str] = None
    collection_name: Optional[str] = None
    position: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Favorite':
        assert isinstance(obj, dict)
        collection_id = from_union([from_str, from_none], obj.get("collection_id"))
        collection_name = from_union([from_str, from_none], obj.get("collection_name"))
        position = from_union([from_str, from_none], obj.get("position"))
        return Favorite(collection_id, collection_name, position)

    def to_dict(self) -> dict:
        result: dict = {}
        result["collection_id"] = from_union([from_str, from_none], self.collection_id)
        result["collection_name"] = from_union([from_str, from_none], self.collection_name)
        result["position"] = from_union([from_str, from_none], self.position)
        return result


@dataclass
class Headers:
    date: Optional[str] = None
    in_reply_to: Optional[str] = None
    reply_to: Optional[str] = None
    message_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Headers':
        assert isinstance(obj, dict)
        date = from_union([from_str, from_none], obj.get("date"))
        in_reply_to = from_union([from_str, from_none], obj.get("in_reply_to"))
        reply_to = from_union([from_str, from_none], obj.get("reply_to"))
        message_id = from_union([from_str, from_none], obj.get("message_id"))
        return Headers(date, in_reply_to, reply_to, message_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["date"] = from_union([from_str, from_none], self.date)
        result["in_reply_to"] = from_union([from_str, from_none], self.in_reply_to)
        result["reply_to"] = from_union([from_str, from_none], self.reply_to)
        result["message_id"] = from_union([from_str, from_none], self.message_id)
        return result


@dataclass
class InitialComment:
    id: Optional[str] = None
    created: Optional[int] = None
    timestamp: Optional[int] = None
    user: Optional[str] = None
    comment: Optional[str] = None
    channel: Optional[str] = None
    is_intro: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InitialComment':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        created = from_union([from_int, from_none], obj.get("created"))
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        user = from_union([from_str, from_none], obj.get("user"))
        comment = from_union([from_str, from_none], obj.get("comment"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        is_intro = from_union([from_bool, from_none], obj.get("is_intro"))
        return InitialComment(id, created, timestamp, user, comment, channel, is_intro)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["created"] = from_union([from_int, from_none], self.created)
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        result["user"] = from_union([from_str, from_none], self.user)
        result["comment"] = from_union([from_str, from_none], self.comment)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["is_intro"] = from_union([from_bool, from_none], self.is_intro)
        return result


@dataclass
class ListLimits:
    over_row_maximum: Optional[bool] = None
    row_count_limit: Optional[int] = None
    row_count: Optional[int] = None
    over_column_maximum: Optional[bool] = None
    column_count: Optional[int] = None
    column_count_limit: Optional[int] = None
    over_view_maximum: Optional[bool] = None
    view_count: Optional[int] = None
    view_count_limit: Optional[int] = None
    max_attachments_per_cell: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ListLimits':
        assert isinstance(obj, dict)
        over_row_maximum = from_union([from_bool, from_none], obj.get("over_row_maximum"))
        row_count_limit = from_union([from_int, from_none], obj.get("row_count_limit"))
        row_count = from_union([from_int, from_none], obj.get("row_count"))
        over_column_maximum = from_union([from_bool, from_none], obj.get("over_column_maximum"))
        column_count = from_union([from_int, from_none], obj.get("column_count"))
        column_count_limit = from_union([from_int, from_none], obj.get("column_count_limit"))
        over_view_maximum = from_union([from_bool, from_none], obj.get("over_view_maximum"))
        view_count = from_union([from_int, from_none], obj.get("view_count"))
        view_count_limit = from_union([from_int, from_none], obj.get("view_count_limit"))
        max_attachments_per_cell = from_union([from_int, from_none], obj.get("max_attachments_per_cell"))
        return ListLimits(over_row_maximum, row_count_limit, row_count, over_column_maximum, column_count, column_count_limit, over_view_maximum, view_count, view_count_limit, max_attachments_per_cell)

    def to_dict(self) -> dict:
        result: dict = {}
        result["over_row_maximum"] = from_union([from_bool, from_none], self.over_row_maximum)
        result["row_count_limit"] = from_union([from_int, from_none], self.row_count_limit)
        result["row_count"] = from_union([from_int, from_none], self.row_count)
        result["over_column_maximum"] = from_union([from_bool, from_none], self.over_column_maximum)
        result["column_count"] = from_union([from_int, from_none], self.column_count)
        result["column_count_limit"] = from_union([from_int, from_none], self.column_count_limit)
        result["over_view_maximum"] = from_union([from_bool, from_none], self.over_view_maximum)
        result["view_count"] = from_union([from_int, from_none], self.view_count)
        result["view_count_limit"] = from_union([from_int, from_none], self.view_count_limit)
        result["max_attachments_per_cell"] = from_union([from_int, from_none], self.max_attachments_per_cell)
        return result


@dataclass
class CreationSource:
    type: Optional[str] = None
    reference_id: Optional[str] = None
    workflow_function_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CreationSource':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        reference_id = from_union([from_str, from_none], obj.get("reference_id"))
        workflow_function_id = from_union([from_str, from_none], obj.get("workflow_function_id"))
        return CreationSource(type, reference_id, workflow_function_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["reference_id"] = from_union([from_str, from_none], self.reference_id)
        result["workflow_function_id"] = from_union([from_str, from_none], self.workflow_function_id)
        return result


@dataclass
class CanvasPlaceholderMapping:
    variable: Optional[str] = None
    column: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CanvasPlaceholderMapping':
        assert isinstance(obj, dict)
        variable = from_union([from_str, from_none], obj.get("variable"))
        column = from_union([from_str, from_none], obj.get("column"))
        return CanvasPlaceholderMapping(variable, column)

    def to_dict(self) -> dict:
        result: dict = {}
        result["variable"] = from_union([from_str, from_none], self.variable)
        result["column"] = from_union([from_str, from_none], self.column)
        return result


@dataclass
class Choice:
    value: Optional[str] = None
    label: Optional[str] = None
    color: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Choice':
        assert isinstance(obj, dict)
        value = from_union([from_str, from_none], obj.get("value"))
        label = from_union([from_str, from_none], obj.get("label"))
        color = from_union([from_str, from_none], obj.get("color"))
        return Choice(value, label, color)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_str, from_none], self.value)
        result["label"] = from_union([from_str, from_none], self.label)
        result["color"] = from_union([from_str, from_none], self.color)
        return result


@dataclass
class DefaultValueTyped:
    select: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DefaultValueTyped':
        assert isinstance(obj, dict)
        select = from_union([lambda x: from_list(from_str, x), from_none], obj.get("select"))
        return DefaultValueTyped(select)

    def to_dict(self) -> dict:
        result: dict = {}
        result["select"] = from_union([lambda x: from_list(from_str, x), from_none], self.select)
        return result


@dataclass
class Options:
    choices: Optional[List[Choice]] = None
    format: Optional[str] = None
    default_value: Optional[str] = None
    default_value_typed: Optional[DefaultValueTyped] = None
    emoji: Optional[str] = None
    max: Optional[int] = None
    precision: Optional[int] = None
    show_member_name: Optional[bool] = None
    date_format: Optional[str] = None
    time_format: Optional[str] = None
    currency_format: Optional[str] = None
    emoji_team_id: Optional[str] = None
    currency: Optional[str] = None
    rounding: Optional[str] = None
    mark_as_done_when_checked: Optional[bool] = None
    for_assignment: Optional[bool] = None
    notify_users: Optional[bool] = None
    linked_to: Optional[List[str]] = None
    canvas_id: Optional[str] = None
    canvas_placeholder_mapping: Optional[List[CanvasPlaceholderMapping]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Options':
        assert isinstance(obj, dict)
        choices = from_union([lambda x: from_list(Choice.from_dict, x), from_none], obj.get("choices"))
        format = from_union([from_str, from_none], obj.get("format"))
        default_value = from_union([from_str, from_none], obj.get("default_value"))
        default_value_typed = from_union([DefaultValueTyped.from_dict, from_none], obj.get("default_value_typed"))
        emoji = from_union([from_str, from_none], obj.get("emoji"))
        max = from_union([from_int, from_none], obj.get("max"))
        precision = from_union([from_int, from_none], obj.get("precision"))
        show_member_name = from_union([from_bool, from_none], obj.get("show_member_name"))
        date_format = from_union([from_str, from_none], obj.get("date_format"))
        time_format = from_union([from_str, from_none], obj.get("time_format"))
        currency_format = from_union([from_str, from_none], obj.get("currency_format"))
        emoji_team_id = from_union([from_str, from_none], obj.get("emoji_team_id"))
        currency = from_union([from_str, from_none], obj.get("currency"))
        rounding = from_union([from_str, from_none], obj.get("rounding"))
        mark_as_done_when_checked = from_union([from_bool, from_none], obj.get("mark_as_done_when_checked"))
        for_assignment = from_union([from_bool, from_none], obj.get("for_assignment"))
        notify_users = from_union([from_bool, from_none], obj.get("notify_users"))
        linked_to = from_union([lambda x: from_list(from_str, x), from_none], obj.get("linked_to"))
        canvas_id = from_union([from_str, from_none], obj.get("canvas_id"))
        canvas_placeholder_mapping = from_union([lambda x: from_list(CanvasPlaceholderMapping.from_dict, x), from_none], obj.get("canvas_placeholder_mapping"))
        return Options(choices, format, default_value, default_value_typed, emoji, max, precision, show_member_name, date_format, time_format, currency_format, emoji_team_id, currency, rounding, mark_as_done_when_checked, for_assignment, notify_users, linked_to, canvas_id, canvas_placeholder_mapping)

    def to_dict(self) -> dict:
        result: dict = {}
        result["choices"] = from_union([lambda x: from_list(lambda x: to_class(Choice, x), x), from_none], self.choices)
        result["format"] = from_union([from_str, from_none], self.format)
        result["default_value"] = from_union([from_str, from_none], self.default_value)
        result["default_value_typed"] = from_union([lambda x: to_class(DefaultValueTyped, x), from_none], self.default_value_typed)
        result["emoji"] = from_union([from_str, from_none], self.emoji)
        result["max"] = from_union([from_int, from_none], self.max)
        result["precision"] = from_union([from_int, from_none], self.precision)
        result["show_member_name"] = from_union([from_bool, from_none], self.show_member_name)
        result["date_format"] = from_union([from_str, from_none], self.date_format)
        result["time_format"] = from_union([from_str, from_none], self.time_format)
        result["currency_format"] = from_union([from_str, from_none], self.currency_format)
        result["emoji_team_id"] = from_union([from_str, from_none], self.emoji_team_id)
        result["currency"] = from_union([from_str, from_none], self.currency)
        result["rounding"] = from_union([from_str, from_none], self.rounding)
        result["mark_as_done_when_checked"] = from_union([from_bool, from_none], self.mark_as_done_when_checked)
        result["for_assignment"] = from_union([from_bool, from_none], self.for_assignment)
        result["notify_users"] = from_union([from_bool, from_none], self.notify_users)
        result["linked_to"] = from_union([lambda x: from_list(from_str, x), from_none], self.linked_to)
        result["canvas_id"] = from_union([from_str, from_none], self.canvas_id)
        result["canvas_placeholder_mapping"] = from_union([lambda x: from_list(lambda x: to_class(CanvasPlaceholderMapping, x), x), from_none], self.canvas_placeholder_mapping)
        return result


@dataclass
class Schema:
    id: Optional[str] = None
    name: Optional[str] = None
    key: Optional[str] = None
    type: Optional[str] = None
    is_primary_column: Optional[bool] = None
    options: Optional[Options] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Schema':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        key = from_union([from_str, from_none], obj.get("key"))
        type = from_union([from_str, from_none], obj.get("type"))
        is_primary_column = from_union([from_bool, from_none], obj.get("is_primary_column"))
        options = from_union([Options.from_dict, from_none], obj.get("options"))
        return Schema(id, name, key, type, is_primary_column, options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["key"] = from_union([from_str, from_none], self.key)
        result["type"] = from_union([from_str, from_none], self.type)
        result["is_primary_column"] = from_union([from_bool, from_none], self.is_primary_column)
        result["options"] = from_union([lambda x: to_class(Options, x), from_none], self.options)
        return result


@dataclass
class Column:
    visible: Optional[bool] = None
    key: Optional[str] = None
    id: Optional[str] = None
    position: Optional[str] = None
    width: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Column':
        assert isinstance(obj, dict)
        visible = from_union([from_bool, from_none], obj.get("visible"))
        key = from_union([from_str, from_none], obj.get("key"))
        id = from_union([from_str, from_none], obj.get("id"))
        position = from_union([from_str, from_none], obj.get("position"))
        width = from_union([from_int, from_none], obj.get("width"))
        return Column(visible, key, id, position, width)

    def to_dict(self) -> dict:
        result: dict = {}
        result["visible"] = from_union([from_bool, from_none], self.visible)
        result["key"] = from_union([from_str, from_none], self.key)
        result["id"] = from_union([from_str, from_none], self.id)
        result["position"] = from_union([from_str, from_none], self.position)
        result["width"] = from_union([from_int, from_none], self.width)
        return result


@dataclass
class FilterElement:
    key: Optional[str] = None
    operator: Optional[str] = None
    values: Optional[List[str]] = None
    typed_values: Optional[List[Any]] = None
    column_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FilterElement':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        operator = from_union([from_str, from_none], obj.get("operator"))
        values = from_union([lambda x: from_list(from_str, x), from_none], obj.get("values"))
        typed_values = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("typed_values"))
        column_id = from_union([from_str, from_none], obj.get("column_id"))
        return FilterElement(key, operator, values, typed_values, column_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["key"] = from_union([from_str, from_none], self.key)
        result["operator"] = from_union([from_str, from_none], self.operator)
        result["values"] = from_union([lambda x: from_list(from_str, x), from_none], self.values)
        result["typed_values"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.typed_values)
        result["column_id"] = from_union([from_str, from_none], self.column_id)
        return result


@dataclass
class Grouping:
    group_by: Optional[str] = None
    group_by_column_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Grouping':
        assert isinstance(obj, dict)
        group_by = from_union([from_str, from_none], obj.get("group_by"))
        group_by_column_id = from_union([from_str, from_none], obj.get("group_by_column_id"))
        return Grouping(group_by, group_by_column_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["group_by"] = from_union([from_str, from_none], self.group_by)
        result["group_by_column_id"] = from_union([from_str, from_none], self.group_by_column_id)
        return result


@dataclass
class View:
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    is_locked: Optional[bool] = None
    position: Optional[str] = None
    columns: Optional[List[Column]] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
    stick_column_left: Optional[bool] = None
    is_all_items_view: Optional[bool] = None
    default_view_key: Optional[str] = None
    show_completed_items: Optional[bool] = None
    grouping: Optional[Grouping] = None
    filters: Optional[List[FilterElement]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'View':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([from_str, from_none], obj.get("type"))
        is_locked = from_union([from_bool, from_none], obj.get("is_locked"))
        position = from_union([from_str, from_none], obj.get("position"))
        columns = from_union([lambda x: from_list(Column.from_dict, x), from_none], obj.get("columns"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        stick_column_left = from_union([from_bool, from_none], obj.get("stick_column_left"))
        is_all_items_view = from_union([from_bool, from_none], obj.get("is_all_items_view"))
        default_view_key = from_union([from_str, from_none], obj.get("default_view_key"))
        show_completed_items = from_union([from_bool, from_none], obj.get("show_completed_items"))
        grouping = from_union([Grouping.from_dict, from_none], obj.get("grouping"))
        filters = from_union([lambda x: from_list(FilterElement.from_dict, x), from_none], obj.get("filters"))
        return View(id, name, type, is_locked, position, columns, date_created, created_by, stick_column_left, is_all_items_view, default_view_key, show_completed_items, grouping, filters)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["type"] = from_union([from_str, from_none], self.type)
        result["is_locked"] = from_union([from_bool, from_none], self.is_locked)
        result["position"] = from_union([from_str, from_none], self.position)
        result["columns"] = from_union([lambda x: from_list(lambda x: to_class(Column, x), x), from_none], self.columns)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["created_by"] = from_union([from_str, from_none], self.created_by)
        result["stick_column_left"] = from_union([from_bool, from_none], self.stick_column_left)
        result["is_all_items_view"] = from_union([from_bool, from_none], self.is_all_items_view)
        result["default_view_key"] = from_union([from_str, from_none], self.default_view_key)
        result["show_completed_items"] = from_union([from_bool, from_none], self.show_completed_items)
        result["grouping"] = from_union([lambda x: to_class(Grouping, x), from_none], self.grouping)
        result["filters"] = from_union([lambda x: from_list(lambda x: to_class(FilterElement, x), x), from_none], self.filters)
        return result


@dataclass
class ListMetadata:
    icon: Optional[str] = None
    icon_url: Optional[str] = None
    icon_team_id: Optional[str] = None
    description: Optional[str] = None
    is_trial: Optional[bool] = None
    creation_source: Optional[CreationSource] = None
    schema: Optional[List[Schema]] = None
    views: Optional[List[View]] = None
    integrations: Optional[List[str]] = None
    description_blocks: Optional[List[DescriptionBlockElement]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ListMetadata':
        assert isinstance(obj, dict)
        icon = from_union([from_str, from_none], obj.get("icon"))
        icon_url = from_union([from_str, from_none], obj.get("icon_url"))
        icon_team_id = from_union([from_str, from_none], obj.get("icon_team_id"))
        description = from_union([from_str, from_none], obj.get("description"))
        is_trial = from_union([from_bool, from_none], obj.get("is_trial"))
        creation_source = from_union([CreationSource.from_dict, from_none], obj.get("creation_source"))
        schema = from_union([lambda x: from_list(Schema.from_dict, x), from_none], obj.get("schema"))
        views = from_union([lambda x: from_list(View.from_dict, x), from_none], obj.get("views"))
        integrations = from_union([lambda x: from_list(from_str, x), from_none], obj.get("integrations"))
        description_blocks = from_union([lambda x: from_list(DescriptionBlockElement.from_dict, x), from_none], obj.get("description_blocks"))
        return ListMetadata(icon, icon_url, icon_team_id, description, is_trial, creation_source, schema, views, integrations, description_blocks)

    def to_dict(self) -> dict:
        result: dict = {}
        result["icon"] = from_union([from_str, from_none], self.icon)
        result["icon_url"] = from_union([from_str, from_none], self.icon_url)
        result["icon_team_id"] = from_union([from_str, from_none], self.icon_team_id)
        result["description"] = from_union([from_str, from_none], self.description)
        result["is_trial"] = from_union([from_bool, from_none], self.is_trial)
        result["creation_source"] = from_union([lambda x: to_class(CreationSource, x), from_none], self.creation_source)
        result["schema"] = from_union([lambda x: from_list(lambda x: to_class(Schema, x), x), from_none], self.schema)
        result["views"] = from_union([lambda x: from_list(lambda x: to_class(View, x), x), from_none], self.views)
        result["integrations"] = from_union([lambda x: from_list(from_str, x), from_none], self.integrations)
        result["description_blocks"] = from_union([lambda x: from_list(lambda x: to_class(DescriptionBlockElement, x), x), from_none], self.description_blocks)
        return result


@dataclass
class MediaProgress:
    offset_ms: Optional[int] = None
    max_offset_ms: Optional[int] = None
    duration_ms: Optional[int] = None
    media_watched: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MediaProgress':
        assert isinstance(obj, dict)
        offset_ms = from_union([from_int, from_none], obj.get("offset_ms"))
        max_offset_ms = from_union([from_int, from_none], obj.get("max_offset_ms"))
        duration_ms = from_union([from_int, from_none], obj.get("duration_ms"))
        media_watched = from_union([from_bool, from_none], obj.get("media_watched"))
        return MediaProgress(offset_ms, max_offset_ms, duration_ms, media_watched)

    def to_dict(self) -> dict:
        result: dict = {}
        result["offset_ms"] = from_union([from_int, from_none], self.offset_ms)
        result["max_offset_ms"] = from_union([from_int, from_none], self.max_offset_ms)
        result["duration_ms"] = from_union([from_int, from_none], self.duration_ms)
        result["media_watched"] = from_union([from_bool, from_none], self.media_watched)
        return result


@dataclass
class Reaction:
    name: Optional[str] = None
    count: Optional[int] = None
    users: Optional[List[str]] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Reaction':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        count = from_union([from_int, from_none], obj.get("count"))
        users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("users"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Reaction(name, count, users, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["count"] = from_union([from_int, from_none], self.count)
        result["users"] = from_union([lambda x: from_list(from_str, x), from_none], self.users)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class Saved:
    is_archived: Optional[bool] = None
    date_completed: Optional[int] = None
    date_due: Optional[int] = None
    state: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Saved':
        assert isinstance(obj, dict)
        is_archived = from_union([from_bool, from_none], obj.get("is_archived"))
        date_completed = from_union([from_int, from_none], obj.get("date_completed"))
        date_due = from_union([from_int, from_none], obj.get("date_due"))
        state = from_union([from_str, from_none], obj.get("state"))
        return Saved(is_archived, date_completed, date_due, state)

    def to_dict(self) -> dict:
        result: dict = {}
        result["is_archived"] = from_union([from_bool, from_none], self.is_archived)
        result["date_completed"] = from_union([from_int, from_none], self.date_completed)
        result["date_due"] = from_union([from_int, from_none], self.date_due)
        result["state"] = from_union([from_str, from_none], self.state)
        return result


@dataclass
class Private:
    share_user_id: Optional[str] = None
    reply_users: Optional[List[str]] = None
    reply_users_count: Optional[int] = None
    reply_count: Optional[int] = None
    ts: Optional[str] = None
    thread_ts: Optional[str] = None
    latest_reply: Optional[str] = None
    channel_name: Optional[str] = None
    team_id: Optional[str] = None
    access: Optional[str] = None
    source: Optional[str] = None
    date_last_shared: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Private':
        assert isinstance(obj, dict)
        share_user_id = from_union([from_str, from_none], obj.get("share_user_id"))
        reply_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("reply_users"))
        reply_users_count = from_union([from_int, from_none], obj.get("reply_users_count"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        thread_ts = from_union([from_str, from_none], obj.get("thread_ts"))
        latest_reply = from_union([from_str, from_none], obj.get("latest_reply"))
        channel_name = from_union([from_str, from_none], obj.get("channel_name"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        access = from_union([from_str, from_none], obj.get("access"))
        source = from_union([from_str, from_none], obj.get("source"))
        date_last_shared = from_union([from_int, from_none], obj.get("date_last_shared"))
        return Private(share_user_id, reply_users, reply_users_count, reply_count, ts, thread_ts, latest_reply, channel_name, team_id, access, source, date_last_shared)

    def to_dict(self) -> dict:
        result: dict = {}
        result["share_user_id"] = from_union([from_str, from_none], self.share_user_id)
        result["reply_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.reply_users)
        result["reply_users_count"] = from_union([from_int, from_none], self.reply_users_count)
        result["reply_count"] = from_union([from_int, from_none], self.reply_count)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["thread_ts"] = from_union([from_str, from_none], self.thread_ts)
        result["latest_reply"] = from_union([from_str, from_none], self.latest_reply)
        result["channel_name"] = from_union([from_str, from_none], self.channel_name)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["access"] = from_union([from_str, from_none], self.access)
        result["source"] = from_union([from_str, from_none], self.source)
        result["date_last_shared"] = from_union([from_int, from_none], self.date_last_shared)
        return result


@dataclass
class Shares:
    public: Optional[Dict[str, List[Private]]] = None
    private: Optional[Dict[str, List[Private]]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Shares':
        assert isinstance(obj, dict)
        public = from_union([lambda x: from_dict(lambda x: from_list(Private.from_dict, x), x), from_none], obj.get("public"))
        private = from_union([lambda x: from_dict(lambda x: from_list(Private.from_dict, x), x), from_none], obj.get("private"))
        return Shares(public, private)

    def to_dict(self) -> dict:
        result: dict = {}
        result["public"] = from_union([lambda x: from_dict(lambda x: from_list(lambda x: to_class(Private, x), x), x), from_none], self.public)
        result["private"] = from_union([lambda x: from_dict(lambda x: from_list(lambda x: to_class(Private, x), x), x), from_none], self.private)
        return result


@dataclass
class Preview:
    content: Optional[str] = None
    has_more: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Preview':
        assert isinstance(obj, dict)
        content = from_union([from_str, from_none], obj.get("content"))
        has_more = from_union([from_bool, from_none], obj.get("has_more"))
        return Preview(content, has_more)

    def to_dict(self) -> dict:
        result: dict = {}
        result["content"] = from_union([from_str, from_none], self.content)
        result["has_more"] = from_union([from_bool, from_none], self.has_more)
        return result


@dataclass
class Transcription:
    status: Optional[str] = None
    locale: Optional[str] = None
    preview: Optional[Preview] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Transcription':
        assert isinstance(obj, dict)
        status = from_union([from_str, from_none], obj.get("status"))
        locale = from_union([from_str, from_none], obj.get("locale"))
        preview = from_union([Preview.from_dict, from_none], obj.get("preview"))
        return Transcription(status, locale, preview)

    def to_dict(self) -> dict:
        result: dict = {}
        result["status"] = from_union([from_str, from_none], self.status)
        result["locale"] = from_union([from_str, from_none], self.locale)
        result["preview"] = from_union([lambda x: to_class(Preview, x), from_none], self.preview)
        return result


@dataclass
class File:
    id: Optional[str] = None
    created: Optional[int] = None
    timestamp: Optional[int] = None
    name: Optional[str] = None
    title: Optional[str] = None
    subject: Optional[str] = None
    mimetype: Optional[str] = None
    filetype: Optional[str] = None
    pretty_type: Optional[str] = None
    user: Optional[str] = None
    user_team: Optional[str] = None
    source_team: Optional[str] = None
    mode: Optional[str] = None
    editable: Optional[bool] = None
    non_owner_editable: Optional[bool] = None
    editor: Optional[str] = None
    last_editor: Optional[str] = None
    updated: Optional[int] = None
    file_access: Optional[str] = None
    editors: Optional[List[str]] = None
    edit_timestamp: Optional[int] = None
    alt_txt: Optional[str] = None
    subtype: Optional[str] = None
    transcription: Optional[Transcription] = None
    mp4: Optional[str] = None
    mp4_low: Optional[str] = None
    vtt: Optional[str] = None
    hls: Optional[str] = None
    hls_embed: Optional[str] = None
    duration_ms: Optional[int] = None
    thumb_video_w: Optional[int] = None
    thumb_video_h: Optional[int] = None
    original_attachment_count: Optional[int] = None
    is_external: Optional[bool] = None
    external_type: Optional[str] = None
    external_id: Optional[str] = None
    external_url: Optional[str] = None
    username: Optional[str] = None
    size: Optional[int] = None
    url_private: Optional[str] = None
    url_private_download: Optional[str] = None
    url_static_preview: Optional[str] = None
    app_id: Optional[str] = None
    app_name: Optional[str] = None
    thumb_64: Optional[str] = None
    thumb_64__gif: Optional[str] = None
    thumb_64__w: Optional[str] = None
    thumb_64__h: Optional[str] = None
    thumb_80: Optional[str] = None
    thumb_80__gif: Optional[str] = None
    thumb_80__w: Optional[str] = None
    thumb_80__h: Optional[str] = None
    thumb_160: Optional[str] = None
    thumb_160__gif: Optional[str] = None
    thumb_160__w: Optional[str] = None
    thumb_160__h: Optional[str] = None
    thumb_360: Optional[str] = None
    thumb_360__gif: Optional[str] = None
    thumb_360__w: Optional[str] = None
    thumb_360__h: Optional[str] = None
    thumb_480: Optional[str] = None
    thumb_480__gif: Optional[str] = None
    thumb_480__w: Optional[str] = None
    thumb_480__h: Optional[str] = None
    thumb_720: Optional[str] = None
    thumb_720__gif: Optional[str] = None
    thumb_720__w: Optional[str] = None
    thumb_720__h: Optional[str] = None
    thumb_800: Optional[str] = None
    thumb_800__gif: Optional[str] = None
    thumb_800__w: Optional[str] = None
    thumb_800__h: Optional[str] = None
    thumb_960: Optional[str] = None
    thumb_960__gif: Optional[str] = None
    thumb_960__w: Optional[str] = None
    thumb_960__h: Optional[str] = None
    thumb_1024: Optional[str] = None
    thumb_1024__gif: Optional[str] = None
    thumb_1024__w: Optional[str] = None
    thumb_1024__h: Optional[str] = None
    thumb_video: Optional[str] = None
    thumb_gif: Optional[str] = None
    thumb_pdf: Optional[str] = None
    thumb_pdf_w: Optional[str] = None
    thumb_pdf_h: Optional[str] = None
    thumb_tiny: Optional[str] = None
    converted_pdf: Optional[str] = None
    image_exif_rotation: Optional[int] = None
    original_w: Optional[str] = None
    original_h: Optional[str] = None
    deanimate: Optional[str] = None
    deanimate_gif: Optional[str] = None
    pjpeg: Optional[str] = None
    permalink: Optional[str] = None
    permalink_public: Optional[str] = None
    edit_link: Optional[str] = None
    has_rich_preview: Optional[bool] = None
    media_display_type: Optional[str] = None
    preview_is_truncated: Optional[bool] = None
    preview: Optional[str] = None
    preview_highlight: Optional[str] = None
    plain_text: Optional[str] = None
    preview_plain_text: Optional[str] = None
    has_more: Optional[bool] = None
    sent_to_self: Optional[bool] = None
    lines: Optional[int] = None
    lines_more: Optional[int] = None
    is_public: Optional[bool] = None
    public_url_shared: Optional[bool] = None
    display_as_bot: Optional[bool] = None
    channels: Optional[List[str]] = None
    groups: Optional[List[str]] = None
    ims: Optional[List[str]] = None
    shares: Optional[Shares] = None
    has_more_shares: Optional[bool] = None
    to: Optional[List[Cc]] = None
    file_from: Optional[List[Cc]] = None
    cc: Optional[List[Cc]] = None
    channel_actions_ts: Optional[str] = None
    channel_actions_count: Optional[int] = None
    headers: Optional[Headers] = None
    simplified_html: Optional[str] = None
    media_progress: Optional[MediaProgress] = None
    saved: Optional[Saved] = None
    quip_thread_id: Optional[str] = None
    is_channel_space: Optional[bool] = None
    linked_channel_id: Optional[str] = None
    access: Optional[str] = None
    teams_shared_with: Optional[List[Any]] = None
    last_read: Optional[int] = None
    title_blocks: Optional[List[DescriptionBlockElement]] = None
    private_channels_with_file_access_count: Optional[int] = None
    private_file_with_access_count: Optional[int] = None
    dm_mpdm_users_with_file_access: Optional[List[DmMpdmUsersWithFileAccess]] = None
    org_or_workspace_access: Optional[str] = None
    update_notification: Optional[int] = None
    canvas_template_mode: Optional[str] = None
    template_conversion_ts: Optional[int] = None
    template_name: Optional[str] = None
    template_title: Optional[str] = None
    template_description: Optional[str] = None
    template_icon: Optional[str] = None
    team_pref_version_history_enabled: Optional[bool] = None
    show_badge: Optional[bool] = None
    favorites: Optional[List[Favorite]] = None
    list_metadata: Optional[ListMetadata] = None
    list_limits: Optional[ListLimits] = None
    list_csv_download_url: Optional[str] = None
    can_toggle_canvas_lock: Optional[bool] = None
    is_restricted_sharing_enabled: Optional[bool] = None
    canvas_printing_enabled: Optional[bool] = None
    bot_id: Optional[str] = None
    initial_comment: Optional[InitialComment] = None
    num_stars: Optional[int] = None
    is_starred: Optional[bool] = None
    pinned_to: Optional[List[str]] = None
    reactions: Optional[List[Reaction]] = None
    comments_count: Optional[int] = None
    attachments: Optional[List[Any]] = None
    blocks: Optional[List[DescriptionBlockElement]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'File':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        created = from_union([from_int, from_none], obj.get("created"))
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        name = from_union([from_str, from_none], obj.get("name"))
        title = from_union([from_str, from_none], obj.get("title"))
        subject = from_union([from_str, from_none], obj.get("subject"))
        mimetype = from_union([from_str, from_none], obj.get("mimetype"))
        filetype = from_union([from_str, from_none], obj.get("filetype"))
        pretty_type = from_union([from_str, from_none], obj.get("pretty_type"))
        user = from_union([from_str, from_none], obj.get("user"))
        user_team = from_union([from_str, from_none], obj.get("user_team"))
        source_team = from_union([from_str, from_none], obj.get("source_team"))
        mode = from_union([from_str, from_none], obj.get("mode"))
        editable = from_union([from_bool, from_none], obj.get("editable"))
        non_owner_editable = from_union([from_bool, from_none], obj.get("non_owner_editable"))
        editor = from_union([from_str, from_none], obj.get("editor"))
        last_editor = from_union([from_str, from_none], obj.get("last_editor"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        file_access = from_union([from_str, from_none], obj.get("file_access"))
        editors = from_union([lambda x: from_list(from_str, x), from_none], obj.get("editors"))
        edit_timestamp = from_union([from_int, from_none], obj.get("edit_timestamp"))
        alt_txt = from_union([from_str, from_none], obj.get("alt_txt"))
        subtype = from_union([from_str, from_none], obj.get("subtype"))
        transcription = from_union([Transcription.from_dict, from_none], obj.get("transcription"))
        mp4 = from_union([from_str, from_none], obj.get("mp4"))
        mp4_low = from_union([from_str, from_none], obj.get("mp4_low"))
        vtt = from_union([from_str, from_none], obj.get("vtt"))
        hls = from_union([from_str, from_none], obj.get("hls"))
        hls_embed = from_union([from_str, from_none], obj.get("hls_embed"))
        duration_ms = from_union([from_int, from_none], obj.get("duration_ms"))
        thumb_video_w = from_union([from_int, from_none], obj.get("thumb_video_w"))
        thumb_video_h = from_union([from_int, from_none], obj.get("thumb_video_h"))
        original_attachment_count = from_union([from_int, from_none], obj.get("original_attachment_count"))
        is_external = from_union([from_bool, from_none], obj.get("is_external"))
        external_type = from_union([from_str, from_none], obj.get("external_type"))
        external_id = from_union([from_str, from_none], obj.get("external_id"))
        external_url = from_union([from_str, from_none], obj.get("external_url"))
        username = from_union([from_str, from_none], obj.get("username"))
        size = from_union([from_int, from_none], obj.get("size"))
        url_private = from_union([from_str, from_none], obj.get("url_private"))
        url_private_download = from_union([from_str, from_none], obj.get("url_private_download"))
        url_static_preview = from_union([from_str, from_none], obj.get("url_static_preview"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        app_name = from_union([from_str, from_none], obj.get("app_name"))
        thumb_64 = from_union([from_str, from_none], obj.get("thumb_64"))
        thumb_64__gif = from_union([from_str, from_none], obj.get("thumb_64_gif"))
        thumb_64__w = from_union([from_str, from_none], obj.get("thumb_64_w"))
        thumb_64__h = from_union([from_str, from_none], obj.get("thumb_64_h"))
        thumb_80 = from_union([from_str, from_none], obj.get("thumb_80"))
        thumb_80__gif = from_union([from_str, from_none], obj.get("thumb_80_gif"))
        thumb_80__w = from_union([from_str, from_none], obj.get("thumb_80_w"))
        thumb_80__h = from_union([from_str, from_none], obj.get("thumb_80_h"))
        thumb_160 = from_union([from_str, from_none], obj.get("thumb_160"))
        thumb_160__gif = from_union([from_str, from_none], obj.get("thumb_160_gif"))
        thumb_160__w = from_union([from_str, from_none], obj.get("thumb_160_w"))
        thumb_160__h = from_union([from_str, from_none], obj.get("thumb_160_h"))
        thumb_360 = from_union([from_str, from_none], obj.get("thumb_360"))
        thumb_360__gif = from_union([from_str, from_none], obj.get("thumb_360_gif"))
        thumb_360__w = from_union([from_str, from_none], obj.get("thumb_360_w"))
        thumb_360__h = from_union([from_str, from_none], obj.get("thumb_360_h"))
        thumb_480 = from_union([from_str, from_none], obj.get("thumb_480"))
        thumb_480__gif = from_union([from_str, from_none], obj.get("thumb_480_gif"))
        thumb_480__w = from_union([from_str, from_none], obj.get("thumb_480_w"))
        thumb_480__h = from_union([from_str, from_none], obj.get("thumb_480_h"))
        thumb_720 = from_union([from_str, from_none], obj.get("thumb_720"))
        thumb_720__gif = from_union([from_str, from_none], obj.get("thumb_720_gif"))
        thumb_720__w = from_union([from_str, from_none], obj.get("thumb_720_w"))
        thumb_720__h = from_union([from_str, from_none], obj.get("thumb_720_h"))
        thumb_800 = from_union([from_str, from_none], obj.get("thumb_800"))
        thumb_800__gif = from_union([from_str, from_none], obj.get("thumb_800_gif"))
        thumb_800__w = from_union([from_str, from_none], obj.get("thumb_800_w"))
        thumb_800__h = from_union([from_str, from_none], obj.get("thumb_800_h"))
        thumb_960 = from_union([from_str, from_none], obj.get("thumb_960"))
        thumb_960__gif = from_union([from_str, from_none], obj.get("thumb_960_gif"))
        thumb_960__w = from_union([from_str, from_none], obj.get("thumb_960_w"))
        thumb_960__h = from_union([from_str, from_none], obj.get("thumb_960_h"))
        thumb_1024 = from_union([from_str, from_none], obj.get("thumb_1024"))
        thumb_1024__gif = from_union([from_str, from_none], obj.get("thumb_1024_gif"))
        thumb_1024__w = from_union([from_str, from_none], obj.get("thumb_1024_w"))
        thumb_1024__h = from_union([from_str, from_none], obj.get("thumb_1024_h"))
        thumb_video = from_union([from_str, from_none], obj.get("thumb_video"))
        thumb_gif = from_union([from_str, from_none], obj.get("thumb_gif"))
        thumb_pdf = from_union([from_str, from_none], obj.get("thumb_pdf"))
        thumb_pdf_w = from_union([from_str, from_none], obj.get("thumb_pdf_w"))
        thumb_pdf_h = from_union([from_str, from_none], obj.get("thumb_pdf_h"))
        thumb_tiny = from_union([from_str, from_none], obj.get("thumb_tiny"))
        converted_pdf = from_union([from_str, from_none], obj.get("converted_pdf"))
        image_exif_rotation = from_union([from_int, from_none], obj.get("image_exif_rotation"))
        original_w = from_union([from_str, from_none], obj.get("original_w"))
        original_h = from_union([from_str, from_none], obj.get("original_h"))
        deanimate = from_union([from_str, from_none], obj.get("deanimate"))
        deanimate_gif = from_union([from_str, from_none], obj.get("deanimate_gif"))
        pjpeg = from_union([from_str, from_none], obj.get("pjpeg"))
        permalink = from_union([from_str, from_none], obj.get("permalink"))
        permalink_public = from_union([from_str, from_none], obj.get("permalink_public"))
        edit_link = from_union([from_str, from_none], obj.get("edit_link"))
        has_rich_preview = from_union([from_bool, from_none], obj.get("has_rich_preview"))
        media_display_type = from_union([from_str, from_none], obj.get("media_display_type"))
        preview_is_truncated = from_union([from_bool, from_none], obj.get("preview_is_truncated"))
        preview = from_union([from_str, from_none], obj.get("preview"))
        preview_highlight = from_union([from_str, from_none], obj.get("preview_highlight"))
        plain_text = from_union([from_str, from_none], obj.get("plain_text"))
        preview_plain_text = from_union([from_str, from_none], obj.get("preview_plain_text"))
        has_more = from_union([from_bool, from_none], obj.get("has_more"))
        sent_to_self = from_union([from_bool, from_none], obj.get("sent_to_self"))
        lines = from_union([from_int, from_none], obj.get("lines"))
        lines_more = from_union([from_int, from_none], obj.get("lines_more"))
        is_public = from_union([from_bool, from_none], obj.get("is_public"))
        public_url_shared = from_union([from_bool, from_none], obj.get("public_url_shared"))
        display_as_bot = from_union([from_bool, from_none], obj.get("display_as_bot"))
        channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channels"))
        groups = from_union([lambda x: from_list(from_str, x), from_none], obj.get("groups"))
        ims = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ims"))
        shares = from_union([Shares.from_dict, from_none], obj.get("shares"))
        has_more_shares = from_union([from_bool, from_none], obj.get("has_more_shares"))
        to = from_union([lambda x: from_list(Cc.from_dict, x), from_none], obj.get("to"))
        file_from = from_union([lambda x: from_list(Cc.from_dict, x), from_none], obj.get("from"))
        cc = from_union([lambda x: from_list(Cc.from_dict, x), from_none], obj.get("cc"))
        channel_actions_ts = from_union([from_str, from_none], obj.get("channel_actions_ts"))
        channel_actions_count = from_union([from_int, from_none], obj.get("channel_actions_count"))
        headers = from_union([Headers.from_dict, from_none], obj.get("headers"))
        simplified_html = from_union([from_str, from_none], obj.get("simplified_html"))
        media_progress = from_union([MediaProgress.from_dict, from_none], obj.get("media_progress"))
        saved = from_union([Saved.from_dict, from_none], obj.get("saved"))
        quip_thread_id = from_union([from_str, from_none], obj.get("quip_thread_id"))
        is_channel_space = from_union([from_bool, from_none], obj.get("is_channel_space"))
        linked_channel_id = from_union([from_str, from_none], obj.get("linked_channel_id"))
        access = from_union([from_str, from_none], obj.get("access"))
        teams_shared_with = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("teams_shared_with"))
        last_read = from_union([from_int, from_none], obj.get("last_read"))
        title_blocks = from_union([lambda x: from_list(DescriptionBlockElement.from_dict, x), from_none], obj.get("title_blocks"))
        private_channels_with_file_access_count = from_union([from_int, from_none], obj.get("private_channels_with_file_access_count"))
        private_file_with_access_count = from_union([from_int, from_none], obj.get("private_file_with_access_count"))
        dm_mpdm_users_with_file_access = from_union([lambda x: from_list(DmMpdmUsersWithFileAccess.from_dict, x), from_none], obj.get("dm_mpdm_users_with_file_access"))
        org_or_workspace_access = from_union([from_str, from_none], obj.get("org_or_workspace_access"))
        update_notification = from_union([from_int, from_none], obj.get("update_notification"))
        canvas_template_mode = from_union([from_str, from_none], obj.get("canvas_template_mode"))
        template_conversion_ts = from_union([from_int, from_none], obj.get("template_conversion_ts"))
        template_name = from_union([from_str, from_none], obj.get("template_name"))
        template_title = from_union([from_str, from_none], obj.get("template_title"))
        template_description = from_union([from_str, from_none], obj.get("template_description"))
        template_icon = from_union([from_str, from_none], obj.get("template_icon"))
        team_pref_version_history_enabled = from_union([from_bool, from_none], obj.get("team_pref_version_history_enabled"))
        show_badge = from_union([from_bool, from_none], obj.get("show_badge"))
        favorites = from_union([lambda x: from_list(Favorite.from_dict, x), from_none], obj.get("favorites"))
        list_metadata = from_union([ListMetadata.from_dict, from_none], obj.get("list_metadata"))
        list_limits = from_union([ListLimits.from_dict, from_none], obj.get("list_limits"))
        list_csv_download_url = from_union([from_str, from_none], obj.get("list_csv_download_url"))
        can_toggle_canvas_lock = from_union([from_bool, from_none], obj.get("can_toggle_canvas_lock"))
        is_restricted_sharing_enabled = from_union([from_bool, from_none], obj.get("is_restricted_sharing_enabled"))
        canvas_printing_enabled = from_union([from_bool, from_none], obj.get("canvas_printing_enabled"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        initial_comment = from_union([InitialComment.from_dict, from_none], obj.get("initial_comment"))
        num_stars = from_union([from_int, from_none], obj.get("num_stars"))
        is_starred = from_union([from_bool, from_none], obj.get("is_starred"))
        pinned_to = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pinned_to"))
        reactions = from_union([lambda x: from_list(Reaction.from_dict, x), from_none], obj.get("reactions"))
        comments_count = from_union([from_int, from_none], obj.get("comments_count"))
        attachments = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("attachments"))
        blocks = from_union([lambda x: from_list(DescriptionBlockElement.from_dict, x), from_none], obj.get("blocks"))
        return File(id, created, timestamp, name, title, subject, mimetype, filetype, pretty_type, user, user_team, source_team, mode, editable, non_owner_editable, editor, last_editor, updated, file_access, editors, edit_timestamp, alt_txt, subtype, transcription, mp4, mp4_low, vtt, hls, hls_embed, duration_ms, thumb_video_w, thumb_video_h, original_attachment_count, is_external, external_type, external_id, external_url, username, size, url_private, url_private_download, url_static_preview, app_id, app_name, thumb_64, thumb_64__gif, thumb_64__w, thumb_64__h, thumb_80, thumb_80__gif, thumb_80__w, thumb_80__h, thumb_160, thumb_160__gif, thumb_160__w, thumb_160__h, thumb_360, thumb_360__gif, thumb_360__w, thumb_360__h, thumb_480, thumb_480__gif, thumb_480__w, thumb_480__h, thumb_720, thumb_720__gif, thumb_720__w, thumb_720__h, thumb_800, thumb_800__gif, thumb_800__w, thumb_800__h, thumb_960, thumb_960__gif, thumb_960__w, thumb_960__h, thumb_1024, thumb_1024__gif, thumb_1024__w, thumb_1024__h, thumb_video, thumb_gif, thumb_pdf, thumb_pdf_w, thumb_pdf_h, thumb_tiny, converted_pdf, image_exif_rotation, original_w, original_h, deanimate, deanimate_gif, pjpeg, permalink, permalink_public, edit_link, has_rich_preview, media_display_type, preview_is_truncated, preview, preview_highlight, plain_text, preview_plain_text, has_more, sent_to_self, lines, lines_more, is_public, public_url_shared, display_as_bot, channels, groups, ims, shares, has_more_shares, to, file_from, cc, channel_actions_ts, channel_actions_count, headers, simplified_html, media_progress, saved, quip_thread_id, is_channel_space, linked_channel_id, access, teams_shared_with, last_read, title_blocks, private_channels_with_file_access_count, private_file_with_access_count, dm_mpdm_users_with_file_access, org_or_workspace_access, update_notification, canvas_template_mode, template_conversion_ts, template_name, template_title, template_description, template_icon, team_pref_version_history_enabled, show_badge, favorites, list_metadata, list_limits, list_csv_download_url, can_toggle_canvas_lock, is_restricted_sharing_enabled, canvas_printing_enabled, bot_id, initial_comment, num_stars, is_starred, pinned_to, reactions, comments_count, attachments, blocks)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["created"] = from_union([from_int, from_none], self.created)
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        result["name"] = from_union([from_str, from_none], self.name)
        result["title"] = from_union([from_str, from_none], self.title)
        result["subject"] = from_union([from_str, from_none], self.subject)
        result["mimetype"] = from_union([from_str, from_none], self.mimetype)
        result["filetype"] = from_union([from_str, from_none], self.filetype)
        result["pretty_type"] = from_union([from_str, from_none], self.pretty_type)
        result["user"] = from_union([from_str, from_none], self.user)
        result["user_team"] = from_union([from_str, from_none], self.user_team)
        result["source_team"] = from_union([from_str, from_none], self.source_team)
        result["mode"] = from_union([from_str, from_none], self.mode)
        result["editable"] = from_union([from_bool, from_none], self.editable)
        result["non_owner_editable"] = from_union([from_bool, from_none], self.non_owner_editable)
        result["editor"] = from_union([from_str, from_none], self.editor)
        result["last_editor"] = from_union([from_str, from_none], self.last_editor)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["file_access"] = from_union([from_str, from_none], self.file_access)
        result["editors"] = from_union([lambda x: from_list(from_str, x), from_none], self.editors)
        result["edit_timestamp"] = from_union([from_int, from_none], self.edit_timestamp)
        result["alt_txt"] = from_union([from_str, from_none], self.alt_txt)
        result["subtype"] = from_union([from_str, from_none], self.subtype)
        result["transcription"] = from_union([lambda x: to_class(Transcription, x), from_none], self.transcription)
        result["mp4"] = from_union([from_str, from_none], self.mp4)
        result["mp4_low"] = from_union([from_str, from_none], self.mp4_low)
        result["vtt"] = from_union([from_str, from_none], self.vtt)
        result["hls"] = from_union([from_str, from_none], self.hls)
        result["hls_embed"] = from_union([from_str, from_none], self.hls_embed)
        result["duration_ms"] = from_union([from_int, from_none], self.duration_ms)
        result["thumb_video_w"] = from_union([from_int, from_none], self.thumb_video_w)
        result["thumb_video_h"] = from_union([from_int, from_none], self.thumb_video_h)
        result["original_attachment_count"] = from_union([from_int, from_none], self.original_attachment_count)
        result["is_external"] = from_union([from_bool, from_none], self.is_external)
        result["external_type"] = from_union([from_str, from_none], self.external_type)
        result["external_id"] = from_union([from_str, from_none], self.external_id)
        result["external_url"] = from_union([from_str, from_none], self.external_url)
        result["username"] = from_union([from_str, from_none], self.username)
        result["size"] = from_union([from_int, from_none], self.size)
        result["url_private"] = from_union([from_str, from_none], self.url_private)
        result["url_private_download"] = from_union([from_str, from_none], self.url_private_download)
        result["url_static_preview"] = from_union([from_str, from_none], self.url_static_preview)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["app_name"] = from_union([from_str, from_none], self.app_name)
        result["thumb_64"] = from_union([from_str, from_none], self.thumb_64)
        result["thumb_64_gif"] = from_union([from_str, from_none], self.thumb_64__gif)
        result["thumb_64_w"] = from_union([from_str, from_none], self.thumb_64__w)
        result["thumb_64_h"] = from_union([from_str, from_none], self.thumb_64__h)
        result["thumb_80"] = from_union([from_str, from_none], self.thumb_80)
        result["thumb_80_gif"] = from_union([from_str, from_none], self.thumb_80__gif)
        result["thumb_80_w"] = from_union([from_str, from_none], self.thumb_80__w)
        result["thumb_80_h"] = from_union([from_str, from_none], self.thumb_80__h)
        result["thumb_160"] = from_union([from_str, from_none], self.thumb_160)
        result["thumb_160_gif"] = from_union([from_str, from_none], self.thumb_160__gif)
        result["thumb_160_w"] = from_union([from_str, from_none], self.thumb_160__w)
        result["thumb_160_h"] = from_union([from_str, from_none], self.thumb_160__h)
        result["thumb_360"] = from_union([from_str, from_none], self.thumb_360)
        result["thumb_360_gif"] = from_union([from_str, from_none], self.thumb_360__gif)
        result["thumb_360_w"] = from_union([from_str, from_none], self.thumb_360__w)
        result["thumb_360_h"] = from_union([from_str, from_none], self.thumb_360__h)
        result["thumb_480"] = from_union([from_str, from_none], self.thumb_480)
        result["thumb_480_gif"] = from_union([from_str, from_none], self.thumb_480__gif)
        result["thumb_480_w"] = from_union([from_str, from_none], self.thumb_480__w)
        result["thumb_480_h"] = from_union([from_str, from_none], self.thumb_480__h)
        result["thumb_720"] = from_union([from_str, from_none], self.thumb_720)
        result["thumb_720_gif"] = from_union([from_str, from_none], self.thumb_720__gif)
        result["thumb_720_w"] = from_union([from_str, from_none], self.thumb_720__w)
        result["thumb_720_h"] = from_union([from_str, from_none], self.thumb_720__h)
        result["thumb_800"] = from_union([from_str, from_none], self.thumb_800)
        result["thumb_800_gif"] = from_union([from_str, from_none], self.thumb_800__gif)
        result["thumb_800_w"] = from_union([from_str, from_none], self.thumb_800__w)
        result["thumb_800_h"] = from_union([from_str, from_none], self.thumb_800__h)
        result["thumb_960"] = from_union([from_str, from_none], self.thumb_960)
        result["thumb_960_gif"] = from_union([from_str, from_none], self.thumb_960__gif)
        result["thumb_960_w"] = from_union([from_str, from_none], self.thumb_960__w)
        result["thumb_960_h"] = from_union([from_str, from_none], self.thumb_960__h)
        result["thumb_1024"] = from_union([from_str, from_none], self.thumb_1024)
        result["thumb_1024_gif"] = from_union([from_str, from_none], self.thumb_1024__gif)
        result["thumb_1024_w"] = from_union([from_str, from_none], self.thumb_1024__w)
        result["thumb_1024_h"] = from_union([from_str, from_none], self.thumb_1024__h)
        result["thumb_video"] = from_union([from_str, from_none], self.thumb_video)
        result["thumb_gif"] = from_union([from_str, from_none], self.thumb_gif)
        result["thumb_pdf"] = from_union([from_str, from_none], self.thumb_pdf)
        result["thumb_pdf_w"] = from_union([from_str, from_none], self.thumb_pdf_w)
        result["thumb_pdf_h"] = from_union([from_str, from_none], self.thumb_pdf_h)
        result["thumb_tiny"] = from_union([from_str, from_none], self.thumb_tiny)
        result["converted_pdf"] = from_union([from_str, from_none], self.converted_pdf)
        result["image_exif_rotation"] = from_union([from_int, from_none], self.image_exif_rotation)
        result["original_w"] = from_union([from_str, from_none], self.original_w)
        result["original_h"] = from_union([from_str, from_none], self.original_h)
        result["deanimate"] = from_union([from_str, from_none], self.deanimate)
        result["deanimate_gif"] = from_union([from_str, from_none], self.deanimate_gif)
        result["pjpeg"] = from_union([from_str, from_none], self.pjpeg)
        result["permalink"] = from_union([from_str, from_none], self.permalink)
        result["permalink_public"] = from_union([from_str, from_none], self.permalink_public)
        result["edit_link"] = from_union([from_str, from_none], self.edit_link)
        result["has_rich_preview"] = from_union([from_bool, from_none], self.has_rich_preview)
        result["media_display_type"] = from_union([from_str, from_none], self.media_display_type)
        result["preview_is_truncated"] = from_union([from_bool, from_none], self.preview_is_truncated)
        result["preview"] = from_union([from_str, from_none], self.preview)
        result["preview_highlight"] = from_union([from_str, from_none], self.preview_highlight)
        result["plain_text"] = from_union([from_str, from_none], self.plain_text)
        result["preview_plain_text"] = from_union([from_str, from_none], self.preview_plain_text)
        result["has_more"] = from_union([from_bool, from_none], self.has_more)
        result["sent_to_self"] = from_union([from_bool, from_none], self.sent_to_self)
        result["lines"] = from_union([from_int, from_none], self.lines)
        result["lines_more"] = from_union([from_int, from_none], self.lines_more)
        result["is_public"] = from_union([from_bool, from_none], self.is_public)
        result["public_url_shared"] = from_union([from_bool, from_none], self.public_url_shared)
        result["display_as_bot"] = from_union([from_bool, from_none], self.display_as_bot)
        result["channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.channels)
        result["groups"] = from_union([lambda x: from_list(from_str, x), from_none], self.groups)
        result["ims"] = from_union([lambda x: from_list(from_str, x), from_none], self.ims)
        result["shares"] = from_union([lambda x: to_class(Shares, x), from_none], self.shares)
        result["has_more_shares"] = from_union([from_bool, from_none], self.has_more_shares)
        result["to"] = from_union([lambda x: from_list(lambda x: to_class(Cc, x), x), from_none], self.to)
        result["from"] = from_union([lambda x: from_list(lambda x: to_class(Cc, x), x), from_none], self.file_from)
        result["cc"] = from_union([lambda x: from_list(lambda x: to_class(Cc, x), x), from_none], self.cc)
        result["channel_actions_ts"] = from_union([from_str, from_none], self.channel_actions_ts)
        result["channel_actions_count"] = from_union([from_int, from_none], self.channel_actions_count)
        result["headers"] = from_union([lambda x: to_class(Headers, x), from_none], self.headers)
        result["simplified_html"] = from_union([from_str, from_none], self.simplified_html)
        result["media_progress"] = from_union([lambda x: to_class(MediaProgress, x), from_none], self.media_progress)
        result["saved"] = from_union([lambda x: to_class(Saved, x), from_none], self.saved)
        result["quip_thread_id"] = from_union([from_str, from_none], self.quip_thread_id)
        result["is_channel_space"] = from_union([from_bool, from_none], self.is_channel_space)
        result["linked_channel_id"] = from_union([from_str, from_none], self.linked_channel_id)
        result["access"] = from_union([from_str, from_none], self.access)
        result["teams_shared_with"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.teams_shared_with)
        result["last_read"] = from_union([from_int, from_none], self.last_read)
        result["title_blocks"] = from_union([lambda x: from_list(lambda x: to_class(DescriptionBlockElement, x), x), from_none], self.title_blocks)
        result["private_channels_with_file_access_count"] = from_union([from_int, from_none], self.private_channels_with_file_access_count)
        result["private_file_with_access_count"] = from_union([from_int, from_none], self.private_file_with_access_count)
        result["dm_mpdm_users_with_file_access"] = from_union([lambda x: from_list(lambda x: to_class(DmMpdmUsersWithFileAccess, x), x), from_none], self.dm_mpdm_users_with_file_access)
        result["org_or_workspace_access"] = from_union([from_str, from_none], self.org_or_workspace_access)
        result["update_notification"] = from_union([from_int, from_none], self.update_notification)
        result["canvas_template_mode"] = from_union([from_str, from_none], self.canvas_template_mode)
        result["template_conversion_ts"] = from_union([from_int, from_none], self.template_conversion_ts)
        result["template_name"] = from_union([from_str, from_none], self.template_name)
        result["template_title"] = from_union([from_str, from_none], self.template_title)
        result["template_description"] = from_union([from_str, from_none], self.template_description)
        result["template_icon"] = from_union([from_str, from_none], self.template_icon)
        result["team_pref_version_history_enabled"] = from_union([from_bool, from_none], self.team_pref_version_history_enabled)
        result["show_badge"] = from_union([from_bool, from_none], self.show_badge)
        result["favorites"] = from_union([lambda x: from_list(lambda x: to_class(Favorite, x), x), from_none], self.favorites)
        result["list_metadata"] = from_union([lambda x: to_class(ListMetadata, x), from_none], self.list_metadata)
        result["list_limits"] = from_union([lambda x: to_class(ListLimits, x), from_none], self.list_limits)
        result["list_csv_download_url"] = from_union([from_str, from_none], self.list_csv_download_url)
        result["can_toggle_canvas_lock"] = from_union([from_bool, from_none], self.can_toggle_canvas_lock)
        result["is_restricted_sharing_enabled"] = from_union([from_bool, from_none], self.is_restricted_sharing_enabled)
        result["canvas_printing_enabled"] = from_union([from_bool, from_none], self.canvas_printing_enabled)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["initial_comment"] = from_union([lambda x: to_class(InitialComment, x), from_none], self.initial_comment)
        result["num_stars"] = from_union([from_int, from_none], self.num_stars)
        result["is_starred"] = from_union([from_bool, from_none], self.is_starred)
        result["pinned_to"] = from_union([lambda x: from_list(from_str, x), from_none], self.pinned_to)
        result["reactions"] = from_union([lambda x: from_list(lambda x: to_class(Reaction, x), x), from_none], self.reactions)
        result["comments_count"] = from_union([from_int, from_none], self.comments_count)
        result["attachments"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.attachments)
        result["blocks"] = from_union([lambda x: from_list(lambda x: to_class(DescriptionBlockElement, x), x), from_none], self.blocks)
        return result


@dataclass
class AssistantAppThreadBlock:
    type: Optional[BlockType] = None
    elements: Optional[List[Accessory]] = None
    block_id: Optional[str] = None
    call_id: Optional[str] = None
    api_decoration_available: Optional[bool] = None
    call: Optional[Call] = None
    external_id: Optional[str] = None
    source: Optional[str] = None
    file_id: Optional[str] = None
    file: Optional[File] = None
    text: Optional[DescriptionElement] = None
    fallback: Optional[str] = None
    image_url: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    is_animated: Optional[bool] = None
    slack_file: Optional[SlackFile] = None
    alt_text: Optional[str] = None
    title: Optional[DescriptionElement] = None
    title_url: Optional[str] = None
    description: Optional[DescriptionElement] = None
    video_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    author_name: Optional[str] = None
    provider_name: Optional[str] = None
    provider_icon_url: Optional[str] = None
    function_trigger_id: Optional[str] = None
    app_id: Optional[str] = None
    is_workflow_app: Optional[bool] = None
    sales_home_workflow_app_type: Optional[int] = None
    app_collaborators: Optional[List[str]] = None
    button_label: Optional[str] = None
    bot_user_id: Optional[str] = None
    url: Optional[str] = None
    owning_team_id: Optional[str] = None
    workflow_id: Optional[str] = None
    developer_trace_id: Optional[str] = None
    trigger_type: Optional[str] = None
    trigger_subtype: Optional[str] = None
    share_url: Optional[str] = None
    fields: Optional[List[DescriptionElement]] = None
    accessory: Optional[Accessory] = None
    expand: Optional[bool] = None
    label: Optional[DescriptionElement] = None
    element: Optional[Accessory] = None
    dispatch_action: Optional[bool] = None
    hint: Optional[DescriptionElement] = None
    optional: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AssistantAppThreadBlock':
        assert isinstance(obj, dict)
        type = from_union([BlockType, from_none], obj.get("type"))
        elements = from_union([lambda x: from_list(Accessory.from_dict, x), from_none], obj.get("elements"))
        block_id = from_union([from_str, from_none], obj.get("block_id"))
        call_id = from_union([from_str, from_none], obj.get("call_id"))
        api_decoration_available = from_union([from_bool, from_none], obj.get("api_decoration_available"))
        call = from_union([Call.from_dict, from_none], obj.get("call"))
        external_id = from_union([from_str, from_none], obj.get("external_id"))
        source = from_union([from_str, from_none], obj.get("source"))
        file_id = from_union([from_str, from_none], obj.get("file_id"))
        file = from_union([File.from_dict, from_none], obj.get("file"))
        text = from_union([DescriptionElement.from_dict, from_none], obj.get("text"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        is_animated = from_union([from_bool, from_none], obj.get("is_animated"))
        slack_file = from_union([SlackFile.from_dict, from_none], obj.get("slack_file"))
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        title = from_union([DescriptionElement.from_dict, from_none], obj.get("title"))
        title_url = from_union([from_str, from_none], obj.get("title_url"))
        description = from_union([DescriptionElement.from_dict, from_none], obj.get("description"))
        video_url = from_union([from_str, from_none], obj.get("video_url"))
        thumbnail_url = from_union([from_str, from_none], obj.get("thumbnail_url"))
        author_name = from_union([from_str, from_none], obj.get("author_name"))
        provider_name = from_union([from_str, from_none], obj.get("provider_name"))
        provider_icon_url = from_union([from_str, from_none], obj.get("provider_icon_url"))
        function_trigger_id = from_union([from_str, from_none], obj.get("function_trigger_id"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        is_workflow_app = from_union([from_bool, from_none], obj.get("is_workflow_app"))
        sales_home_workflow_app_type = from_union([from_int, from_none], obj.get("sales_home_workflow_app_type"))
        app_collaborators = from_union([lambda x: from_list(from_str, x), from_none], obj.get("app_collaborators"))
        button_label = from_union([from_str, from_none], obj.get("button_label"))
        bot_user_id = from_union([from_str, from_none], obj.get("bot_user_id"))
        url = from_union([from_str, from_none], obj.get("url"))
        owning_team_id = from_union([from_str, from_none], obj.get("owning_team_id"))
        workflow_id = from_union([from_str, from_none], obj.get("workflow_id"))
        developer_trace_id = from_union([from_str, from_none], obj.get("developer_trace_id"))
        trigger_type = from_union([from_str, from_none], obj.get("trigger_type"))
        trigger_subtype = from_union([from_str, from_none], obj.get("trigger_subtype"))
        share_url = from_union([from_str, from_none], obj.get("share_url"))
        fields = from_union([lambda x: from_list(DescriptionElement.from_dict, x), from_none], obj.get("fields"))
        accessory = from_union([Accessory.from_dict, from_none], obj.get("accessory"))
        expand = from_union([from_bool, from_none], obj.get("expand"))
        label = from_union([DescriptionElement.from_dict, from_none], obj.get("label"))
        element = from_union([Accessory.from_dict, from_none], obj.get("element"))
        dispatch_action = from_union([from_bool, from_none], obj.get("dispatch_action"))
        hint = from_union([DescriptionElement.from_dict, from_none], obj.get("hint"))
        optional = from_union([from_bool, from_none], obj.get("optional"))
        return AssistantAppThreadBlock(type, elements, block_id, call_id, api_decoration_available, call, external_id, source, file_id, file, text, fallback, image_url, image_width, image_height, image_bytes, is_animated, slack_file, alt_text, title, title_url, description, video_url, thumbnail_url, author_name, provider_name, provider_icon_url, function_trigger_id, app_id, is_workflow_app, sales_home_workflow_app_type, app_collaborators, button_label, bot_user_id, url, owning_team_id, workflow_id, developer_trace_id, trigger_type, trigger_subtype, share_url, fields, accessory, expand, label, element, dispatch_action, hint, optional)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: to_enum(BlockType, x), from_none], self.type)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(Accessory, x), x), from_none], self.elements)
        result["block_id"] = from_union([from_str, from_none], self.block_id)
        result["call_id"] = from_union([from_str, from_none], self.call_id)
        result["api_decoration_available"] = from_union([from_bool, from_none], self.api_decoration_available)
        result["call"] = from_union([lambda x: to_class(Call, x), from_none], self.call)
        result["external_id"] = from_union([from_str, from_none], self.external_id)
        result["source"] = from_union([from_str, from_none], self.source)
        result["file_id"] = from_union([from_str, from_none], self.file_id)
        result["file"] = from_union([lambda x: to_class(File, x), from_none], self.file)
        result["text"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.text)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["is_animated"] = from_union([from_bool, from_none], self.is_animated)
        result["slack_file"] = from_union([lambda x: to_class(SlackFile, x), from_none], self.slack_file)
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["title"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.title)
        result["title_url"] = from_union([from_str, from_none], self.title_url)
        result["description"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.description)
        result["video_url"] = from_union([from_str, from_none], self.video_url)
        result["thumbnail_url"] = from_union([from_str, from_none], self.thumbnail_url)
        result["author_name"] = from_union([from_str, from_none], self.author_name)
        result["provider_name"] = from_union([from_str, from_none], self.provider_name)
        result["provider_icon_url"] = from_union([from_str, from_none], self.provider_icon_url)
        result["function_trigger_id"] = from_union([from_str, from_none], self.function_trigger_id)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["is_workflow_app"] = from_union([from_bool, from_none], self.is_workflow_app)
        result["sales_home_workflow_app_type"] = from_union([from_int, from_none], self.sales_home_workflow_app_type)
        result["app_collaborators"] = from_union([lambda x: from_list(from_str, x), from_none], self.app_collaborators)
        result["button_label"] = from_union([from_str, from_none], self.button_label)
        result["bot_user_id"] = from_union([from_str, from_none], self.bot_user_id)
        result["url"] = from_union([from_str, from_none], self.url)
        result["owning_team_id"] = from_union([from_str, from_none], self.owning_team_id)
        result["workflow_id"] = from_union([from_str, from_none], self.workflow_id)
        result["developer_trace_id"] = from_union([from_str, from_none], self.developer_trace_id)
        result["trigger_type"] = from_union([from_str, from_none], self.trigger_type)
        result["trigger_subtype"] = from_union([from_str, from_none], self.trigger_subtype)
        result["share_url"] = from_union([from_str, from_none], self.share_url)
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(DescriptionElement, x), x), from_none], self.fields)
        result["accessory"] = from_union([lambda x: to_class(Accessory, x), from_none], self.accessory)
        result["expand"] = from_union([from_bool, from_none], self.expand)
        result["label"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.label)
        result["element"] = from_union([lambda x: to_class(Accessory, x), from_none], self.element)
        result["dispatch_action"] = from_union([from_bool, from_none], self.dispatch_action)
        result["hint"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.hint)
        result["optional"] = from_union([from_bool, from_none], self.optional)
        return result


@dataclass
class AssistantAppThread:
    title: Optional[str] = None
    title_blocks: Optional[List[AssistantAppThreadBlock]] = None
    first_user_thread_reply: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AssistantAppThread':
        assert isinstance(obj, dict)
        title = from_union([from_str, from_none], obj.get("title"))
        title_blocks = from_union([lambda x: from_list(AssistantAppThreadBlock.from_dict, x), from_none], obj.get("title_blocks"))
        first_user_thread_reply = from_union([from_str, from_none], obj.get("first_user_thread_reply"))
        return AssistantAppThread(title, title_blocks, first_user_thread_reply)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([from_str, from_none], self.title)
        result["title_blocks"] = from_union([lambda x: from_list(lambda x: to_class(AssistantAppThreadBlock, x), x), from_none], self.title_blocks)
        result["first_user_thread_reply"] = from_union([from_str, from_none], self.first_user_thread_reply)
        return result


@dataclass
class Icons:
    image_36: Optional[str] = None
    image_48: Optional[str] = None
    image_72: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Icons':
        assert isinstance(obj, dict)
        image_36 = from_union([from_str, from_none], obj.get("image_36"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        return Icons(image_36, image_48, image_72)

    def to_dict(self) -> dict:
        result: dict = {}
        result["image_36"] = from_union([from_str, from_none], self.image_36)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        return result


@dataclass
class BotProfile:
    id: Optional[str] = None
    deleted: Optional[bool] = None
    name: Optional[str] = None
    updated: Optional[int] = None
    app_id: Optional[str] = None
    icons: Optional[Icons] = None
    team_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BotProfile':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        deleted = from_union([from_bool, from_none], obj.get("deleted"))
        name = from_union([from_str, from_none], obj.get("name"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        icons = from_union([Icons.from_dict, from_none], obj.get("icons"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        return BotProfile(id, deleted, name, updated, app_id, icons, team_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["deleted"] = from_union([from_bool, from_none], self.deleted)
        result["name"] = from_union([from_str, from_none], self.name)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["icons"] = from_union([lambda x: to_class(Icons, x), from_none], self.icons)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        return result


@dataclass
class Knocks:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'Knocks':
        assert isinstance(obj, dict)
        return Knocks()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class Recording:
    transcript: Optional[bool] = None
    summary: Optional[bool] = None
    notetaking: Optional[bool] = None
    summary_status: Optional[str] = None
    can_record_summary: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Recording':
        assert isinstance(obj, dict)
        transcript = from_union([from_bool, from_none], obj.get("transcript"))
        summary = from_union([from_bool, from_none], obj.get("summary"))
        notetaking = from_union([from_bool, from_none], obj.get("notetaking"))
        summary_status = from_union([from_str, from_none], obj.get("summary_status"))
        can_record_summary = from_union([from_str, from_none], obj.get("can_record_summary"))
        return Recording(transcript, summary, notetaking, summary_status, can_record_summary)

    def to_dict(self) -> dict:
        result: dict = {}
        result["transcript"] = from_union([from_bool, from_none], self.transcript)
        result["summary"] = from_union([from_bool, from_none], self.summary)
        result["notetaking"] = from_union([from_bool, from_none], self.notetaking)
        result["summary_status"] = from_union([from_str, from_none], self.summary_status)
        result["can_record_summary"] = from_union([from_str, from_none], self.can_record_summary)
        return result


@dataclass
class Room:
    id: Optional[str] = None
    name: Optional[str] = None
    media_server: Optional[str] = None
    created_by: Optional[str] = None
    date_start: Optional[int] = None
    date_end: Optional[int] = None
    participants: Optional[List[str]] = None
    participant_history: Optional[List[str]] = None
    participants_camera_on: Optional[List[str]] = None
    participants_camera_off: Optional[List[str]] = None
    participants_screenshare_on: Optional[List[str]] = None
    participants_screenshare_off: Optional[List[str]] = None
    canvas_thread_ts: Optional[str] = None
    thread_root_ts: Optional[str] = None
    channels: Optional[List[str]] = None
    is_dm_call: Optional[bool] = None
    was_rejected: Optional[bool] = None
    was_missed: Optional[bool] = None
    was_accepted: Optional[bool] = None
    has_ended: Optional[bool] = None
    background_id: Optional[str] = None
    canvas_background: Optional[str] = None
    is_prewarmed: Optional[bool] = None
    is_scheduled: Optional[bool] = None
    attached_file_ids: Optional[List[str]] = None
    media_backend_type: Optional[str] = None
    display_id: Optional[str] = None
    external_unique_id: Optional[str] = None
    app_id: Optional[str] = None
    call_family: Optional[str] = None
    pending_invitees: Optional[Knocks] = None
    last_invite_status_by_user: Optional[Knocks] = None
    knocks: Optional[Knocks] = None
    recording: Optional[Recording] = None
    huddle_link: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Room':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        media_server = from_union([from_str, from_none], obj.get("media_server"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        date_start = from_union([from_int, from_none], obj.get("date_start"))
        date_end = from_union([from_int, from_none], obj.get("date_end"))
        participants = from_union([lambda x: from_list(from_str, x), from_none], obj.get("participants"))
        participant_history = from_union([lambda x: from_list(from_str, x), from_none], obj.get("participant_history"))
        participants_camera_on = from_union([lambda x: from_list(from_str, x), from_none], obj.get("participants_camera_on"))
        participants_camera_off = from_union([lambda x: from_list(from_str, x), from_none], obj.get("participants_camera_off"))
        participants_screenshare_on = from_union([lambda x: from_list(from_str, x), from_none], obj.get("participants_screenshare_on"))
        participants_screenshare_off = from_union([lambda x: from_list(from_str, x), from_none], obj.get("participants_screenshare_off"))
        canvas_thread_ts = from_union([from_str, from_none], obj.get("canvas_thread_ts"))
        thread_root_ts = from_union([from_str, from_none], obj.get("thread_root_ts"))
        channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channels"))
        is_dm_call = from_union([from_bool, from_none], obj.get("is_dm_call"))
        was_rejected = from_union([from_bool, from_none], obj.get("was_rejected"))
        was_missed = from_union([from_bool, from_none], obj.get("was_missed"))
        was_accepted = from_union([from_bool, from_none], obj.get("was_accepted"))
        has_ended = from_union([from_bool, from_none], obj.get("has_ended"))
        background_id = from_union([from_str, from_none], obj.get("background_id"))
        canvas_background = from_union([from_str, from_none], obj.get("canvas_background"))
        is_prewarmed = from_union([from_bool, from_none], obj.get("is_prewarmed"))
        is_scheduled = from_union([from_bool, from_none], obj.get("is_scheduled"))
        attached_file_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("attached_file_ids"))
        media_backend_type = from_union([from_str, from_none], obj.get("media_backend_type"))
        display_id = from_union([from_str, from_none], obj.get("display_id"))
        external_unique_id = from_union([from_str, from_none], obj.get("external_unique_id"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        call_family = from_union([from_str, from_none], obj.get("call_family"))
        pending_invitees = from_union([Knocks.from_dict, from_none], obj.get("pending_invitees"))
        last_invite_status_by_user = from_union([Knocks.from_dict, from_none], obj.get("last_invite_status_by_user"))
        knocks = from_union([Knocks.from_dict, from_none], obj.get("knocks"))
        recording = from_union([Recording.from_dict, from_none], obj.get("recording"))
        huddle_link = from_union([from_str, from_none], obj.get("huddle_link"))
        return Room(id, name, media_server, created_by, date_start, date_end, participants, participant_history, participants_camera_on, participants_camera_off, participants_screenshare_on, participants_screenshare_off, canvas_thread_ts, thread_root_ts, channels, is_dm_call, was_rejected, was_missed, was_accepted, has_ended, background_id, canvas_background, is_prewarmed, is_scheduled, attached_file_ids, media_backend_type, display_id, external_unique_id, app_id, call_family, pending_invitees, last_invite_status_by_user, knocks, recording, huddle_link)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["media_server"] = from_union([from_str, from_none], self.media_server)
        result["created_by"] = from_union([from_str, from_none], self.created_by)
        result["date_start"] = from_union([from_int, from_none], self.date_start)
        result["date_end"] = from_union([from_int, from_none], self.date_end)
        result["participants"] = from_union([lambda x: from_list(from_str, x), from_none], self.participants)
        result["participant_history"] = from_union([lambda x: from_list(from_str, x), from_none], self.participant_history)
        result["participants_camera_on"] = from_union([lambda x: from_list(from_str, x), from_none], self.participants_camera_on)
        result["participants_camera_off"] = from_union([lambda x: from_list(from_str, x), from_none], self.participants_camera_off)
        result["participants_screenshare_on"] = from_union([lambda x: from_list(from_str, x), from_none], self.participants_screenshare_on)
        result["participants_screenshare_off"] = from_union([lambda x: from_list(from_str, x), from_none], self.participants_screenshare_off)
        result["canvas_thread_ts"] = from_union([from_str, from_none], self.canvas_thread_ts)
        result["thread_root_ts"] = from_union([from_str, from_none], self.thread_root_ts)
        result["channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.channels)
        result["is_dm_call"] = from_union([from_bool, from_none], self.is_dm_call)
        result["was_rejected"] = from_union([from_bool, from_none], self.was_rejected)
        result["was_missed"] = from_union([from_bool, from_none], self.was_missed)
        result["was_accepted"] = from_union([from_bool, from_none], self.was_accepted)
        result["has_ended"] = from_union([from_bool, from_none], self.has_ended)
        result["background_id"] = from_union([from_str, from_none], self.background_id)
        result["canvas_background"] = from_union([from_str, from_none], self.canvas_background)
        result["is_prewarmed"] = from_union([from_bool, from_none], self.is_prewarmed)
        result["is_scheduled"] = from_union([from_bool, from_none], self.is_scheduled)
        result["attached_file_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.attached_file_ids)
        result["media_backend_type"] = from_union([from_str, from_none], self.media_backend_type)
        result["display_id"] = from_union([from_str, from_none], self.display_id)
        result["external_unique_id"] = from_union([from_str, from_none], self.external_unique_id)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["call_family"] = from_union([from_str, from_none], self.call_family)
        result["pending_invitees"] = from_union([lambda x: to_class(Knocks, x), from_none], self.pending_invitees)
        result["last_invite_status_by_user"] = from_union([lambda x: to_class(Knocks, x), from_none], self.last_invite_status_by_user)
        result["knocks"] = from_union([lambda x: to_class(Knocks, x), from_none], self.knocks)
        result["recording"] = from_union([lambda x: to_class(Recording, x), from_none], self.recording)
        result["huddle_link"] = from_union([from_str, from_none], self.huddle_link)
        return result


@dataclass
class Message:
    bot_id: Optional[str] = None
    type: Optional[str] = None
    text: Optional[str] = None
    user: Optional[str] = None
    ts: Optional[str] = None
    team: Optional[str] = None
    bot_profile: Optional[BotProfile] = None
    reactions: Optional[List[Reaction]] = None
    permalink: Optional[str] = None
    app_id: Optional[str] = None
    room: Optional[Room] = None
    blocks: Optional[List[AssistantAppThreadBlock]] = None
    assistant_app_thread: Optional[AssistantAppThread] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Message':
        assert isinstance(obj, dict)
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        text = from_union([from_str, from_none], obj.get("text"))
        user = from_union([from_str, from_none], obj.get("user"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        team = from_union([from_str, from_none], obj.get("team"))
        bot_profile = from_union([BotProfile.from_dict, from_none], obj.get("bot_profile"))
        reactions = from_union([lambda x: from_list(Reaction.from_dict, x), from_none], obj.get("reactions"))
        permalink = from_union([from_str, from_none], obj.get("permalink"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        room = from_union([Room.from_dict, from_none], obj.get("room"))
        blocks = from_union([lambda x: from_list(AssistantAppThreadBlock.from_dict, x), from_none], obj.get("blocks"))
        assistant_app_thread = from_union([AssistantAppThread.from_dict, from_none], obj.get("assistant_app_thread"))
        return Message(bot_id, type, text, user, ts, team, bot_profile, reactions, permalink, app_id, room, blocks, assistant_app_thread)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["text"] = from_union([from_str, from_none], self.text)
        result["user"] = from_union([from_str, from_none], self.user)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["team"] = from_union([from_str, from_none], self.team)
        result["bot_profile"] = from_union([lambda x: to_class(BotProfile, x), from_none], self.bot_profile)
        result["reactions"] = from_union([lambda x: from_list(lambda x: to_class(Reaction, x), x), from_none], self.reactions)
        result["permalink"] = from_union([from_str, from_none], self.permalink)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["room"] = from_union([lambda x: to_class(Room, x), from_none], self.room)
        result["blocks"] = from_union([lambda x: from_list(lambda x: to_class(AssistantAppThreadBlock, x), x), from_none], self.blocks)
        result["assistant_app_thread"] = from_union([lambda x: to_class(AssistantAppThread, x), from_none], self.assistant_app_thread)
        return result


@dataclass
class ReactionsGetResponse:
    ok: Optional[bool] = None
    type: Optional[str] = None
    channel: Optional[str] = None
    message: Optional[Message] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ReactionsGetResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        type = from_union([from_str, from_none], obj.get("type"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        message = from_union([Message.from_dict, from_none], obj.get("message"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return ReactionsGetResponse(ok, type, channel, message, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["type"] = from_union([from_str, from_none], self.type)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["message"] = from_union([lambda x: to_class(Message, x), from_none], self.message)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def reactions_get_response_from_dict(s: Any) -> ReactionsGetResponse:
    return ReactionsGetResponse.from_dict(s)


def reactions_get_response_to_dict(x: ReactionsGetResponse) -> Any:
    return to_class(ReactionsGetResponse, x)

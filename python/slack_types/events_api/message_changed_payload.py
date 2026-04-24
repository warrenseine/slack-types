# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = message_changed_payload_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


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


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


@dataclass
class Authorization:
    enterprise_id: Optional[str] = None
    team_id: Optional[str] = None
    user_id: Optional[str] = None
    is_bot: Optional[bool] = None
    is_enterprise_install: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Authorization':
        assert isinstance(obj, dict)
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        is_bot = from_union([from_bool, from_none], obj.get("is_bot"))
        is_enterprise_install = from_union([from_bool, from_none], obj.get("is_enterprise_install"))
        return Authorization(enterprise_id, team_id, user_id, is_bot, is_enterprise_install)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["is_bot"] = from_union([from_bool, from_none], self.is_bot)
        result["is_enterprise_install"] = from_union([from_bool, from_none], self.is_enterprise_install)
        return result


@dataclass
class ActionConfirm:
    title: Optional[str] = None
    text: Optional[str] = None
    ok_text: Optional[str] = None
    dismiss_text: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ActionConfirm':
        assert isinstance(obj, dict)
        title = from_union([from_str, from_none], obj.get("title"))
        text = from_union([from_str, from_none], obj.get("text"))
        ok_text = from_union([from_str, from_none], obj.get("ok_text"))
        dismiss_text = from_union([from_str, from_none], obj.get("dismiss_text"))
        return ActionConfirm(title, text, ok_text, dismiss_text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([from_str, from_none], self.title)
        result["text"] = from_union([from_str, from_none], self.text)
        result["ok_text"] = from_union([from_str, from_none], self.ok_text)
        result["dismiss_text"] = from_union([from_str, from_none], self.dismiss_text)
        return result


@dataclass
class Action:
    id: Optional[str] = None
    name: Optional[str] = None
    text: Optional[str] = None
    style: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    confirm: Optional[ActionConfirm] = None
    options: Optional[List[Any]] = None
    selected_options: Optional[List[Any]] = None
    data_source: Optional[str] = None
    min_query_length: Optional[int] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Action':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        text = from_union([from_str, from_none], obj.get("text"))
        style = from_union([from_str, from_none], obj.get("style"))
        type = from_union([from_str, from_none], obj.get("type"))
        value = from_union([from_str, from_none], obj.get("value"))
        confirm = from_union([ActionConfirm.from_dict, from_none], obj.get("confirm"))
        options = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("options"))
        selected_options = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("selected_options"))
        data_source = from_union([from_str, from_none], obj.get("data_source"))
        min_query_length = from_union([from_int, from_none], obj.get("min_query_length"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Action(id, name, text, style, type, value, confirm, options, selected_options, data_source, min_query_length, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["text"] = from_union([from_str, from_none], self.text)
        result["style"] = from_union([from_str, from_none], self.style)
        result["type"] = from_union([from_str, from_none], self.type)
        result["value"] = from_union([from_str, from_none], self.value)
        result["confirm"] = from_union([lambda x: to_class(ActionConfirm, x), from_none], self.confirm)
        result["options"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.options)
        result["selected_options"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.selected_options)
        result["data_source"] = from_union([from_str, from_none], self.data_source)
        result["min_query_length"] = from_union([from_int, from_none], self.min_query_length)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class Field:
    title: Optional[str] = None
    value: Optional[str] = None
    short: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Field':
        assert isinstance(obj, dict)
        title = from_union([from_str, from_none], obj.get("title"))
        value = from_union([from_str, from_none], obj.get("value"))
        short = from_union([from_bool, from_none], obj.get("short"))
        return Field(title, value, short)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([from_str, from_none], self.title)
        result["value"] = from_union([from_str, from_none], self.value)
        result["short"] = from_union([from_bool, from_none], self.short)
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
class ListMetadata:
    icon: Optional[str] = None
    icon_url: Optional[str] = None
    icon_team_id: Optional[str] = None
    description: Optional[str] = None
    is_trial: Optional[bool] = None
    creation_source: Optional[CreationSource] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ListMetadata':
        assert isinstance(obj, dict)
        icon = from_union([from_str, from_none], obj.get("icon"))
        icon_url = from_union([from_str, from_none], obj.get("icon_url"))
        icon_team_id = from_union([from_str, from_none], obj.get("icon_team_id"))
        description = from_union([from_str, from_none], obj.get("description"))
        is_trial = from_union([from_bool, from_none], obj.get("is_trial"))
        creation_source = from_union([CreationSource.from_dict, from_none], obj.get("creation_source"))
        return ListMetadata(icon, icon_url, icon_team_id, description, is_trial, creation_source)

    def to_dict(self) -> dict:
        result: dict = {}
        result["icon"] = from_union([from_str, from_none], self.icon)
        result["icon_url"] = from_union([from_str, from_none], self.icon_url)
        result["icon_team_id"] = from_union([from_str, from_none], self.icon_team_id)
        result["description"] = from_union([from_str, from_none], self.description)
        result["is_trial"] = from_union([from_bool, from_none], self.is_trial)
        result["creation_source"] = from_union([lambda x: to_class(CreationSource, x), from_none], self.creation_source)
        return result


@dataclass
class Shares:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'Shares':
        assert isinstance(obj, dict)
        return Shares()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class ListClass:
    id: Optional[str] = None
    created: Optional[int] = None
    timestamp: Optional[int] = None
    name: Optional[str] = None
    title: Optional[str] = None
    mimetype: Optional[str] = None
    filetype: Optional[str] = None
    external_type: Optional[str] = None
    pretty_type: Optional[str] = None
    user: Optional[str] = None
    user_team: Optional[str] = None
    editable: Optional[bool] = None
    size: Optional[int] = None
    mode: Optional[str] = None
    is_external: Optional[bool] = None
    is_public: Optional[bool] = None
    public_url_shared: Optional[bool] = None
    display_as_bot: Optional[bool] = None
    username: Optional[str] = None
    list_metadata: Optional[ListMetadata] = None
    list_limits: Optional[ListLimits] = None
    url_private: Optional[str] = None
    url_private_download: Optional[str] = None
    permalink: Optional[str] = None
    permalink_public: Optional[str] = None
    last_editor: Optional[str] = None
    updated: Optional[int] = None
    comments_count: Optional[int] = None
    shares: Optional[Shares] = None
    has_more_shares: Optional[bool] = None
    private_channels_with_file_access_count: Optional[int] = None
    private_file_with_access_count: Optional[int] = None
    has_rich_preview: Optional[bool] = None
    file_access: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ListClass':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        created = from_union([from_int, from_none], obj.get("created"))
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        name = from_union([from_str, from_none], obj.get("name"))
        title = from_union([from_str, from_none], obj.get("title"))
        mimetype = from_union([from_str, from_none], obj.get("mimetype"))
        filetype = from_union([from_str, from_none], obj.get("filetype"))
        external_type = from_union([from_str, from_none], obj.get("external_type"))
        pretty_type = from_union([from_str, from_none], obj.get("pretty_type"))
        user = from_union([from_str, from_none], obj.get("user"))
        user_team = from_union([from_str, from_none], obj.get("user_team"))
        editable = from_union([from_bool, from_none], obj.get("editable"))
        size = from_union([from_int, from_none], obj.get("size"))
        mode = from_union([from_str, from_none], obj.get("mode"))
        is_external = from_union([from_bool, from_none], obj.get("is_external"))
        is_public = from_union([from_bool, from_none], obj.get("is_public"))
        public_url_shared = from_union([from_bool, from_none], obj.get("public_url_shared"))
        display_as_bot = from_union([from_bool, from_none], obj.get("display_as_bot"))
        username = from_union([from_str, from_none], obj.get("username"))
        list_metadata = from_union([ListMetadata.from_dict, from_none], obj.get("list_metadata"))
        list_limits = from_union([ListLimits.from_dict, from_none], obj.get("list_limits"))
        url_private = from_union([from_str, from_none], obj.get("url_private"))
        url_private_download = from_union([from_str, from_none], obj.get("url_private_download"))
        permalink = from_union([from_str, from_none], obj.get("permalink"))
        permalink_public = from_union([from_str, from_none], obj.get("permalink_public"))
        last_editor = from_union([from_str, from_none], obj.get("last_editor"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        comments_count = from_union([from_int, from_none], obj.get("comments_count"))
        shares = from_union([Shares.from_dict, from_none], obj.get("shares"))
        has_more_shares = from_union([from_bool, from_none], obj.get("has_more_shares"))
        private_channels_with_file_access_count = from_union([from_int, from_none], obj.get("private_channels_with_file_access_count"))
        private_file_with_access_count = from_union([from_int, from_none], obj.get("private_file_with_access_count"))
        has_rich_preview = from_union([from_bool, from_none], obj.get("has_rich_preview"))
        file_access = from_union([from_str, from_none], obj.get("file_access"))
        return ListClass(id, created, timestamp, name, title, mimetype, filetype, external_type, pretty_type, user, user_team, editable, size, mode, is_external, is_public, public_url_shared, display_as_bot, username, list_metadata, list_limits, url_private, url_private_download, permalink, permalink_public, last_editor, updated, comments_count, shares, has_more_shares, private_channels_with_file_access_count, private_file_with_access_count, has_rich_preview, file_access)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["created"] = from_union([from_int, from_none], self.created)
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        result["name"] = from_union([from_str, from_none], self.name)
        result["title"] = from_union([from_str, from_none], self.title)
        result["mimetype"] = from_union([from_str, from_none], self.mimetype)
        result["filetype"] = from_union([from_str, from_none], self.filetype)
        result["external_type"] = from_union([from_str, from_none], self.external_type)
        result["pretty_type"] = from_union([from_str, from_none], self.pretty_type)
        result["user"] = from_union([from_str, from_none], self.user)
        result["user_team"] = from_union([from_str, from_none], self.user_team)
        result["editable"] = from_union([from_bool, from_none], self.editable)
        result["size"] = from_union([from_int, from_none], self.size)
        result["mode"] = from_union([from_str, from_none], self.mode)
        result["is_external"] = from_union([from_bool, from_none], self.is_external)
        result["is_public"] = from_union([from_bool, from_none], self.is_public)
        result["public_url_shared"] = from_union([from_bool, from_none], self.public_url_shared)
        result["display_as_bot"] = from_union([from_bool, from_none], self.display_as_bot)
        result["username"] = from_union([from_str, from_none], self.username)
        result["list_metadata"] = from_union([lambda x: to_class(ListMetadata, x), from_none], self.list_metadata)
        result["list_limits"] = from_union([lambda x: to_class(ListLimits, x), from_none], self.list_limits)
        result["url_private"] = from_union([from_str, from_none], self.url_private)
        result["url_private_download"] = from_union([from_str, from_none], self.url_private_download)
        result["permalink"] = from_union([from_str, from_none], self.permalink)
        result["permalink_public"] = from_union([from_str, from_none], self.permalink_public)
        result["last_editor"] = from_union([from_str, from_none], self.last_editor)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["comments_count"] = from_union([from_int, from_none], self.comments_count)
        result["shares"] = from_union([lambda x: to_class(Shares, x), from_none], self.shares)
        result["has_more_shares"] = from_union([from_bool, from_none], self.has_more_shares)
        result["private_channels_with_file_access_count"] = from_union([from_int, from_none], self.private_channels_with_file_access_count)
        result["private_file_with_access_count"] = from_union([from_int, from_none], self.private_file_with_access_count)
        result["has_rich_preview"] = from_union([from_bool, from_none], self.has_rich_preview)
        result["file_access"] = from_union([from_str, from_none], self.file_access)
        return result


@dataclass
class Record:
    record_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Record':
        assert isinstance(obj, dict)
        record_id = from_union([from_str, from_none], obj.get("record_id"))
        return Record(record_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["record_id"] = from_union([from_str, from_none], self.record_id)
        return result


@dataclass
class ListRecord:
    record: Optional[Record] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ListRecord':
        assert isinstance(obj, dict)
        record = from_union([Record.from_dict, from_none], obj.get("record"))
        return ListRecord(record)

    def to_dict(self) -> dict:
        result: dict = {}
        result["record"] = from_union([lambda x: to_class(Record, x), from_none], self.record)
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
class ListView:
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    is_locked: Optional[bool] = None
    position: Optional[str] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
    stick_column_left: Optional[bool] = None
    is_all_items_view: Optional[bool] = None
    default_view_key: Optional[str] = None
    show_completed_items: Optional[bool] = None
    grouping: Optional[Grouping] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ListView':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([from_str, from_none], obj.get("type"))
        is_locked = from_union([from_bool, from_none], obj.get("is_locked"))
        position = from_union([from_str, from_none], obj.get("position"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        stick_column_left = from_union([from_bool, from_none], obj.get("stick_column_left"))
        is_all_items_view = from_union([from_bool, from_none], obj.get("is_all_items_view"))
        default_view_key = from_union([from_str, from_none], obj.get("default_view_key"))
        show_completed_items = from_union([from_bool, from_none], obj.get("show_completed_items"))
        grouping = from_union([Grouping.from_dict, from_none], obj.get("grouping"))
        return ListView(id, name, type, is_locked, position, date_created, created_by, stick_column_left, is_all_items_view, default_view_key, show_completed_items, grouping)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["type"] = from_union([from_str, from_none], self.type)
        result["is_locked"] = from_union([from_bool, from_none], self.is_locked)
        result["position"] = from_union([from_str, from_none], self.position)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["created_by"] = from_union([from_str, from_none], self.created_by)
        result["stick_column_left"] = from_union([from_bool, from_none], self.stick_column_left)
        result["is_all_items_view"] = from_union([from_bool, from_none], self.is_all_items_view)
        result["default_view_key"] = from_union([from_str, from_none], self.default_view_key)
        result["show_completed_items"] = from_union([from_bool, from_none], self.show_completed_items)
        result["grouping"] = from_union([lambda x: to_class(Grouping, x), from_none], self.grouping)
        return result


@dataclass
class Metadata:
    thumb_64: Optional[bool] = None
    thumb_80: Optional[bool] = None
    thumb_160: Optional[bool] = None
    original_w: Optional[int] = None
    original_h: Optional[int] = None
    thumb_360__w: Optional[int] = None
    thumb_360__h: Optional[int] = None
    format: Optional[str] = None
    extension: Optional[str] = None
    rotation: Optional[int] = None
    thumb_tiny: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Metadata':
        assert isinstance(obj, dict)
        thumb_64 = from_union([from_bool, from_none], obj.get("thumb_64"))
        thumb_80 = from_union([from_bool, from_none], obj.get("thumb_80"))
        thumb_160 = from_union([from_bool, from_none], obj.get("thumb_160"))
        original_w = from_union([from_int, from_none], obj.get("original_w"))
        original_h = from_union([from_int, from_none], obj.get("original_h"))
        thumb_360__w = from_union([from_int, from_none], obj.get("thumb_360_w"))
        thumb_360__h = from_union([from_int, from_none], obj.get("thumb_360_h"))
        format = from_union([from_str, from_none], obj.get("format"))
        extension = from_union([from_str, from_none], obj.get("extension"))
        rotation = from_union([from_int, from_none], obj.get("rotation"))
        thumb_tiny = from_union([from_str, from_none], obj.get("thumb_tiny"))
        return Metadata(thumb_64, thumb_80, thumb_160, original_w, original_h, thumb_360__w, thumb_360__h, format, extension, rotation, thumb_tiny)

    def to_dict(self) -> dict:
        result: dict = {}
        result["thumb_64"] = from_union([from_bool, from_none], self.thumb_64)
        result["thumb_80"] = from_union([from_bool, from_none], self.thumb_80)
        result["thumb_160"] = from_union([from_bool, from_none], self.thumb_160)
        result["original_w"] = from_union([from_int, from_none], self.original_w)
        result["original_h"] = from_union([from_int, from_none], self.original_h)
        result["thumb_360_w"] = from_union([from_int, from_none], self.thumb_360__w)
        result["thumb_360_h"] = from_union([from_int, from_none], self.thumb_360__h)
        result["format"] = from_union([from_str, from_none], self.format)
        result["extension"] = from_union([from_str, from_none], self.extension)
        result["rotation"] = from_union([from_int, from_none], self.rotation)
        result["thumb_tiny"] = from_union([from_str, from_none], self.thumb_tiny)
        return result


class TypeEnum(Enum):
    MRKDWN = "mrkdwn"
    PLAIN_TEXT = "plain_text"


@dataclass
class Text:
    type: Optional[TypeEnum] = None
    text: Optional[str] = None
    emoji: Optional[bool] = None
    verbatim: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Text':
        assert isinstance(obj, dict)
        type = from_union([TypeEnum, from_none], obj.get("type"))
        text = from_union([from_str, from_none], obj.get("text"))
        emoji = from_union([from_bool, from_none], obj.get("emoji"))
        verbatim = from_union([from_bool, from_none], obj.get("verbatim"))
        return Text(type, text, emoji, verbatim)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: to_enum(TypeEnum, x), from_none], self.type)
        result["text"] = from_union([from_str, from_none], self.text)
        result["emoji"] = from_union([from_bool, from_none], self.emoji)
        result["verbatim"] = from_union([from_bool, from_none], self.verbatim)
        return result


@dataclass
class Preview:
    type: Optional[str] = None
    can_remove: Optional[bool] = None
    title: Optional[Text] = None
    subtitle: Optional[Text] = None
    icon_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Preview':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        can_remove = from_union([from_bool, from_none], obj.get("can_remove"))
        title = from_union([Text.from_dict, from_none], obj.get("title"))
        subtitle = from_union([Text.from_dict, from_none], obj.get("subtitle"))
        icon_url = from_union([from_str, from_none], obj.get("icon_url"))
        return Preview(type, can_remove, title, subtitle, icon_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["can_remove"] = from_union([from_bool, from_none], self.can_remove)
        result["title"] = from_union([lambda x: to_class(Text, x), from_none], self.title)
        result["subtitle"] = from_union([lambda x: to_class(Text, x), from_none], self.subtitle)
        result["icon_url"] = from_union([from_str, from_none], self.icon_url)
        return result


@dataclass
class Attachment:
    msg_subtype: Optional[str] = None
    fallback: Optional[str] = None
    callback_id: Optional[str] = None
    color: Optional[str] = None
    hide_color: Optional[bool] = None
    pretext: Optional[str] = None
    service_url: Optional[str] = None
    service_name: Optional[str] = None
    service_icon: Optional[str] = None
    author_id: Optional[str] = None
    author_name: Optional[str] = None
    author_link: Optional[str] = None
    author_icon: Optional[str] = None
    from_url: Optional[str] = None
    original_url: Optional[str] = None
    author_subname: Optional[str] = None
    channel_id: Optional[str] = None
    channel_name: Optional[str] = None
    channel_team: Optional[str] = None
    id: Optional[int] = None
    app_id: Optional[str] = None
    bot_id: Optional[str] = None
    indent: Optional[bool] = None
    is_msg_unfurl: Optional[bool] = None
    is_reply_unfurl: Optional[bool] = None
    is_thread_root_unfurl: Optional[bool] = None
    is_app_unfurl: Optional[bool] = None
    app_unfurl_url: Optional[str] = None
    title: Optional[str] = None
    title_link: Optional[str] = None
    text: Optional[str] = None
    fields: Optional[List[Field]] = None
    image_url: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    thumb_url: Optional[str] = None
    thumb_width: Optional[int] = None
    thumb_height: Optional[int] = None
    video_url: Optional[str] = None
    video_html: Optional[str] = None
    video_html_width: Optional[float] = None
    video_html_height: Optional[float] = None
    footer: Optional[str] = None
    footer_icon: Optional[str] = None
    ts: Optional[str] = None
    mrkdwn_in: Optional[List[str]] = None
    actions: Optional[List[Action]] = None
    preview: Optional[Preview] = None
    file_id: Optional[str] = None
    list_record_id: Optional[str] = None
    list_record: Optional[ListRecord] = None
    hide_border: Optional[bool] = None
    list_view_id: Optional[str] = None
    list: Optional[ListClass] = None
    list_view: Optional[ListView] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    mimetype: Optional[str] = None
    url: Optional[str] = None
    metadata: Optional[Metadata] = None
    is_file_attachment: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Attachment':
        assert isinstance(obj, dict)
        msg_subtype = from_union([from_str, from_none], obj.get("msg_subtype"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        callback_id = from_union([from_str, from_none], obj.get("callback_id"))
        color = from_union([from_str, from_none], obj.get("color"))
        hide_color = from_union([from_bool, from_none], obj.get("hide_color"))
        pretext = from_union([from_str, from_none], obj.get("pretext"))
        service_url = from_union([from_str, from_none], obj.get("service_url"))
        service_name = from_union([from_str, from_none], obj.get("service_name"))
        service_icon = from_union([from_str, from_none], obj.get("service_icon"))
        author_id = from_union([from_str, from_none], obj.get("author_id"))
        author_name = from_union([from_str, from_none], obj.get("author_name"))
        author_link = from_union([from_str, from_none], obj.get("author_link"))
        author_icon = from_union([from_str, from_none], obj.get("author_icon"))
        from_url = from_union([from_str, from_none], obj.get("from_url"))
        original_url = from_union([from_str, from_none], obj.get("original_url"))
        author_subname = from_union([from_str, from_none], obj.get("author_subname"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        channel_name = from_union([from_str, from_none], obj.get("channel_name"))
        channel_team = from_union([from_str, from_none], obj.get("channel_team"))
        id = from_union([from_int, from_none], obj.get("id"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        indent = from_union([from_bool, from_none], obj.get("indent"))
        is_msg_unfurl = from_union([from_bool, from_none], obj.get("is_msg_unfurl"))
        is_reply_unfurl = from_union([from_bool, from_none], obj.get("is_reply_unfurl"))
        is_thread_root_unfurl = from_union([from_bool, from_none], obj.get("is_thread_root_unfurl"))
        is_app_unfurl = from_union([from_bool, from_none], obj.get("is_app_unfurl"))
        app_unfurl_url = from_union([from_str, from_none], obj.get("app_unfurl_url"))
        title = from_union([from_str, from_none], obj.get("title"))
        title_link = from_union([from_str, from_none], obj.get("title_link"))
        text = from_union([from_str, from_none], obj.get("text"))
        fields = from_union([lambda x: from_list(Field.from_dict, x), from_none], obj.get("fields"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        thumb_url = from_union([from_str, from_none], obj.get("thumb_url"))
        thumb_width = from_union([from_int, from_none], obj.get("thumb_width"))
        thumb_height = from_union([from_int, from_none], obj.get("thumb_height"))
        video_url = from_union([from_str, from_none], obj.get("video_url"))
        video_html = from_union([from_str, from_none], obj.get("video_html"))
        video_html_width = from_union([from_float, from_none], obj.get("video_html_width"))
        video_html_height = from_union([from_float, from_none], obj.get("video_html_height"))
        footer = from_union([from_str, from_none], obj.get("footer"))
        footer_icon = from_union([from_str, from_none], obj.get("footer_icon"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        mrkdwn_in = from_union([lambda x: from_list(from_str, x), from_none], obj.get("mrkdwn_in"))
        actions = from_union([lambda x: from_list(Action.from_dict, x), from_none], obj.get("actions"))
        preview = from_union([Preview.from_dict, from_none], obj.get("preview"))
        file_id = from_union([from_str, from_none], obj.get("file_id"))
        list_record_id = from_union([from_str, from_none], obj.get("list_record_id"))
        list_record = from_union([ListRecord.from_dict, from_none], obj.get("list_record"))
        hide_border = from_union([from_bool, from_none], obj.get("hide_border"))
        list_view_id = from_union([from_str, from_none], obj.get("list_view_id"))
        list = from_union([ListClass.from_dict, from_none], obj.get("list"))
        list_view = from_union([ListView.from_dict, from_none], obj.get("list_view"))
        filename = from_union([from_str, from_none], obj.get("filename"))
        size = from_union([from_int, from_none], obj.get("size"))
        mimetype = from_union([from_str, from_none], obj.get("mimetype"))
        url = from_union([from_str, from_none], obj.get("url"))
        metadata = from_union([Metadata.from_dict, from_none], obj.get("metadata"))
        is_file_attachment = from_union([from_bool, from_none], obj.get("is_file_attachment"))
        return Attachment(msg_subtype, fallback, callback_id, color, hide_color, pretext, service_url, service_name, service_icon, author_id, author_name, author_link, author_icon, from_url, original_url, author_subname, channel_id, channel_name, channel_team, id, app_id, bot_id, indent, is_msg_unfurl, is_reply_unfurl, is_thread_root_unfurl, is_app_unfurl, app_unfurl_url, title, title_link, text, fields, image_url, image_width, image_height, image_bytes, thumb_url, thumb_width, thumb_height, video_url, video_html, video_html_width, video_html_height, footer, footer_icon, ts, mrkdwn_in, actions, preview, file_id, list_record_id, list_record, hide_border, list_view_id, list, list_view, filename, size, mimetype, url, metadata, is_file_attachment)

    def to_dict(self) -> dict:
        result: dict = {}
        result["msg_subtype"] = from_union([from_str, from_none], self.msg_subtype)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["callback_id"] = from_union([from_str, from_none], self.callback_id)
        result["color"] = from_union([from_str, from_none], self.color)
        result["hide_color"] = from_union([from_bool, from_none], self.hide_color)
        result["pretext"] = from_union([from_str, from_none], self.pretext)
        result["service_url"] = from_union([from_str, from_none], self.service_url)
        result["service_name"] = from_union([from_str, from_none], self.service_name)
        result["service_icon"] = from_union([from_str, from_none], self.service_icon)
        result["author_id"] = from_union([from_str, from_none], self.author_id)
        result["author_name"] = from_union([from_str, from_none], self.author_name)
        result["author_link"] = from_union([from_str, from_none], self.author_link)
        result["author_icon"] = from_union([from_str, from_none], self.author_icon)
        result["from_url"] = from_union([from_str, from_none], self.from_url)
        result["original_url"] = from_union([from_str, from_none], self.original_url)
        result["author_subname"] = from_union([from_str, from_none], self.author_subname)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["channel_name"] = from_union([from_str, from_none], self.channel_name)
        result["channel_team"] = from_union([from_str, from_none], self.channel_team)
        result["id"] = from_union([from_int, from_none], self.id)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["indent"] = from_union([from_bool, from_none], self.indent)
        result["is_msg_unfurl"] = from_union([from_bool, from_none], self.is_msg_unfurl)
        result["is_reply_unfurl"] = from_union([from_bool, from_none], self.is_reply_unfurl)
        result["is_thread_root_unfurl"] = from_union([from_bool, from_none], self.is_thread_root_unfurl)
        result["is_app_unfurl"] = from_union([from_bool, from_none], self.is_app_unfurl)
        result["app_unfurl_url"] = from_union([from_str, from_none], self.app_unfurl_url)
        result["title"] = from_union([from_str, from_none], self.title)
        result["title_link"] = from_union([from_str, from_none], self.title_link)
        result["text"] = from_union([from_str, from_none], self.text)
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(Field, x), x), from_none], self.fields)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["thumb_url"] = from_union([from_str, from_none], self.thumb_url)
        result["thumb_width"] = from_union([from_int, from_none], self.thumb_width)
        result["thumb_height"] = from_union([from_int, from_none], self.thumb_height)
        result["video_url"] = from_union([from_str, from_none], self.video_url)
        result["video_html"] = from_union([from_str, from_none], self.video_html)
        result["video_html_width"] = from_union([to_float, from_none], self.video_html_width)
        result["video_html_height"] = from_union([to_float, from_none], self.video_html_height)
        result["footer"] = from_union([from_str, from_none], self.footer)
        result["footer_icon"] = from_union([from_str, from_none], self.footer_icon)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["mrkdwn_in"] = from_union([lambda x: from_list(from_str, x), from_none], self.mrkdwn_in)
        result["actions"] = from_union([lambda x: from_list(lambda x: to_class(Action, x), x), from_none], self.actions)
        result["preview"] = from_union([lambda x: to_class(Preview, x), from_none], self.preview)
        result["file_id"] = from_union([from_str, from_none], self.file_id)
        result["list_record_id"] = from_union([from_str, from_none], self.list_record_id)
        result["list_record"] = from_union([lambda x: to_class(ListRecord, x), from_none], self.list_record)
        result["hide_border"] = from_union([from_bool, from_none], self.hide_border)
        result["list_view_id"] = from_union([from_str, from_none], self.list_view_id)
        result["list"] = from_union([lambda x: to_class(ListClass, x), from_none], self.list)
        result["list_view"] = from_union([lambda x: to_class(ListView, x), from_none], self.list_view)
        result["filename"] = from_union([from_str, from_none], self.filename)
        result["size"] = from_union([from_int, from_none], self.size)
        result["mimetype"] = from_union([from_str, from_none], self.mimetype)
        result["url"] = from_union([from_str, from_none], self.url)
        result["metadata"] = from_union([lambda x: to_class(Metadata, x), from_none], self.metadata)
        result["is_file_attachment"] = from_union([from_bool, from_none], self.is_file_attachment)
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


@dataclass
class ElementConfirm:
    title: Optional[Text] = None
    text: Optional[Text] = None
    confirm: Optional[Text] = None
    deny: Optional[Text] = None
    style: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ElementConfirm':
        assert isinstance(obj, dict)
        title = from_union([Text.from_dict, from_none], obj.get("title"))
        text = from_union([Text.from_dict, from_none], obj.get("text"))
        confirm = from_union([Text.from_dict, from_none], obj.get("confirm"))
        deny = from_union([Text.from_dict, from_none], obj.get("deny"))
        style = from_union([from_str, from_none], obj.get("style"))
        return ElementConfirm(title, text, confirm, deny, style)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([lambda x: to_class(Text, x), from_none], self.title)
        result["text"] = from_union([lambda x: to_class(Text, x), from_none], self.text)
        result["confirm"] = from_union([lambda x: to_class(Text, x), from_none], self.confirm)
        result["deny"] = from_union([lambda x: to_class(Text, x), from_none], self.deny)
        result["style"] = from_union([from_str, from_none], self.style)
        return result


@dataclass
class Filter:
    include: Optional[List[str]] = None
    exclude_external_shared_channels: Optional[bool] = None
    exclude_bot_users: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Filter':
        assert isinstance(obj, dict)
        include = from_union([lambda x: from_list(from_str, x), from_none], obj.get("include"))
        exclude_external_shared_channels = from_union([from_bool, from_none], obj.get("exclude_external_shared_channels"))
        exclude_bot_users = from_union([from_bool, from_none], obj.get("exclude_bot_users"))
        return Filter(include, exclude_external_shared_channels, exclude_bot_users)

    def to_dict(self) -> dict:
        result: dict = {}
        result["include"] = from_union([lambda x: from_list(from_str, x), from_none], self.include)
        result["exclude_external_shared_channels"] = from_union([from_bool, from_none], self.exclude_external_shared_channels)
        result["exclude_bot_users"] = from_union([from_bool, from_none], self.exclude_bot_users)
        return result


@dataclass
class InitialOption:
    text: Optional[Text] = None
    value: Optional[str] = None
    description: Optional[Text] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InitialOption':
        assert isinstance(obj, dict)
        text = from_union([Text.from_dict, from_none], obj.get("text"))
        value = from_union([from_str, from_none], obj.get("value"))
        description = from_union([Text.from_dict, from_none], obj.get("description"))
        url = from_union([from_str, from_none], obj.get("url"))
        return InitialOption(text, value, description, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([lambda x: to_class(Text, x), from_none], self.text)
        result["value"] = from_union([from_str, from_none], self.value)
        result["description"] = from_union([lambda x: to_class(Text, x), from_none], self.description)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class Element:
    type: Optional[str] = None
    text: Optional[Text] = None
    action_id: Optional[str] = None
    url: Optional[str] = None
    value: Optional[str] = None
    style: Optional[str] = None
    confirm: Optional[ElementConfirm] = None
    accessibility_label: Optional[str] = None
    placeholder: Optional[Text] = None
    initial_channel: Optional[str] = None
    response_url_enabled: Optional[bool] = None
    focus_on_load: Optional[bool] = None
    max_selected_items: Optional[int] = None
    initial_conversation: Optional[str] = None
    default_to_current_conversation: Optional[bool] = None
    filter: Optional[Filter] = None
    initial_date: Optional[str] = None
    initial_option: Optional[InitialOption] = None
    min_query_length: Optional[int] = None
    image_url: Optional[str] = None
    alt_text: Optional[str] = None
    fallback: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    slack_file: Optional[SlackFile] = None
    initial_user: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Element':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        text = from_union([Text.from_dict, from_none], obj.get("text"))
        action_id = from_union([from_str, from_none], obj.get("action_id"))
        url = from_union([from_str, from_none], obj.get("url"))
        value = from_union([from_str, from_none], obj.get("value"))
        style = from_union([from_str, from_none], obj.get("style"))
        confirm = from_union([ElementConfirm.from_dict, from_none], obj.get("confirm"))
        accessibility_label = from_union([from_str, from_none], obj.get("accessibility_label"))
        placeholder = from_union([Text.from_dict, from_none], obj.get("placeholder"))
        initial_channel = from_union([from_str, from_none], obj.get("initial_channel"))
        response_url_enabled = from_union([from_bool, from_none], obj.get("response_url_enabled"))
        focus_on_load = from_union([from_bool, from_none], obj.get("focus_on_load"))
        max_selected_items = from_union([from_int, from_none], obj.get("max_selected_items"))
        initial_conversation = from_union([from_str, from_none], obj.get("initial_conversation"))
        default_to_current_conversation = from_union([from_bool, from_none], obj.get("default_to_current_conversation"))
        filter = from_union([Filter.from_dict, from_none], obj.get("filter"))
        initial_date = from_union([from_str, from_none], obj.get("initial_date"))
        initial_option = from_union([InitialOption.from_dict, from_none], obj.get("initial_option"))
        min_query_length = from_union([from_int, from_none], obj.get("min_query_length"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        slack_file = from_union([SlackFile.from_dict, from_none], obj.get("slack_file"))
        initial_user = from_union([from_str, from_none], obj.get("initial_user"))
        return Element(type, text, action_id, url, value, style, confirm, accessibility_label, placeholder, initial_channel, response_url_enabled, focus_on_load, max_selected_items, initial_conversation, default_to_current_conversation, filter, initial_date, initial_option, min_query_length, image_url, alt_text, fallback, image_width, image_height, image_bytes, slack_file, initial_user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["text"] = from_union([lambda x: to_class(Text, x), from_none], self.text)
        result["action_id"] = from_union([from_str, from_none], self.action_id)
        result["url"] = from_union([from_str, from_none], self.url)
        result["value"] = from_union([from_str, from_none], self.value)
        result["style"] = from_union([from_str, from_none], self.style)
        result["confirm"] = from_union([lambda x: to_class(ElementConfirm, x), from_none], self.confirm)
        result["accessibility_label"] = from_union([from_str, from_none], self.accessibility_label)
        result["placeholder"] = from_union([lambda x: to_class(Text, x), from_none], self.placeholder)
        result["initial_channel"] = from_union([from_str, from_none], self.initial_channel)
        result["response_url_enabled"] = from_union([from_bool, from_none], self.response_url_enabled)
        result["focus_on_load"] = from_union([from_bool, from_none], self.focus_on_load)
        result["max_selected_items"] = from_union([from_int, from_none], self.max_selected_items)
        result["initial_conversation"] = from_union([from_str, from_none], self.initial_conversation)
        result["default_to_current_conversation"] = from_union([from_bool, from_none], self.default_to_current_conversation)
        result["filter"] = from_union([lambda x: to_class(Filter, x), from_none], self.filter)
        result["initial_date"] = from_union([from_str, from_none], self.initial_date)
        result["initial_option"] = from_union([lambda x: to_class(InitialOption, x), from_none], self.initial_option)
        result["min_query_length"] = from_union([from_int, from_none], self.min_query_length)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["slack_file"] = from_union([lambda x: to_class(SlackFile, x), from_none], self.slack_file)
        result["initial_user"] = from_union([from_str, from_none], self.initial_user)
        return result


@dataclass
class Block:
    type: Optional[str] = None
    elements: Optional[List[Element]] = None
    block_id: Optional[str] = None
    fallback: Optional[str] = None
    image_url: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    is_animated: Optional[bool] = None
    slack_file: Optional[SlackFile] = None
    alt_text: Optional[str] = None
    title: Optional[Text] = None
    text: Optional[Text] = None
    fields: Optional[List[Text]] = None
    accessory: Optional[Accessory] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Block':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        elements = from_union([lambda x: from_list(Element.from_dict, x), from_none], obj.get("elements"))
        block_id = from_union([from_str, from_none], obj.get("block_id"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        is_animated = from_union([from_bool, from_none], obj.get("is_animated"))
        slack_file = from_union([SlackFile.from_dict, from_none], obj.get("slack_file"))
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        title = from_union([Text.from_dict, from_none], obj.get("title"))
        text = from_union([Text.from_dict, from_none], obj.get("text"))
        fields = from_union([lambda x: from_list(Text.from_dict, x), from_none], obj.get("fields"))
        accessory = from_union([Accessory.from_dict, from_none], obj.get("accessory"))
        return Block(type, elements, block_id, fallback, image_url, image_width, image_height, image_bytes, is_animated, slack_file, alt_text, title, text, fields, accessory)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(Element, x), x), from_none], self.elements)
        result["block_id"] = from_union([from_str, from_none], self.block_id)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["is_animated"] = from_union([from_bool, from_none], self.is_animated)
        result["slack_file"] = from_union([lambda x: to_class(SlackFile, x), from_none], self.slack_file)
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["title"] = from_union([lambda x: to_class(Text, x), from_none], self.title)
        result["text"] = from_union([lambda x: to_class(Text, x), from_none], self.text)
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(Text, x), x), from_none], self.fields)
        result["accessory"] = from_union([lambda x: to_class(Accessory, x), from_none], self.accessory)
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
class Edited:
    user: Optional[str] = None
    ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Edited':
        assert isinstance(obj, dict)
        user = from_union([from_str, from_none], obj.get("user"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        return Edited(user, ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user"] = from_union([from_str, from_none], self.user)
        result["ts"] = from_union([from_str, from_none], self.ts)
        return result


@dataclass
class Message:
    client_msg_id: Optional[str] = None
    type: Optional[str] = None
    subtype: Optional[str] = None
    user: Optional[str] = None
    team: Optional[str] = None
    bot_id: Optional[str] = None
    bot_profile: Optional[BotProfile] = None
    edited: Optional[Edited] = None
    text: Optional[str] = None
    blocks: Optional[List[Block]] = None
    attachments: Optional[List[Attachment]] = None
    upload: Optional[bool] = None
    display_as_bot: Optional[bool] = None
    thread_ts: Optional[str] = None
    parent_user_id: Optional[str] = None
    hidden: Optional[bool] = None
    is_locked: Optional[bool] = None
    subscribed: Optional[bool] = None
    ts: Optional[str] = None
    user_team: Optional[str] = None
    source_team: Optional[str] = None
    is_starred: Optional[bool] = None
    reply_count: Optional[int] = None
    reply_users_count: Optional[int] = None
    latest_reply: Optional[str] = None
    last_read: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Message':
        assert isinstance(obj, dict)
        client_msg_id = from_union([from_str, from_none], obj.get("client_msg_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        subtype = from_union([from_str, from_none], obj.get("subtype"))
        user = from_union([from_str, from_none], obj.get("user"))
        team = from_union([from_str, from_none], obj.get("team"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        bot_profile = from_union([BotProfile.from_dict, from_none], obj.get("bot_profile"))
        edited = from_union([Edited.from_dict, from_none], obj.get("edited"))
        text = from_union([from_str, from_none], obj.get("text"))
        blocks = from_union([lambda x: from_list(Block.from_dict, x), from_none], obj.get("blocks"))
        attachments = from_union([lambda x: from_list(Attachment.from_dict, x), from_none], obj.get("attachments"))
        upload = from_union([from_bool, from_none], obj.get("upload"))
        display_as_bot = from_union([from_bool, from_none], obj.get("display_as_bot"))
        thread_ts = from_union([from_str, from_none], obj.get("thread_ts"))
        parent_user_id = from_union([from_str, from_none], obj.get("parent_user_id"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        is_locked = from_union([from_bool, from_none], obj.get("is_locked"))
        subscribed = from_union([from_bool, from_none], obj.get("subscribed"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        user_team = from_union([from_str, from_none], obj.get("user_team"))
        source_team = from_union([from_str, from_none], obj.get("source_team"))
        is_starred = from_union([from_bool, from_none], obj.get("is_starred"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        reply_users_count = from_union([from_int, from_none], obj.get("reply_users_count"))
        latest_reply = from_union([from_str, from_none], obj.get("latest_reply"))
        last_read = from_union([from_str, from_none], obj.get("last_read"))
        return Message(client_msg_id, type, subtype, user, team, bot_id, bot_profile, edited, text, blocks, attachments, upload, display_as_bot, thread_ts, parent_user_id, hidden, is_locked, subscribed, ts, user_team, source_team, is_starred, reply_count, reply_users_count, latest_reply, last_read)

    def to_dict(self) -> dict:
        result: dict = {}
        result["client_msg_id"] = from_union([from_str, from_none], self.client_msg_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["subtype"] = from_union([from_str, from_none], self.subtype)
        result["user"] = from_union([from_str, from_none], self.user)
        result["team"] = from_union([from_str, from_none], self.team)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["bot_profile"] = from_union([lambda x: to_class(BotProfile, x), from_none], self.bot_profile)
        result["edited"] = from_union([lambda x: to_class(Edited, x), from_none], self.edited)
        result["text"] = from_union([from_str, from_none], self.text)
        result["blocks"] = from_union([lambda x: from_list(lambda x: to_class(Block, x), x), from_none], self.blocks)
        result["attachments"] = from_union([lambda x: from_list(lambda x: to_class(Attachment, x), x), from_none], self.attachments)
        result["upload"] = from_union([from_bool, from_none], self.upload)
        result["display_as_bot"] = from_union([from_bool, from_none], self.display_as_bot)
        result["thread_ts"] = from_union([from_str, from_none], self.thread_ts)
        result["parent_user_id"] = from_union([from_str, from_none], self.parent_user_id)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["is_locked"] = from_union([from_bool, from_none], self.is_locked)
        result["subscribed"] = from_union([from_bool, from_none], self.subscribed)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["user_team"] = from_union([from_str, from_none], self.user_team)
        result["source_team"] = from_union([from_str, from_none], self.source_team)
        result["is_starred"] = from_union([from_bool, from_none], self.is_starred)
        result["reply_count"] = from_union([from_int, from_none], self.reply_count)
        result["reply_users_count"] = from_union([from_int, from_none], self.reply_users_count)
        result["latest_reply"] = from_union([from_str, from_none], self.latest_reply)
        result["last_read"] = from_union([from_str, from_none], self.last_read)
        return result


@dataclass
class Event:
    type: Optional[str] = None
    subtype: Optional[str] = None
    channel: Optional[str] = None
    hidden: Optional[bool] = None
    message: Optional[Message] = None
    previous_message: Optional[Message] = None
    event_ts: Optional[str] = None
    ts: Optional[str] = None
    channel_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Event':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        subtype = from_union([from_str, from_none], obj.get("subtype"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        message = from_union([Message.from_dict, from_none], obj.get("message"))
        previous_message = from_union([Message.from_dict, from_none], obj.get("previous_message"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        channel_type = from_union([from_str, from_none], obj.get("channel_type"))
        return Event(type, subtype, channel, hidden, message, previous_message, event_ts, ts, channel_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["subtype"] = from_union([from_str, from_none], self.subtype)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["message"] = from_union([lambda x: to_class(Message, x), from_none], self.message)
        result["previous_message"] = from_union([lambda x: to_class(Message, x), from_none], self.previous_message)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["channel_type"] = from_union([from_str, from_none], self.channel_type)
        return result


@dataclass
class MessageChangedPayload:
    token: Optional[str] = None
    enterprise_id: Optional[str] = None
    team_id: Optional[str] = None
    api_app_id: Optional[str] = None
    type: Optional[str] = None
    authed_users: Optional[List[str]] = None
    authed_teams: Optional[List[str]] = None
    authorizations: Optional[List[Authorization]] = None
    is_ext_shared_channel: Optional[bool] = None
    event_id: Optional[str] = None
    event_time: Optional[int] = None
    event_context: Optional[str] = None
    event: Optional[Event] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MessageChangedPayload':
        assert isinstance(obj, dict)
        token = from_union([from_str, from_none], obj.get("token"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        api_app_id = from_union([from_str, from_none], obj.get("api_app_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        authed_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("authed_users"))
        authed_teams = from_union([lambda x: from_list(from_str, x), from_none], obj.get("authed_teams"))
        authorizations = from_union([lambda x: from_list(Authorization.from_dict, x), from_none], obj.get("authorizations"))
        is_ext_shared_channel = from_union([from_bool, from_none], obj.get("is_ext_shared_channel"))
        event_id = from_union([from_str, from_none], obj.get("event_id"))
        event_time = from_union([from_int, from_none], obj.get("event_time"))
        event_context = from_union([from_str, from_none], obj.get("event_context"))
        event = from_union([Event.from_dict, from_none], obj.get("event"))
        return MessageChangedPayload(token, enterprise_id, team_id, api_app_id, type, authed_users, authed_teams, authorizations, is_ext_shared_channel, event_id, event_time, event_context, event)

    def to_dict(self) -> dict:
        result: dict = {}
        result["token"] = from_union([from_str, from_none], self.token)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["api_app_id"] = from_union([from_str, from_none], self.api_app_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["authed_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.authed_users)
        result["authed_teams"] = from_union([lambda x: from_list(from_str, x), from_none], self.authed_teams)
        result["authorizations"] = from_union([lambda x: from_list(lambda x: to_class(Authorization, x), x), from_none], self.authorizations)
        result["is_ext_shared_channel"] = from_union([from_bool, from_none], self.is_ext_shared_channel)
        result["event_id"] = from_union([from_str, from_none], self.event_id)
        result["event_time"] = from_union([from_int, from_none], self.event_time)
        result["event_context"] = from_union([from_str, from_none], self.event_context)
        result["event"] = from_union([lambda x: to_class(Event, x), from_none], self.event)
        return result


def message_changed_payload_from_dict(s: Any) -> MessageChangedPayload:
    return MessageChangedPayload.from_dict(s)


def message_changed_payload_to_dict(x: MessageChangedPayload) -> Any:
    return to_class(MessageChangedPayload, x)

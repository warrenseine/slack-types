# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = slack_lists_items_info_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


@dataclass
class ListLimits:
    over_row_maximum: Optional[bool] = None
    row_count_limit: Optional[int] = None
    row_count: Optional[int] = None
    archived_row_count: Optional[int] = None
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
        archived_row_count = from_union([from_int, from_none], obj.get("archived_row_count"))
        over_column_maximum = from_union([from_bool, from_none], obj.get("over_column_maximum"))
        column_count = from_union([from_int, from_none], obj.get("column_count"))
        column_count_limit = from_union([from_int, from_none], obj.get("column_count_limit"))
        over_view_maximum = from_union([from_bool, from_none], obj.get("over_view_maximum"))
        view_count = from_union([from_int, from_none], obj.get("view_count"))
        view_count_limit = from_union([from_int, from_none], obj.get("view_count_limit"))
        max_attachments_per_cell = from_union([from_int, from_none], obj.get("max_attachments_per_cell"))
        return ListLimits(over_row_maximum, row_count_limit, row_count, archived_row_count, over_column_maximum, column_count, column_count_limit, over_view_maximum, view_count, view_count_limit, max_attachments_per_cell)

    def to_dict(self) -> dict:
        result: dict = {}
        result["over_row_maximum"] = from_union([from_bool, from_none], self.over_row_maximum)
        result["row_count_limit"] = from_union([from_int, from_none], self.row_count_limit)
        result["row_count"] = from_union([from_int, from_none], self.row_count)
        result["archived_row_count"] = from_union([from_int, from_none], self.archived_row_count)
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

    @staticmethod
    def from_dict(obj: Any) -> 'CreationSource':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        reference_id = from_union([from_str, from_none], obj.get("reference_id"))
        return CreationSource(type, reference_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["reference_id"] = from_union([from_str, from_none], self.reference_id)
        return result


@dataclass
class ElementElementClass:
    type: Optional[str] = None
    text: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ElementElementClass':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        text = from_union([from_str, from_none], obj.get("text"))
        return ElementElementClass(type, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["text"] = from_union([from_str, from_none], self.text)
        return result


@dataclass
class DescriptionBlockElement:
    type: Optional[str] = None
    elements: Optional[List[ElementElementClass]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DescriptionBlockElement':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        elements = from_union([lambda x: from_list(ElementElementClass.from_dict, x), from_none], obj.get("elements"))
        return DescriptionBlockElement(type, elements)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(ElementElementClass, x), x), from_none], self.elements)
        return result


@dataclass
class DescriptionBlock:
    type: Optional[str] = None
    block_id: Optional[str] = None
    elements: Optional[List[DescriptionBlockElement]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DescriptionBlock':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        block_id = from_union([from_str, from_none], obj.get("block_id"))
        elements = from_union([lambda x: from_list(DescriptionBlockElement.from_dict, x), from_none], obj.get("elements"))
        return DescriptionBlock(type, block_id, elements)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["block_id"] = from_union([from_str, from_none], self.block_id)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(DescriptionBlockElement, x), x), from_none], self.elements)
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
class SchemaOptions:
    format: Optional[str] = None
    show_member_name: Optional[bool] = None
    choices: Optional[List[Choice]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SchemaOptions':
        assert isinstance(obj, dict)
        format = from_union([from_str, from_none], obj.get("format"))
        show_member_name = from_union([from_bool, from_none], obj.get("show_member_name"))
        choices = from_union([lambda x: from_list(Choice.from_dict, x), from_none], obj.get("choices"))
        return SchemaOptions(format, show_member_name, choices)

    def to_dict(self) -> dict:
        result: dict = {}
        result["format"] = from_union([from_str, from_none], self.format)
        result["show_member_name"] = from_union([from_bool, from_none], self.show_member_name)
        result["choices"] = from_union([lambda x: from_list(lambda x: to_class(Choice, x), x), from_none], self.choices)
        return result


@dataclass
class Schema:
    id: Optional[str] = None
    name: Optional[str] = None
    key: Optional[str] = None
    type: Optional[str] = None
    is_primary_column: Optional[bool] = None
    options: Optional[SchemaOptions] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Schema':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        key = from_union([from_str, from_none], obj.get("key"))
        type = from_union([from_str, from_none], obj.get("type"))
        is_primary_column = from_union([from_bool, from_none], obj.get("is_primary_column"))
        options = from_union([SchemaOptions.from_dict, from_none], obj.get("options"))
        return Schema(id, name, key, type, is_primary_column, options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["key"] = from_union([from_str, from_none], self.key)
        result["type"] = from_union([from_str, from_none], self.type)
        result["is_primary_column"] = from_union([from_bool, from_none], self.is_primary_column)
        result["options"] = from_union([lambda x: to_class(SchemaOptions, x), from_none], self.options)
        return result


@dataclass
class SubtaskSchemaOptions:
    format: Optional[str] = None
    show_member_name: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SubtaskSchemaOptions':
        assert isinstance(obj, dict)
        format = from_union([from_str, from_none], obj.get("format"))
        show_member_name = from_union([from_bool, from_none], obj.get("show_member_name"))
        return SubtaskSchemaOptions(format, show_member_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["format"] = from_union([from_str, from_none], self.format)
        result["show_member_name"] = from_union([from_bool, from_none], self.show_member_name)
        return result


@dataclass
class SubtaskSchema:
    id: Optional[str] = None
    name: Optional[str] = None
    key: Optional[str] = None
    type: Optional[str] = None
    is_primary_column: Optional[bool] = None
    options: Optional[SubtaskSchemaOptions] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SubtaskSchema':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        key = from_union([from_str, from_none], obj.get("key"))
        type = from_union([from_str, from_none], obj.get("type"))
        is_primary_column = from_union([from_bool, from_none], obj.get("is_primary_column"))
        options = from_union([SubtaskSchemaOptions.from_dict, from_none], obj.get("options"))
        return SubtaskSchema(id, name, key, type, is_primary_column, options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["key"] = from_union([from_str, from_none], self.key)
        result["type"] = from_union([from_str, from_none], self.type)
        result["is_primary_column"] = from_union([from_bool, from_none], self.is_primary_column)
        result["options"] = from_union([lambda x: to_class(SubtaskSchemaOptions, x), from_none], self.options)
        return result


@dataclass
class Column:
    position: Optional[int] = None
    visible: Optional[bool] = None
    key: Optional[str] = None
    id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Column':
        assert isinstance(obj, dict)
        position = from_union([from_none, lambda x: int(from_str(x))], obj.get("position"))
        visible = from_union([from_bool, from_none], obj.get("visible"))
        key = from_union([from_str, from_none], obj.get("key"))
        id = from_union([from_str, from_none], obj.get("id"))
        return Column(position, visible, key, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["position"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.position)
        result["visible"] = from_union([from_bool, from_none], self.visible)
        result["key"] = from_union([from_str, from_none], self.key)
        result["id"] = from_union([from_str, from_none], self.id)
        return result


@dataclass
class View:
    position: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    is_locked: Optional[bool] = None
    columns: Optional[List[Column]] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
    stick_column_left: Optional[bool] = None
    is_all_items_view: Optional[bool] = None
    default_view_key: Optional[str] = None
    show_completed_items: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'View':
        assert isinstance(obj, dict)
        position = from_union([from_none, lambda x: int(from_str(x))], obj.get("position"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([from_str, from_none], obj.get("type"))
        is_locked = from_union([from_bool, from_none], obj.get("is_locked"))
        columns = from_union([lambda x: from_list(Column.from_dict, x), from_none], obj.get("columns"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        stick_column_left = from_union([from_bool, from_none], obj.get("stick_column_left"))
        is_all_items_view = from_union([from_bool, from_none], obj.get("is_all_items_view"))
        default_view_key = from_union([from_str, from_none], obj.get("default_view_key"))
        show_completed_items = from_union([from_bool, from_none], obj.get("show_completed_items"))
        return View(position, id, name, type, is_locked, columns, date_created, created_by, stick_column_left, is_all_items_view, default_view_key, show_completed_items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["position"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.position)
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["type"] = from_union([from_str, from_none], self.type)
        result["is_locked"] = from_union([from_bool, from_none], self.is_locked)
        result["columns"] = from_union([lambda x: from_list(lambda x: to_class(Column, x), x), from_none], self.columns)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["created_by"] = from_union([from_str, from_none], self.created_by)
        result["stick_column_left"] = from_union([from_bool, from_none], self.stick_column_left)
        result["is_all_items_view"] = from_union([from_bool, from_none], self.is_all_items_view)
        result["default_view_key"] = from_union([from_str, from_none], self.default_view_key)
        result["show_completed_items"] = from_union([from_bool, from_none], self.show_completed_items)
        return result


@dataclass
class ListMetadata:
    schema: Optional[List[Schema]] = None
    views: Optional[List[View]] = None
    integrations: Optional[List[str]] = None
    icon: Optional[str] = None
    description: Optional[str] = None
    description_blocks: Optional[List[DescriptionBlock]] = None
    is_trial: Optional[bool] = None
    subtask_schema: Optional[List[SubtaskSchema]] = None
    creation_source: Optional[CreationSource] = None
    todo_mode: Optional[bool] = None
    default_view: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ListMetadata':
        assert isinstance(obj, dict)
        schema = from_union([lambda x: from_list(Schema.from_dict, x), from_none], obj.get("schema"))
        views = from_union([lambda x: from_list(View.from_dict, x), from_none], obj.get("views"))
        integrations = from_union([lambda x: from_list(from_str, x), from_none], obj.get("integrations"))
        icon = from_union([from_str, from_none], obj.get("icon"))
        description = from_union([from_str, from_none], obj.get("description"))
        description_blocks = from_union([lambda x: from_list(DescriptionBlock.from_dict, x), from_none], obj.get("description_blocks"))
        is_trial = from_union([from_bool, from_none], obj.get("is_trial"))
        subtask_schema = from_union([lambda x: from_list(SubtaskSchema.from_dict, x), from_none], obj.get("subtask_schema"))
        creation_source = from_union([CreationSource.from_dict, from_none], obj.get("creation_source"))
        todo_mode = from_union([from_bool, from_none], obj.get("todo_mode"))
        default_view = from_union([from_str, from_none], obj.get("default_view"))
        return ListMetadata(schema, views, integrations, icon, description, description_blocks, is_trial, subtask_schema, creation_source, todo_mode, default_view)

    def to_dict(self) -> dict:
        result: dict = {}
        result["schema"] = from_union([lambda x: from_list(lambda x: to_class(Schema, x), x), from_none], self.schema)
        result["views"] = from_union([lambda x: from_list(lambda x: to_class(View, x), x), from_none], self.views)
        result["integrations"] = from_union([lambda x: from_list(from_str, x), from_none], self.integrations)
        result["icon"] = from_union([from_str, from_none], self.icon)
        result["description"] = from_union([from_str, from_none], self.description)
        result["description_blocks"] = from_union([lambda x: from_list(lambda x: to_class(DescriptionBlock, x), x), from_none], self.description_blocks)
        result["is_trial"] = from_union([from_bool, from_none], self.is_trial)
        result["subtask_schema"] = from_union([lambda x: from_list(lambda x: to_class(SubtaskSchema, x), x), from_none], self.subtask_schema)
        result["creation_source"] = from_union([lambda x: to_class(CreationSource, x), from_none], self.creation_source)
        result["todo_mode"] = from_union([from_bool, from_none], self.todo_mode)
        result["default_view"] = from_union([from_str, from_none], self.default_view)
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
    pretty_type: Optional[str] = None
    user: Optional[str] = None
    user_team: Optional[str] = None
    editable: Optional[bool] = None
    size: Optional[int] = None
    mode: Optional[str] = None
    is_external: Optional[bool] = None
    external_type: Optional[str] = None
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
    list_csv_download_url: Optional[str] = None
    updated: Optional[int] = None
    is_starred: Optional[bool] = None
    skipped_shares: Optional[bool] = None
    teams_shared_with: Optional[List[str]] = None
    is_restricted_sharing_enabled: Optional[bool] = None
    has_rich_preview: Optional[bool] = None
    file_access: Optional[str] = None
    access: Optional[str] = None
    org_or_workspace_access: Optional[str] = None
    is_ai_suggested: Optional[bool] = None

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
        pretty_type = from_union([from_str, from_none], obj.get("pretty_type"))
        user = from_union([from_str, from_none], obj.get("user"))
        user_team = from_union([from_str, from_none], obj.get("user_team"))
        editable = from_union([from_bool, from_none], obj.get("editable"))
        size = from_union([from_int, from_none], obj.get("size"))
        mode = from_union([from_str, from_none], obj.get("mode"))
        is_external = from_union([from_bool, from_none], obj.get("is_external"))
        external_type = from_union([from_str, from_none], obj.get("external_type"))
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
        list_csv_download_url = from_union([from_str, from_none], obj.get("list_csv_download_url"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        is_starred = from_union([from_bool, from_none], obj.get("is_starred"))
        skipped_shares = from_union([from_bool, from_none], obj.get("skipped_shares"))
        teams_shared_with = from_union([lambda x: from_list(from_str, x), from_none], obj.get("teams_shared_with"))
        is_restricted_sharing_enabled = from_union([from_bool, from_none], obj.get("is_restricted_sharing_enabled"))
        has_rich_preview = from_union([from_bool, from_none], obj.get("has_rich_preview"))
        file_access = from_union([from_str, from_none], obj.get("file_access"))
        access = from_union([from_str, from_none], obj.get("access"))
        org_or_workspace_access = from_union([from_str, from_none], obj.get("org_or_workspace_access"))
        is_ai_suggested = from_union([from_bool, from_none], obj.get("is_ai_suggested"))
        return ListClass(id, created, timestamp, name, title, mimetype, filetype, pretty_type, user, user_team, editable, size, mode, is_external, external_type, is_public, public_url_shared, display_as_bot, username, list_metadata, list_limits, url_private, url_private_download, permalink, permalink_public, last_editor, list_csv_download_url, updated, is_starred, skipped_shares, teams_shared_with, is_restricted_sharing_enabled, has_rich_preview, file_access, access, org_or_workspace_access, is_ai_suggested)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["created"] = from_union([from_int, from_none], self.created)
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        result["name"] = from_union([from_str, from_none], self.name)
        result["title"] = from_union([from_str, from_none], self.title)
        result["mimetype"] = from_union([from_str, from_none], self.mimetype)
        result["filetype"] = from_union([from_str, from_none], self.filetype)
        result["pretty_type"] = from_union([from_str, from_none], self.pretty_type)
        result["user"] = from_union([from_str, from_none], self.user)
        result["user_team"] = from_union([from_str, from_none], self.user_team)
        result["editable"] = from_union([from_bool, from_none], self.editable)
        result["size"] = from_union([from_int, from_none], self.size)
        result["mode"] = from_union([from_str, from_none], self.mode)
        result["is_external"] = from_union([from_bool, from_none], self.is_external)
        result["external_type"] = from_union([from_str, from_none], self.external_type)
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
        result["list_csv_download_url"] = from_union([from_str, from_none], self.list_csv_download_url)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["is_starred"] = from_union([from_bool, from_none], self.is_starred)
        result["skipped_shares"] = from_union([from_bool, from_none], self.skipped_shares)
        result["teams_shared_with"] = from_union([lambda x: from_list(from_str, x), from_none], self.teams_shared_with)
        result["is_restricted_sharing_enabled"] = from_union([from_bool, from_none], self.is_restricted_sharing_enabled)
        result["has_rich_preview"] = from_union([from_bool, from_none], self.has_rich_preview)
        result["file_access"] = from_union([from_str, from_none], self.file_access)
        result["access"] = from_union([from_str, from_none], self.access)
        result["org_or_workspace_access"] = from_union([from_str, from_none], self.org_or_workspace_access)
        result["is_ai_suggested"] = from_union([from_bool, from_none], self.is_ai_suggested)
        return result


@dataclass
class Field:
    key: Optional[str] = None
    value: Optional[bool] = None
    checkbox: Optional[bool] = None
    column_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Field':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        value = from_union([from_bool, from_none], obj.get("value"))
        checkbox = from_union([from_bool, from_none], obj.get("checkbox"))
        column_id = from_union([from_str, from_none], obj.get("column_id"))
        return Field(key, value, checkbox, column_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["key"] = from_union([from_str, from_none], self.key)
        result["value"] = from_union([from_bool, from_none], self.value)
        result["checkbox"] = from_union([from_bool, from_none], self.checkbox)
        result["column_id"] = from_union([from_str, from_none], self.column_id)
        return result


@dataclass
class Record:
    id: Optional[str] = None
    list_id: Optional[str] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    fields: Optional[List[Field]] = None
    updated_timestamp: Optional[str] = None
    is_subscribed: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Record':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        list_id = from_union([from_str, from_none], obj.get("list_id"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        updated_by = from_union([from_str, from_none], obj.get("updated_by"))
        fields = from_union([lambda x: from_list(Field.from_dict, x), from_none], obj.get("fields"))
        updated_timestamp = from_union([from_str, from_none], obj.get("updated_timestamp"))
        is_subscribed = from_union([from_bool, from_none], obj.get("is_subscribed"))
        return Record(id, list_id, date_created, created_by, updated_by, fields, updated_timestamp, is_subscribed)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["list_id"] = from_union([from_str, from_none], self.list_id)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["created_by"] = from_union([from_str, from_none], self.created_by)
        result["updated_by"] = from_union([from_str, from_none], self.updated_by)
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(Field, x), x), from_none], self.fields)
        result["updated_timestamp"] = from_union([from_str, from_none], self.updated_timestamp)
        result["is_subscribed"] = from_union([from_bool, from_none], self.is_subscribed)
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
class SlackListsItemsInfoResponse:
    ok: Optional[bool] = None
    list: Optional[ListClass] = None
    record: Optional[Record] = None
    subtasks: Optional[List[Record]] = None
    response_metadata: Optional[ResponseMetadata] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SlackListsItemsInfoResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        list = from_union([ListClass.from_dict, from_none], obj.get("list"))
        record = from_union([Record.from_dict, from_none], obj.get("record"))
        subtasks = from_union([lambda x: from_list(Record.from_dict, x), from_none], obj.get("subtasks"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return SlackListsItemsInfoResponse(ok, list, record, subtasks, response_metadata, error, needed, provided, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["list"] = from_union([lambda x: to_class(ListClass, x), from_none], self.list)
        result["record"] = from_union([lambda x: to_class(Record, x), from_none], self.record)
        result["subtasks"] = from_union([lambda x: from_list(lambda x: to_class(Record, x), x), from_none], self.subtasks)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def slack_lists_items_info_response_from_dict(s: Any) -> SlackListsItemsInfoResponse:
    return SlackListsItemsInfoResponse.from_dict(s)


def slack_lists_items_info_response_to_dict(x: SlackListsItemsInfoResponse) -> Any:
    return to_class(SlackListsItemsInfoResponse, x)

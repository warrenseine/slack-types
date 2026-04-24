# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = pin_added_event_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, Union, Dict, TypeVar, Callable, Type, cast
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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


@dataclass
class InitialCommentClass:
    id: Optional[str] = None
    created: Optional[int] = None
    timestamp: Optional[int] = None
    user: Optional[str] = None
    comment: Optional[str] = None
    channel: Optional[str] = None
    is_intro: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InitialCommentClass':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        created = from_union([from_int, from_none], obj.get("created"))
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        user = from_union([from_str, from_none], obj.get("user"))
        comment = from_union([from_str, from_none], obj.get("comment"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        is_intro = from_union([from_bool, from_none], obj.get("is_intro"))
        return InitialCommentClass(id, created, timestamp, user, comment, channel, is_intro)

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
class MediaProgress:
    offset_ms: Optional[int] = None
    max_offset_ms: Optional[int] = None
    duration_ms: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MediaProgress':
        assert isinstance(obj, dict)
        offset_ms = from_union([from_int, from_none], obj.get("offset_ms"))
        max_offset_ms = from_union([from_int, from_none], obj.get("max_offset_ms"))
        duration_ms = from_union([from_int, from_none], obj.get("duration_ms"))
        return MediaProgress(offset_ms, max_offset_ms, duration_ms)

    def to_dict(self) -> dict:
        result: dict = {}
        result["offset_ms"] = from_union([from_int, from_none], self.offset_ms)
        result["max_offset_ms"] = from_union([from_int, from_none], self.max_offset_ms)
        result["duration_ms"] = from_union([from_int, from_none], self.duration_ms)
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
class PurpleShares:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleShares':
        assert isinstance(obj, dict)
        return PurpleShares()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class Transcription:
    status: Optional[str] = None
    locale: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Transcription':
        assert isinstance(obj, dict)
        status = from_union([from_str, from_none], obj.get("status"))
        locale = from_union([from_str, from_none], obj.get("locale"))
        return Transcription(status, locale)

    def to_dict(self) -> dict:
        result: dict = {}
        result["status"] = from_union([from_str, from_none], self.status)
        result["locale"] = from_union([from_str, from_none], self.locale)
        return result


@dataclass
class ItemFile:
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
    editors: Optional[List[Any]] = None
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
    channels: Optional[List[Any]] = None
    groups: Optional[List[Any]] = None
    ims: Optional[List[Any]] = None
    shares: Optional[PurpleShares] = None
    has_more_shares: Optional[bool] = None
    to: Optional[List[Any]] = None
    file_from: Optional[List[Any]] = None
    cc: Optional[List[Any]] = None
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
    title_blocks: Optional[List[Any]] = None
    private_channels_with_file_access_count: Optional[int] = None
    dm_mpdm_users_with_file_access: Optional[List[Any]] = None
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
    bot_id: Optional[str] = None
    initial_comment: Optional[InitialCommentClass] = None
    num_stars: Optional[int] = None
    is_starred: Optional[bool] = None
    pinned_to: Optional[List[Any]] = None
    reactions: Optional[List[Any]] = None
    comments_count: Optional[int] = None
    attachments: Optional[List[Any]] = None
    blocks: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemFile':
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
        editors = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("editors"))
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
        channels = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("channels"))
        groups = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("groups"))
        ims = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("ims"))
        shares = from_union([PurpleShares.from_dict, from_none], obj.get("shares"))
        has_more_shares = from_union([from_bool, from_none], obj.get("has_more_shares"))
        to = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("to"))
        file_from = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("from"))
        cc = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("cc"))
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
        title_blocks = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("title_blocks"))
        private_channels_with_file_access_count = from_union([from_int, from_none], obj.get("private_channels_with_file_access_count"))
        dm_mpdm_users_with_file_access = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("dm_mpdm_users_with_file_access"))
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
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        initial_comment = from_union([InitialCommentClass.from_dict, from_none], obj.get("initial_comment"))
        num_stars = from_union([from_int, from_none], obj.get("num_stars"))
        is_starred = from_union([from_bool, from_none], obj.get("is_starred"))
        pinned_to = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("pinned_to"))
        reactions = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("reactions"))
        comments_count = from_union([from_int, from_none], obj.get("comments_count"))
        attachments = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("attachments"))
        blocks = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("blocks"))
        return ItemFile(id, created, timestamp, name, title, subject, mimetype, filetype, pretty_type, user, user_team, source_team, mode, editable, non_owner_editable, editor, last_editor, updated, file_access, editors, edit_timestamp, alt_txt, subtype, transcription, mp4, mp4_low, vtt, hls, hls_embed, duration_ms, thumb_video_w, thumb_video_h, original_attachment_count, is_external, external_type, external_id, external_url, username, size, url_private, url_private_download, url_static_preview, app_id, app_name, thumb_64, thumb_64__gif, thumb_64__w, thumb_64__h, thumb_80, thumb_80__gif, thumb_80__w, thumb_80__h, thumb_160, thumb_160__gif, thumb_160__w, thumb_160__h, thumb_360, thumb_360__gif, thumb_360__w, thumb_360__h, thumb_480, thumb_480__gif, thumb_480__w, thumb_480__h, thumb_720, thumb_720__gif, thumb_720__w, thumb_720__h, thumb_800, thumb_800__gif, thumb_800__w, thumb_800__h, thumb_960, thumb_960__gif, thumb_960__w, thumb_960__h, thumb_1024, thumb_1024__gif, thumb_1024__w, thumb_1024__h, thumb_video, thumb_gif, thumb_pdf, thumb_pdf_w, thumb_pdf_h, thumb_tiny, converted_pdf, image_exif_rotation, original_w, original_h, deanimate, deanimate_gif, pjpeg, permalink, permalink_public, edit_link, has_rich_preview, media_display_type, preview_is_truncated, preview, preview_highlight, plain_text, preview_plain_text, has_more, sent_to_self, lines, lines_more, is_public, public_url_shared, display_as_bot, channels, groups, ims, shares, has_more_shares, to, file_from, cc, channel_actions_ts, channel_actions_count, headers, simplified_html, media_progress, saved, quip_thread_id, is_channel_space, linked_channel_id, access, teams_shared_with, last_read, title_blocks, private_channels_with_file_access_count, dm_mpdm_users_with_file_access, org_or_workspace_access, update_notification, canvas_template_mode, template_conversion_ts, template_name, template_title, template_description, template_icon, team_pref_version_history_enabled, show_badge, bot_id, initial_comment, num_stars, is_starred, pinned_to, reactions, comments_count, attachments, blocks)

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
        result["editors"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.editors)
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
        result["channels"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.channels)
        result["groups"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.groups)
        result["ims"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.ims)
        result["shares"] = from_union([lambda x: to_class(PurpleShares, x), from_none], self.shares)
        result["has_more_shares"] = from_union([from_bool, from_none], self.has_more_shares)
        result["to"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.to)
        result["from"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.file_from)
        result["cc"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.cc)
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
        result["title_blocks"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.title_blocks)
        result["private_channels_with_file_access_count"] = from_union([from_int, from_none], self.private_channels_with_file_access_count)
        result["dm_mpdm_users_with_file_access"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.dm_mpdm_users_with_file_access)
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
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["initial_comment"] = from_union([lambda x: to_class(InitialCommentClass, x), from_none], self.initial_comment)
        result["num_stars"] = from_union([from_int, from_none], self.num_stars)
        result["is_starred"] = from_union([from_bool, from_none], self.is_starred)
        result["pinned_to"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.pinned_to)
        result["reactions"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.reactions)
        result["comments_count"] = from_union([from_int, from_none], self.comments_count)
        result["attachments"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.attachments)
        result["blocks"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.blocks)
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
class SelectedOptionElement:
    text: Optional[str] = None
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SelectedOptionElement':
        assert isinstance(obj, dict)
        text = from_union([from_str, from_none], obj.get("text"))
        value = from_union([from_str, from_none], obj.get("value"))
        return SelectedOptionElement(text, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([from_str, from_none], self.text)
        result["value"] = from_union([from_str, from_none], self.value)
        return result


@dataclass
class ActionOptionGroup:
    text: Optional[str] = None
    options: Optional[List[SelectedOptionElement]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ActionOptionGroup':
        assert isinstance(obj, dict)
        text = from_union([from_str, from_none], obj.get("text"))
        options = from_union([lambda x: from_list(SelectedOptionElement.from_dict, x), from_none], obj.get("options"))
        return ActionOptionGroup(text, options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([from_str, from_none], self.text)
        result["options"] = from_union([lambda x: from_list(lambda x: to_class(SelectedOptionElement, x), x), from_none], self.options)
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
    options: Optional[List[SelectedOptionElement]] = None
    selected_options: Optional[List[SelectedOptionElement]] = None
    data_source: Optional[str] = None
    min_query_length: Optional[int] = None
    option_groups: Optional[List[ActionOptionGroup]] = None
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
        options = from_union([lambda x: from_list(SelectedOptionElement.from_dict, x), from_none], obj.get("options"))
        selected_options = from_union([lambda x: from_list(SelectedOptionElement.from_dict, x), from_none], obj.get("selected_options"))
        data_source = from_union([from_str, from_none], obj.get("data_source"))
        min_query_length = from_union([from_int, from_none], obj.get("min_query_length"))
        option_groups = from_union([lambda x: from_list(ActionOptionGroup.from_dict, x), from_none], obj.get("option_groups"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Action(id, name, text, style, type, value, confirm, options, selected_options, data_source, min_query_length, option_groups, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["text"] = from_union([from_str, from_none], self.text)
        result["style"] = from_union([from_str, from_none], self.style)
        result["type"] = from_union([from_str, from_none], self.type)
        result["value"] = from_union([from_str, from_none], self.value)
        result["confirm"] = from_union([lambda x: to_class(ActionConfirm, x), from_none], self.confirm)
        result["options"] = from_union([lambda x: from_list(lambda x: to_class(SelectedOptionElement, x), x), from_none], self.options)
        result["selected_options"] = from_union([lambda x: from_list(lambda x: to_class(SelectedOptionElement, x), x), from_none], self.selected_options)
        result["data_source"] = from_union([from_str, from_none], self.data_source)
        result["min_query_length"] = from_union([from_int, from_none], self.min_query_length)
        result["option_groups"] = from_union([lambda x: from_list(lambda x: to_class(ActionOptionGroup, x), x), from_none], self.option_groups)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


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
class AccessoryConfirm:
    title: Optional[DescriptionElement] = None
    text: Optional[DescriptionElement] = None
    confirm: Optional[DescriptionElement] = None
    deny: Optional[DescriptionElement] = None
    style: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AccessoryConfirm':
        assert isinstance(obj, dict)
        title = from_union([DescriptionElement.from_dict, from_none], obj.get("title"))
        text = from_union([DescriptionElement.from_dict, from_none], obj.get("text"))
        confirm = from_union([DescriptionElement.from_dict, from_none], obj.get("confirm"))
        deny = from_union([DescriptionElement.from_dict, from_none], obj.get("deny"))
        style = from_union([from_str, from_none], obj.get("style"))
        return AccessoryConfirm(title, text, confirm, deny, style)

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
    code: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Style':
        assert isinstance(obj, dict)
        bold = from_union([from_bool, from_none], obj.get("bold"))
        italic = from_union([from_bool, from_none], obj.get("italic"))
        strike = from_union([from_bool, from_none], obj.get("strike"))
        code = from_union([from_bool, from_none], obj.get("code"))
        return Style(bold, italic, strike, code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bold"] = from_union([from_bool, from_none], self.bold)
        result["italic"] = from_union([from_bool, from_none], self.italic)
        result["strike"] = from_union([from_bool, from_none], self.strike)
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
    url: Optional[str] = None
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
        url = from_union([from_str, from_none], obj.get("url"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        usergroup_id = from_union([from_str, from_none], obj.get("usergroup_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        skin_tone = from_union([from_int, from_none], obj.get("skin_tone"))
        unicode = from_union([from_str, from_none], obj.get("unicode"))
        return PurpleElement(type, range, style, text, channel_id, value, timestamp, url, team_id, user_id, usergroup_id, name, skin_tone, unicode)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: to_enum(PurpleType, x), from_none], self.type)
        result["range"] = from_union([from_str, from_none], self.range)
        result["style"] = from_union([lambda x: to_class(Style, x), from_none], self.style)
        result["text"] = from_union([from_str, from_none], self.text)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["value"] = from_union([from_str, from_none], self.value)
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        result["url"] = from_union([from_str, from_none], self.url)
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
class InitialOptionElement:
    text: Optional[DescriptionElement] = None
    value: Optional[str] = None
    description: Optional[DescriptionElement] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InitialOptionElement':
        assert isinstance(obj, dict)
        text = from_union([DescriptionElement.from_dict, from_none], obj.get("text"))
        value = from_union([from_str, from_none], obj.get("value"))
        description = from_union([DescriptionElement.from_dict, from_none], obj.get("description"))
        url = from_union([from_str, from_none], obj.get("url"))
        return InitialOptionElement(text, value, description, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.text)
        result["value"] = from_union([from_str, from_none], self.value)
        result["description"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.description)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class AccessoryOptionGroup:
    label: Optional[DescriptionElement] = None
    options: Optional[List[InitialOptionElement]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AccessoryOptionGroup':
        assert isinstance(obj, dict)
        label = from_union([DescriptionElement.from_dict, from_none], obj.get("label"))
        options = from_union([lambda x: from_list(InitialOptionElement.from_dict, x), from_none], obj.get("options"))
        return AccessoryOptionGroup(label, options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["label"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.label)
        result["options"] = from_union([lambda x: from_list(lambda x: to_class(InitialOptionElement, x), x), from_none], self.options)
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
    image_url: Optional[str] = None
    alt_text: Optional[str] = None
    fallback: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    text: Optional[DescriptionElement] = None
    action_id: Optional[str] = None
    url: Optional[str] = None
    value: Optional[str] = None
    style: Optional[str] = None
    confirm: Optional[AccessoryConfirm] = None
    accessibility_label: Optional[str] = None
    workflow: Optional[Workflow] = None
    options: Optional[List[InitialOptionElement]] = None
    initial_options: Optional[List[InitialOptionElement]] = None
    focus_on_load: Optional[bool] = None
    initial_option: Optional[InitialOptionElement] = None
    placeholder: Optional[DescriptionElement] = None
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
    option_groups: Optional[List[AccessoryOptionGroup]] = None
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
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        text = from_union([DescriptionElement.from_dict, from_none], obj.get("text"))
        action_id = from_union([from_str, from_none], obj.get("action_id"))
        url = from_union([from_str, from_none], obj.get("url"))
        value = from_union([from_str, from_none], obj.get("value"))
        style = from_union([from_str, from_none], obj.get("style"))
        confirm = from_union([AccessoryConfirm.from_dict, from_none], obj.get("confirm"))
        accessibility_label = from_union([from_str, from_none], obj.get("accessibility_label"))
        workflow = from_union([Workflow.from_dict, from_none], obj.get("workflow"))
        options = from_union([lambda x: from_list(InitialOptionElement.from_dict, x), from_none], obj.get("options"))
        initial_options = from_union([lambda x: from_list(InitialOptionElement.from_dict, x), from_none], obj.get("initial_options"))
        focus_on_load = from_union([from_bool, from_none], obj.get("focus_on_load"))
        initial_option = from_union([InitialOptionElement.from_dict, from_none], obj.get("initial_option"))
        placeholder = from_union([DescriptionElement.from_dict, from_none], obj.get("placeholder"))
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
        option_groups = from_union([lambda x: from_list(AccessoryOptionGroup.from_dict, x), from_none], obj.get("option_groups"))
        initial_user = from_union([from_str, from_none], obj.get("initial_user"))
        initial_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("initial_users"))
        elements = from_union([lambda x: from_list(AccessoryElement.from_dict, x), from_none], obj.get("elements"))
        indent = from_union([from_int, from_none], obj.get("indent"))
        offset = from_union([from_int, from_none], obj.get("offset"))
        border = from_union([from_int, from_none], obj.get("border"))
        return Accessory(type, image_url, alt_text, fallback, image_width, image_height, image_bytes, text, action_id, url, value, style, confirm, accessibility_label, workflow, options, initial_options, focus_on_load, initial_option, placeholder, initial_channel, response_url_enabled, initial_channels, max_selected_items, initial_conversation, default_to_current_conversation, filter, initial_conversations, initial_date, initial_time, timezone, initial_date_time, min_query_length, option_groups, initial_user, initial_users, elements, indent, offset, border)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["text"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.text)
        result["action_id"] = from_union([from_str, from_none], self.action_id)
        result["url"] = from_union([from_str, from_none], self.url)
        result["value"] = from_union([from_str, from_none], self.value)
        result["style"] = from_union([from_str, from_none], self.style)
        result["confirm"] = from_union([lambda x: to_class(AccessoryConfirm, x), from_none], self.confirm)
        result["accessibility_label"] = from_union([from_str, from_none], self.accessibility_label)
        result["workflow"] = from_union([lambda x: to_class(Workflow, x), from_none], self.workflow)
        result["options"] = from_union([lambda x: from_list(lambda x: to_class(InitialOptionElement, x), x), from_none], self.options)
        result["initial_options"] = from_union([lambda x: from_list(lambda x: to_class(InitialOptionElement, x), x), from_none], self.initial_options)
        result["focus_on_load"] = from_union([from_bool, from_none], self.focus_on_load)
        result["initial_option"] = from_union([lambda x: to_class(InitialOptionElement, x), from_none], self.initial_option)
        result["placeholder"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.placeholder)
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
        result["option_groups"] = from_union([lambda x: from_list(lambda x: to_class(AccessoryOptionGroup, x), x), from_none], self.option_groups)
        result["initial_user"] = from_union([from_str, from_none], self.initial_user)
        result["initial_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.initial_users)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(AccessoryElement, x), x), from_none], self.elements)
        result["indent"] = from_union([from_int, from_none], self.indent)
        result["offset"] = from_union([from_int, from_none], self.offset)
        result["border"] = from_union([from_int, from_none], self.border)
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
class Block:
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
    alt_text: Optional[str] = None
    text: Optional[DescriptionElement] = None
    fields: Optional[List[DescriptionElement]] = None
    accessory: Optional[Accessory] = None
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
    def from_dict(obj: Any) -> 'Block':
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
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        text = from_union([DescriptionElement.from_dict, from_none], obj.get("text"))
        fields = from_union([lambda x: from_list(DescriptionElement.from_dict, x), from_none], obj.get("fields"))
        accessory = from_union([Accessory.from_dict, from_none], obj.get("accessory"))
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
        return Block(title, description, type, elements, block_id, fallback, image_url, image_width, image_height, image_bytes, alt_text, text, fields, accessory, title_url, video_url, thumbnail_url, author_name, provider_name, provider_icon_url, function_trigger_id, app_id, is_workflow_app, sales_home_workflow_app_type, app_collaborators, button_label, bot_user_id, url, owning_team_id, workflow_id, developer_trace_id, trigger_type, trigger_subtype, share_url)

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
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["text"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.text)
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(DescriptionElement, x), x), from_none], self.fields)
        result["accessory"] = from_union([lambda x: to_class(Accessory, x), from_none], self.accessory)
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
class FluffyShares:
    public: Optional[Dict[str, List[Private]]] = None
    private: Optional[Dict[str, List[Private]]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyShares':
        assert isinstance(obj, dict)
        public = from_union([lambda x: from_dict(lambda x: from_list(Private.from_dict, x), x), from_none], obj.get("public"))
        private = from_union([lambda x: from_dict(lambda x: from_list(Private.from_dict, x), x), from_none], obj.get("private"))
        return FluffyShares(public, private)

    def to_dict(self) -> dict:
        result: dict = {}
        result["public"] = from_union([lambda x: from_dict(lambda x: from_list(lambda x: to_class(Private, x), x), x), from_none], self.public)
        result["private"] = from_union([lambda x: from_dict(lambda x: from_list(lambda x: to_class(Private, x), x), x), from_none], self.private)
        return result


@dataclass
class FileElement:
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
    shares: Optional[FluffyShares] = None
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
    title_blocks: Optional[List[Block]] = None
    private_channels_with_file_access_count: Optional[int] = None
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
    bot_id: Optional[str] = None
    initial_comment: Optional[InitialCommentClass] = None
    num_stars: Optional[int] = None
    is_starred: Optional[bool] = None
    pinned_to: Optional[List[str]] = None
    reactions: Optional[List[Reaction]] = None
    comments_count: Optional[int] = None
    attachments: Optional[List[Any]] = None
    blocks: Optional[List[Block]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FileElement':
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
        shares = from_union([FluffyShares.from_dict, from_none], obj.get("shares"))
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
        title_blocks = from_union([lambda x: from_list(Block.from_dict, x), from_none], obj.get("title_blocks"))
        private_channels_with_file_access_count = from_union([from_int, from_none], obj.get("private_channels_with_file_access_count"))
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
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        initial_comment = from_union([InitialCommentClass.from_dict, from_none], obj.get("initial_comment"))
        num_stars = from_union([from_int, from_none], obj.get("num_stars"))
        is_starred = from_union([from_bool, from_none], obj.get("is_starred"))
        pinned_to = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pinned_to"))
        reactions = from_union([lambda x: from_list(Reaction.from_dict, x), from_none], obj.get("reactions"))
        comments_count = from_union([from_int, from_none], obj.get("comments_count"))
        attachments = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("attachments"))
        blocks = from_union([lambda x: from_list(Block.from_dict, x), from_none], obj.get("blocks"))
        return FileElement(id, created, timestamp, name, title, subject, mimetype, filetype, pretty_type, user, user_team, source_team, mode, editable, non_owner_editable, editor, last_editor, updated, file_access, editors, edit_timestamp, alt_txt, subtype, transcription, mp4, mp4_low, vtt, hls, hls_embed, duration_ms, thumb_video_w, thumb_video_h, original_attachment_count, is_external, external_type, external_id, external_url, username, size, url_private, url_private_download, url_static_preview, app_id, app_name, thumb_64, thumb_64__gif, thumb_64__w, thumb_64__h, thumb_80, thumb_80__gif, thumb_80__w, thumb_80__h, thumb_160, thumb_160__gif, thumb_160__w, thumb_160__h, thumb_360, thumb_360__gif, thumb_360__w, thumb_360__h, thumb_480, thumb_480__gif, thumb_480__w, thumb_480__h, thumb_720, thumb_720__gif, thumb_720__w, thumb_720__h, thumb_800, thumb_800__gif, thumb_800__w, thumb_800__h, thumb_960, thumb_960__gif, thumb_960__w, thumb_960__h, thumb_1024, thumb_1024__gif, thumb_1024__w, thumb_1024__h, thumb_video, thumb_gif, thumb_pdf, thumb_pdf_w, thumb_pdf_h, thumb_tiny, converted_pdf, image_exif_rotation, original_w, original_h, deanimate, deanimate_gif, pjpeg, permalink, permalink_public, edit_link, has_rich_preview, media_display_type, preview_is_truncated, preview, preview_highlight, plain_text, preview_plain_text, has_more, sent_to_self, lines, lines_more, is_public, public_url_shared, display_as_bot, channels, groups, ims, shares, has_more_shares, to, file_from, cc, channel_actions_ts, channel_actions_count, headers, simplified_html, media_progress, saved, quip_thread_id, is_channel_space, linked_channel_id, access, teams_shared_with, last_read, title_blocks, private_channels_with_file_access_count, dm_mpdm_users_with_file_access, org_or_workspace_access, update_notification, canvas_template_mode, template_conversion_ts, template_name, template_title, template_description, template_icon, team_pref_version_history_enabled, show_badge, bot_id, initial_comment, num_stars, is_starred, pinned_to, reactions, comments_count, attachments, blocks)

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
        result["shares"] = from_union([lambda x: to_class(FluffyShares, x), from_none], self.shares)
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
        result["title_blocks"] = from_union([lambda x: from_list(lambda x: to_class(Block, x), x), from_none], self.title_blocks)
        result["private_channels_with_file_access_count"] = from_union([from_int, from_none], self.private_channels_with_file_access_count)
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
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["initial_comment"] = from_union([lambda x: to_class(InitialCommentClass, x), from_none], self.initial_comment)
        result["num_stars"] = from_union([from_int, from_none], self.num_stars)
        result["is_starred"] = from_union([from_bool, from_none], self.is_starred)
        result["pinned_to"] = from_union([lambda x: from_list(from_str, x), from_none], self.pinned_to)
        result["reactions"] = from_union([lambda x: from_list(lambda x: to_class(Reaction, x), x), from_none], self.reactions)
        result["comments_count"] = from_union([from_int, from_none], self.comments_count)
        result["attachments"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.attachments)
        result["blocks"] = from_union([lambda x: from_list(lambda x: to_class(Block, x), x), from_none], self.blocks)
        return result


@dataclass
class BotProfileIcons:
    image_36: Optional[str] = None
    image_48: Optional[str] = None
    image_72: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BotProfileIcons':
        assert isinstance(obj, dict)
        image_36 = from_union([from_str, from_none], obj.get("image_36"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        return BotProfileIcons(image_36, image_48, image_72)

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
    icons: Optional[BotProfileIcons] = None
    team_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BotProfile':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        deleted = from_union([from_bool, from_none], obj.get("deleted"))
        name = from_union([from_str, from_none], obj.get("name"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        icons = from_union([BotProfileIcons.from_dict, from_none], obj.get("icons"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        return BotProfile(id, deleted, name, updated, app_id, icons, team_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["deleted"] = from_union([from_bool, from_none], self.deleted)
        result["name"] = from_union([from_str, from_none], self.name)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["icons"] = from_union([lambda x: to_class(BotProfileIcons, x), from_none], self.icons)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        return result


@dataclass
class ItemClass:
    id: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    created: Optional[str] = None
    timestamp: Optional[str] = None
    user: Optional[str] = None
    username: Optional[str] = None
    is_intro: Optional[bool] = None
    is_public: Optional[bool] = None
    is_starred: Optional[bool] = None
    public_url_shared: Optional[bool] = None
    url_private: Optional[str] = None
    url_private_download: Optional[bool] = None
    permalink: Optional[str] = None
    permalink_public: Optional[bool] = None
    edit_link: Optional[str] = None
    preview: Optional[str] = None
    preview_highlight: Optional[str] = None
    lines: Optional[int] = None
    lines_more: Optional[int] = None
    preview_is_truncated: Optional[bool] = None
    has_rich_preview: Optional[bool] = None
    media_display_type: Optional[str] = None
    mimetype: Optional[str] = None
    filetype: Optional[str] = None
    pretty_type: Optional[str] = None
    is_external: Optional[bool] = None
    external_type: Optional[str] = None
    editable: Optional[bool] = None
    display_as_bot: Optional[bool] = None
    size: Optional[int] = None
    mode: Optional[str] = None
    comment: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemClass':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        title = from_union([from_str, from_none], obj.get("title"))
        created = from_union([from_str, from_none], obj.get("created"))
        timestamp = from_union([from_str, from_none], obj.get("timestamp"))
        user = from_union([from_str, from_none], obj.get("user"))
        username = from_union([from_str, from_none], obj.get("username"))
        is_intro = from_union([from_bool, from_none], obj.get("is_intro"))
        is_public = from_union([from_bool, from_none], obj.get("is_public"))
        is_starred = from_union([from_bool, from_none], obj.get("is_starred"))
        public_url_shared = from_union([from_bool, from_none], obj.get("public_url_shared"))
        url_private = from_union([from_str, from_none], obj.get("url_private"))
        url_private_download = from_union([from_bool, from_none], obj.get("url_private_download"))
        permalink = from_union([from_str, from_none], obj.get("permalink"))
        permalink_public = from_union([from_bool, from_none], obj.get("permalink_public"))
        edit_link = from_union([from_str, from_none], obj.get("edit_link"))
        preview = from_union([from_str, from_none], obj.get("preview"))
        preview_highlight = from_union([from_str, from_none], obj.get("preview_highlight"))
        lines = from_union([from_int, from_none], obj.get("lines"))
        lines_more = from_union([from_int, from_none], obj.get("lines_more"))
        preview_is_truncated = from_union([from_bool, from_none], obj.get("preview_is_truncated"))
        has_rich_preview = from_union([from_bool, from_none], obj.get("has_rich_preview"))
        media_display_type = from_union([from_str, from_none], obj.get("media_display_type"))
        mimetype = from_union([from_str, from_none], obj.get("mimetype"))
        filetype = from_union([from_str, from_none], obj.get("filetype"))
        pretty_type = from_union([from_str, from_none], obj.get("pretty_type"))
        is_external = from_union([from_bool, from_none], obj.get("is_external"))
        external_type = from_union([from_str, from_none], obj.get("external_type"))
        editable = from_union([from_bool, from_none], obj.get("editable"))
        display_as_bot = from_union([from_bool, from_none], obj.get("display_as_bot"))
        size = from_union([from_int, from_none], obj.get("size"))
        mode = from_union([from_str, from_none], obj.get("mode"))
        comment = from_union([from_str, from_none], obj.get("comment"))
        return ItemClass(id, name, title, created, timestamp, user, username, is_intro, is_public, is_starred, public_url_shared, url_private, url_private_download, permalink, permalink_public, edit_link, preview, preview_highlight, lines, lines_more, preview_is_truncated, has_rich_preview, media_display_type, mimetype, filetype, pretty_type, is_external, external_type, editable, display_as_bot, size, mode, comment)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["title"] = from_union([from_str, from_none], self.title)
        result["created"] = from_union([from_str, from_none], self.created)
        result["timestamp"] = from_union([from_str, from_none], self.timestamp)
        result["user"] = from_union([from_str, from_none], self.user)
        result["username"] = from_union([from_str, from_none], self.username)
        result["is_intro"] = from_union([from_bool, from_none], self.is_intro)
        result["is_public"] = from_union([from_bool, from_none], self.is_public)
        result["is_starred"] = from_union([from_bool, from_none], self.is_starred)
        result["public_url_shared"] = from_union([from_bool, from_none], self.public_url_shared)
        result["url_private"] = from_union([from_str, from_none], self.url_private)
        result["url_private_download"] = from_union([from_bool, from_none], self.url_private_download)
        result["permalink"] = from_union([from_str, from_none], self.permalink)
        result["permalink_public"] = from_union([from_bool, from_none], self.permalink_public)
        result["edit_link"] = from_union([from_str, from_none], self.edit_link)
        result["preview"] = from_union([from_str, from_none], self.preview)
        result["preview_highlight"] = from_union([from_str, from_none], self.preview_highlight)
        result["lines"] = from_union([from_int, from_none], self.lines)
        result["lines_more"] = from_union([from_int, from_none], self.lines_more)
        result["preview_is_truncated"] = from_union([from_bool, from_none], self.preview_is_truncated)
        result["has_rich_preview"] = from_union([from_bool, from_none], self.has_rich_preview)
        result["media_display_type"] = from_union([from_str, from_none], self.media_display_type)
        result["mimetype"] = from_union([from_str, from_none], self.mimetype)
        result["filetype"] = from_union([from_str, from_none], self.filetype)
        result["pretty_type"] = from_union([from_str, from_none], self.pretty_type)
        result["is_external"] = from_union([from_bool, from_none], self.is_external)
        result["external_type"] = from_union([from_str, from_none], self.external_type)
        result["editable"] = from_union([from_bool, from_none], self.editable)
        result["display_as_bot"] = from_union([from_bool, from_none], self.display_as_bot)
        result["size"] = from_union([from_int, from_none], self.size)
        result["mode"] = from_union([from_str, from_none], self.mode)
        result["comment"] = from_union([from_str, from_none], self.comment)
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
class MessageIcons:
    emoji: Optional[str] = None
    image_36: Optional[str] = None
    image_48: Optional[str] = None
    image_64: Optional[str] = None
    image_72: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MessageIcons':
        assert isinstance(obj, dict)
        emoji = from_union([from_str, from_none], obj.get("emoji"))
        image_36 = from_union([from_str, from_none], obj.get("image_36"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_64 = from_union([from_str, from_none], obj.get("image_64"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        return MessageIcons(emoji, image_36, image_48, image_64, image_72)

    def to_dict(self) -> dict:
        result: dict = {}
        result["emoji"] = from_union([from_str, from_none], self.emoji)
        result["image_36"] = from_union([from_str, from_none], self.image_36)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_64"] = from_union([from_str, from_none], self.image_64)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        return result


@dataclass
class MessageMetadata:
    event_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MessageMetadata':
        assert isinstance(obj, dict)
        event_type = from_union([from_str, from_none], obj.get("event_type"))
        return MessageMetadata(event_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = from_union([from_str, from_none], self.event_type)
        return result


@dataclass
class Room:
    id: Optional[str] = None
    name: Optional[str] = None
    media_server: Optional[str] = None
    created_by: Optional[str] = None
    date_start: Optional[int] = None
    date_end: Optional[int] = None
    participants: Optional[List[Any]] = None
    participant_history: Optional[List[Any]] = None
    participants_camera_on: Optional[List[Any]] = None
    participants_camera_off: Optional[List[Any]] = None
    participants_screenshare_on: Optional[List[Any]] = None
    participants_screenshare_off: Optional[List[Any]] = None
    canvas_thread_ts: Optional[str] = None
    thread_root_ts: Optional[str] = None
    channels: Optional[List[Any]] = None
    is_dm_call: Optional[bool] = None
    was_rejected: Optional[bool] = None
    was_missed: Optional[bool] = None
    was_accepted: Optional[bool] = None
    has_ended: Optional[bool] = None
    background_id: Optional[str] = None
    canvas_background: Optional[str] = None
    is_prewarmed: Optional[bool] = None
    is_scheduled: Optional[bool] = None
    attached_file_ids: Optional[List[Any]] = None
    media_backend_type: Optional[str] = None
    display_id: Optional[str] = None
    external_unique_id: Optional[str] = None
    app_id: Optional[str] = None
    call_family: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Room':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        media_server = from_union([from_str, from_none], obj.get("media_server"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        date_start = from_union([from_int, from_none], obj.get("date_start"))
        date_end = from_union([from_int, from_none], obj.get("date_end"))
        participants = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("participants"))
        participant_history = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("participant_history"))
        participants_camera_on = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("participants_camera_on"))
        participants_camera_off = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("participants_camera_off"))
        participants_screenshare_on = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("participants_screenshare_on"))
        participants_screenshare_off = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("participants_screenshare_off"))
        canvas_thread_ts = from_union([from_str, from_none], obj.get("canvas_thread_ts"))
        thread_root_ts = from_union([from_str, from_none], obj.get("thread_root_ts"))
        channels = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("channels"))
        is_dm_call = from_union([from_bool, from_none], obj.get("is_dm_call"))
        was_rejected = from_union([from_bool, from_none], obj.get("was_rejected"))
        was_missed = from_union([from_bool, from_none], obj.get("was_missed"))
        was_accepted = from_union([from_bool, from_none], obj.get("was_accepted"))
        has_ended = from_union([from_bool, from_none], obj.get("has_ended"))
        background_id = from_union([from_str, from_none], obj.get("background_id"))
        canvas_background = from_union([from_str, from_none], obj.get("canvas_background"))
        is_prewarmed = from_union([from_bool, from_none], obj.get("is_prewarmed"))
        is_scheduled = from_union([from_bool, from_none], obj.get("is_scheduled"))
        attached_file_ids = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("attached_file_ids"))
        media_backend_type = from_union([from_str, from_none], obj.get("media_backend_type"))
        display_id = from_union([from_str, from_none], obj.get("display_id"))
        external_unique_id = from_union([from_str, from_none], obj.get("external_unique_id"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        call_family = from_union([from_str, from_none], obj.get("call_family"))
        return Room(id, name, media_server, created_by, date_start, date_end, participants, participant_history, participants_camera_on, participants_camera_off, participants_screenshare_on, participants_screenshare_off, canvas_thread_ts, thread_root_ts, channels, is_dm_call, was_rejected, was_missed, was_accepted, has_ended, background_id, canvas_background, is_prewarmed, is_scheduled, attached_file_ids, media_backend_type, display_id, external_unique_id, app_id, call_family)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["media_server"] = from_union([from_str, from_none], self.media_server)
        result["created_by"] = from_union([from_str, from_none], self.created_by)
        result["date_start"] = from_union([from_int, from_none], self.date_start)
        result["date_end"] = from_union([from_int, from_none], self.date_end)
        result["participants"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.participants)
        result["participant_history"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.participant_history)
        result["participants_camera_on"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.participants_camera_on)
        result["participants_camera_off"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.participants_camera_off)
        result["participants_screenshare_on"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.participants_screenshare_on)
        result["participants_screenshare_off"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.participants_screenshare_off)
        result["canvas_thread_ts"] = from_union([from_str, from_none], self.canvas_thread_ts)
        result["thread_root_ts"] = from_union([from_str, from_none], self.thread_root_ts)
        result["channels"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.channels)
        result["is_dm_call"] = from_union([from_bool, from_none], self.is_dm_call)
        result["was_rejected"] = from_union([from_bool, from_none], self.was_rejected)
        result["was_missed"] = from_union([from_bool, from_none], self.was_missed)
        result["was_accepted"] = from_union([from_bool, from_none], self.was_accepted)
        result["has_ended"] = from_union([from_bool, from_none], self.has_ended)
        result["background_id"] = from_union([from_str, from_none], self.background_id)
        result["canvas_background"] = from_union([from_str, from_none], self.canvas_background)
        result["is_prewarmed"] = from_union([from_bool, from_none], self.is_prewarmed)
        result["is_scheduled"] = from_union([from_bool, from_none], self.is_scheduled)
        result["attached_file_ids"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.attached_file_ids)
        result["media_backend_type"] = from_union([from_str, from_none], self.media_backend_type)
        result["display_id"] = from_union([from_str, from_none], self.display_id)
        result["external_unique_id"] = from_union([from_str, from_none], self.external_unique_id)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["call_family"] = from_union([from_str, from_none], self.call_family)
        return result


@dataclass
class Root:
    text: Optional[str] = None
    user: Optional[str] = None
    parent_user_id: Optional[str] = None
    username: Optional[str] = None
    team: Optional[str] = None
    bot_id: Optional[str] = None
    mrkdwn: Optional[bool] = None
    type: Optional[str] = None
    subtype: Optional[str] = None
    thread_ts: Optional[str] = None
    icons: Optional[MessageIcons] = None
    bot_profile: Optional[BotProfile] = None
    edited: Optional[Edited] = None
    replies: Optional[List[Any]] = None
    reply_count: Optional[int] = None
    reply_users: Optional[List[Any]] = None
    reply_users_count: Optional[int] = None
    latest_reply: Optional[str] = None
    subscribed: Optional[bool] = None
    last_read: Optional[str] = None
    unread_count: Optional[int] = None
    ts: Optional[str] = None
    room: Optional[Room] = None
    no_notifications: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        assert isinstance(obj, dict)
        text = from_union([from_str, from_none], obj.get("text"))
        user = from_union([from_str, from_none], obj.get("user"))
        parent_user_id = from_union([from_str, from_none], obj.get("parent_user_id"))
        username = from_union([from_str, from_none], obj.get("username"))
        team = from_union([from_str, from_none], obj.get("team"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        mrkdwn = from_union([from_bool, from_none], obj.get("mrkdwn"))
        type = from_union([from_str, from_none], obj.get("type"))
        subtype = from_union([from_str, from_none], obj.get("subtype"))
        thread_ts = from_union([from_str, from_none], obj.get("thread_ts"))
        icons = from_union([MessageIcons.from_dict, from_none], obj.get("icons"))
        bot_profile = from_union([BotProfile.from_dict, from_none], obj.get("bot_profile"))
        edited = from_union([Edited.from_dict, from_none], obj.get("edited"))
        replies = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("replies"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        reply_users = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("reply_users"))
        reply_users_count = from_union([from_int, from_none], obj.get("reply_users_count"))
        latest_reply = from_union([from_str, from_none], obj.get("latest_reply"))
        subscribed = from_union([from_bool, from_none], obj.get("subscribed"))
        last_read = from_union([from_str, from_none], obj.get("last_read"))
        unread_count = from_union([from_int, from_none], obj.get("unread_count"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        room = from_union([Room.from_dict, from_none], obj.get("room"))
        no_notifications = from_union([from_bool, from_none], obj.get("no_notifications"))
        return Root(text, user, parent_user_id, username, team, bot_id, mrkdwn, type, subtype, thread_ts, icons, bot_profile, edited, replies, reply_count, reply_users, reply_users_count, latest_reply, subscribed, last_read, unread_count, ts, room, no_notifications)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([from_str, from_none], self.text)
        result["user"] = from_union([from_str, from_none], self.user)
        result["parent_user_id"] = from_union([from_str, from_none], self.parent_user_id)
        result["username"] = from_union([from_str, from_none], self.username)
        result["team"] = from_union([from_str, from_none], self.team)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["mrkdwn"] = from_union([from_bool, from_none], self.mrkdwn)
        result["type"] = from_union([from_str, from_none], self.type)
        result["subtype"] = from_union([from_str, from_none], self.subtype)
        result["thread_ts"] = from_union([from_str, from_none], self.thread_ts)
        result["icons"] = from_union([lambda x: to_class(MessageIcons, x), from_none], self.icons)
        result["bot_profile"] = from_union([lambda x: to_class(BotProfile, x), from_none], self.bot_profile)
        result["edited"] = from_union([lambda x: to_class(Edited, x), from_none], self.edited)
        result["replies"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.replies)
        result["reply_count"] = from_union([from_int, from_none], self.reply_count)
        result["reply_users"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.reply_users)
        result["reply_users_count"] = from_union([from_int, from_none], self.reply_users_count)
        result["latest_reply"] = from_union([from_str, from_none], self.latest_reply)
        result["subscribed"] = from_union([from_bool, from_none], self.subscribed)
        result["last_read"] = from_union([from_str, from_none], self.last_read)
        result["unread_count"] = from_union([from_int, from_none], self.unread_count)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["room"] = from_union([lambda x: to_class(Room, x), from_none], self.room)
        result["no_notifications"] = from_union([from_bool, from_none], self.no_notifications)
        return result


@dataclass
class MessageBlockMessage:
    type: Optional[str] = None
    subtype: Optional[str] = None
    team: Optional[str] = None
    channel: Optional[str] = None
    user: Optional[str] = None
    username: Optional[str] = None
    text: Optional[str] = None
    blocks: Optional[List[Block]] = None
    attachments: Optional[List[Any]] = None
    ts: Optional[str] = None
    thread_ts: Optional[str] = None
    is_intro: Optional[bool] = None
    is_starred: Optional[bool] = None
    wibblr: Optional[bool] = None
    pinned_to: Optional[List[Any]] = None
    reactions: Optional[List[Any]] = None
    app_id: Optional[str] = None
    bot_id: Optional[str] = None
    bot_link: Optional[str] = None
    display_as_bot: Optional[bool] = None
    bot_profile: Optional[BotProfile] = None
    icons: Optional[MessageIcons] = None
    file: Optional[ItemFile] = None
    files: Optional[List[Any]] = None
    upload: Optional[bool] = None
    parent_user_id: Optional[str] = None
    inviter: Optional[str] = None
    client_msg_id: Optional[str] = None
    comment: Optional[ItemClass] = None
    topic: Optional[str] = None
    purpose: Optional[str] = None
    edited: Optional[Edited] = None
    unfurl_links: Optional[bool] = None
    unfurl_media: Optional[bool] = None
    is_thread_broadcast: Optional[bool] = None
    is_locked: Optional[bool] = None
    replies: Optional[List[Any]] = None
    reply_count: Optional[int] = None
    reply_users: Optional[List[Any]] = None
    reply_users_count: Optional[int] = None
    latest_reply: Optional[str] = None
    subscribed: Optional[bool] = None
    x_files: Optional[List[Any]] = None
    hidden: Optional[bool] = None
    last_read: Optional[str] = None
    root: Optional[Root] = None
    item_type: Optional[str] = None
    item: Optional[ItemClass] = None
    metadata: Optional[MessageMetadata] = None
    room: Optional[Room] = None
    no_notifications: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MessageBlockMessage':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        subtype = from_union([from_str, from_none], obj.get("subtype"))
        team = from_union([from_str, from_none], obj.get("team"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        user = from_union([from_str, from_none], obj.get("user"))
        username = from_union([from_str, from_none], obj.get("username"))
        text = from_union([from_str, from_none], obj.get("text"))
        blocks = from_union([lambda x: from_list(Block.from_dict, x), from_none], obj.get("blocks"))
        attachments = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("attachments"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        thread_ts = from_union([from_str, from_none], obj.get("thread_ts"))
        is_intro = from_union([from_bool, from_none], obj.get("is_intro"))
        is_starred = from_union([from_bool, from_none], obj.get("is_starred"))
        wibblr = from_union([from_bool, from_none], obj.get("wibblr"))
        pinned_to = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("pinned_to"))
        reactions = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("reactions"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        bot_link = from_union([from_str, from_none], obj.get("bot_link"))
        display_as_bot = from_union([from_bool, from_none], obj.get("display_as_bot"))
        bot_profile = from_union([BotProfile.from_dict, from_none], obj.get("bot_profile"))
        icons = from_union([MessageIcons.from_dict, from_none], obj.get("icons"))
        file = from_union([ItemFile.from_dict, from_none], obj.get("file"))
        files = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("files"))
        upload = from_union([from_bool, from_none], obj.get("upload"))
        parent_user_id = from_union([from_str, from_none], obj.get("parent_user_id"))
        inviter = from_union([from_str, from_none], obj.get("inviter"))
        client_msg_id = from_union([from_str, from_none], obj.get("client_msg_id"))
        comment = from_union([ItemClass.from_dict, from_none], obj.get("comment"))
        topic = from_union([from_str, from_none], obj.get("topic"))
        purpose = from_union([from_str, from_none], obj.get("purpose"))
        edited = from_union([Edited.from_dict, from_none], obj.get("edited"))
        unfurl_links = from_union([from_bool, from_none], obj.get("unfurl_links"))
        unfurl_media = from_union([from_bool, from_none], obj.get("unfurl_media"))
        is_thread_broadcast = from_union([from_bool, from_none], obj.get("is_thread_broadcast"))
        is_locked = from_union([from_bool, from_none], obj.get("is_locked"))
        replies = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("replies"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        reply_users = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("reply_users"))
        reply_users_count = from_union([from_int, from_none], obj.get("reply_users_count"))
        latest_reply = from_union([from_str, from_none], obj.get("latest_reply"))
        subscribed = from_union([from_bool, from_none], obj.get("subscribed"))
        x_files = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("x_files"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        last_read = from_union([from_str, from_none], obj.get("last_read"))
        root = from_union([Root.from_dict, from_none], obj.get("root"))
        item_type = from_union([from_str, from_none], obj.get("item_type"))
        item = from_union([ItemClass.from_dict, from_none], obj.get("item"))
        metadata = from_union([MessageMetadata.from_dict, from_none], obj.get("metadata"))
        room = from_union([Room.from_dict, from_none], obj.get("room"))
        no_notifications = from_union([from_bool, from_none], obj.get("no_notifications"))
        return MessageBlockMessage(type, subtype, team, channel, user, username, text, blocks, attachments, ts, thread_ts, is_intro, is_starred, wibblr, pinned_to, reactions, app_id, bot_id, bot_link, display_as_bot, bot_profile, icons, file, files, upload, parent_user_id, inviter, client_msg_id, comment, topic, purpose, edited, unfurl_links, unfurl_media, is_thread_broadcast, is_locked, replies, reply_count, reply_users, reply_users_count, latest_reply, subscribed, x_files, hidden, last_read, root, item_type, item, metadata, room, no_notifications)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["subtype"] = from_union([from_str, from_none], self.subtype)
        result["team"] = from_union([from_str, from_none], self.team)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["user"] = from_union([from_str, from_none], self.user)
        result["username"] = from_union([from_str, from_none], self.username)
        result["text"] = from_union([from_str, from_none], self.text)
        result["blocks"] = from_union([lambda x: from_list(lambda x: to_class(Block, x), x), from_none], self.blocks)
        result["attachments"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.attachments)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["thread_ts"] = from_union([from_str, from_none], self.thread_ts)
        result["is_intro"] = from_union([from_bool, from_none], self.is_intro)
        result["is_starred"] = from_union([from_bool, from_none], self.is_starred)
        result["wibblr"] = from_union([from_bool, from_none], self.wibblr)
        result["pinned_to"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.pinned_to)
        result["reactions"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.reactions)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["bot_link"] = from_union([from_str, from_none], self.bot_link)
        result["display_as_bot"] = from_union([from_bool, from_none], self.display_as_bot)
        result["bot_profile"] = from_union([lambda x: to_class(BotProfile, x), from_none], self.bot_profile)
        result["icons"] = from_union([lambda x: to_class(MessageIcons, x), from_none], self.icons)
        result["file"] = from_union([lambda x: to_class(ItemFile, x), from_none], self.file)
        result["files"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.files)
        result["upload"] = from_union([from_bool, from_none], self.upload)
        result["parent_user_id"] = from_union([from_str, from_none], self.parent_user_id)
        result["inviter"] = from_union([from_str, from_none], self.inviter)
        result["client_msg_id"] = from_union([from_str, from_none], self.client_msg_id)
        result["comment"] = from_union([lambda x: to_class(ItemClass, x), from_none], self.comment)
        result["topic"] = from_union([from_str, from_none], self.topic)
        result["purpose"] = from_union([from_str, from_none], self.purpose)
        result["edited"] = from_union([lambda x: to_class(Edited, x), from_none], self.edited)
        result["unfurl_links"] = from_union([from_bool, from_none], self.unfurl_links)
        result["unfurl_media"] = from_union([from_bool, from_none], self.unfurl_media)
        result["is_thread_broadcast"] = from_union([from_bool, from_none], self.is_thread_broadcast)
        result["is_locked"] = from_union([from_bool, from_none], self.is_locked)
        result["replies"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.replies)
        result["reply_count"] = from_union([from_int, from_none], self.reply_count)
        result["reply_users"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.reply_users)
        result["reply_users_count"] = from_union([from_int, from_none], self.reply_users_count)
        result["latest_reply"] = from_union([from_str, from_none], self.latest_reply)
        result["subscribed"] = from_union([from_bool, from_none], self.subscribed)
        result["x_files"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.x_files)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["last_read"] = from_union([from_str, from_none], self.last_read)
        result["root"] = from_union([lambda x: to_class(Root, x), from_none], self.root)
        result["item_type"] = from_union([from_str, from_none], self.item_type)
        result["item"] = from_union([lambda x: to_class(ItemClass, x), from_none], self.item)
        result["metadata"] = from_union([lambda x: to_class(MessageMetadata, x), from_none], self.metadata)
        result["room"] = from_union([lambda x: to_class(Room, x), from_none], self.room)
        result["no_notifications"] = from_union([from_bool, from_none], self.no_notifications)
        return result


@dataclass
class MessageBlock:
    team: Optional[str] = None
    channel: Optional[str] = None
    ts: Optional[str] = None
    message: Optional[MessageBlockMessage] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MessageBlock':
        assert isinstance(obj, dict)
        team = from_union([from_str, from_none], obj.get("team"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        message = from_union([MessageBlockMessage.from_dict, from_none], obj.get("message"))
        return MessageBlock(team, channel, ts, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["team"] = from_union([from_str, from_none], self.team)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["message"] = from_union([lambda x: to_class(MessageBlockMessage, x), from_none], self.message)
        return result


@dataclass
class AttachmentMetadata:
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
    def from_dict(obj: Any) -> 'AttachmentMetadata':
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
        return AttachmentMetadata(thumb_64, thumb_80, thumb_160, original_w, original_h, thumb_360__w, thumb_360__h, format, extension, rotation, thumb_tiny)

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


@dataclass
class Preview:
    type: Optional[str] = None
    can_remove: Optional[bool] = None
    title: Optional[DescriptionElement] = None
    subtitle: Optional[DescriptionElement] = None
    icon_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Preview':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        can_remove = from_union([from_bool, from_none], obj.get("can_remove"))
        title = from_union([DescriptionElement.from_dict, from_none], obj.get("title"))
        subtitle = from_union([DescriptionElement.from_dict, from_none], obj.get("subtitle"))
        icon_url = from_union([from_str, from_none], obj.get("icon_url"))
        return Preview(type, can_remove, title, subtitle, icon_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["can_remove"] = from_union([from_bool, from_none], self.can_remove)
        result["title"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.title)
        result["subtitle"] = from_union([lambda x: to_class(DescriptionElement, x), from_none], self.subtitle)
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
    video_html_width: Optional[int] = None
    video_html_height: Optional[int] = None
    footer: Optional[str] = None
    footer_icon: Optional[str] = None
    ts: Optional[str] = None
    mrkdwn_in: Optional[List[str]] = None
    actions: Optional[List[Action]] = None
    blocks: Optional[List[Block]] = None
    message_blocks: Optional[List[MessageBlock]] = None
    preview: Optional[Preview] = None
    files: Optional[List[FileElement]] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    mimetype: Optional[str] = None
    url: Optional[str] = None
    metadata: Optional[AttachmentMetadata] = None
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
        video_html_width = from_union([from_int, from_none], obj.get("video_html_width"))
        video_html_height = from_union([from_int, from_none], obj.get("video_html_height"))
        footer = from_union([from_str, from_none], obj.get("footer"))
        footer_icon = from_union([from_str, from_none], obj.get("footer_icon"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        mrkdwn_in = from_union([lambda x: from_list(from_str, x), from_none], obj.get("mrkdwn_in"))
        actions = from_union([lambda x: from_list(Action.from_dict, x), from_none], obj.get("actions"))
        blocks = from_union([lambda x: from_list(Block.from_dict, x), from_none], obj.get("blocks"))
        message_blocks = from_union([lambda x: from_list(MessageBlock.from_dict, x), from_none], obj.get("message_blocks"))
        preview = from_union([Preview.from_dict, from_none], obj.get("preview"))
        files = from_union([lambda x: from_list(FileElement.from_dict, x), from_none], obj.get("files"))
        filename = from_union([from_str, from_none], obj.get("filename"))
        size = from_union([from_int, from_none], obj.get("size"))
        mimetype = from_union([from_str, from_none], obj.get("mimetype"))
        url = from_union([from_str, from_none], obj.get("url"))
        metadata = from_union([AttachmentMetadata.from_dict, from_none], obj.get("metadata"))
        is_file_attachment = from_union([from_bool, from_none], obj.get("is_file_attachment"))
        return Attachment(msg_subtype, fallback, callback_id, color, hide_color, pretext, service_url, service_name, service_icon, author_id, author_name, author_link, author_icon, from_url, original_url, author_subname, channel_id, channel_name, channel_team, id, app_id, bot_id, indent, is_msg_unfurl, is_reply_unfurl, is_thread_root_unfurl, is_app_unfurl, app_unfurl_url, title, title_link, text, fields, image_url, image_width, image_height, image_bytes, thumb_url, thumb_width, thumb_height, video_url, video_html, video_html_width, video_html_height, footer, footer_icon, ts, mrkdwn_in, actions, blocks, message_blocks, preview, files, filename, size, mimetype, url, metadata, is_file_attachment)

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
        result["video_html_width"] = from_union([from_int, from_none], self.video_html_width)
        result["video_html_height"] = from_union([from_int, from_none], self.video_html_height)
        result["footer"] = from_union([from_str, from_none], self.footer)
        result["footer_icon"] = from_union([from_str, from_none], self.footer_icon)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["mrkdwn_in"] = from_union([lambda x: from_list(from_str, x), from_none], self.mrkdwn_in)
        result["actions"] = from_union([lambda x: from_list(lambda x: to_class(Action, x), x), from_none], self.actions)
        result["blocks"] = from_union([lambda x: from_list(lambda x: to_class(Block, x), x), from_none], self.blocks)
        result["message_blocks"] = from_union([lambda x: from_list(lambda x: to_class(MessageBlock, x), x), from_none], self.message_blocks)
        result["preview"] = from_union([lambda x: to_class(Preview, x), from_none], self.preview)
        result["files"] = from_union([lambda x: from_list(lambda x: to_class(FileElement, x), x), from_none], self.files)
        result["filename"] = from_union([from_str, from_none], self.filename)
        result["size"] = from_union([from_int, from_none], self.size)
        result["mimetype"] = from_union([from_str, from_none], self.mimetype)
        result["url"] = from_union([from_str, from_none], self.url)
        result["metadata"] = from_union([lambda x: to_class(AttachmentMetadata, x), from_none], self.metadata)
        result["is_file_attachment"] = from_union([from_bool, from_none], self.is_file_attachment)
        return result


@dataclass
class ItemMessage:
    client_msg_id: Optional[str] = None
    type: Optional[str] = None
    app_id: Optional[str] = None
    team: Optional[str] = None
    user: Optional[str] = None
    bot_id: Optional[str] = None
    bot_profile: Optional[BotProfile] = None
    text: Optional[str] = None
    blocks: Optional[List[Block]] = None
    attachments: Optional[List[Attachment]] = None
    ts: Optional[str] = None
    pinned_to: Optional[List[str]] = None
    permalink: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemMessage':
        assert isinstance(obj, dict)
        client_msg_id = from_union([from_str, from_none], obj.get("client_msg_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        team = from_union([from_str, from_none], obj.get("team"))
        user = from_union([from_str, from_none], obj.get("user"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        bot_profile = from_union([BotProfile.from_dict, from_none], obj.get("bot_profile"))
        text = from_union([from_str, from_none], obj.get("text"))
        blocks = from_union([lambda x: from_list(Block.from_dict, x), from_none], obj.get("blocks"))
        attachments = from_union([lambda x: from_list(Attachment.from_dict, x), from_none], obj.get("attachments"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        pinned_to = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pinned_to"))
        permalink = from_union([from_str, from_none], obj.get("permalink"))
        return ItemMessage(client_msg_id, type, app_id, team, user, bot_id, bot_profile, text, blocks, attachments, ts, pinned_to, permalink)

    def to_dict(self) -> dict:
        result: dict = {}
        result["client_msg_id"] = from_union([from_str, from_none], self.client_msg_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["team"] = from_union([from_str, from_none], self.team)
        result["user"] = from_union([from_str, from_none], self.user)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["bot_profile"] = from_union([lambda x: to_class(BotProfile, x), from_none], self.bot_profile)
        result["text"] = from_union([from_str, from_none], self.text)
        result["blocks"] = from_union([lambda x: from_list(lambda x: to_class(Block, x), x), from_none], self.blocks)
        result["attachments"] = from_union([lambda x: from_list(lambda x: to_class(Attachment, x), x), from_none], self.attachments)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["pinned_to"] = from_union([lambda x: from_list(from_str, x), from_none], self.pinned_to)
        result["permalink"] = from_union([from_str, from_none], self.permalink)
        return result


@dataclass
class Item:
    type: Optional[str] = None
    channel: Optional[str] = None
    created_by: Optional[str] = None
    created: Optional[int] = None
    message: Optional[ItemMessage] = None
    file: Optional[ItemFile] = None
    comment: Optional[InitialCommentClass] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        created = from_union([from_int, from_none], obj.get("created"))
        message = from_union([ItemMessage.from_dict, from_none], obj.get("message"))
        file = from_union([ItemFile.from_dict, from_none], obj.get("file"))
        comment = from_union([InitialCommentClass.from_dict, from_none], obj.get("comment"))
        return Item(type, channel, created_by, created, message, file, comment)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["created_by"] = from_union([from_str, from_none], self.created_by)
        result["created"] = from_union([from_int, from_none], self.created)
        result["message"] = from_union([lambda x: to_class(ItemMessage, x), from_none], self.message)
        result["file"] = from_union([lambda x: to_class(ItemFile, x), from_none], self.file)
        result["comment"] = from_union([lambda x: to_class(InitialCommentClass, x), from_none], self.comment)
        return result


@dataclass
class PinnedInfo:
    channel: Optional[str] = None
    pinned_by: Optional[str] = None
    pinned_ts: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PinnedInfo':
        assert isinstance(obj, dict)
        channel = from_union([from_str, from_none], obj.get("channel"))
        pinned_by = from_union([from_str, from_none], obj.get("pinned_by"))
        pinned_ts = from_union([from_int, from_none], obj.get("pinned_ts"))
        return PinnedInfo(channel, pinned_by, pinned_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["pinned_by"] = from_union([from_str, from_none], self.pinned_by)
        result["pinned_ts"] = from_union([from_int, from_none], self.pinned_ts)
        return result


@dataclass
class PinAddedEvent:
    type: Optional[str] = None
    user: Optional[str] = None
    channel_id: Optional[str] = None
    item: Optional[Item] = None
    item_user: Optional[str] = None
    pin_count: Optional[int] = None
    pinned_info: Optional[PinnedInfo] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PinAddedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user = from_union([from_str, from_none], obj.get("user"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        item = from_union([Item.from_dict, from_none], obj.get("item"))
        item_user = from_union([from_str, from_none], obj.get("item_user"))
        pin_count = from_union([from_int, from_none], obj.get("pin_count"))
        pinned_info = from_union([PinnedInfo.from_dict, from_none], obj.get("pinned_info"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return PinAddedEvent(type, user, channel_id, item, item_user, pin_count, pinned_info, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user"] = from_union([from_str, from_none], self.user)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["item"] = from_union([lambda x: to_class(Item, x), from_none], self.item)
        result["item_user"] = from_union([from_str, from_none], self.item_user)
        result["pin_count"] = from_union([from_int, from_none], self.pin_count)
        result["pinned_info"] = from_union([lambda x: to_class(PinnedInfo, x), from_none], self.pinned_info)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


def pin_added_event_from_dict(s: Any) -> PinAddedEvent:
    return PinAddedEvent.from_dict(s)


def pin_added_event_to_dict(x: PinAddedEvent) -> Any:
    return to_class(PinAddedEvent, x)

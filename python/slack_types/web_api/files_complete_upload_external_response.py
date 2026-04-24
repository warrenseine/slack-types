# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = files_complete_upload_external_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, Dict, TypeVar, Callable, Type, cast


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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Public:
    reply_users: Optional[List[str]] = None
    reply_users_count: Optional[int] = None
    reply_count: Optional[int] = None
    ts: Optional[str] = None
    channel_name: Optional[str] = None
    team_id: Optional[str] = None
    share_user_id: Optional[str] = None
    thread_ts: Optional[str] = None
    latest_reply: Optional[str] = None
    source: Optional[str] = None
    is_silent_share: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Public':
        assert isinstance(obj, dict)
        reply_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("reply_users"))
        reply_users_count = from_union([from_int, from_none], obj.get("reply_users_count"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        channel_name = from_union([from_str, from_none], obj.get("channel_name"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        share_user_id = from_union([from_str, from_none], obj.get("share_user_id"))
        thread_ts = from_union([from_str, from_none], obj.get("thread_ts"))
        latest_reply = from_union([from_str, from_none], obj.get("latest_reply"))
        source = from_union([from_str, from_none], obj.get("source"))
        is_silent_share = from_union([from_bool, from_none], obj.get("is_silent_share"))
        return Public(reply_users, reply_users_count, reply_count, ts, channel_name, team_id, share_user_id, thread_ts, latest_reply, source, is_silent_share)

    def to_dict(self) -> dict:
        result: dict = {}
        result["reply_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.reply_users)
        result["reply_users_count"] = from_union([from_int, from_none], self.reply_users_count)
        result["reply_count"] = from_union([from_int, from_none], self.reply_count)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["channel_name"] = from_union([from_str, from_none], self.channel_name)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["share_user_id"] = from_union([from_str, from_none], self.share_user_id)
        result["thread_ts"] = from_union([from_str, from_none], self.thread_ts)
        result["latest_reply"] = from_union([from_str, from_none], self.latest_reply)
        result["source"] = from_union([from_str, from_none], self.source)
        result["is_silent_share"] = from_union([from_bool, from_none], self.is_silent_share)
        return result


@dataclass
class Shares:
    public: Optional[Dict[str, List[Public]]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Shares':
        assert isinstance(obj, dict)
        public = from_union([lambda x: from_dict(lambda x: from_list(Public.from_dict, x), x), from_none], obj.get("public"))
        return Shares(public)

    def to_dict(self) -> dict:
        result: dict = {}
        result["public"] = from_union([lambda x: from_dict(lambda x: from_list(lambda x: to_class(Public, x), x), x), from_none], self.public)
        return result


@dataclass
class File:
    id: Optional[str] = None
    title: Optional[str] = None
    created: Optional[int] = None
    timestamp: Optional[int] = None
    name: Optional[str] = None
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
    url_private: Optional[str] = None
    url_private_download: Optional[str] = None
    permalink: Optional[str] = None
    permalink_public: Optional[str] = None
    edit_link: Optional[str] = None
    preview: Optional[str] = None
    preview_highlight: Optional[str] = None
    lines: Optional[int] = None
    lines_more: Optional[int] = None
    preview_is_truncated: Optional[bool] = None
    comments_count: Optional[int] = None
    is_starred: Optional[bool] = None
    shares: Optional[Shares] = None
    channels: Optional[List[str]] = None
    groups: Optional[List[str]] = None
    ims: Optional[List[str]] = None
    has_more_shares: Optional[bool] = None
    has_rich_preview: Optional[bool] = None
    file_access: Optional[str] = None
    media_display_type: Optional[str] = None
    thumb_64: Optional[str] = None
    thumb_80: Optional[str] = None
    thumb_360: Optional[str] = None
    thumb_360__w: Optional[int] = None
    thumb_360__h: Optional[int] = None
    thumb_160: Optional[str] = None
    original_w: Optional[int] = None
    original_h: Optional[int] = None
    thumb_tiny: Optional[str] = None
    alt_txt: Optional[str] = None
    thumb_480: Optional[str] = None
    thumb_480__w: Optional[int] = None
    thumb_480__h: Optional[int] = None
    thumb_360__gif: Optional[str] = None
    thumb_480__gif: Optional[str] = None
    deanimate: Optional[str] = None
    deanimate_gif: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'File':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        created = from_union([from_int, from_none], obj.get("created"))
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        name = from_union([from_str, from_none], obj.get("name"))
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
        url_private = from_union([from_str, from_none], obj.get("url_private"))
        url_private_download = from_union([from_str, from_none], obj.get("url_private_download"))
        permalink = from_union([from_str, from_none], obj.get("permalink"))
        permalink_public = from_union([from_str, from_none], obj.get("permalink_public"))
        edit_link = from_union([from_str, from_none], obj.get("edit_link"))
        preview = from_union([from_str, from_none], obj.get("preview"))
        preview_highlight = from_union([from_str, from_none], obj.get("preview_highlight"))
        lines = from_union([from_int, from_none], obj.get("lines"))
        lines_more = from_union([from_int, from_none], obj.get("lines_more"))
        preview_is_truncated = from_union([from_bool, from_none], obj.get("preview_is_truncated"))
        comments_count = from_union([from_int, from_none], obj.get("comments_count"))
        is_starred = from_union([from_bool, from_none], obj.get("is_starred"))
        shares = from_union([Shares.from_dict, from_none], obj.get("shares"))
        channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channels"))
        groups = from_union([lambda x: from_list(from_str, x), from_none], obj.get("groups"))
        ims = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ims"))
        has_more_shares = from_union([from_bool, from_none], obj.get("has_more_shares"))
        has_rich_preview = from_union([from_bool, from_none], obj.get("has_rich_preview"))
        file_access = from_union([from_str, from_none], obj.get("file_access"))
        media_display_type = from_union([from_str, from_none], obj.get("media_display_type"))
        thumb_64 = from_union([from_str, from_none], obj.get("thumb_64"))
        thumb_80 = from_union([from_str, from_none], obj.get("thumb_80"))
        thumb_360 = from_union([from_str, from_none], obj.get("thumb_360"))
        thumb_360__w = from_union([from_int, from_none], obj.get("thumb_360_w"))
        thumb_360__h = from_union([from_int, from_none], obj.get("thumb_360_h"))
        thumb_160 = from_union([from_str, from_none], obj.get("thumb_160"))
        original_w = from_union([from_int, from_none], obj.get("original_w"))
        original_h = from_union([from_int, from_none], obj.get("original_h"))
        thumb_tiny = from_union([from_str, from_none], obj.get("thumb_tiny"))
        alt_txt = from_union([from_str, from_none], obj.get("alt_txt"))
        thumb_480 = from_union([from_str, from_none], obj.get("thumb_480"))
        thumb_480__w = from_union([from_int, from_none], obj.get("thumb_480_w"))
        thumb_480__h = from_union([from_int, from_none], obj.get("thumb_480_h"))
        thumb_360__gif = from_union([from_str, from_none], obj.get("thumb_360_gif"))
        thumb_480__gif = from_union([from_str, from_none], obj.get("thumb_480_gif"))
        deanimate = from_union([from_str, from_none], obj.get("deanimate"))
        deanimate_gif = from_union([from_str, from_none], obj.get("deanimate_gif"))
        return File(id, title, created, timestamp, name, mimetype, filetype, pretty_type, user, user_team, editable, size, mode, is_external, external_type, is_public, public_url_shared, display_as_bot, username, url_private, url_private_download, permalink, permalink_public, edit_link, preview, preview_highlight, lines, lines_more, preview_is_truncated, comments_count, is_starred, shares, channels, groups, ims, has_more_shares, has_rich_preview, file_access, media_display_type, thumb_64, thumb_80, thumb_360, thumb_360__w, thumb_360__h, thumb_160, original_w, original_h, thumb_tiny, alt_txt, thumb_480, thumb_480__w, thumb_480__h, thumb_360__gif, thumb_480__gif, deanimate, deanimate_gif)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["created"] = from_union([from_int, from_none], self.created)
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        result["name"] = from_union([from_str, from_none], self.name)
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
        result["url_private"] = from_union([from_str, from_none], self.url_private)
        result["url_private_download"] = from_union([from_str, from_none], self.url_private_download)
        result["permalink"] = from_union([from_str, from_none], self.permalink)
        result["permalink_public"] = from_union([from_str, from_none], self.permalink_public)
        result["edit_link"] = from_union([from_str, from_none], self.edit_link)
        result["preview"] = from_union([from_str, from_none], self.preview)
        result["preview_highlight"] = from_union([from_str, from_none], self.preview_highlight)
        result["lines"] = from_union([from_int, from_none], self.lines)
        result["lines_more"] = from_union([from_int, from_none], self.lines_more)
        result["preview_is_truncated"] = from_union([from_bool, from_none], self.preview_is_truncated)
        result["comments_count"] = from_union([from_int, from_none], self.comments_count)
        result["is_starred"] = from_union([from_bool, from_none], self.is_starred)
        result["shares"] = from_union([lambda x: to_class(Shares, x), from_none], self.shares)
        result["channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.channels)
        result["groups"] = from_union([lambda x: from_list(from_str, x), from_none], self.groups)
        result["ims"] = from_union([lambda x: from_list(from_str, x), from_none], self.ims)
        result["has_more_shares"] = from_union([from_bool, from_none], self.has_more_shares)
        result["has_rich_preview"] = from_union([from_bool, from_none], self.has_rich_preview)
        result["file_access"] = from_union([from_str, from_none], self.file_access)
        result["media_display_type"] = from_union([from_str, from_none], self.media_display_type)
        result["thumb_64"] = from_union([from_str, from_none], self.thumb_64)
        result["thumb_80"] = from_union([from_str, from_none], self.thumb_80)
        result["thumb_360"] = from_union([from_str, from_none], self.thumb_360)
        result["thumb_360_w"] = from_union([from_int, from_none], self.thumb_360__w)
        result["thumb_360_h"] = from_union([from_int, from_none], self.thumb_360__h)
        result["thumb_160"] = from_union([from_str, from_none], self.thumb_160)
        result["original_w"] = from_union([from_int, from_none], self.original_w)
        result["original_h"] = from_union([from_int, from_none], self.original_h)
        result["thumb_tiny"] = from_union([from_str, from_none], self.thumb_tiny)
        result["alt_txt"] = from_union([from_str, from_none], self.alt_txt)
        result["thumb_480"] = from_union([from_str, from_none], self.thumb_480)
        result["thumb_480_w"] = from_union([from_int, from_none], self.thumb_480__w)
        result["thumb_480_h"] = from_union([from_int, from_none], self.thumb_480__h)
        result["thumb_360_gif"] = from_union([from_str, from_none], self.thumb_360__gif)
        result["thumb_480_gif"] = from_union([from_str, from_none], self.thumb_480__gif)
        result["deanimate"] = from_union([from_str, from_none], self.deanimate)
        result["deanimate_gif"] = from_union([from_str, from_none], self.deanimate_gif)
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
class FilesCompleteUploadExternalResponse:
    ok: Optional[bool] = None
    files: Optional[List[File]] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FilesCompleteUploadExternalResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        files = from_union([lambda x: from_list(File.from_dict, x), from_none], obj.get("files"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return FilesCompleteUploadExternalResponse(ok, files, error, needed, provided, response_metadata, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["files"] = from_union([lambda x: from_list(lambda x: to_class(File, x), x), from_none], self.files)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def files_complete_upload_external_response_from_dict(s: Any) -> FilesCompleteUploadExternalResponse:
    return FilesCompleteUploadExternalResponse.from_dict(s)


def files_complete_upload_external_response_to_dict(x: FilesCompleteUploadExternalResponse) -> Any:
    return to_class(FilesCompleteUploadExternalResponse, x)

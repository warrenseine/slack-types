# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = conversations_list_response_from_dict(json.loads(json_string))

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


@dataclass
class Canvas:
    file_id: Optional[str] = None
    is_empty: Optional[bool] = None
    quip_thread_id: Optional[str] = None
    is_migrated: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Canvas':
        assert isinstance(obj, dict)
        file_id = from_union([from_str, from_none], obj.get("file_id"))
        is_empty = from_union([from_bool, from_none], obj.get("is_empty"))
        quip_thread_id = from_union([from_str, from_none], obj.get("quip_thread_id"))
        is_migrated = from_union([from_bool, from_none], obj.get("is_migrated"))
        return Canvas(file_id, is_empty, quip_thread_id, is_migrated)

    def to_dict(self) -> dict:
        result: dict = {}
        result["file_id"] = from_union([from_str, from_none], self.file_id)
        result["is_empty"] = from_union([from_bool, from_none], self.is_empty)
        result["quip_thread_id"] = from_union([from_str, from_none], self.quip_thread_id)
        result["is_migrated"] = from_union([from_bool, from_none], self.is_migrated)
        return result


@dataclass
class ChannelWorkflow:
    workflow_trigger_id: Optional[str] = None
    title: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ChannelWorkflow':
        assert isinstance(obj, dict)
        workflow_trigger_id = from_union([from_str, from_none], obj.get("workflow_trigger_id"))
        title = from_union([from_str, from_none], obj.get("title"))
        return ChannelWorkflow(workflow_trigger_id, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["workflow_trigger_id"] = from_union([from_str, from_none], self.workflow_trigger_id)
        result["title"] = from_union([from_str, from_none], self.title)
        return result


@dataclass
class MeetingNotes:
    file_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MeetingNotes':
        assert isinstance(obj, dict)
        file_id = from_union([from_str, from_none], obj.get("file_id"))
        return MeetingNotes(file_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["file_id"] = from_union([from_str, from_none], self.file_id)
        return result


@dataclass
class RestrictedTo:
    type: Optional[List[str]] = None
    user: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RestrictedTo':
        assert isinstance(obj, dict)
        type = from_union([lambda x: from_list(from_str, x), from_none], obj.get("type"))
        user = from_union([lambda x: from_list(from_str, x), from_none], obj.get("user"))
        return RestrictedTo(type, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: from_list(from_str, x), from_none], self.type)
        result["user"] = from_union([lambda x: from_list(from_str, x), from_none], self.user)
        return result


@dataclass
class Data:
    file_id: Optional[str] = None
    shared_ts: Optional[str] = None
    folder_bookmark_id: Optional[str] = None
    mute_edit_updates: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        file_id = from_union([from_str, from_none], obj.get("file_id"))
        shared_ts = from_union([from_str, from_none], obj.get("shared_ts"))
        folder_bookmark_id = from_union([from_str, from_none], obj.get("folder_bookmark_id"))
        mute_edit_updates = from_union([from_bool, from_none], obj.get("mute_edit_updates"))
        return Data(file_id, shared_ts, folder_bookmark_id, mute_edit_updates)

    def to_dict(self) -> dict:
        result: dict = {}
        result["file_id"] = from_union([from_str, from_none], self.file_id)
        result["shared_ts"] = from_union([from_str, from_none], self.shared_ts)
        result["folder_bookmark_id"] = from_union([from_str, from_none], self.folder_bookmark_id)
        result["mute_edit_updates"] = from_union([from_bool, from_none], self.mute_edit_updates)
        return result


@dataclass
class Tab:
    id: Optional[str] = None
    label: Optional[str] = None
    type: Optional[str] = None
    data: Optional[Data] = None
    is_disabled: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Tab':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        label = from_union([from_str, from_none], obj.get("label"))
        type = from_union([from_str, from_none], obj.get("type"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        is_disabled = from_union([from_bool, from_none], obj.get("is_disabled"))
        return Tab(id, label, type, data, is_disabled)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["label"] = from_union([from_str, from_none], self.label)
        result["type"] = from_union([from_str, from_none], self.type)
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        result["is_disabled"] = from_union([from_bool, from_none], self.is_disabled)
        return result


@dataclass
class Properties:
    posting_restricted_to: Optional[RestrictedTo] = None
    threads_restricted_to: Optional[RestrictedTo] = None
    canvas: Optional[Canvas] = None
    tabs: Optional[List[Tab]] = None
    tabz: Optional[List[Tab]] = None
    meeting_notes: Optional[MeetingNotes] = None
    is_dormant: Optional[bool] = None
    use_case: Optional[str] = None
    channel_workflows: Optional[List[ChannelWorkflow]] = None
    has_slack_connect_invite_created: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Properties':
        assert isinstance(obj, dict)
        posting_restricted_to = from_union([RestrictedTo.from_dict, from_none], obj.get("posting_restricted_to"))
        threads_restricted_to = from_union([RestrictedTo.from_dict, from_none], obj.get("threads_restricted_to"))
        canvas = from_union([Canvas.from_dict, from_none], obj.get("canvas"))
        tabs = from_union([lambda x: from_list(Tab.from_dict, x), from_none], obj.get("tabs"))
        tabz = from_union([lambda x: from_list(Tab.from_dict, x), from_none], obj.get("tabz"))
        meeting_notes = from_union([MeetingNotes.from_dict, from_none], obj.get("meeting_notes"))
        is_dormant = from_union([from_bool, from_none], obj.get("is_dormant"))
        use_case = from_union([from_str, from_none], obj.get("use_case"))
        channel_workflows = from_union([lambda x: from_list(ChannelWorkflow.from_dict, x), from_none], obj.get("channel_workflows"))
        has_slack_connect_invite_created = from_union([from_bool, from_none], obj.get("has_slack_connect_invite_created"))
        return Properties(posting_restricted_to, threads_restricted_to, canvas, tabs, tabz, meeting_notes, is_dormant, use_case, channel_workflows, has_slack_connect_invite_created)

    def to_dict(self) -> dict:
        result: dict = {}
        result["posting_restricted_to"] = from_union([lambda x: to_class(RestrictedTo, x), from_none], self.posting_restricted_to)
        result["threads_restricted_to"] = from_union([lambda x: to_class(RestrictedTo, x), from_none], self.threads_restricted_to)
        result["canvas"] = from_union([lambda x: to_class(Canvas, x), from_none], self.canvas)
        result["tabs"] = from_union([lambda x: from_list(lambda x: to_class(Tab, x), x), from_none], self.tabs)
        result["tabz"] = from_union([lambda x: from_list(lambda x: to_class(Tab, x), x), from_none], self.tabz)
        result["meeting_notes"] = from_union([lambda x: to_class(MeetingNotes, x), from_none], self.meeting_notes)
        result["is_dormant"] = from_union([from_bool, from_none], self.is_dormant)
        result["use_case"] = from_union([from_str, from_none], self.use_case)
        result["channel_workflows"] = from_union([lambda x: from_list(lambda x: to_class(ChannelWorkflow, x), x), from_none], self.channel_workflows)
        result["has_slack_connect_invite_created"] = from_union([from_bool, from_none], self.has_slack_connect_invite_created)
        return result


@dataclass
class Purpose:
    value: Optional[str] = None
    creator: Optional[str] = None
    last_set: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Purpose':
        assert isinstance(obj, dict)
        value = from_union([from_str, from_none], obj.get("value"))
        creator = from_union([from_str, from_none], obj.get("creator"))
        last_set = from_union([from_int, from_none], obj.get("last_set"))
        return Purpose(value, creator, last_set)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_str, from_none], self.value)
        result["creator"] = from_union([from_str, from_none], self.creator)
        result["last_set"] = from_union([from_int, from_none], self.last_set)
        return result


@dataclass
class Channel:
    id: Optional[str] = None
    created: Optional[int] = None
    is_archived: Optional[bool] = None
    is_im: Optional[bool] = None
    is_org_shared: Optional[bool] = None
    user: Optional[str] = None
    is_user_deleted: Optional[bool] = None
    priority: Optional[int] = None
    name: Optional[str] = None
    is_channel: Optional[bool] = None
    is_group: Optional[bool] = None
    is_mpim: Optional[bool] = None
    is_private: Optional[bool] = None
    is_general: Optional[bool] = None
    unlinked: Optional[int] = None
    name_normalized: Optional[str] = None
    is_shared: Optional[bool] = None
    is_pending_ext_shared: Optional[bool] = None
    pending_shared: Optional[List[str]] = None
    creator: Optional[str] = None
    is_ext_shared: Optional[bool] = None
    shared_team_ids: Optional[List[str]] = None
    pending_connected_team_ids: Optional[List[str]] = None
    is_member: Optional[bool] = None
    topic: Optional[Purpose] = None
    purpose: Optional[Purpose] = None
    previous_names: Optional[List[str]] = None
    num_members: Optional[int] = None
    is_moved: Optional[int] = None
    is_global_shared: Optional[bool] = None
    is_org_default: Optional[bool] = None
    is_org_mandatory: Optional[bool] = None
    conversation_host_id: Optional[str] = None
    internal_team_ids: Optional[List[str]] = None
    context_team_id: Optional[str] = None
    updated: Optional[int] = None
    properties: Optional[Properties] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        created = from_union([from_int, from_none], obj.get("created"))
        is_archived = from_union([from_bool, from_none], obj.get("is_archived"))
        is_im = from_union([from_bool, from_none], obj.get("is_im"))
        is_org_shared = from_union([from_bool, from_none], obj.get("is_org_shared"))
        user = from_union([from_str, from_none], obj.get("user"))
        is_user_deleted = from_union([from_bool, from_none], obj.get("is_user_deleted"))
        priority = from_union([from_int, from_none], obj.get("priority"))
        name = from_union([from_str, from_none], obj.get("name"))
        is_channel = from_union([from_bool, from_none], obj.get("is_channel"))
        is_group = from_union([from_bool, from_none], obj.get("is_group"))
        is_mpim = from_union([from_bool, from_none], obj.get("is_mpim"))
        is_private = from_union([from_bool, from_none], obj.get("is_private"))
        is_general = from_union([from_bool, from_none], obj.get("is_general"))
        unlinked = from_union([from_int, from_none], obj.get("unlinked"))
        name_normalized = from_union([from_str, from_none], obj.get("name_normalized"))
        is_shared = from_union([from_bool, from_none], obj.get("is_shared"))
        is_pending_ext_shared = from_union([from_bool, from_none], obj.get("is_pending_ext_shared"))
        pending_shared = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pending_shared"))
        creator = from_union([from_str, from_none], obj.get("creator"))
        is_ext_shared = from_union([from_bool, from_none], obj.get("is_ext_shared"))
        shared_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("shared_team_ids"))
        pending_connected_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pending_connected_team_ids"))
        is_member = from_union([from_bool, from_none], obj.get("is_member"))
        topic = from_union([Purpose.from_dict, from_none], obj.get("topic"))
        purpose = from_union([Purpose.from_dict, from_none], obj.get("purpose"))
        previous_names = from_union([lambda x: from_list(from_str, x), from_none], obj.get("previous_names"))
        num_members = from_union([from_int, from_none], obj.get("num_members"))
        is_moved = from_union([from_int, from_none], obj.get("is_moved"))
        is_global_shared = from_union([from_bool, from_none], obj.get("is_global_shared"))
        is_org_default = from_union([from_bool, from_none], obj.get("is_org_default"))
        is_org_mandatory = from_union([from_bool, from_none], obj.get("is_org_mandatory"))
        conversation_host_id = from_union([from_str, from_none], obj.get("conversation_host_id"))
        internal_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("internal_team_ids"))
        context_team_id = from_union([from_str, from_none], obj.get("context_team_id"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        properties = from_union([Properties.from_dict, from_none], obj.get("properties"))
        return Channel(id, created, is_archived, is_im, is_org_shared, user, is_user_deleted, priority, name, is_channel, is_group, is_mpim, is_private, is_general, unlinked, name_normalized, is_shared, is_pending_ext_shared, pending_shared, creator, is_ext_shared, shared_team_ids, pending_connected_team_ids, is_member, topic, purpose, previous_names, num_members, is_moved, is_global_shared, is_org_default, is_org_mandatory, conversation_host_id, internal_team_ids, context_team_id, updated, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["created"] = from_union([from_int, from_none], self.created)
        result["is_archived"] = from_union([from_bool, from_none], self.is_archived)
        result["is_im"] = from_union([from_bool, from_none], self.is_im)
        result["is_org_shared"] = from_union([from_bool, from_none], self.is_org_shared)
        result["user"] = from_union([from_str, from_none], self.user)
        result["is_user_deleted"] = from_union([from_bool, from_none], self.is_user_deleted)
        result["priority"] = from_union([from_int, from_none], self.priority)
        result["name"] = from_union([from_str, from_none], self.name)
        result["is_channel"] = from_union([from_bool, from_none], self.is_channel)
        result["is_group"] = from_union([from_bool, from_none], self.is_group)
        result["is_mpim"] = from_union([from_bool, from_none], self.is_mpim)
        result["is_private"] = from_union([from_bool, from_none], self.is_private)
        result["is_general"] = from_union([from_bool, from_none], self.is_general)
        result["unlinked"] = from_union([from_int, from_none], self.unlinked)
        result["name_normalized"] = from_union([from_str, from_none], self.name_normalized)
        result["is_shared"] = from_union([from_bool, from_none], self.is_shared)
        result["is_pending_ext_shared"] = from_union([from_bool, from_none], self.is_pending_ext_shared)
        result["pending_shared"] = from_union([lambda x: from_list(from_str, x), from_none], self.pending_shared)
        result["creator"] = from_union([from_str, from_none], self.creator)
        result["is_ext_shared"] = from_union([from_bool, from_none], self.is_ext_shared)
        result["shared_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.shared_team_ids)
        result["pending_connected_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.pending_connected_team_ids)
        result["is_member"] = from_union([from_bool, from_none], self.is_member)
        result["topic"] = from_union([lambda x: to_class(Purpose, x), from_none], self.topic)
        result["purpose"] = from_union([lambda x: to_class(Purpose, x), from_none], self.purpose)
        result["previous_names"] = from_union([lambda x: from_list(from_str, x), from_none], self.previous_names)
        result["num_members"] = from_union([from_int, from_none], self.num_members)
        result["is_moved"] = from_union([from_int, from_none], self.is_moved)
        result["is_global_shared"] = from_union([from_bool, from_none], self.is_global_shared)
        result["is_org_default"] = from_union([from_bool, from_none], self.is_org_default)
        result["is_org_mandatory"] = from_union([from_bool, from_none], self.is_org_mandatory)
        result["conversation_host_id"] = from_union([from_str, from_none], self.conversation_host_id)
        result["internal_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.internal_team_ids)
        result["context_team_id"] = from_union([from_str, from_none], self.context_team_id)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["properties"] = from_union([lambda x: to_class(Properties, x), from_none], self.properties)
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
class ConversationsListResponse:
    ok: Optional[bool] = None
    channels: Optional[List[Channel]] = None
    response_metadata: Optional[ResponseMetadata] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    arg: Optional[str] = None
    callstack: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ConversationsListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        channels = from_union([lambda x: from_list(Channel.from_dict, x), from_none], obj.get("channels"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        arg = from_union([from_str, from_none], obj.get("arg"))
        callstack = from_union([from_str, from_none], obj.get("callstack"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return ConversationsListResponse(ok, channels, response_metadata, error, needed, provided, arg, callstack, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["channels"] = from_union([lambda x: from_list(lambda x: to_class(Channel, x), x), from_none], self.channels)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["arg"] = from_union([from_str, from_none], self.arg)
        result["callstack"] = from_union([from_str, from_none], self.callstack)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def conversations_list_response_from_dict(s: Any) -> ConversationsListResponse:
    return ConversationsListResponse.from_dict(s)


def conversations_list_response_to_dict(x: ConversationsListResponse) -> Any:
    return to_class(ConversationsListResponse, x)

# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = team_external_teams_list_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, Union, TypeVar, Callable, Type, cast


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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


@dataclass
class OwnershipDetail:
    team_id: Optional[str] = None
    count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OwnershipDetail':
        assert isinstance(obj, dict)
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        count = from_union([from_int, from_none], obj.get("count"))
        return OwnershipDetail(team_id, count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["count"] = from_union([from_int, from_none], self.count)
        return result


@dataclass
class Canvas:
    total_count: Optional[int] = None
    ownership_details: Optional[List[OwnershipDetail]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Canvas':
        assert isinstance(obj, dict)
        total_count = from_union([from_int, from_none], obj.get("total_count"))
        ownership_details = from_union([lambda x: from_list(OwnershipDetail.from_dict, x), from_none], obj.get("ownership_details"))
        return Canvas(total_count, ownership_details)

    def to_dict(self) -> dict:
        result: dict = {}
        result["total_count"] = from_union([from_int, from_none], self.total_count)
        result["ownership_details"] = from_union([lambda x: from_list(lambda x: to_class(OwnershipDetail, x), x), from_none], self.ownership_details)
        return result


@dataclass
class ConnectedWorkspace:
    workspace_id: Optional[str] = None
    workspace_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ConnectedWorkspace':
        assert isinstance(obj, dict)
        workspace_id = from_union([from_str, from_none], obj.get("workspace_id"))
        workspace_name = from_union([from_str, from_none], obj.get("workspace_name"))
        return ConnectedWorkspace(workspace_id, workspace_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["workspace_id"] = from_union([from_str, from_none], self.workspace_id)
        result["workspace_name"] = from_union([from_str, from_none], self.workspace_name)
        return result


@dataclass
class AcceptScInvites:
    type: Optional[str] = None
    accept_in_workspace_ids: Optional[List[str]] = None
    invalid_workspace_ids: Optional[List[str]] = None
    use_allowed_workspaces: Optional[bool] = None
    accept_private: Optional[bool] = None
    actor: Optional[str] = None
    date_update: Optional[int] = None
    source: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AcceptScInvites':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        accept_in_workspace_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("accept_in_workspace_ids"))
        invalid_workspace_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("invalid_workspace_ids"))
        use_allowed_workspaces = from_union([from_bool, from_none], obj.get("use_allowed_workspaces"))
        accept_private = from_union([from_bool, from_none], obj.get("accept_private"))
        actor = from_union([from_str, from_none], obj.get("actor"))
        date_update = from_union([from_int, from_none], obj.get("date_update"))
        source = from_union([from_str, from_none], obj.get("source"))
        return AcceptScInvites(type, accept_in_workspace_ids, invalid_workspace_ids, use_allowed_workspaces, accept_private, actor, date_update, source)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["accept_in_workspace_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.accept_in_workspace_ids)
        result["invalid_workspace_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.invalid_workspace_ids)
        result["use_allowed_workspaces"] = from_union([from_bool, from_none], self.use_allowed_workspaces)
        result["accept_private"] = from_union([from_bool, from_none], self.accept_private)
        result["actor"] = from_union([from_str, from_none], self.actor)
        result["date_update"] = from_union([from_int, from_none], self.date_update)
        result["source"] = from_union([from_str, from_none], self.source)
        return result


@dataclass
class AllowScFileUploads:
    type: Union[bool, None, str]
    value: Optional[bool] = None
    actor: Optional[str] = None
    date_update: Optional[int] = None
    source: Optional[str] = None
    approval_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AllowScFileUploads':
        assert isinstance(obj, dict)
        type = from_union([from_bool, from_str, from_none], obj.get("type"))
        value = from_union([from_bool, from_none], obj.get("value"))
        actor = from_union([from_str, from_none], obj.get("actor"))
        date_update = from_union([from_int, from_none], obj.get("date_update"))
        source = from_union([from_str, from_none], obj.get("source"))
        approval_type = from_union([from_str, from_none], obj.get("approval_type"))
        return AllowScFileUploads(type, value, actor, date_update, source, approval_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_bool, from_str, from_none], self.type)
        result["value"] = from_union([from_bool, from_none], self.value)
        result["actor"] = from_union([from_str, from_none], self.actor)
        result["date_update"] = from_union([from_int, from_none], self.date_update)
        result["source"] = from_union([from_str, from_none], self.source)
        result["approval_type"] = from_union([from_str, from_none], self.approval_type)
        return result


@dataclass
class AllowedWorkspaces:
    type: Optional[str] = None
    team_ids: Optional[List[str]] = None
    actor: Optional[str] = None
    date_update: Optional[int] = None
    source: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AllowedWorkspaces':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("team_ids"))
        actor = from_union([from_str, from_none], obj.get("actor"))
        date_update = from_union([from_int, from_none], obj.get("date_update"))
        source = from_union([from_str, from_none], obj.get("source"))
        return AllowedWorkspaces(type, team_ids, actor, date_update, source)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.team_ids)
        result["actor"] = from_union([from_str, from_none], self.actor)
        result["date_update"] = from_union([from_int, from_none], self.date_update)
        result["source"] = from_union([from_str, from_none], self.source)
        return result


@dataclass
class ScMpdmToPrivate:
    type: Optional[str] = None
    accept_in_workspace_id: Optional[str] = None
    invalid_workspace_ids: Optional[List[str]] = None
    actor: Optional[str] = None
    date_update: Optional[int] = None
    source: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ScMpdmToPrivate':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        accept_in_workspace_id = from_union([from_str, from_none], obj.get("accept_in_workspace_id"))
        invalid_workspace_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("invalid_workspace_ids"))
        actor = from_union([from_str, from_none], obj.get("actor"))
        date_update = from_union([from_int, from_none], obj.get("date_update"))
        source = from_union([from_str, from_none], obj.get("source"))
        return ScMpdmToPrivate(type, accept_in_workspace_id, invalid_workspace_ids, actor, date_update, source)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["accept_in_workspace_id"] = from_union([from_str, from_none], self.accept_in_workspace_id)
        result["invalid_workspace_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.invalid_workspace_ids)
        result["actor"] = from_union([from_str, from_none], self.actor)
        result["date_update"] = from_union([from_int, from_none], self.date_update)
        result["source"] = from_union([from_str, from_none], self.source)
        return result


@dataclass
class ApprovalDestination:
    all_who_can_manage_shared_channels: Optional[bool] = None
    channel_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ApprovalDestination':
        assert isinstance(obj, dict)
        all_who_can_manage_shared_channels = from_union([from_bool, from_none], obj.get("all_who_can_manage_shared_channels"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        return ApprovalDestination(all_who_can_manage_shared_channels, channel_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["all_who_can_manage_shared_channels"] = from_union([from_bool, from_none], self.all_who_can_manage_shared_channels)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        return result


@dataclass
class UsergroupClude:
    id: Optional[str] = None
    team_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UsergroupClude':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        return UsergroupClude(id, team_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        return result


@dataclass
class SharedChannelInviteRequested:
    enabled: Optional[bool] = None
    usergroup_include: Optional[UsergroupClude] = None
    usergroup_exclude: Optional[UsergroupClude] = None
    approval_destination: Optional[ApprovalDestination] = None
    actor: Optional[str] = None
    date_update: Optional[int] = None
    source: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SharedChannelInviteRequested':
        assert isinstance(obj, dict)
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        usergroup_include = from_union([UsergroupClude.from_dict, from_none], obj.get("usergroup_include"))
        usergroup_exclude = from_union([UsergroupClude.from_dict, from_none], obj.get("usergroup_exclude"))
        approval_destination = from_union([ApprovalDestination.from_dict, from_none], obj.get("approval_destination"))
        actor = from_union([from_str, from_none], obj.get("actor"))
        date_update = from_union([from_int, from_none], obj.get("date_update"))
        source = from_union([from_str, from_none], obj.get("source"))
        return SharedChannelInviteRequested(enabled, usergroup_include, usergroup_exclude, approval_destination, actor, date_update, source)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enabled"] = from_union([from_bool, from_none], self.enabled)
        result["usergroup_include"] = from_union([lambda x: to_class(UsergroupClude, x), from_none], self.usergroup_include)
        result["usergroup_exclude"] = from_union([lambda x: to_class(UsergroupClude, x), from_none], self.usergroup_exclude)
        result["approval_destination"] = from_union([lambda x: to_class(ApprovalDestination, x), from_none], self.approval_destination)
        result["actor"] = from_union([from_str, from_none], self.actor)
        result["date_update"] = from_union([from_int, from_none], self.date_update)
        result["source"] = from_union([from_str, from_none], self.source)
        return result


@dataclass
class SlackConnectPrefs:
    allow_sc_file_uploads: Optional[AllowScFileUploads] = None
    approved_org_info: Optional[AllowScFileUploads] = None
    profile_visibility: Optional[AllowScFileUploads] = None
    allowed_workspaces: Optional[AllowedWorkspaces] = None
    allowed_canvas_sharing: Optional[AllowScFileUploads] = None
    allowed_list_sharing: Optional[AllowScFileUploads] = None
    away_team_sc_invite_permissions: Optional[AllowedWorkspaces] = None
    away_team_sc_invite_require_2_fa: Optional[AllowScFileUploads] = None
    accept_sc_invites: Optional[AcceptScInvites] = None
    sc_channel_limited_access: Optional[AllowScFileUploads] = None
    sc_mpdm_to_private: Optional[ScMpdmToPrivate] = None
    external_awareness_context_bar: Optional[AllowScFileUploads] = None
    require_sc_channel_for_sc_dm: Optional[AllowScFileUploads] = None
    shared_channel_invite_requested: Optional[SharedChannelInviteRequested] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SlackConnectPrefs':
        assert isinstance(obj, dict)
        allow_sc_file_uploads = from_union([AllowScFileUploads.from_dict, from_none], obj.get("allow_sc_file_uploads"))
        approved_org_info = from_union([AllowScFileUploads.from_dict, from_none], obj.get("approved_org_info"))
        profile_visibility = from_union([AllowScFileUploads.from_dict, from_none], obj.get("profile_visibility"))
        allowed_workspaces = from_union([AllowedWorkspaces.from_dict, from_none], obj.get("allowed_workspaces"))
        allowed_canvas_sharing = from_union([AllowScFileUploads.from_dict, from_none], obj.get("allowed_canvas_sharing"))
        allowed_list_sharing = from_union([AllowScFileUploads.from_dict, from_none], obj.get("allowed_list_sharing"))
        away_team_sc_invite_permissions = from_union([AllowedWorkspaces.from_dict, from_none], obj.get("away_team_sc_invite_permissions"))
        away_team_sc_invite_require_2_fa = from_union([AllowScFileUploads.from_dict, from_none], obj.get("away_team_sc_invite_require_2fa"))
        accept_sc_invites = from_union([AcceptScInvites.from_dict, from_none], obj.get("accept_sc_invites"))
        sc_channel_limited_access = from_union([AllowScFileUploads.from_dict, from_none], obj.get("sc_channel_limited_access"))
        sc_mpdm_to_private = from_union([ScMpdmToPrivate.from_dict, from_none], obj.get("sc_mpdm_to_private"))
        external_awareness_context_bar = from_union([AllowScFileUploads.from_dict, from_none], obj.get("external_awareness_context_bar"))
        require_sc_channel_for_sc_dm = from_union([AllowScFileUploads.from_dict, from_none], obj.get("require_sc_channel_for_sc_dm"))
        shared_channel_invite_requested = from_union([SharedChannelInviteRequested.from_dict, from_none], obj.get("shared_channel_invite_requested"))
        return SlackConnectPrefs(allow_sc_file_uploads, approved_org_info, profile_visibility, allowed_workspaces, allowed_canvas_sharing, allowed_list_sharing, away_team_sc_invite_permissions, away_team_sc_invite_require_2_fa, accept_sc_invites, sc_channel_limited_access, sc_mpdm_to_private, external_awareness_context_bar, require_sc_channel_for_sc_dm, shared_channel_invite_requested)

    def to_dict(self) -> dict:
        result: dict = {}
        result["allow_sc_file_uploads"] = from_union([lambda x: to_class(AllowScFileUploads, x), from_none], self.allow_sc_file_uploads)
        result["approved_org_info"] = from_union([lambda x: to_class(AllowScFileUploads, x), from_none], self.approved_org_info)
        result["profile_visibility"] = from_union([lambda x: to_class(AllowScFileUploads, x), from_none], self.profile_visibility)
        result["allowed_workspaces"] = from_union([lambda x: to_class(AllowedWorkspaces, x), from_none], self.allowed_workspaces)
        result["allowed_canvas_sharing"] = from_union([lambda x: to_class(AllowScFileUploads, x), from_none], self.allowed_canvas_sharing)
        result["allowed_list_sharing"] = from_union([lambda x: to_class(AllowScFileUploads, x), from_none], self.allowed_list_sharing)
        result["away_team_sc_invite_permissions"] = from_union([lambda x: to_class(AllowedWorkspaces, x), from_none], self.away_team_sc_invite_permissions)
        result["away_team_sc_invite_require_2fa"] = from_union([lambda x: to_class(AllowScFileUploads, x), from_none], self.away_team_sc_invite_require_2_fa)
        result["accept_sc_invites"] = from_union([lambda x: to_class(AcceptScInvites, x), from_none], self.accept_sc_invites)
        result["sc_channel_limited_access"] = from_union([lambda x: to_class(AllowScFileUploads, x), from_none], self.sc_channel_limited_access)
        result["sc_mpdm_to_private"] = from_union([lambda x: to_class(ScMpdmToPrivate, x), from_none], self.sc_mpdm_to_private)
        result["external_awareness_context_bar"] = from_union([lambda x: to_class(AllowScFileUploads, x), from_none], self.external_awareness_context_bar)
        result["require_sc_channel_for_sc_dm"] = from_union([lambda x: to_class(AllowScFileUploads, x), from_none], self.require_sc_channel_for_sc_dm)
        result["shared_channel_invite_requested"] = from_union([lambda x: to_class(SharedChannelInviteRequested, x), from_none], self.shared_channel_invite_requested)
        return result


@dataclass
class Organization:
    team_id: Optional[str] = None
    team_name: Optional[str] = None
    team_domain: Optional[str] = None
    public_channel_count: Optional[int] = None
    private_channel_count: Optional[int] = None
    im_channel_count: Optional[int] = None
    mpim_channel_count: Optional[int] = None
    connected_workspaces: Optional[List[ConnectedWorkspace]] = None
    slack_connect_prefs: Optional[SlackConnectPrefs] = None
    connection_status: Optional[str] = None
    last_active_timestamp: Optional[int] = None
    is_sponsored: Optional[bool] = None
    canvas: Optional[Canvas] = None
    lists: Optional[Canvas] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Organization':
        assert isinstance(obj, dict)
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        team_name = from_union([from_str, from_none], obj.get("team_name"))
        team_domain = from_union([from_str, from_none], obj.get("team_domain"))
        public_channel_count = from_union([from_int, from_none], obj.get("public_channel_count"))
        private_channel_count = from_union([from_int, from_none], obj.get("private_channel_count"))
        im_channel_count = from_union([from_int, from_none], obj.get("im_channel_count"))
        mpim_channel_count = from_union([from_int, from_none], obj.get("mpim_channel_count"))
        connected_workspaces = from_union([lambda x: from_list(ConnectedWorkspace.from_dict, x), from_none], obj.get("connected_workspaces"))
        slack_connect_prefs = from_union([SlackConnectPrefs.from_dict, from_none], obj.get("slack_connect_prefs"))
        connection_status = from_union([from_str, from_none], obj.get("connection_status"))
        last_active_timestamp = from_union([from_int, from_none], obj.get("last_active_timestamp"))
        is_sponsored = from_union([from_bool, from_none], obj.get("is_sponsored"))
        canvas = from_union([Canvas.from_dict, from_none], obj.get("canvas"))
        lists = from_union([Canvas.from_dict, from_none], obj.get("lists"))
        return Organization(team_id, team_name, team_domain, public_channel_count, private_channel_count, im_channel_count, mpim_channel_count, connected_workspaces, slack_connect_prefs, connection_status, last_active_timestamp, is_sponsored, canvas, lists)

    def to_dict(self) -> dict:
        result: dict = {}
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["team_name"] = from_union([from_str, from_none], self.team_name)
        result["team_domain"] = from_union([from_str, from_none], self.team_domain)
        result["public_channel_count"] = from_union([from_int, from_none], self.public_channel_count)
        result["private_channel_count"] = from_union([from_int, from_none], self.private_channel_count)
        result["im_channel_count"] = from_union([from_int, from_none], self.im_channel_count)
        result["mpim_channel_count"] = from_union([from_int, from_none], self.mpim_channel_count)
        result["connected_workspaces"] = from_union([lambda x: from_list(lambda x: to_class(ConnectedWorkspace, x), x), from_none], self.connected_workspaces)
        result["slack_connect_prefs"] = from_union([lambda x: to_class(SlackConnectPrefs, x), from_none], self.slack_connect_prefs)
        result["connection_status"] = from_union([from_str, from_none], self.connection_status)
        result["last_active_timestamp"] = from_union([from_int, from_none], self.last_active_timestamp)
        result["is_sponsored"] = from_union([from_bool, from_none], self.is_sponsored)
        result["canvas"] = from_union([lambda x: to_class(Canvas, x), from_none], self.canvas)
        result["lists"] = from_union([lambda x: to_class(Canvas, x), from_none], self.lists)
        return result


@dataclass
class ResponseMetadata:
    next_cursor: Optional[str] = None
    messages: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        next_cursor = from_union([from_str, from_none], obj.get("next_cursor"))
        messages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("messages"))
        return ResponseMetadata(next_cursor, messages)

    def to_dict(self) -> dict:
        result: dict = {}
        result["next_cursor"] = from_union([from_str, from_none], self.next_cursor)
        result["messages"] = from_union([lambda x: from_list(from_str, x), from_none], self.messages)
        return result


@dataclass
class TeamExternalTeamsListResponse:
    ok: Optional[bool] = None
    organizations: Optional[List[Organization]] = None
    total_count: Optional[int] = None
    response_metadata: Optional[ResponseMetadata] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TeamExternalTeamsListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        organizations = from_union([lambda x: from_list(Organization.from_dict, x), from_none], obj.get("organizations"))
        total_count = from_union([from_int, from_none], obj.get("total_count"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return TeamExternalTeamsListResponse(ok, organizations, total_count, response_metadata, error, needed, provided, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["organizations"] = from_union([lambda x: from_list(lambda x: to_class(Organization, x), x), from_none], self.organizations)
        result["total_count"] = from_union([from_int, from_none], self.total_count)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def team_external_teams_list_response_from_dict(s: Any) -> TeamExternalTeamsListResponse:
    return TeamExternalTeamsListResponse.from_dict(s)


def team_external_teams_list_response_to_dict(x: TeamExternalTeamsListResponse) -> Any:
    return to_class(TeamExternalTeamsListResponse, x)

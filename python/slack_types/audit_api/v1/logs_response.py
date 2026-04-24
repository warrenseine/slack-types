# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = logs_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


@dataclass
class User:
    id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    team: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        email = from_union([from_str, from_none], obj.get("email"))
        team = from_union([from_str, from_none], obj.get("team"))
        return User(id, name, email, team)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["email"] = from_union([from_str, from_none], self.email)
        result["team"] = from_union([from_str, from_none], self.team)
        return result


@dataclass
class Actor:
    type: Optional[str] = None
    user: Optional[User] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Actor':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        return Actor(type, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        return result


@dataclass
class App:
    id: Optional[str] = None
    name: Optional[str] = None
    is_distributed: Optional[bool] = None
    is_directory_approved: Optional[bool] = None
    is_workflow_app: Optional[bool] = None
    scopes: Optional[List[str]] = None
    scopes_bot: Optional[List[Any]] = None
    creator: Optional[str] = None
    team: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'App':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        is_distributed = from_union([from_bool, from_none], obj.get("is_distributed"))
        is_directory_approved = from_union([from_bool, from_none], obj.get("is_directory_approved"))
        is_workflow_app = from_union([from_bool, from_none], obj.get("is_workflow_app"))
        scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("scopes"))
        scopes_bot = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("scopes_bot"))
        creator = from_union([from_str, from_none], obj.get("creator"))
        team = from_union([from_str, from_none], obj.get("team"))
        return App(id, name, is_distributed, is_directory_approved, is_workflow_app, scopes, scopes_bot, creator, team)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["is_distributed"] = from_union([from_bool, from_none], self.is_distributed)
        result["is_directory_approved"] = from_union([from_bool, from_none], self.is_directory_approved)
        result["is_workflow_app"] = from_union([from_bool, from_none], self.is_workflow_app)
        result["scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.scopes)
        result["scopes_bot"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.scopes_bot)
        result["creator"] = from_union([from_str, from_none], self.creator)
        result["team"] = from_union([from_str, from_none], self.team)
        return result


@dataclass
class Location:
    type: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    domain: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Location':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        domain = from_union([from_str, from_none], obj.get("domain"))
        return Location(type, id, name, domain)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["domain"] = from_union([from_str, from_none], self.domain)
        return result


@dataclass
class Context:
    session_id: Optional[str] = None
    location: Optional[Location] = None
    ua: Optional[str] = None
    ip_address: Optional[str] = None
    app: Optional[App] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Context':
        assert isinstance(obj, dict)
        session_id = from_union([from_str, from_none], obj.get("session_id"))
        location = from_union([Location.from_dict, from_none], obj.get("location"))
        ua = from_union([from_str, from_none], obj.get("ua"))
        ip_address = from_union([from_str, from_none], obj.get("ip_address"))
        app = from_union([App.from_dict, from_none], obj.get("app"))
        return Context(session_id, location, ua, ip_address, app)

    def to_dict(self) -> dict:
        result: dict = {}
        result["session_id"] = from_union([from_str, from_none], self.session_id)
        result["location"] = from_union([lambda x: to_class(Location, x), from_none], self.location)
        result["ua"] = from_union([from_str, from_none], self.ua)
        result["ip_address"] = from_union([from_str, from_none], self.ip_address)
        result["app"] = from_union([lambda x: to_class(App, x), from_none], self.app)
        return result


@dataclass
class CanHuddle:
    enabled: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CanHuddle':
        assert isinstance(obj, dict)
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        return CanHuddle(enabled)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enabled"] = from_union([from_bool, from_none], self.enabled)
        return result


@dataclass
class CanThread:
    type: Optional[List[str]] = None
    user: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CanThread':
        assert isinstance(obj, dict)
        type = from_union([lambda x: from_list(from_str, x), from_none], obj.get("type"))
        user = from_union([lambda x: from_list(from_str, x), from_none], obj.get("user"))
        return CanThread(type, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: from_list(from_str, x), from_none], self.type)
        result["user"] = from_union([lambda x: from_list(from_str, x), from_none], self.user)
        return result


@dataclass
class Inviter:
    type: Optional[str] = None
    user: Optional[User] = None
    id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    team: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Inviter':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        email = from_union([from_str, from_none], obj.get("email"))
        team = from_union([from_str, from_none], obj.get("team"))
        return Inviter(type, user, id, name, email, team)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["email"] = from_union([from_str, from_none], self.email)
        result["team"] = from_union([from_str, from_none], self.team)
        return result


@dataclass
class Resolution:
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Resolution':
        assert isinstance(obj, dict)
        value = from_union([from_str, from_none], obj.get("value"))
        return Resolution(value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_str, from_none], self.value)
        return result


@dataclass
class Action:
    resolution: Optional[Resolution] = None
    notify: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Action':
        assert isinstance(obj, dict)
        resolution = from_union([Resolution.from_dict, from_none], obj.get("resolution"))
        notify = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("notify"))
        return Action(resolution, notify)

    def to_dict(self) -> dict:
        result: dict = {}
        result["resolution"] = from_union([lambda x: to_class(Resolution, x), from_none], self.resolution)
        result["notify"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.notify)
        return result


@dataclass
class Condition:
    datatype: Optional[str] = None
    operator: Optional[str] = None
    values: Optional[List[Any]] = None
    entity_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Condition':
        assert isinstance(obj, dict)
        datatype = from_union([from_str, from_none], obj.get("datatype"))
        operator = from_union([from_str, from_none], obj.get("operator"))
        values = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("values"))
        entity_type = from_union([from_str, from_none], obj.get("entity_type"))
        return Condition(datatype, operator, values, entity_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["datatype"] = from_union([from_str, from_none], self.datatype)
        result["operator"] = from_union([from_str, from_none], self.operator)
        result["values"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.values)
        result["entity_type"] = from_union([from_str, from_none], self.entity_type)
        return result


@dataclass
class MatchedRule:
    id: Optional[str] = None
    team_id: Optional[str] = None
    title: Optional[str] = None
    action: Optional[Action] = None
    condition: Optional[Condition] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MatchedRule':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        title = from_union([from_str, from_none], obj.get("title"))
        action = from_union([Action.from_dict, from_none], obj.get("action"))
        condition = from_union([Condition.from_dict, from_none], obj.get("condition"))
        return MatchedRule(id, team_id, title, action, condition)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["action"] = from_union([lambda x: to_class(Action, x), from_none], self.action)
        result["condition"] = from_union([lambda x: to_class(Condition, x), from_none], self.condition)
        return result


@dataclass
class Profile:
    real_name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    display_name: Optional[str] = None
    image_original: Optional[str] = None
    image_24: Optional[str] = None
    image_32: Optional[str] = None
    image_48: Optional[str] = None
    image_72: Optional[str] = None
    image_192: Optional[str] = None
    image_512: Optional[str] = None
    image_1024: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        assert isinstance(obj, dict)
        real_name = from_union([from_str, from_none], obj.get("real_name"))
        first_name = from_union([from_str, from_none], obj.get("first_name"))
        last_name = from_union([from_str, from_none], obj.get("last_name"))
        display_name = from_union([from_str, from_none], obj.get("display_name"))
        image_original = from_union([from_str, from_none], obj.get("image_original"))
        image_24 = from_union([from_str, from_none], obj.get("image_24"))
        image_32 = from_union([from_str, from_none], obj.get("image_32"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        image_192 = from_union([from_str, from_none], obj.get("image_192"))
        image_512 = from_union([from_str, from_none], obj.get("image_512"))
        image_1024 = from_union([from_str, from_none], obj.get("image_1024"))
        return Profile(real_name, first_name, last_name, display_name, image_original, image_24, image_32, image_48, image_72, image_192, image_512, image_1024)

    def to_dict(self) -> dict:
        result: dict = {}
        result["real_name"] = from_union([from_str, from_none], self.real_name)
        result["first_name"] = from_union([from_str, from_none], self.first_name)
        result["last_name"] = from_union([from_str, from_none], self.last_name)
        result["display_name"] = from_union([from_str, from_none], self.display_name)
        result["image_original"] = from_union([from_str, from_none], self.image_original)
        result["image_24"] = from_union([from_str, from_none], self.image_24)
        result["image_32"] = from_union([from_str, from_none], self.image_32)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        result["image_192"] = from_union([from_str, from_none], self.image_192)
        result["image_512"] = from_union([from_str, from_none], self.image_512)
        result["image_1024"] = from_union([from_str, from_none], self.image_1024)
        return result


@dataclass
class RetentionPolicy:
    type: Optional[str] = None
    duration_days: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RetentionPolicy':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        duration_days = from_union([from_int, from_none], obj.get("duration_days"))
        return RetentionPolicy(type, duration_days)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["duration_days"] = from_union([from_int, from_none], self.duration_days)
        return result


@dataclass
class Wildcard:
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Wildcard':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        return Wildcard(type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class Grant:
    type: Optional[str] = None
    resource_id: Optional[str] = None
    wildcard: Optional[Wildcard] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Grant':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        resource_id = from_union([from_str, from_none], obj.get("resource_id"))
        wildcard = from_union([Wildcard.from_dict, from_none], obj.get("wildcard"))
        return Grant(type, resource_id, wildcard)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["resource_id"] = from_union([from_str, from_none], self.resource_id)
        result["wildcard"] = from_union([lambda x: to_class(Wildcard, x), from_none], self.wildcard)
        return result


@dataclass
class Resource:
    type: Optional[str] = None
    grant: Optional[Grant] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Resource':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        grant = from_union([Grant.from_dict, from_none], obj.get("grant"))
        return Resource(type, grant)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["grant"] = from_union([lambda x: to_class(Grant, x), from_none], self.grant)
        return result


@dataclass
class Permission:
    resource: Optional[Resource] = None
    scopes: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Permission':
        assert isinstance(obj, dict)
        resource = from_union([Resource.from_dict, from_none], obj.get("resource"))
        scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("scopes"))
        return Permission(resource, scopes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["resource"] = from_union([lambda x: to_class(Resource, x), from_none], self.resource)
        result["scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.scopes)
        return result


@dataclass
class Request:
    id: Optional[str] = None
    team_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Request':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        return Request(id, team_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        return result


@dataclass
class SharedWith:
    channel_id: Optional[str] = None
    access_level: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SharedWith':
        assert isinstance(obj, dict)
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        access_level = from_union([from_str, from_none], obj.get("access_level"))
        return SharedWith(channel_id, access_level)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["access_level"] = from_union([from_str, from_none], self.access_level)
        return result


@dataclass
class SpaceFileID:
    payload: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SpaceFileID':
        assert isinstance(obj, dict)
        payload = from_union([from_str, from_none], obj.get("payload"))
        return SpaceFileID(payload)

    def to_dict(self) -> dict:
        result: dict = {}
        result["payload"] = from_union([from_str, from_none], self.payload)
        return result


@dataclass
class Details:
    type: Optional[str] = None
    app_owner_id: Optional[str] = None
    scopes: Optional[List[str]] = None
    bot_scopes: Optional[List[str]] = None
    new_scopes: Optional[List[str]] = None
    previous_scopes: Optional[List[str]] = None
    inviter: Optional[Inviter] = None
    kicker: Optional[Inviter] = None
    installer_user_id: Optional[str] = None
    approver_id: Optional[str] = None
    approval_type: Optional[str] = None
    app_previously_approved: Optional[bool] = None
    old_scopes: Optional[List[str]] = None
    name: Optional[str] = None
    bot_id: Optional[str] = None
    channels: Optional[List[str]] = None
    permissions: Optional[List[Permission]] = None
    shared_to: Optional[str] = None
    reason: Optional[str] = None
    is_internal_integration: Optional[bool] = None
    cleared_resolution: Optional[str] = None
    is_workflow: Optional[bool] = None
    mobile_only: Optional[bool] = None
    web_only: Optional[bool] = None
    non_sso_only: Optional[bool] = None
    expires_on: Optional[int] = None
    new_version_id: Optional[str] = None
    trigger: Optional[str] = None
    granular_bot_token: Optional[bool] = None
    origin_team: Optional[str] = None
    target_team: Optional[str] = None
    resolution: Optional[str] = None
    app_previously_resolved: Optional[bool] = None
    admin_app_id: Optional[str] = None
    export_type: Optional[str] = None
    export_start_ts: Optional[str] = None
    export_end_ts: Optional[str] = None
    barrier_id: Optional[str] = None
    primary_usergroup_id: Optional[str] = None
    barriered_from_usergroup_ids: Optional[List[str]] = None
    restricted_subjects: Optional[List[str]] = None
    duration: Optional[int] = None
    desktop_app_browser_quit: Optional[bool] = None
    invite_id: Optional[str] = None
    external_organization_id: Optional[str] = None
    external_organization_name: Optional[str] = None
    external_user_id: Optional[str] = None
    external_user_email: Optional[str] = None
    channel_id: Optional[str] = None
    added_team_id: Optional[str] = None
    is_token_rotation_enabled_app: Optional[bool] = None
    old_retention_policy: Optional[RetentionPolicy] = None
    new_retention_policy: Optional[RetentionPolicy] = None
    who_can_post: Optional[CanThread] = None
    can_thread: Optional[CanThread] = None
    is_external_limited: Optional[bool] = None
    exporting_team_id: Optional[int] = None
    session_search_start: Optional[int] = None
    deprecation_search_end: Optional[int] = None
    is_error: Optional[bool] = None
    app_id: Optional[str] = None
    enable_at_here: Optional[CanHuddle] = None
    enable_at_channel: Optional[CanHuddle] = None
    can_huddle: Optional[CanHuddle] = None
    url_private: Optional[str] = None
    shared_with: Optional[SharedWith] = None
    initiated_by: Optional[str] = None
    source_team: Optional[str] = None
    destination_team: Optional[str] = None
    succeeded_users: Optional[List[Any]] = None
    failed_users: Optional[List[Any]] = None
    enterprise: Optional[str] = None
    team: Optional[str] = None
    subteam: Optional[str] = None
    action: Optional[str] = None
    idp_group_member_count: Optional[int] = None
    workspace_member_count: Optional[int] = None
    added_user_count: Optional[int] = None
    added_user_error_count: Optional[int] = None
    reactivated_user_count: Optional[int] = None
    removed_user_count: Optional[int] = None
    removed_user_error_count: Optional[int] = None
    total_removal_count: Optional[int] = None
    is_flagged: Optional[str] = None
    target_user: Optional[str] = None
    target_entity: Optional[str] = None
    idp_config_id: Optional[str] = None
    config_type: Optional[str] = None
    idp_entity_id: Optional[str] = None
    idp_entity_id_hash: Optional[str] = None
    label: Optional[str] = None
    previous_profile: Optional[Profile] = None
    new_profile: Optional[Profile] = None
    target_user_id: Optional[str] = None
    space_file_id: Optional[SpaceFileID] = None
    target_entity_id: Optional[str] = None
    changed_permissions: Optional[List[Any]] = None
    datastore_name: Optional[str] = None
    attributes: Optional[List[Any]] = None
    channel: Optional[str] = None
    entity_type: Optional[str] = None
    actor: Optional[str] = None
    access_level: Optional[str] = None
    functions: Optional[List[Any]] = None
    workflows: Optional[List[Any]] = None
    datastores: Optional[List[Any]] = None
    permissions_updated: Optional[bool] = None
    matched_rule: Optional[MatchedRule] = None
    request: Optional[Request] = None
    rules_checked: Optional[List[Any]] = None
    disconnecting_team: Optional[str] = None
    is_channel_canvas: Optional[bool] = None
    linked_channel_id: Optional[str] = None
    column_id: Optional[str] = None
    row_id: Optional[str] = None
    cell_date_updated: Optional[int] = None
    view_id: Optional[str] = None
    user: Optional[str] = None
    file_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Details':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        app_owner_id = from_union([from_str, from_none], obj.get("app_owner_id"))
        scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("scopes"))
        bot_scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("bot_scopes"))
        new_scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("new_scopes"))
        previous_scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("previous_scopes"))
        inviter = from_union([Inviter.from_dict, from_none], obj.get("inviter"))
        kicker = from_union([Inviter.from_dict, from_none], obj.get("kicker"))
        installer_user_id = from_union([from_str, from_none], obj.get("installer_user_id"))
        approver_id = from_union([from_str, from_none], obj.get("approver_id"))
        approval_type = from_union([from_str, from_none], obj.get("approval_type"))
        app_previously_approved = from_union([from_bool, from_none], obj.get("app_previously_approved"))
        old_scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("old_scopes"))
        name = from_union([from_str, from_none], obj.get("name"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channels"))
        permissions = from_union([lambda x: from_list(Permission.from_dict, x), from_none], obj.get("permissions"))
        shared_to = from_union([from_str, from_none], obj.get("shared_to"))
        reason = from_union([from_str, from_none], obj.get("reason"))
        is_internal_integration = from_union([from_bool, from_none], obj.get("is_internal_integration"))
        cleared_resolution = from_union([from_str, from_none], obj.get("cleared_resolution"))
        is_workflow = from_union([from_bool, from_none], obj.get("is_workflow"))
        mobile_only = from_union([from_bool, from_none], obj.get("mobile_only"))
        web_only = from_union([from_bool, from_none], obj.get("web_only"))
        non_sso_only = from_union([from_bool, from_none], obj.get("non_sso_only"))
        expires_on = from_union([from_int, from_none], obj.get("expires_on"))
        new_version_id = from_union([from_str, from_none], obj.get("new_version_id"))
        trigger = from_union([from_str, from_none], obj.get("trigger"))
        granular_bot_token = from_union([from_bool, from_none], obj.get("granular_bot_token"))
        origin_team = from_union([from_str, from_none], obj.get("origin_team"))
        target_team = from_union([from_str, from_none], obj.get("target_team"))
        resolution = from_union([from_str, from_none], obj.get("resolution"))
        app_previously_resolved = from_union([from_bool, from_none], obj.get("app_previously_resolved"))
        admin_app_id = from_union([from_str, from_none], obj.get("admin_app_id"))
        export_type = from_union([from_str, from_none], obj.get("export_type"))
        export_start_ts = from_union([from_str, from_none], obj.get("export_start_ts"))
        export_end_ts = from_union([from_str, from_none], obj.get("export_end_ts"))
        barrier_id = from_union([from_str, from_none], obj.get("barrier_id"))
        primary_usergroup_id = from_union([from_str, from_none], obj.get("primary_usergroup_id"))
        barriered_from_usergroup_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("barriered_from_usergroup_ids"))
        restricted_subjects = from_union([lambda x: from_list(from_str, x), from_none], obj.get("restricted_subjects"))
        duration = from_union([from_int, from_none], obj.get("duration"))
        desktop_app_browser_quit = from_union([from_bool, from_none], obj.get("desktop_app_browser_quit"))
        invite_id = from_union([from_str, from_none], obj.get("invite_id"))
        external_organization_id = from_union([from_str, from_none], obj.get("external_organization_id"))
        external_organization_name = from_union([from_str, from_none], obj.get("external_organization_name"))
        external_user_id = from_union([from_str, from_none], obj.get("external_user_id"))
        external_user_email = from_union([from_str, from_none], obj.get("external_user_email"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        added_team_id = from_union([from_str, from_none], obj.get("added_team_id"))
        is_token_rotation_enabled_app = from_union([from_bool, from_none], obj.get("is_token_rotation_enabled_app"))
        old_retention_policy = from_union([RetentionPolicy.from_dict, from_none], obj.get("old_retention_policy"))
        new_retention_policy = from_union([RetentionPolicy.from_dict, from_none], obj.get("new_retention_policy"))
        who_can_post = from_union([CanThread.from_dict, from_none], obj.get("who_can_post"))
        can_thread = from_union([CanThread.from_dict, from_none], obj.get("can_thread"))
        is_external_limited = from_union([from_bool, from_none], obj.get("is_external_limited"))
        exporting_team_id = from_union([from_int, from_none], obj.get("exporting_team_id"))
        session_search_start = from_union([from_int, from_none], obj.get("session_search_start"))
        deprecation_search_end = from_union([from_int, from_none], obj.get("deprecation_search_end"))
        is_error = from_union([from_bool, from_none], obj.get("is_error"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        enable_at_here = from_union([CanHuddle.from_dict, from_none], obj.get("enable_at_here"))
        enable_at_channel = from_union([CanHuddle.from_dict, from_none], obj.get("enable_at_channel"))
        can_huddle = from_union([CanHuddle.from_dict, from_none], obj.get("can_huddle"))
        url_private = from_union([from_str, from_none], obj.get("url_private"))
        shared_with = from_union([SharedWith.from_dict, from_none], obj.get("shared_with"))
        initiated_by = from_union([from_str, from_none], obj.get("initiated_by"))
        source_team = from_union([from_str, from_none], obj.get("source_team"))
        destination_team = from_union([from_str, from_none], obj.get("destination_team"))
        succeeded_users = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("succeeded_users"))
        failed_users = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("failed_users"))
        enterprise = from_union([from_str, from_none], obj.get("enterprise"))
        team = from_union([from_str, from_none], obj.get("team"))
        subteam = from_union([from_str, from_none], obj.get("subteam"))
        action = from_union([from_str, from_none], obj.get("action"))
        idp_group_member_count = from_union([from_int, from_none], obj.get("idp_group_member_count"))
        workspace_member_count = from_union([from_int, from_none], obj.get("workspace_member_count"))
        added_user_count = from_union([from_int, from_none], obj.get("added_user_count"))
        added_user_error_count = from_union([from_int, from_none], obj.get("added_user_error_count"))
        reactivated_user_count = from_union([from_int, from_none], obj.get("reactivated_user_count"))
        removed_user_count = from_union([from_int, from_none], obj.get("removed_user_count"))
        removed_user_error_count = from_union([from_int, from_none], obj.get("removed_user_error_count"))
        total_removal_count = from_union([from_int, from_none], obj.get("total_removal_count"))
        is_flagged = from_union([from_str, from_none], obj.get("is_flagged"))
        target_user = from_union([from_str, from_none], obj.get("target_user"))
        target_entity = from_union([from_str, from_none], obj.get("target_entity"))
        idp_config_id = from_union([from_str, from_none], obj.get("idp_config_id"))
        config_type = from_union([from_str, from_none], obj.get("config_type"))
        idp_entity_id = from_union([from_str, from_none], obj.get("idp_entity_id"))
        idp_entity_id_hash = from_union([from_str, from_none], obj.get("idp_entity_id_hash"))
        label = from_union([from_str, from_none], obj.get("label"))
        previous_profile = from_union([Profile.from_dict, from_none], obj.get("previous_profile"))
        new_profile = from_union([Profile.from_dict, from_none], obj.get("new_profile"))
        target_user_id = from_union([from_str, from_none], obj.get("target_user_id"))
        space_file_id = from_union([SpaceFileID.from_dict, from_none], obj.get("space_file_id"))
        target_entity_id = from_union([from_str, from_none], obj.get("target_entity_id"))
        changed_permissions = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("changed_permissions"))
        datastore_name = from_union([from_str, from_none], obj.get("datastore_name"))
        attributes = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("attributes"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        entity_type = from_union([from_str, from_none], obj.get("entity_type"))
        actor = from_union([from_str, from_none], obj.get("actor"))
        access_level = from_union([from_str, from_none], obj.get("access_level"))
        functions = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("functions"))
        workflows = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("workflows"))
        datastores = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("datastores"))
        permissions_updated = from_union([from_bool, from_none], obj.get("permissions_updated"))
        matched_rule = from_union([MatchedRule.from_dict, from_none], obj.get("matched_rule"))
        request = from_union([Request.from_dict, from_none], obj.get("request"))
        rules_checked = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("rules_checked"))
        disconnecting_team = from_union([from_str, from_none], obj.get("disconnecting_team"))
        is_channel_canvas = from_union([from_bool, from_none], obj.get("is_channel_canvas"))
        linked_channel_id = from_union([from_str, from_none], obj.get("linked_channel_id"))
        column_id = from_union([from_str, from_none], obj.get("column_id"))
        row_id = from_union([from_str, from_none], obj.get("row_id"))
        cell_date_updated = from_union([from_int, from_none], obj.get("cell_date_updated"))
        view_id = from_union([from_str, from_none], obj.get("view_id"))
        user = from_union([from_str, from_none], obj.get("user"))
        file_id = from_union([from_str, from_none], obj.get("file_id"))
        return Details(type, app_owner_id, scopes, bot_scopes, new_scopes, previous_scopes, inviter, kicker, installer_user_id, approver_id, approval_type, app_previously_approved, old_scopes, name, bot_id, channels, permissions, shared_to, reason, is_internal_integration, cleared_resolution, is_workflow, mobile_only, web_only, non_sso_only, expires_on, new_version_id, trigger, granular_bot_token, origin_team, target_team, resolution, app_previously_resolved, admin_app_id, export_type, export_start_ts, export_end_ts, barrier_id, primary_usergroup_id, barriered_from_usergroup_ids, restricted_subjects, duration, desktop_app_browser_quit, invite_id, external_organization_id, external_organization_name, external_user_id, external_user_email, channel_id, added_team_id, is_token_rotation_enabled_app, old_retention_policy, new_retention_policy, who_can_post, can_thread, is_external_limited, exporting_team_id, session_search_start, deprecation_search_end, is_error, app_id, enable_at_here, enable_at_channel, can_huddle, url_private, shared_with, initiated_by, source_team, destination_team, succeeded_users, failed_users, enterprise, team, subteam, action, idp_group_member_count, workspace_member_count, added_user_count, added_user_error_count, reactivated_user_count, removed_user_count, removed_user_error_count, total_removal_count, is_flagged, target_user, target_entity, idp_config_id, config_type, idp_entity_id, idp_entity_id_hash, label, previous_profile, new_profile, target_user_id, space_file_id, target_entity_id, changed_permissions, datastore_name, attributes, channel, entity_type, actor, access_level, functions, workflows, datastores, permissions_updated, matched_rule, request, rules_checked, disconnecting_team, is_channel_canvas, linked_channel_id, column_id, row_id, cell_date_updated, view_id, user, file_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["app_owner_id"] = from_union([from_str, from_none], self.app_owner_id)
        result["scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.scopes)
        result["bot_scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.bot_scopes)
        result["new_scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.new_scopes)
        result["previous_scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.previous_scopes)
        result["inviter"] = from_union([lambda x: to_class(Inviter, x), from_none], self.inviter)
        result["kicker"] = from_union([lambda x: to_class(Inviter, x), from_none], self.kicker)
        result["installer_user_id"] = from_union([from_str, from_none], self.installer_user_id)
        result["approver_id"] = from_union([from_str, from_none], self.approver_id)
        result["approval_type"] = from_union([from_str, from_none], self.approval_type)
        result["app_previously_approved"] = from_union([from_bool, from_none], self.app_previously_approved)
        result["old_scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.old_scopes)
        result["name"] = from_union([from_str, from_none], self.name)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.channels)
        result["permissions"] = from_union([lambda x: from_list(lambda x: to_class(Permission, x), x), from_none], self.permissions)
        result["shared_to"] = from_union([from_str, from_none], self.shared_to)
        result["reason"] = from_union([from_str, from_none], self.reason)
        result["is_internal_integration"] = from_union([from_bool, from_none], self.is_internal_integration)
        result["cleared_resolution"] = from_union([from_str, from_none], self.cleared_resolution)
        result["is_workflow"] = from_union([from_bool, from_none], self.is_workflow)
        result["mobile_only"] = from_union([from_bool, from_none], self.mobile_only)
        result["web_only"] = from_union([from_bool, from_none], self.web_only)
        result["non_sso_only"] = from_union([from_bool, from_none], self.non_sso_only)
        result["expires_on"] = from_union([from_int, from_none], self.expires_on)
        result["new_version_id"] = from_union([from_str, from_none], self.new_version_id)
        result["trigger"] = from_union([from_str, from_none], self.trigger)
        result["granular_bot_token"] = from_union([from_bool, from_none], self.granular_bot_token)
        result["origin_team"] = from_union([from_str, from_none], self.origin_team)
        result["target_team"] = from_union([from_str, from_none], self.target_team)
        result["resolution"] = from_union([from_str, from_none], self.resolution)
        result["app_previously_resolved"] = from_union([from_bool, from_none], self.app_previously_resolved)
        result["admin_app_id"] = from_union([from_str, from_none], self.admin_app_id)
        result["export_type"] = from_union([from_str, from_none], self.export_type)
        result["export_start_ts"] = from_union([from_str, from_none], self.export_start_ts)
        result["export_end_ts"] = from_union([from_str, from_none], self.export_end_ts)
        result["barrier_id"] = from_union([from_str, from_none], self.barrier_id)
        result["primary_usergroup_id"] = from_union([from_str, from_none], self.primary_usergroup_id)
        result["barriered_from_usergroup_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.barriered_from_usergroup_ids)
        result["restricted_subjects"] = from_union([lambda x: from_list(from_str, x), from_none], self.restricted_subjects)
        result["duration"] = from_union([from_int, from_none], self.duration)
        result["desktop_app_browser_quit"] = from_union([from_bool, from_none], self.desktop_app_browser_quit)
        result["invite_id"] = from_union([from_str, from_none], self.invite_id)
        result["external_organization_id"] = from_union([from_str, from_none], self.external_organization_id)
        result["external_organization_name"] = from_union([from_str, from_none], self.external_organization_name)
        result["external_user_id"] = from_union([from_str, from_none], self.external_user_id)
        result["external_user_email"] = from_union([from_str, from_none], self.external_user_email)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["added_team_id"] = from_union([from_str, from_none], self.added_team_id)
        result["is_token_rotation_enabled_app"] = from_union([from_bool, from_none], self.is_token_rotation_enabled_app)
        result["old_retention_policy"] = from_union([lambda x: to_class(RetentionPolicy, x), from_none], self.old_retention_policy)
        result["new_retention_policy"] = from_union([lambda x: to_class(RetentionPolicy, x), from_none], self.new_retention_policy)
        result["who_can_post"] = from_union([lambda x: to_class(CanThread, x), from_none], self.who_can_post)
        result["can_thread"] = from_union([lambda x: to_class(CanThread, x), from_none], self.can_thread)
        result["is_external_limited"] = from_union([from_bool, from_none], self.is_external_limited)
        result["exporting_team_id"] = from_union([from_int, from_none], self.exporting_team_id)
        result["session_search_start"] = from_union([from_int, from_none], self.session_search_start)
        result["deprecation_search_end"] = from_union([from_int, from_none], self.deprecation_search_end)
        result["is_error"] = from_union([from_bool, from_none], self.is_error)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["enable_at_here"] = from_union([lambda x: to_class(CanHuddle, x), from_none], self.enable_at_here)
        result["enable_at_channel"] = from_union([lambda x: to_class(CanHuddle, x), from_none], self.enable_at_channel)
        result["can_huddle"] = from_union([lambda x: to_class(CanHuddle, x), from_none], self.can_huddle)
        result["url_private"] = from_union([from_str, from_none], self.url_private)
        result["shared_with"] = from_union([lambda x: to_class(SharedWith, x), from_none], self.shared_with)
        result["initiated_by"] = from_union([from_str, from_none], self.initiated_by)
        result["source_team"] = from_union([from_str, from_none], self.source_team)
        result["destination_team"] = from_union([from_str, from_none], self.destination_team)
        result["succeeded_users"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.succeeded_users)
        result["failed_users"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.failed_users)
        result["enterprise"] = from_union([from_str, from_none], self.enterprise)
        result["team"] = from_union([from_str, from_none], self.team)
        result["subteam"] = from_union([from_str, from_none], self.subteam)
        result["action"] = from_union([from_str, from_none], self.action)
        result["idp_group_member_count"] = from_union([from_int, from_none], self.idp_group_member_count)
        result["workspace_member_count"] = from_union([from_int, from_none], self.workspace_member_count)
        result["added_user_count"] = from_union([from_int, from_none], self.added_user_count)
        result["added_user_error_count"] = from_union([from_int, from_none], self.added_user_error_count)
        result["reactivated_user_count"] = from_union([from_int, from_none], self.reactivated_user_count)
        result["removed_user_count"] = from_union([from_int, from_none], self.removed_user_count)
        result["removed_user_error_count"] = from_union([from_int, from_none], self.removed_user_error_count)
        result["total_removal_count"] = from_union([from_int, from_none], self.total_removal_count)
        result["is_flagged"] = from_union([from_str, from_none], self.is_flagged)
        result["target_user"] = from_union([from_str, from_none], self.target_user)
        result["target_entity"] = from_union([from_str, from_none], self.target_entity)
        result["idp_config_id"] = from_union([from_str, from_none], self.idp_config_id)
        result["config_type"] = from_union([from_str, from_none], self.config_type)
        result["idp_entity_id"] = from_union([from_str, from_none], self.idp_entity_id)
        result["idp_entity_id_hash"] = from_union([from_str, from_none], self.idp_entity_id_hash)
        result["label"] = from_union([from_str, from_none], self.label)
        result["previous_profile"] = from_union([lambda x: to_class(Profile, x), from_none], self.previous_profile)
        result["new_profile"] = from_union([lambda x: to_class(Profile, x), from_none], self.new_profile)
        result["target_user_id"] = from_union([from_str, from_none], self.target_user_id)
        result["space_file_id"] = from_union([lambda x: to_class(SpaceFileID, x), from_none], self.space_file_id)
        result["target_entity_id"] = from_union([from_str, from_none], self.target_entity_id)
        result["changed_permissions"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.changed_permissions)
        result["datastore_name"] = from_union([from_str, from_none], self.datastore_name)
        result["attributes"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.attributes)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["entity_type"] = from_union([from_str, from_none], self.entity_type)
        result["actor"] = from_union([from_str, from_none], self.actor)
        result["access_level"] = from_union([from_str, from_none], self.access_level)
        result["functions"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.functions)
        result["workflows"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.workflows)
        result["datastores"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.datastores)
        result["permissions_updated"] = from_union([from_bool, from_none], self.permissions_updated)
        result["matched_rule"] = from_union([lambda x: to_class(MatchedRule, x), from_none], self.matched_rule)
        result["request"] = from_union([lambda x: to_class(Request, x), from_none], self.request)
        result["rules_checked"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.rules_checked)
        result["disconnecting_team"] = from_union([from_str, from_none], self.disconnecting_team)
        result["is_channel_canvas"] = from_union([from_bool, from_none], self.is_channel_canvas)
        result["linked_channel_id"] = from_union([from_str, from_none], self.linked_channel_id)
        result["column_id"] = from_union([from_str, from_none], self.column_id)
        result["row_id"] = from_union([from_str, from_none], self.row_id)
        result["cell_date_updated"] = from_union([from_int, from_none], self.cell_date_updated)
        result["view_id"] = from_union([from_str, from_none], self.view_id)
        result["user"] = from_union([from_str, from_none], self.user)
        result["file_id"] = from_union([from_str, from_none], self.file_id)
        return result


@dataclass
class AccountTypeRole:
    id: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AccountTypeRole':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return AccountTypeRole(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class Barrier:
    id: Optional[str] = None
    primary_usergroup: Optional[str] = None
    barriered_from_usergroups: Optional[List[str]] = None
    restricted_subjects: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Barrier':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        primary_usergroup = from_union([from_str, from_none], obj.get("primary_usergroup"))
        barriered_from_usergroups = from_union([lambda x: from_list(from_str, x), from_none], obj.get("barriered_from_usergroups"))
        restricted_subjects = from_union([lambda x: from_list(from_str, x), from_none], obj.get("restricted_subjects"))
        return Barrier(id, primary_usergroup, barriered_from_usergroups, restricted_subjects)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["primary_usergroup"] = from_union([from_str, from_none], self.primary_usergroup)
        result["barriered_from_usergroups"] = from_union([lambda x: from_list(from_str, x), from_none], self.barriered_from_usergroups)
        result["restricted_subjects"] = from_union([lambda x: from_list(from_str, x), from_none], self.restricted_subjects)
        return result


@dataclass
class Channel:
    id: Optional[str] = None
    name: Optional[str] = None
    privacy: Optional[str] = None
    is_shared: Optional[bool] = None
    is_org_shared: Optional[bool] = None
    teams_shared_with: Optional[List[str]] = None
    original_connected_channel_id: Optional[str] = None
    is_salesforce_channel: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        privacy = from_union([from_str, from_none], obj.get("privacy"))
        is_shared = from_union([from_bool, from_none], obj.get("is_shared"))
        is_org_shared = from_union([from_bool, from_none], obj.get("is_org_shared"))
        teams_shared_with = from_union([lambda x: from_list(from_str, x), from_none], obj.get("teams_shared_with"))
        original_connected_channel_id = from_union([from_str, from_none], obj.get("original_connected_channel_id"))
        is_salesforce_channel = from_union([from_bool, from_none], obj.get("is_salesforce_channel"))
        return Channel(id, name, privacy, is_shared, is_org_shared, teams_shared_with, original_connected_channel_id, is_salesforce_channel)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["privacy"] = from_union([from_str, from_none], self.privacy)
        result["is_shared"] = from_union([from_bool, from_none], self.is_shared)
        result["is_org_shared"] = from_union([from_bool, from_none], self.is_org_shared)
        result["teams_shared_with"] = from_union([lambda x: from_list(from_str, x), from_none], self.teams_shared_with)
        result["original_connected_channel_id"] = from_union([from_str, from_none], self.original_connected_channel_id)
        result["is_salesforce_channel"] = from_union([from_bool, from_none], self.is_salesforce_channel)
        return result


@dataclass
class File:
    id: Optional[str] = None
    name: Optional[str] = None
    filetype: Optional[str] = None
    title: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'File':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        filetype = from_union([from_str, from_none], obj.get("filetype"))
        title = from_union([from_str, from_none], obj.get("title"))
        return File(id, name, filetype, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["filetype"] = from_union([from_str, from_none], self.filetype)
        result["title"] = from_union([from_str, from_none], self.title)
        return result


@dataclass
class Huddle:
    id: Optional[str] = None
    date_start: Optional[int] = None
    date_end: Optional[int] = None
    participants: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Huddle':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        date_start = from_union([from_int, from_none], obj.get("date_start"))
        date_end = from_union([from_int, from_none], obj.get("date_end"))
        participants = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("participants"))
        return Huddle(id, date_start, date_end, participants)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["date_start"] = from_union([from_int, from_none], self.date_start)
        result["date_end"] = from_union([from_int, from_none], self.date_end)
        result["participants"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.participants)
        return result


@dataclass
class ListClass:
    id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ListClass':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        return ListClass(id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        return result


@dataclass
class Message:
    channel: Optional[str] = None
    team: Optional[str] = None
    timestamp: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Message':
        assert isinstance(obj, dict)
        channel = from_union([from_str, from_none], obj.get("channel"))
        team = from_union([from_str, from_none], obj.get("team"))
        timestamp = from_union([from_str, from_none], obj.get("timestamp"))
        return Message(channel, team, timestamp)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["team"] = from_union([from_str, from_none], self.team)
        result["timestamp"] = from_union([from_str, from_none], self.timestamp)
        return result


@dataclass
class WorkflowV2:
    id: Optional[str] = None
    app_id: Optional[str] = None
    date_updated: Optional[int] = None
    callback_id: Optional[str] = None
    name: Optional[str] = None
    updated_by: Optional[str] = None
    step_configuration: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'WorkflowV2':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        date_updated = from_union([from_int, from_none], obj.get("date_updated"))
        callback_id = from_union([from_str, from_none], obj.get("callback_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        updated_by = from_union([from_str, from_none], obj.get("updated_by"))
        step_configuration = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("step_configuration"))
        return WorkflowV2(id, app_id, date_updated, callback_id, name, updated_by, step_configuration)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["date_updated"] = from_union([from_int, from_none], self.date_updated)
        result["callback_id"] = from_union([from_str, from_none], self.callback_id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["updated_by"] = from_union([from_str, from_none], self.updated_by)
        result["step_configuration"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.step_configuration)
        return result


@dataclass
class Entity:
    type: Optional[str] = None
    app: Optional[App] = None
    user: Optional[User] = None
    usergroup: Optional[AccountTypeRole] = None
    workspace: Optional[Location] = None
    enterprise: Optional[Location] = None
    file: Optional[File] = None
    channel: Optional[Channel] = None
    message: Optional[Message] = None
    huddle: Optional[Huddle] = None
    role: Optional[Location] = None
    account_type_role: Optional[AccountTypeRole] = None
    workflow: Optional[AccountTypeRole] = None
    barrier: Optional[Barrier] = None
    workflow_v2: Optional[WorkflowV2] = None
    list: Optional[ListClass] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Entity':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        app = from_union([App.from_dict, from_none], obj.get("app"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        usergroup = from_union([AccountTypeRole.from_dict, from_none], obj.get("usergroup"))
        workspace = from_union([Location.from_dict, from_none], obj.get("workspace"))
        enterprise = from_union([Location.from_dict, from_none], obj.get("enterprise"))
        file = from_union([File.from_dict, from_none], obj.get("file"))
        channel = from_union([Channel.from_dict, from_none], obj.get("channel"))
        message = from_union([Message.from_dict, from_none], obj.get("message"))
        huddle = from_union([Huddle.from_dict, from_none], obj.get("huddle"))
        role = from_union([Location.from_dict, from_none], obj.get("role"))
        account_type_role = from_union([AccountTypeRole.from_dict, from_none], obj.get("account_type_role"))
        workflow = from_union([AccountTypeRole.from_dict, from_none], obj.get("workflow"))
        barrier = from_union([Barrier.from_dict, from_none], obj.get("barrier"))
        workflow_v2 = from_union([WorkflowV2.from_dict, from_none], obj.get("workflow_v2"))
        list = from_union([ListClass.from_dict, from_none], obj.get("list"))
        return Entity(type, app, user, usergroup, workspace, enterprise, file, channel, message, huddle, role, account_type_role, workflow, barrier, workflow_v2, list)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["app"] = from_union([lambda x: to_class(App, x), from_none], self.app)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        result["usergroup"] = from_union([lambda x: to_class(AccountTypeRole, x), from_none], self.usergroup)
        result["workspace"] = from_union([lambda x: to_class(Location, x), from_none], self.workspace)
        result["enterprise"] = from_union([lambda x: to_class(Location, x), from_none], self.enterprise)
        result["file"] = from_union([lambda x: to_class(File, x), from_none], self.file)
        result["channel"] = from_union([lambda x: to_class(Channel, x), from_none], self.channel)
        result["message"] = from_union([lambda x: to_class(Message, x), from_none], self.message)
        result["huddle"] = from_union([lambda x: to_class(Huddle, x), from_none], self.huddle)
        result["role"] = from_union([lambda x: to_class(Location, x), from_none], self.role)
        result["account_type_role"] = from_union([lambda x: to_class(AccountTypeRole, x), from_none], self.account_type_role)
        result["workflow"] = from_union([lambda x: to_class(AccountTypeRole, x), from_none], self.workflow)
        result["barrier"] = from_union([lambda x: to_class(Barrier, x), from_none], self.barrier)
        result["workflow_v2"] = from_union([lambda x: to_class(WorkflowV2, x), from_none], self.workflow_v2)
        result["list"] = from_union([lambda x: to_class(ListClass, x), from_none], self.list)
        return result


@dataclass
class Entry:
    id: Optional[str] = None
    date_create: Optional[int] = None
    action: Optional[str] = None
    actor: Optional[Actor] = None
    entity: Optional[Entity] = None
    context: Optional[Context] = None
    details: Optional[Details] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Entry':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        date_create = from_union([from_int, from_none], obj.get("date_create"))
        action = from_union([from_str, from_none], obj.get("action"))
        actor = from_union([Actor.from_dict, from_none], obj.get("actor"))
        entity = from_union([Entity.from_dict, from_none], obj.get("entity"))
        context = from_union([Context.from_dict, from_none], obj.get("context"))
        details = from_union([Details.from_dict, from_none], obj.get("details"))
        return Entry(id, date_create, action, actor, entity, context, details)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["date_create"] = from_union([from_int, from_none], self.date_create)
        result["action"] = from_union([from_str, from_none], self.action)
        result["actor"] = from_union([lambda x: to_class(Actor, x), from_none], self.actor)
        result["entity"] = from_union([lambda x: to_class(Entity, x), from_none], self.entity)
        result["context"] = from_union([lambda x: to_class(Context, x), from_none], self.context)
        result["details"] = from_union([lambda x: to_class(Details, x), from_none], self.details)
        return result


@dataclass
class ResponseMetadata:
    next_cursor: Optional[str] = None
    messages: Optional[List[Any]] = None
    warnings: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        next_cursor = from_union([from_str, from_none], obj.get("next_cursor"))
        messages = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("messages"))
        warnings = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("warnings"))
        return ResponseMetadata(next_cursor, messages, warnings)

    def to_dict(self) -> dict:
        result: dict = {}
        result["next_cursor"] = from_union([from_str, from_none], self.next_cursor)
        result["messages"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.messages)
        result["warnings"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.warnings)
        return result


@dataclass
class LogsResponse:
    ok: Optional[bool] = None
    warning: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    entries: Optional[List[Entry]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LogsResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        entries = from_union([lambda x: from_list(Entry.from_dict, x), from_none], obj.get("entries"))
        return LogsResponse(ok, warning, error, needed, provided, response_metadata, entries)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["warning"] = from_union([from_str, from_none], self.warning)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["entries"] = from_union([lambda x: from_list(lambda x: to_class(Entry, x), x), from_none], self.entries)
        return result


def logs_response_from_dict(s: Any) -> LogsResponse:
    return LogsResponse.from_dict(s)


def logs_response_to_dict(x: LogsResponse) -> Any:
    return to_class(LogsResponse, x)

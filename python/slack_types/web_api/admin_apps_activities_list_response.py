# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_apps_activities_list_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, Optional, List, TypeVar, Type, cast, Callable


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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


@dataclass
class Inputs:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'Inputs':
        assert isinstance(obj, dict)
        return Inputs()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class Outputs:
    channel_id: Optional[str] = None
    message_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Outputs':
        assert isinstance(obj, dict)
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        message_ts = from_union([from_str, from_none], obj.get("message_ts"))
        return Outputs(channel_id, message_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["message_ts"] = from_union([from_str, from_none], self.message_ts)
        return result


@dataclass
class Config:
    name: Optional[str] = None
    description: Optional[str] = None
    schema: Optional[Inputs] = None
    event_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Config':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        description = from_union([from_str, from_none], obj.get("description"))
        schema = from_union([Inputs.from_dict, from_none], obj.get("schema"))
        event_type = from_union([from_str, from_none], obj.get("event_type"))
        return Config(name, description, schema, event_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["description"] = from_union([from_str, from_none], self.description)
        result["schema"] = from_union([lambda x: to_class(Inputs, x), from_none], self.schema)
        result["event_type"] = from_union([from_str, from_none], self.event_type)
        return result


@dataclass
class TripInformation:
    user_id: Optional[str] = None
    channel_id: Optional[str] = None
    reaction: Optional[str] = None
    message_ts: Optional[str] = None
    list_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TripInformation':
        assert isinstance(obj, dict)
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        reaction = from_union([from_str, from_none], obj.get("reaction"))
        message_ts = from_union([from_str, from_none], obj.get("message_ts"))
        list_id = from_union([from_str, from_none], obj.get("list_id"))
        return TripInformation(user_id, channel_id, reaction, message_ts, list_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["reaction"] = from_union([from_str, from_none], self.reaction)
        result["message_ts"] = from_union([from_str, from_none], self.message_ts)
        result["list_id"] = from_union([from_str, from_none], self.list_id)
        return result


@dataclass
class Trigger:
    id: Optional[str] = None
    type: Optional[str] = None
    config: Optional[Config] = None
    trip_information: Optional[TripInformation] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Trigger':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        type = from_union([from_str, from_none], obj.get("type"))
        config = from_union([Config.from_dict, from_none], obj.get("config"))
        trip_information = from_union([TripInformation.from_dict, from_none], obj.get("trip_information"))
        return Trigger(id, type, config, trip_information)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["config"] = from_union([lambda x: to_class(Config, x), from_none], self.config)
        result["trip_information"] = from_union([lambda x: to_class(TripInformation, x), from_none], self.trip_information)
        return result


@dataclass
class Payload:
    exec_outcome: Optional[str] = None
    workflow_name: Optional[str] = None
    function_name: Optional[str] = None
    function_type: Optional[str] = None
    function_id: Optional[str] = None
    function_execution_id: Optional[str] = None
    total_steps: Optional[int] = None
    current_step: Optional[int] = None
    actor: Optional[str] = None
    error: Optional[str] = None
    log: Optional[str] = None
    type: Optional[str] = None
    billing_reason: Optional[List[str]] = None
    is_billing_excluded: Optional[bool] = None
    trigger: Optional[Trigger] = None
    channel_id: Optional[str] = None
    bot_user_id: Optional[str] = None
    inputs: Optional[Inputs] = None
    details: Optional[str] = None
    request_type: Optional[str] = None
    datastore_name: Optional[str] = None
    action: Optional[str] = None
    team_id: Optional[str] = None
    user_id: Optional[str] = None
    bundle_size_kb: Optional[int] = None
    outputs: Optional[Outputs] = None
    code: Optional[str] = None
    app_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Payload':
        assert isinstance(obj, dict)
        exec_outcome = from_union([from_str, from_none], obj.get("exec_outcome"))
        workflow_name = from_union([from_str, from_none], obj.get("workflow_name"))
        function_name = from_union([from_str, from_none], obj.get("function_name"))
        function_type = from_union([from_str, from_none], obj.get("function_type"))
        function_id = from_union([from_str, from_none], obj.get("function_id"))
        function_execution_id = from_union([from_str, from_none], obj.get("function_execution_id"))
        total_steps = from_union([from_int, from_none], obj.get("total_steps"))
        current_step = from_union([from_int, from_none], obj.get("current_step"))
        actor = from_union([from_str, from_none], obj.get("actor"))
        error = from_union([from_str, from_none], obj.get("error"))
        log = from_union([from_str, from_none], obj.get("log"))
        type = from_union([from_str, from_none], obj.get("type"))
        billing_reason = from_union([lambda x: from_list(from_str, x), from_none], obj.get("billing_reason"))
        is_billing_excluded = from_union([from_bool, from_none], obj.get("is_billing_excluded"))
        trigger = from_union([Trigger.from_dict, from_none], obj.get("trigger"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        bot_user_id = from_union([from_str, from_none], obj.get("bot_user_id"))
        inputs = from_union([Inputs.from_dict, from_none], obj.get("inputs"))
        details = from_union([from_str, from_none], obj.get("details"))
        request_type = from_union([from_str, from_none], obj.get("request_type"))
        datastore_name = from_union([from_str, from_none], obj.get("datastore_name"))
        action = from_union([from_str, from_none], obj.get("action"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        bundle_size_kb = from_union([from_int, from_none], obj.get("bundle_size_kb"))
        outputs = from_union([Outputs.from_dict, from_none], obj.get("outputs"))
        code = from_union([from_str, from_none], obj.get("code"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        return Payload(exec_outcome, workflow_name, function_name, function_type, function_id, function_execution_id, total_steps, current_step, actor, error, log, type, billing_reason, is_billing_excluded, trigger, channel_id, bot_user_id, inputs, details, request_type, datastore_name, action, team_id, user_id, bundle_size_kb, outputs, code, app_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["exec_outcome"] = from_union([from_str, from_none], self.exec_outcome)
        result["workflow_name"] = from_union([from_str, from_none], self.workflow_name)
        result["function_name"] = from_union([from_str, from_none], self.function_name)
        result["function_type"] = from_union([from_str, from_none], self.function_type)
        result["function_id"] = from_union([from_str, from_none], self.function_id)
        result["function_execution_id"] = from_union([from_str, from_none], self.function_execution_id)
        result["total_steps"] = from_union([from_int, from_none], self.total_steps)
        result["current_step"] = from_union([from_int, from_none], self.current_step)
        result["actor"] = from_union([from_str, from_none], self.actor)
        result["error"] = from_union([from_str, from_none], self.error)
        result["log"] = from_union([from_str, from_none], self.log)
        result["type"] = from_union([from_str, from_none], self.type)
        result["billing_reason"] = from_union([lambda x: from_list(from_str, x), from_none], self.billing_reason)
        result["is_billing_excluded"] = from_union([from_bool, from_none], self.is_billing_excluded)
        result["trigger"] = from_union([lambda x: to_class(Trigger, x), from_none], self.trigger)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["bot_user_id"] = from_union([from_str, from_none], self.bot_user_id)
        result["inputs"] = from_union([lambda x: to_class(Inputs, x), from_none], self.inputs)
        result["details"] = from_union([from_str, from_none], self.details)
        result["request_type"] = from_union([from_str, from_none], self.request_type)
        result["datastore_name"] = from_union([from_str, from_none], self.datastore_name)
        result["action"] = from_union([from_str, from_none], self.action)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["bundle_size_kb"] = from_union([from_int, from_none], self.bundle_size_kb)
        result["outputs"] = from_union([lambda x: to_class(Outputs, x), from_none], self.outputs)
        result["code"] = from_union([from_str, from_none], self.code)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        return result


@dataclass
class Activity:
    app_id: Optional[str] = None
    level: Optional[str] = None
    event_type: Optional[str] = None
    source: Optional[str] = None
    component_type: Optional[str] = None
    component_id: Optional[str] = None
    team_id: Optional[str] = None
    enterprise_id: Optional[str] = None
    payload: Optional[Payload] = None
    created: Optional[int] = None
    trace_id: Optional[str] = None
    parent_execution_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Activity':
        assert isinstance(obj, dict)
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        level = from_union([from_str, from_none], obj.get("level"))
        event_type = from_union([from_str, from_none], obj.get("event_type"))
        source = from_union([from_str, from_none], obj.get("source"))
        component_type = from_union([from_str, from_none], obj.get("component_type"))
        component_id = from_union([from_str, from_none], obj.get("component_id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        payload = from_union([Payload.from_dict, from_none], obj.get("payload"))
        created = from_union([from_int, from_none], obj.get("created"))
        trace_id = from_union([from_str, from_none], obj.get("trace_id"))
        parent_execution_id = from_union([from_str, from_none], obj.get("parent_execution_id"))
        return Activity(app_id, level, event_type, source, component_type, component_id, team_id, enterprise_id, payload, created, trace_id, parent_execution_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["level"] = from_union([from_str, from_none], self.level)
        result["event_type"] = from_union([from_str, from_none], self.event_type)
        result["source"] = from_union([from_str, from_none], self.source)
        result["component_type"] = from_union([from_str, from_none], self.component_type)
        result["component_id"] = from_union([from_str, from_none], self.component_id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["payload"] = from_union([lambda x: to_class(Payload, x), from_none], self.payload)
        result["created"] = from_union([from_int, from_none], self.created)
        result["trace_id"] = from_union([from_str, from_none], self.trace_id)
        result["parent_execution_id"] = from_union([from_str, from_none], self.parent_execution_id)
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
class AdminAppsActivitiesListResponse:
    ok: Optional[bool] = None
    activities: Optional[List[Activity]] = None
    response_metadata: Optional[ResponseMetadata] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminAppsActivitiesListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        activities = from_union([lambda x: from_list(Activity.from_dict, x), from_none], obj.get("activities"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return AdminAppsActivitiesListResponse(ok, activities, response_metadata, error, needed, provided, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["activities"] = from_union([lambda x: from_list(lambda x: to_class(Activity, x), x), from_none], self.activities)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def admin_apps_activities_list_response_from_dict(s: Any) -> AdminAppsActivitiesListResponse:
    return AdminAppsActivitiesListResponse.from_dict(s)


def admin_apps_activities_list_response_to_dict(x: AdminAppsActivitiesListResponse) -> Any:
    return to_class(AdminAppsActivitiesListResponse, x)

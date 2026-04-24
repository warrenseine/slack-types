# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_workflows_search_response_from_dict(json.loads(json_string))

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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


@dataclass
class ResponseMetadata:
    messages: Optional[List[str]] = None
    next_cursor: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        messages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("messages"))
        next_cursor = from_union([from_str, from_none], obj.get("next_cursor"))
        return ResponseMetadata(messages, next_cursor)

    def to_dict(self) -> dict:
        result: dict = {}
        result["messages"] = from_union([lambda x: from_list(from_str, x), from_none], self.messages)
        result["next_cursor"] = from_union([from_str, from_none], self.next_cursor)
        return result


@dataclass
class Icons:
    image_96: Optional[str] = None
    image_192: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Icons':
        assert isinstance(obj, dict)
        image_96 = from_union([from_str, from_none], obj.get("image_96"))
        image_192 = from_union([from_str, from_none], obj.get("image_192"))
        return Icons(image_96, image_192)

    def to_dict(self) -> dict:
        result: dict = {}
        result["image_96"] = from_union([from_str, from_none], self.image_96)
        result["image_192"] = from_union([from_str, from_none], self.image_192)
        return result


@dataclass
class InputParameter:
    type: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    is_required: Optional[bool] = None
    is_hidden: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InputParameter':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        name = from_union([from_str, from_none], obj.get("name"))
        title = from_union([from_str, from_none], obj.get("title"))
        description = from_union([from_str, from_none], obj.get("description"))
        is_required = from_union([from_bool, from_none], obj.get("is_required"))
        is_hidden = from_union([from_bool, from_none], obj.get("is_hidden"))
        return InputParameter(type, name, title, description, is_required, is_hidden)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["name"] = from_union([from_str, from_none], self.name)
        result["title"] = from_union([from_str, from_none], self.title)
        result["description"] = from_union([from_str, from_none], self.description)
        result["is_required"] = from_union([from_bool, from_none], self.is_required)
        result["is_hidden"] = from_union([from_bool, from_none], self.is_hidden)
        return result


@dataclass
class Input:
    hidden: Optional[bool] = None
    locked: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Input':
        assert isinstance(obj, dict)
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        locked = from_union([from_bool, from_none], obj.get("locked"))
        return Input(hidden, locked)

    def to_dict(self) -> dict:
        result: dict = {}
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["locked"] = from_union([from_bool, from_none], self.locked)
        return result


@dataclass
class Step:
    id: Optional[int] = None
    function_id: Optional[str] = None
    inputs: Optional[Dict[str, Input]] = None
    is_pristine: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Step':
        assert isinstance(obj, dict)
        id = from_union([from_none, lambda x: int(from_str(x))], obj.get("id"))
        function_id = from_union([from_str, from_none], obj.get("function_id"))
        inputs = from_union([lambda x: from_dict(Input.from_dict, x), from_none], obj.get("inputs"))
        is_pristine = from_union([from_bool, from_none], obj.get("is_pristine"))
        return Step(id, function_id, inputs, is_pristine)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.id)
        result["function_id"] = from_union([from_str, from_none], self.function_id)
        result["inputs"] = from_union([lambda x: from_dict(lambda x: to_class(Input, x), x), from_none], self.inputs)
        result["is_pristine"] = from_union([from_bool, from_none], self.is_pristine)
        return result


@dataclass
class Workflow:
    last_published_date: Optional[int] = None
    id: Optional[str] = None
    team_id: Optional[str] = None
    workflow_function_id: Optional[str] = None
    callback_id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    input_parameters: Optional[Dict[str, InputParameter]] = None
    steps: Optional[List[Step]] = None
    collaborators: Optional[List[str]] = None
    icons: Optional[Icons] = None
    is_published: Optional[bool] = None
    last_updated_by: Optional[str] = None
    unpublished_change_count: Optional[int] = None
    app_id: Optional[str] = None
    source: Optional[str] = None
    billing_type: Optional[str] = None
    date_updated: Optional[int] = None
    is_billable: Optional[bool] = None
    last_published_version_id: Optional[str] = None
    trigger_ids: Optional[List[str]] = None
    is_sales_home_workflow: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Workflow':
        assert isinstance(obj, dict)
        last_published_date = from_union([from_none, lambda x: int(from_str(x))], obj.get("last_published_date"))
        id = from_union([from_str, from_none], obj.get("id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        workflow_function_id = from_union([from_str, from_none], obj.get("workflow_function_id"))
        callback_id = from_union([from_str, from_none], obj.get("callback_id"))
        title = from_union([from_str, from_none], obj.get("title"))
        description = from_union([from_str, from_none], obj.get("description"))
        input_parameters = from_union([lambda x: from_dict(InputParameter.from_dict, x), from_none], obj.get("input_parameters"))
        steps = from_union([lambda x: from_list(Step.from_dict, x), from_none], obj.get("steps"))
        collaborators = from_union([lambda x: from_list(from_str, x), from_none], obj.get("collaborators"))
        icons = from_union([Icons.from_dict, from_none], obj.get("icons"))
        is_published = from_union([from_bool, from_none], obj.get("is_published"))
        last_updated_by = from_union([from_str, from_none], obj.get("last_updated_by"))
        unpublished_change_count = from_union([from_int, from_none], obj.get("unpublished_change_count"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        source = from_union([from_str, from_none], obj.get("source"))
        billing_type = from_union([from_str, from_none], obj.get("billing_type"))
        date_updated = from_union([from_int, from_none], obj.get("date_updated"))
        is_billable = from_union([from_bool, from_none], obj.get("is_billable"))
        last_published_version_id = from_union([from_str, from_none], obj.get("last_published_version_id"))
        trigger_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("trigger_ids"))
        is_sales_home_workflow = from_union([from_bool, from_none], obj.get("is_sales_home_workflow"))
        return Workflow(last_published_date, id, team_id, workflow_function_id, callback_id, title, description, input_parameters, steps, collaborators, icons, is_published, last_updated_by, unpublished_change_count, app_id, source, billing_type, date_updated, is_billable, last_published_version_id, trigger_ids, is_sales_home_workflow)

    def to_dict(self) -> dict:
        result: dict = {}
        result["last_published_date"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.last_published_date)
        result["id"] = from_union([from_str, from_none], self.id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["workflow_function_id"] = from_union([from_str, from_none], self.workflow_function_id)
        result["callback_id"] = from_union([from_str, from_none], self.callback_id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["description"] = from_union([from_str, from_none], self.description)
        result["input_parameters"] = from_union([lambda x: from_dict(lambda x: to_class(InputParameter, x), x), from_none], self.input_parameters)
        result["steps"] = from_union([lambda x: from_list(lambda x: to_class(Step, x), x), from_none], self.steps)
        result["collaborators"] = from_union([lambda x: from_list(from_str, x), from_none], self.collaborators)
        result["icons"] = from_union([lambda x: to_class(Icons, x), from_none], self.icons)
        result["is_published"] = from_union([from_bool, from_none], self.is_published)
        result["last_updated_by"] = from_union([from_str, from_none], self.last_updated_by)
        result["unpublished_change_count"] = from_union([from_int, from_none], self.unpublished_change_count)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["source"] = from_union([from_str, from_none], self.source)
        result["billing_type"] = from_union([from_str, from_none], self.billing_type)
        result["date_updated"] = from_union([from_int, from_none], self.date_updated)
        result["is_billable"] = from_union([from_bool, from_none], self.is_billable)
        result["last_published_version_id"] = from_union([from_str, from_none], self.last_published_version_id)
        result["trigger_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.trigger_ids)
        result["is_sales_home_workflow"] = from_union([from_bool, from_none], self.is_sales_home_workflow)
        return result


@dataclass
class AdminWorkflowsSearchResponse:
    ok: Optional[bool] = None
    workflows: Optional[List[Workflow]] = None
    total_found: Optional[int] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminWorkflowsSearchResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        workflows = from_union([lambda x: from_list(Workflow.from_dict, x), from_none], obj.get("workflows"))
        total_found = from_union([from_int, from_none], obj.get("total_found"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        return AdminWorkflowsSearchResponse(ok, workflows, total_found, error, needed, provided, response_metadata)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["workflows"] = from_union([lambda x: from_list(lambda x: to_class(Workflow, x), x), from_none], self.workflows)
        result["total_found"] = from_union([from_int, from_none], self.total_found)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        return result


def admin_workflows_search_response_from_dict(s: Any) -> AdminWorkflowsSearchResponse:
    return AdminWorkflowsSearchResponse.from_dict(s)


def admin_workflows_search_response_to_dict(x: AdminWorkflowsSearchResponse) -> Any:
    return to_class(AdminWorkflowsSearchResponse, x)

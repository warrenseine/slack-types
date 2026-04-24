# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = resource_types_response_from_dict(json.loads(json_string))

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


@dataclass
class Meta:
    location: Optional[str] = None
    resource_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        assert isinstance(obj, dict)
        location = from_union([from_str, from_none], obj.get("location"))
        resource_type = from_union([from_str, from_none], obj.get("resourceType"))
        return Meta(location, resource_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["location"] = from_union([from_str, from_none], self.location)
        result["resourceType"] = from_union([from_str, from_none], self.resource_type)
        return result


@dataclass
class SchemaExtension:
    schema: Optional[str] = None
    required: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SchemaExtension':
        assert isinstance(obj, dict)
        schema = from_union([from_str, from_none], obj.get("schema"))
        required = from_union([from_bool, from_none], obj.get("required"))
        return SchemaExtension(schema, required)

    def to_dict(self) -> dict:
        result: dict = {}
        result["schema"] = from_union([from_str, from_none], self.schema)
        result["required"] = from_union([from_bool, from_none], self.required)
        return result


@dataclass
class Resource:
    schemas: Optional[List[str]] = None
    id: Optional[str] = None
    name: Optional[str] = None
    endpoint: Optional[str] = None
    description: Optional[str] = None
    schema: Optional[str] = None
    meta: Optional[Meta] = None
    schema_extensions: Optional[List[SchemaExtension]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Resource':
        assert isinstance(obj, dict)
        schemas = from_union([lambda x: from_list(from_str, x), from_none], obj.get("schemas"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        endpoint = from_union([from_str, from_none], obj.get("endpoint"))
        description = from_union([from_str, from_none], obj.get("description"))
        schema = from_union([from_str, from_none], obj.get("schema"))
        meta = from_union([Meta.from_dict, from_none], obj.get("meta"))
        schema_extensions = from_union([lambda x: from_list(SchemaExtension.from_dict, x), from_none], obj.get("schemaExtensions"))
        return Resource(schemas, id, name, endpoint, description, schema, meta, schema_extensions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["schemas"] = from_union([lambda x: from_list(from_str, x), from_none], self.schemas)
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["endpoint"] = from_union([from_str, from_none], self.endpoint)
        result["description"] = from_union([from_str, from_none], self.description)
        result["schema"] = from_union([from_str, from_none], self.schema)
        result["meta"] = from_union([lambda x: to_class(Meta, x), from_none], self.meta)
        result["schemaExtensions"] = from_union([lambda x: from_list(lambda x: to_class(SchemaExtension, x), x), from_none], self.schema_extensions)
        return result


@dataclass
class ResourceTypesResponse:
    schemas: Optional[List[str]] = None
    resources: Optional[List[Resource]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResourceTypesResponse':
        assert isinstance(obj, dict)
        schemas = from_union([lambda x: from_list(from_str, x), from_none], obj.get("schemas"))
        resources = from_union([lambda x: from_list(Resource.from_dict, x), from_none], obj.get("Resources"))
        return ResourceTypesResponse(schemas, resources)

    def to_dict(self) -> dict:
        result: dict = {}
        result["schemas"] = from_union([lambda x: from_list(from_str, x), from_none], self.schemas)
        result["Resources"] = from_union([lambda x: from_list(lambda x: to_class(Resource, x), x), from_none], self.resources)
        return result


def resource_types_response_from_dict(s: Any) -> ResourceTypesResponse:
    return ResourceTypesResponse.from_dict(s)


def resource_types_response_to_dict(x: ResourceTypesResponse) -> Any:
    return to_class(ResourceTypesResponse, x)

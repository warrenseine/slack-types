# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = users_response_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class Errors:
    description: Optional[str] = None
    code: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Errors':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("description"))
        code = from_union([from_int, from_none], obj.get("code"))
        return Errors(description, code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_union([from_str, from_none], self.description)
        result["code"] = from_union([from_int, from_none], self.code)
        return result


@dataclass
class Address:
    street_address: Optional[str] = None
    locality: Optional[str] = None
    region: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    primary: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Address':
        assert isinstance(obj, dict)
        street_address = from_union([from_str, from_none], obj.get("streetAddress"))
        locality = from_union([from_str, from_none], obj.get("locality"))
        region = from_union([from_str, from_none], obj.get("region"))
        postal_code = from_union([from_str, from_none], obj.get("postalCode"))
        country = from_union([from_str, from_none], obj.get("country"))
        primary = from_union([from_bool, from_none], obj.get("primary"))
        return Address(street_address, locality, region, postal_code, country, primary)

    def to_dict(self) -> dict:
        result: dict = {}
        result["streetAddress"] = from_union([from_str, from_none], self.street_address)
        result["locality"] = from_union([from_str, from_none], self.locality)
        result["region"] = from_union([from_str, from_none], self.region)
        result["postalCode"] = from_union([from_str, from_none], self.postal_code)
        result["country"] = from_union([from_str, from_none], self.country)
        result["primary"] = from_union([from_bool, from_none], self.primary)
        return result


@dataclass
class Email:
    value: Optional[str] = None
    primary: Optional[bool] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Email':
        assert isinstance(obj, dict)
        value = from_union([from_str, from_none], obj.get("value"))
        primary = from_union([from_bool, from_none], obj.get("primary"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Email(value, primary, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_str, from_none], self.value)
        result["primary"] = from_union([from_bool, from_none], self.primary)
        result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class Group:
    value: Optional[str] = None
    display: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Group':
        assert isinstance(obj, dict)
        value = from_union([from_str, from_none], obj.get("value"))
        display = from_union([from_str, from_none], obj.get("display"))
        return Group(value, display)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_str, from_none], self.value)
        result["display"] = from_union([from_str, from_none], self.display)
        return result


@dataclass
class Meta:
    created: Optional[str] = None
    location: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        assert isinstance(obj, dict)
        created = from_union([from_str, from_none], obj.get("created"))
        location = from_union([from_str, from_none], obj.get("location"))
        return Meta(created, location)

    def to_dict(self) -> dict:
        result: dict = {}
        result["created"] = from_union([from_str, from_none], self.created)
        result["location"] = from_union([from_str, from_none], self.location)
        return result


@dataclass
class Name:
    given_name: Optional[str] = None
    family_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Name':
        assert isinstance(obj, dict)
        given_name = from_union([from_str, from_none], obj.get("givenName"))
        family_name = from_union([from_str, from_none], obj.get("familyName"))
        return Name(given_name, family_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["givenName"] = from_union([from_str, from_none], self.given_name)
        result["familyName"] = from_union([from_str, from_none], self.family_name)
        return result


@dataclass
class Photo:
    value: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Photo':
        assert isinstance(obj, dict)
        value = from_union([from_str, from_none], obj.get("value"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Photo(value, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_str, from_none], self.value)
        result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class Manager:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'Manager':
        assert isinstance(obj, dict)
        return Manager()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class UrnIETFParamsScimSchemasExtensionEnterprise20User:
    manager: Optional[Manager] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UrnIETFParamsScimSchemasExtensionEnterprise20User':
        assert isinstance(obj, dict)
        manager = from_union([Manager.from_dict, from_none], obj.get("manager"))
        return UrnIETFParamsScimSchemasExtensionEnterprise20User(manager)

    def to_dict(self) -> dict:
        result: dict = {}
        result["manager"] = from_union([lambda x: to_class(Manager, x), from_none], self.manager)
        return result


@dataclass
class UrnIETFParamsScimSchemasExtensionSlackGuest20User:
    type: Optional[str] = None
    expiration: Optional[str] = None
    channels: Optional[List[Group]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UrnIETFParamsScimSchemasExtensionSlackGuest20User':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        expiration = from_union([from_str, from_none], obj.get("expiration"))
        channels = from_union([lambda x: from_list(Group.from_dict, x), from_none], obj.get("channels"))
        return UrnIETFParamsScimSchemasExtensionSlackGuest20User(type, expiration, channels)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["expiration"] = from_union([from_str, from_none], self.expiration)
        result["channels"] = from_union([lambda x: from_list(lambda x: to_class(Group, x), x), from_none], self.channels)
        return result


@dataclass
class UrnIETFParamsScimSchemasExtensionSlackProfile20User:
    start_date: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UrnIETFParamsScimSchemasExtensionSlackProfile20User':
        assert isinstance(obj, dict)
        start_date = from_union([from_str, from_none], obj.get("startDate"))
        return UrnIETFParamsScimSchemasExtensionSlackProfile20User(start_date)

    def to_dict(self) -> dict:
        result: dict = {}
        result["startDate"] = from_union([from_str, from_none], self.start_date)
        return result


@dataclass
class Resource:
    schemas: Optional[List[str]] = None
    id: Optional[str] = None
    external_id: Optional[str] = None
    meta: Optional[Meta] = None
    user_name: Optional[str] = None
    nick_name: Optional[str] = None
    name: Optional[Name] = None
    display_name: Optional[str] = None
    profile_url: Optional[str] = None
    title: Optional[str] = None
    timezone: Optional[str] = None
    active: Optional[bool] = None
    emails: Optional[List[Email]] = None
    photos: Optional[List[Photo]] = None
    addresses: Optional[List[Address]] = None
    phone_numbers: Optional[List[Email]] = None
    roles: Optional[List[Email]] = None
    urn_ietf_params_scim_schemas_extension_enterprise_20_user: Optional[UrnIETFParamsScimSchemasExtensionEnterprise20User] = None
    groups: Optional[List[Group]] = None
    urn_ietf_params_scim_schemas_extension_slack_guest_20_user: Optional[UrnIETFParamsScimSchemasExtensionSlackGuest20User] = None
    urn_ietf_params_scim_schemas_extension_slack_profile_20_user: Optional[UrnIETFParamsScimSchemasExtensionSlackProfile20User] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Resource':
        assert isinstance(obj, dict)
        schemas = from_union([lambda x: from_list(from_str, x), from_none], obj.get("schemas"))
        id = from_union([from_str, from_none], obj.get("id"))
        external_id = from_union([from_str, from_none], obj.get("externalId"))
        meta = from_union([Meta.from_dict, from_none], obj.get("meta"))
        user_name = from_union([from_str, from_none], obj.get("userName"))
        nick_name = from_union([from_str, from_none], obj.get("nickName"))
        name = from_union([Name.from_dict, from_none], obj.get("name"))
        display_name = from_union([from_str, from_none], obj.get("displayName"))
        profile_url = from_union([from_str, from_none], obj.get("profileUrl"))
        title = from_union([from_str, from_none], obj.get("title"))
        timezone = from_union([from_str, from_none], obj.get("timezone"))
        active = from_union([from_bool, from_none], obj.get("active"))
        emails = from_union([lambda x: from_list(Email.from_dict, x), from_none], obj.get("emails"))
        photos = from_union([lambda x: from_list(Photo.from_dict, x), from_none], obj.get("photos"))
        addresses = from_union([lambda x: from_list(Address.from_dict, x), from_none], obj.get("addresses"))
        phone_numbers = from_union([lambda x: from_list(Email.from_dict, x), from_none], obj.get("phoneNumbers"))
        roles = from_union([lambda x: from_list(Email.from_dict, x), from_none], obj.get("roles"))
        urn_ietf_params_scim_schemas_extension_enterprise_20_user = from_union([UrnIETFParamsScimSchemasExtensionEnterprise20User.from_dict, from_none], obj.get("urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"))
        groups = from_union([lambda x: from_list(Group.from_dict, x), from_none], obj.get("groups"))
        urn_ietf_params_scim_schemas_extension_slack_guest_20_user = from_union([UrnIETFParamsScimSchemasExtensionSlackGuest20User.from_dict, from_none], obj.get("urn:ietf:params:scim:schemas:extension:slack:guest:2.0:User"))
        urn_ietf_params_scim_schemas_extension_slack_profile_20_user = from_union([UrnIETFParamsScimSchemasExtensionSlackProfile20User.from_dict, from_none], obj.get("urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User"))
        return Resource(schemas, id, external_id, meta, user_name, nick_name, name, display_name, profile_url, title, timezone, active, emails, photos, addresses, phone_numbers, roles, urn_ietf_params_scim_schemas_extension_enterprise_20_user, groups, urn_ietf_params_scim_schemas_extension_slack_guest_20_user, urn_ietf_params_scim_schemas_extension_slack_profile_20_user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["schemas"] = from_union([lambda x: from_list(from_str, x), from_none], self.schemas)
        result["id"] = from_union([from_str, from_none], self.id)
        result["externalId"] = from_union([from_str, from_none], self.external_id)
        result["meta"] = from_union([lambda x: to_class(Meta, x), from_none], self.meta)
        result["userName"] = from_union([from_str, from_none], self.user_name)
        result["nickName"] = from_union([from_str, from_none], self.nick_name)
        result["name"] = from_union([lambda x: to_class(Name, x), from_none], self.name)
        result["displayName"] = from_union([from_str, from_none], self.display_name)
        result["profileUrl"] = from_union([from_str, from_none], self.profile_url)
        result["title"] = from_union([from_str, from_none], self.title)
        result["timezone"] = from_union([from_str, from_none], self.timezone)
        result["active"] = from_union([from_bool, from_none], self.active)
        result["emails"] = from_union([lambda x: from_list(lambda x: to_class(Email, x), x), from_none], self.emails)
        result["photos"] = from_union([lambda x: from_list(lambda x: to_class(Photo, x), x), from_none], self.photos)
        result["addresses"] = from_union([lambda x: from_list(lambda x: to_class(Address, x), x), from_none], self.addresses)
        result["phoneNumbers"] = from_union([lambda x: from_list(lambda x: to_class(Email, x), x), from_none], self.phone_numbers)
        result["roles"] = from_union([lambda x: from_list(lambda x: to_class(Email, x), x), from_none], self.roles)
        result["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"] = from_union([lambda x: to_class(UrnIETFParamsScimSchemasExtensionEnterprise20User, x), from_none], self.urn_ietf_params_scim_schemas_extension_enterprise_20_user)
        result["groups"] = from_union([lambda x: from_list(lambda x: to_class(Group, x), x), from_none], self.groups)
        result["urn:ietf:params:scim:schemas:extension:slack:guest:2.0:User"] = from_union([lambda x: to_class(UrnIETFParamsScimSchemasExtensionSlackGuest20User, x), from_none], self.urn_ietf_params_scim_schemas_extension_slack_guest_20_user)
        result["urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User"] = from_union([lambda x: to_class(UrnIETFParamsScimSchemasExtensionSlackProfile20User, x), from_none], self.urn_ietf_params_scim_schemas_extension_slack_profile_20_user)
        return result


@dataclass
class UsersResponse:
    schemas: Optional[List[str]] = None
    resources: Optional[List[Resource]] = None
    total_results: Optional[int] = None
    items_per_page: Optional[int] = None
    start_index: Optional[int] = None
    errors: Optional[Errors] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UsersResponse':
        assert isinstance(obj, dict)
        schemas = from_union([lambda x: from_list(from_str, x), from_none], obj.get("schemas"))
        resources = from_union([lambda x: from_list(Resource.from_dict, x), from_none], obj.get("Resources"))
        total_results = from_union([from_int, from_none], obj.get("totalResults"))
        items_per_page = from_union([from_int, from_none], obj.get("itemsPerPage"))
        start_index = from_union([from_int, from_none], obj.get("startIndex"))
        errors = from_union([Errors.from_dict, from_none], obj.get("Errors"))
        return UsersResponse(schemas, resources, total_results, items_per_page, start_index, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["schemas"] = from_union([lambda x: from_list(from_str, x), from_none], self.schemas)
        result["Resources"] = from_union([lambda x: from_list(lambda x: to_class(Resource, x), x), from_none], self.resources)
        result["totalResults"] = from_union([from_int, from_none], self.total_results)
        result["itemsPerPage"] = from_union([from_int, from_none], self.items_per_page)
        result["startIndex"] = from_union([from_int, from_none], self.start_index)
        result["Errors"] = from_union([lambda x: to_class(Errors, x), from_none], self.errors)
        return result


def users_response_from_dict(s: Any) -> UsersResponse:
    return UsersResponse.from_dict(s)


def users_response_to_dict(x: UsersResponse) -> Any:
    return to_class(UsersResponse, x)

export interface UsersResponse {
    schemas?:      string[];
    Resources?:    Resource[];
    totalResults?: number;
    itemsPerPage?: number;
    startIndex?:   number;
    Errors?:       Errors;
}

export interface Errors {
    description?: string;
    code?:        number;
}

export interface Resource {
    schemas?:                                                         string[];
    id?:                                                              string;
    externalId?:                                                      string;
    meta?:                                                            Meta;
    userName?:                                                        string;
    nickName?:                                                        string;
    name?:                                                            Name;
    displayName?:                                                     string;
    profileUrl?:                                                      string;
    title?:                                                           string;
    timezone?:                                                        string;
    active?:                                                          boolean;
    emails?:                                                          Email[];
    photos?:                                                          Photo[];
    addresses?:                                                       Address[];
    phoneNumbers?:                                                    Email[];
    roles?:                                                           Email[];
    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"?:    UrnietfParamsScimSchemasExtensionEnterprise20User;
    groups?:                                                          Group[];
    "urn:ietf:params:scim:schemas:extension:slack:guest:2.0:User"?:   UrnietfParamsScimSchemasExtensionSlackGuest20User;
    "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User"?: UrnietfParamsScimSchemasExtensionSlackProfile20User;
}

export interface Address {
    streetAddress?: string;
    locality?:      string;
    region?:        string;
    postalCode?:    string;
    country?:       string;
    primary?:       boolean;
}

export interface Email {
    value?:   string;
    primary?: boolean;
    type?:    string;
}

export interface Group {
    value?:   string;
    display?: string;
}

export interface Meta {
    created?:  string;
    location?: string;
}

export interface Name {
    givenName?:  string;
    familyName?: string;
}

export interface Photo {
    value?: string;
    type?:  string;
}

export interface UrnietfParamsScimSchemasExtensionEnterprise20User {
    manager?: Manager;
}

export interface Manager {
}

export interface UrnietfParamsScimSchemasExtensionSlackGuest20User {
    type?:       string;
    expiration?: string;
    channels?:   Group[];
}

export interface UrnietfParamsScimSchemasExtensionSlackProfile20User {
    startDate?: string;
}

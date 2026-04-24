export interface UserResponse {
    Errors?:                                                        Errors;
    schemas?:                                                       string[];
    id?:                                                            string;
    externalId?:                                                    string;
    meta?:                                                          Meta;
    userName?:                                                      string;
    nickName?:                                                      string;
    name?:                                                          Name;
    displayName?:                                                   string;
    profileUrl?:                                                    string;
    title?:                                                         string;
    timezone?:                                                      string;
    active?:                                                        boolean;
    emails?:                                                        Email[];
    photos?:                                                        Photo[];
    addresses?:                                                     Address[];
    phoneNumbers?:                                                  Email[];
    roles?:                                                         Email[];
    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"?:  UrnietfParamsScimSchemasExtensionEnterprise20User;
    groups?:                                                        Group[];
    "urn:ietf:params:scim:schemas:extension:slack:guest:2.0:User"?: UrnietfParamsScimSchemasExtensionSlackGuest20User;
}

export interface Errors {
    description?: string;
    code?:        number;
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
    type?:    string;
    primary?: boolean;
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
}

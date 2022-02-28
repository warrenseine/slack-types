export interface UserResponse {
    Errors?:                                       Errors;
    schemas?:                                      string[];
    id?:                                           string;
    externalId?:                                   string;
    meta?:                                         Meta;
    userName?:                                     string;
    nickName?:                                     string;
    name?:                                         Name;
    displayName?:                                  string;
    profileUrl?:                                   string;
    title?:                                        string;
    timezone?:                                     string;
    active?:                                       boolean;
    emails?:                                       Email[];
    photos?:                                       Photo[];
    groups?:                                       Group[];
    addresses?:                                    Address[];
    phoneNumbers?:                                 Email[];
    roles?:                                        Email[];
    "urn:scim:schemas:extension:enterprise:1.0"?:  UrnScimSchemasExtensionEnterprise10;
    "urn:scim:schemas:extension:slack:guest:1.0"?: UrnScimSchemasExtensionSlackGuest10;
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

export interface UrnScimSchemasExtensionEnterprise10 {
    manager?: Manager;
}

export interface Manager {
}

export interface UrnScimSchemasExtensionSlackGuest10 {
    type?:       string;
    expiration?: string;
}

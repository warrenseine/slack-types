export interface GroupsResponse {
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
    schemas?:     string[];
    id?:          string;
    meta?:        Meta;
    displayName?: string;
    members?:     Member[];
}

export interface Member {
    value?:   string;
    display?: string;
}

export interface Meta {
    created?:  string;
    location?: string;
}

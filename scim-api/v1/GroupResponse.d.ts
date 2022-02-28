export interface GroupResponse {
    schemas?:     string[];
    id?:          string;
    displayName?: string;
    members?:     Member[];
    meta?:        Meta;
}

export interface Member {
    value?:   string;
    display?: string;
}

export interface Meta {
    created?:  string;
    location?: string;
}

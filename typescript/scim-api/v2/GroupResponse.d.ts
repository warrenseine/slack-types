export interface GroupResponse {
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

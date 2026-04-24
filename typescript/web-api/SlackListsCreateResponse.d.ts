export interface SlackListsCreateResponse {
    ok?:            boolean;
    list_id?:       string;
    list_metadata?: ListMetadata;
    error?:         string;
    needed?:        string;
    provided?:      string;
    warning?:       string;
}

export interface ListMetadata {
    schema?:         Schema[];
    subtask_schema?: SubtaskSchema[];
    views?:          View[];
    integrations?:   string[];
}

export interface Schema {
    key?:               string;
    name?:              string;
    is_primary_column?: boolean;
    type?:              string;
    id?:                string;
    options?:           SchemaOptions;
}

export interface SchemaOptions {
    format?:           string;
    show_member_name?: boolean;
    choices?:          Choice[];
}

export interface Choice {
    value?: string;
    label?: string;
    color?: string;
}

export interface SubtaskSchema {
    key?:               string;
    name?:              string;
    is_primary_column?: boolean;
    type?:              string;
    id?:                string;
    options?:           SubtaskSchemaOptions;
}

export interface SubtaskSchemaOptions {
    format?:           string;
    show_member_name?: boolean;
}

export interface View {
    id?:        string;
    name?:      string;
    type?:      string;
    is_locked?: boolean;
    position?:  string;
}

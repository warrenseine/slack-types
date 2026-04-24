export interface SchemasResponse {
    schemas?:  Schema[];
    ok?:       boolean;
    error?:    string;
    needed?:   string;
    provided?: string;
    warning?:  string;
}

export interface Schema {
    type?:              string;
    workspace?:         Enterprise;
    enterprise?:        Enterprise;
    user?:              User;
    file?:              Canvas;
    channel?:           Channel;
    app?:               App;
    workflow?:          AccountTypeRole;
    barrier?:           Barrier;
    message?:           Message;
    usergroup?:         AccountTypeRole;
    role?:              Role;
    account_type_role?: AccountTypeRole;
    canvas?:            Canvas;
    workflow_v2?:       WorkflowV2;
    template?:          Template;
    legal_hold_policy?: AccountTypeRole;
}

export interface AccountTypeRole {
    id?:   string;
    name?: string;
}

export interface App {
    id?:                    string;
    name?:                  string;
    is_distributed?:        string;
    is_directory_approved?: string;
    is_workflow_app?:       string;
    scopes?:                string;
    app_id?:                string;
    distribution_type?:     string;
    user_ids?:              string;
}

export interface Barrier {
    id?:                       string;
    primary_usergroup?:        string;
    barriered_from_usergroup?: string;
}

export interface Canvas {
    id?:       string;
    filetype?: string;
    title?:    string;
    name?:     string;
}

export interface Channel {
    id?:                string;
    name?:              string;
    privacy?:           string;
    is_shared?:         string;
    is_org_shared?:     string;
    teams_shared_with?: string;
}

export interface Enterprise {
    id?:     string;
    name?:   string;
    domain?: string;
}

export interface Message {
    team?:      string;
    channel?:   string;
    timestamp?: string;
}

export interface Role {
    id?:   string;
    name?: string;
    type?: string;
}

export interface Template {
    id?:            string;
    template_name?: string;
}

export interface User {
    id?:           string;
    name?:         string;
    email?:        string;
    team?:         string;
    account_type?: string;
}

export interface WorkflowV2 {
    id?:                    string;
    app_id?:                string;
    date_updated?:          string;
    callback_id?:           string;
    name?:                  string;
    updated_by?:            string;
    step_configuration?:    string;
    template_id?:           string;
    suspicious_keywords?:   string;
    trigger_name?:          string;
    trigger_channels?:      string;
    trigger_configuration?: string;
}

export interface AdminUsersListResponse {
    ok?:                boolean;
    users?:             User[];
    response_metadata?: ResponseMetadata;
    error?:             string;
    needed?:            string;
    provided?:          string;
    warning?:           string;
}

export interface ResponseMetadata {
    next_cursor?: string;
    messages?:    string[];
}

export interface User {
    id?:                  string;
    email?:               string;
    is_admin?:            boolean;
    is_owner?:            boolean;
    is_primary_owner?:    boolean;
    is_restricted?:       boolean;
    is_ultra_restricted?: boolean;
    is_bot?:              boolean;
    expiration_ts?:       number;
    username?:            string;
    full_name?:           string;
    is_active?:           boolean;
    date_created?:        number;
    roles?:               string[];
    workspaces?:          string[];
    has_2fa?:             boolean;
    has_sso?:             boolean;
    last_active_ts?:      number;
}

export interface AppsEventAuthorizationsListResponse {
    ok?:             boolean;
    error?:          string;
    authorizations?: Authorization[];
    needed?:         string;
    provided?:       string;
    warning?:        string;
}

export interface Authorization {
    enterprise_id?:         string;
    team_id?:               string;
    user_id?:               string;
    is_bot?:                boolean;
    is_enterprise_install?: boolean;
}

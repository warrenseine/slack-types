export interface UsergroupsDisableResponse {
    ok?:        boolean;
    usergroup?: Usergroup;
    error?:     string;
    needed?:    string;
    provided?:  string;
    warning?:   string;
}

export interface Usergroup {
    id?:                    string;
    team_id?:               string;
    is_usergroup?:          boolean;
    is_subteam?:            boolean;
    name?:                  string;
    description?:           string;
    handle?:                string;
    is_external?:           boolean;
    date_create?:           number;
    date_update?:           number;
    date_delete?:           number;
    auto_provision?:        boolean;
    enterprise_subteam_id?: string;
    created_by?:            string;
    updated_by?:            string;
    deleted_by?:            string;
    prefs?:                 Prefs;
    channel_count?:         number;
    users?:                 string[];
    is_section?:            boolean;
    is_idp_group?:          boolean;
    is_visible?:            boolean;
    is_editing_restricted?: boolean;
    is_membership_locked?:  boolean;
    is_org_level?:          boolean;
}

export interface Prefs {
    channels?: string[];
    groups?:   string[];
}

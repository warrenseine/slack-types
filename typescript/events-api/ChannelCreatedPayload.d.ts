export interface ChannelCreatedPayload {
    token?:                 string;
    team_id?:               string;
    enterprise_id?:         string;
    api_app_id?:            string;
    event?:                 Event;
    type?:                  string;
    event_id?:              string;
    event_time?:            number;
    authorizations?:        Authorization[];
    is_ext_shared_channel?: boolean;
    event_context?:         string;
}

export interface Authorization {
    enterprise_id?:         string;
    team_id?:               string;
    user_id?:               string;
    is_bot?:                boolean;
    is_enterprise_install?: boolean;
}

export interface Event {
    type?:     string;
    channel?:  Channel;
    event_ts?: string;
}

export interface Channel {
    id?:                         string;
    is_channel?:                 boolean;
    name?:                       string;
    name_normalized?:            string;
    created?:                    number;
    creator?:                    string;
    is_shared?:                  boolean;
    is_org_shared?:              boolean;
    context_team_id?:            string;
    is_group?:                   boolean;
    is_im?:                      boolean;
    is_mpim?:                    boolean;
    is_private?:                 boolean;
    is_archived?:                boolean;
    is_general?:                 boolean;
    unlinked?:                   number;
    is_pending_ext_shared?:      boolean;
    pending_shared?:             string[];
    updated?:                    number;
    is_moved?:                   number;
    is_ext_shared?:              boolean;
    shared_team_ids?:            string[];
    internal_team_ids?:          string[];
    pending_connected_team_ids?: string[];
    topic?:                      Purpose;
    purpose?:                    Purpose;
    previous_names?:             string[];
}

export interface Purpose {
    value?:    string;
    creator?:  string;
    last_set?: number;
}

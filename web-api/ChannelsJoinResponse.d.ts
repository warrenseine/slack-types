export interface ChannelsJoinResponse {
    ok?:       boolean;
    channel?:  Channel;
    error?:    string;
    needed?:   string;
    provided?: string;
}

export interface Channel {
    id?:                   string;
    name?:                 string;
    is_channel?:           boolean;
    created?:              number;
    is_archived?:          boolean;
    is_general?:           boolean;
    unlinked?:             number;
    creator?:              string;
    name_normalized?:      string;
    is_shared?:            boolean;
    is_org_shared?:        boolean;
    is_member?:            boolean;
    is_private?:           boolean;
    is_mpim?:              boolean;
    last_read?:            string;
    latest?:               Latest;
    unread_count?:         number;
    unread_count_display?: number;
    members?:              string[];
    topic?:                Purpose;
    purpose?:              Purpose;
    previous_names?:       string[];
    priority?:             number;
}

export interface Latest {
    type?:    string;
    subtype?: string;
    ts?:      string;
    user?:    string;
    text?:    string;
}

export interface Purpose {
    value?:    string;
    creator?:  string;
    last_set?: number;
}

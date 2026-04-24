export interface AdminConversationsSearchResponse {
    ok?:                boolean;
    conversations?:     Conversation[];
    next_cursor?:       string;
    error?:             string;
    needed?:            string;
    provided?:          string;
    total_count?:       number;
    response_metadata?: ResponseMetadata;
    warning?:           string;
}

export interface Conversation {
    id?:                            string;
    name?:                          string;
    purpose?:                       string;
    member_count?:                  number;
    created?:                       number;
    creator_id?:                    string;
    is_private?:                    boolean;
    is_archived?:                   boolean;
    is_general?:                    boolean;
    last_activity_ts?:              number;
    is_ext_shared?:                 boolean;
    is_global_shared?:              boolean;
    is_org_default?:                boolean;
    is_org_mandatory?:              boolean;
    is_org_shared?:                 boolean;
    is_frozen?:                     boolean;
    internal_team_ids_count?:       number;
    internal_team_ids_sample_team?: string;
    pending_connected_team_ids?:    string[];
    is_pending_ext_shared?:         boolean;
    connected_team_ids?:            string[];
    conversation_host_id?:          string;
    channel_email_addresses?:       ChannelEmailAddress[];
    connected_limited_team_ids?:    string[];
    external_user_count?:           number;
    internal_team_ids?:             string[];
    channel_manager_count?:         number;
    is_disconnect_in_progress?:     boolean;
    canvas?:                        ListsClass;
    context_team_id?:               string;
    lists?:                         ListsClass;
    properties?:                    Properties;
}

export interface ListsClass {
    total_count?:       number;
    ownership_details?: OwnershipDetail[];
}

export interface OwnershipDetail {
    count?:   number;
    team_id?: string;
}

export interface ChannelEmailAddress {
    team_id?:         string;
    user_id?:         string;
    conversation_id?: string;
    date_created?:    number;
    address?:         string;
    name?:            string;
    icons?:           Icons;
}

export interface Icons {
    image_36?: string;
    image_48?: string;
    image_72?: string;
}

export interface Properties {
    canvas?:                           PropertiesCanvas;
    posting_restricted_to?:            PostingRestrictedTo;
    threads_restricted_to?:            ThreadsRestrictedTo;
    huddles_restricted?:               boolean;
    at_here_restricted?:               boolean;
    at_channel_restricted?:            boolean;
    tabs?:                             Tab[];
    tabz?:                             Tab[];
    meeting_notes?:                    MeetingNotes;
    is_dormant?:                       boolean;
    has_slack_connect_invite_created?: boolean;
}

export interface PropertiesCanvas {
    file_id?:        string;
    is_empty?:       boolean;
    quip_thread_id?: string;
    is_migrated?:    boolean;
}

export interface MeetingNotes {
    file_id?: string;
}

export interface PostingRestrictedTo {
    type?: string[];
    user?: string[];
}

export interface Tab {
    id?:          string;
    label?:       string;
    type?:        string;
    data?:        Data;
    is_disabled?: boolean;
}

export interface Data {
    file_id?:   string;
    shared_ts?: string;
}

export interface ThreadsRestrictedTo {
    type?: string[];
}

export interface ResponseMetadata {
    messages?: string[];
}

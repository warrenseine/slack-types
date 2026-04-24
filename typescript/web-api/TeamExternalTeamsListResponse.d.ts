export interface TeamExternalTeamsListResponse {
    ok?:                boolean;
    organizations?:     Organization[];
    total_count?:       number;
    response_metadata?: ResponseMetadata;
    error?:             string;
    needed?:            string;
    provided?:          string;
    warning?:           string;
}

export interface Organization {
    team_id?:               string;
    team_name?:             string;
    team_domain?:           string;
    public_channel_count?:  number;
    private_channel_count?: number;
    im_channel_count?:      number;
    mpim_channel_count?:    number;
    connected_workspaces?:  ConnectedWorkspace[];
    slack_connect_prefs?:   SlackConnectPrefs;
    connection_status?:     string;
    last_active_timestamp?: number;
    is_sponsored?:          boolean;
    canvas?:                Canvas;
    lists?:                 Canvas;
}

export interface Canvas {
    total_count?:       number;
    ownership_details?: OwnershipDetail[];
}

export interface OwnershipDetail {
    team_id?: string;
    count?:   number;
}

export interface ConnectedWorkspace {
    workspace_id?:   string;
    workspace_name?: string;
}

export interface SlackConnectPrefs {
    allow_sc_file_uploads?:           AllowScFileUploads;
    approved_org_info?:               AllowScFileUploads;
    profile_visibility?:              AllowScFileUploads;
    allowed_workspaces?:              AllowedWorkspaces;
    allowed_canvas_sharing?:          AllowScFileUploads;
    allowed_list_sharing?:            AllowScFileUploads;
    away_team_sc_invite_permissions?: AllowedWorkspaces;
    away_team_sc_invite_require_2fa?: AllowScFileUploads;
    accept_sc_invites?:               AcceptScInvites;
    sc_channel_limited_access?:       AllowScFileUploads;
    sc_mpdm_to_private?:              ScMpdmToPrivate;
    external_awareness_context_bar?:  AllowScFileUploads;
    require_sc_channel_for_sc_dm?:    AllowScFileUploads;
    shared_channel_invite_requested?: SharedChannelInviteRequested;
}

export interface AcceptScInvites {
    type?:                    string;
    accept_in_workspace_ids?: string[];
    invalid_workspace_ids?:   string[];
    use_allowed_workspaces?:  boolean;
    accept_private?:          boolean;
    actor?:                   string;
    date_update?:             number;
    source?:                  string;
}

export interface AllowScFileUploads {
    value?:         boolean;
    actor?:         string;
    date_update?:   number;
    source?:        string;
    approval_type?: string;
    type?:          boolean | string;
}

export interface AllowedWorkspaces {
    type?:        string;
    team_ids?:    string[];
    actor?:       string;
    date_update?: number;
    source?:      string;
}

export interface ScMpdmToPrivate {
    type?:                   string;
    accept_in_workspace_id?: string;
    invalid_workspace_ids?:  string[];
    actor?:                  string;
    date_update?:            number;
    source?:                 string;
}

export interface SharedChannelInviteRequested {
    enabled?:              boolean;
    usergroup_include?:    UsergroupClude;
    usergroup_exclude?:    UsergroupClude;
    approval_destination?: ApprovalDestination;
    actor?:                string;
    date_update?:          number;
    source?:               string;
}

export interface ApprovalDestination {
    all_who_can_manage_shared_channels?: boolean;
    channel_id?:                         string;
}

export interface UsergroupClude {
    id?:      string;
    team_id?: string;
}

export interface ResponseMetadata {
    next_cursor?: string;
    messages?:    string[];
}

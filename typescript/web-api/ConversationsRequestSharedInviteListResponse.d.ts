export interface ConversationsRequestSharedInviteListResponse {
    ok?:              boolean;
    invite_requests?: InviteRequest[];
    error?:           string;
    needed?:          string;
    provided?:        string;
}

export interface InviteRequest {
    id?:                  string;
    date_created?:        number;
    expires_at?:          number;
    inviting_team?:       Team;
    inviting_user?:       InvitingUser;
    channel?:             Channel;
    is_external_limited?: boolean;
    date_last_updated?:   number;
    target_user?:         TargetUser;
}

export interface Channel {
    id?:                   string;
    is_im?:                boolean;
    is_private?:           boolean;
    date_created?:         number;
    name?:                 string;
    connections?:          Connection[];
    pending_connections?:  Connection[];
    previous_connections?: Connection[];
}

export interface Connection {
    team?:       Team;
    is_private?: boolean;
}

export interface Team {
    id?:                   string;
    name?:                 string;
    icon?:                 Icon;
    avatar_base_url?:      string;
    is_verified?:          boolean;
    domain?:               string;
    date_created?:         number;
    requires_sponsorship?: boolean;
}

export interface Icon {
    image_default?: boolean;
    image_34?:      string;
    image_44?:      string;
    image_68?:      string;
    image_88?:      string;
    image_102?:     string;
    image_230?:     string;
    image_132?:     string;
}

export interface InvitingUser {
    id?:                         string;
    team_id?:                    string;
    name?:                       string;
    updated?:                    number;
    who_can_share_contact_card?: string;
    profile?:                    Profile;
}

export interface Profile {
    real_name?:               string;
    display_name?:            string;
    real_name_normalized?:    string;
    display_name_normalized?: string;
    team?:                    string;
    avatar_hash?:             string;
    email?:                   string;
    image_24?:                string;
    image_32?:                string;
    image_48?:                string;
    image_72?:                string;
    image_192?:               string;
    image_512?:               string;
}

export interface TargetUser {
    recipient_email?: string;
}

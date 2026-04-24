export interface AdminInviteRequestsDeniedListResponse {
    ok?:                boolean;
    denied_requests?:   DeniedRequest[];
    error?:             string;
    needed?:            string;
    provided?:          string;
    response_metadata?: ResponseMetadata;
    warning?:           string;
}

export interface DeniedRequest {
    invite_request?: InviteRequest;
    denied_by?:      DeniedBy;
}

export interface DeniedBy {
    actor_type?: string;
    actor_id?:   string;
}

export interface InviteRequest {
    id?:             string;
    email?:          string;
    date_created?:   number;
    requester_ids?:  string[];
    channel_ids?:    string[];
    invite_type?:    string;
    request_reason?: string;
}

export interface ResponseMetadata {
    next_cursor?: string;
}

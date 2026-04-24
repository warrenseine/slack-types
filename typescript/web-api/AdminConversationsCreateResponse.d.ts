export interface AdminConversationsCreateResponse {
    ok?:                boolean;
    channel_id?:        string;
    error?:             string;
    needed?:            string;
    provided?:          string;
    response_metadata?: ResponseMetadata;
    warning?:           string;
}

export interface ResponseMetadata {
    messages?: string[];
}

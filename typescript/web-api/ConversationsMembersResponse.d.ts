export interface ConversationsMembersResponse {
    ok?:                boolean;
    members?:           string[];
    response_metadata?: ResponseMetadata;
    error?:             string;
    needed?:            string;
    provided?:          string;
    warning?:           string;
}

export interface ResponseMetadata {
    next_cursor?: string;
}

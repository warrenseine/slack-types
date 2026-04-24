export interface TeamExternalTeamsDisconnectResponse {
    ok?:                boolean;
    error?:             string;
    response_metadata?: ResponseMetadata;
    needed?:            string;
    provided?:          string;
    warning?:           string;
}

export interface ResponseMetadata {
    messages?: string[];
}

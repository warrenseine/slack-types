export interface ChatUnfurlResponse {
    ok?:                boolean;
    error?:             string;
    needed?:            string;
    provided?:          string;
    callstack?:         string;
    warning?:           string;
    response_metadata?: ResponseMetadata;
}

export interface ResponseMetadata {
    messages?: string[];
    warnings?: string[];
}

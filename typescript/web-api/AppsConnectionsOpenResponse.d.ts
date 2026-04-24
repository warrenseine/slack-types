export interface AppsConnectionsOpenResponse {
    ok?:                boolean;
    error?:             string;
    needed?:            string;
    provided?:          string;
    url?:               string;
    warning?:           string;
    response_metadata?: ResponseMetadata;
}

export interface ResponseMetadata {
    messages?: string[];
}

export interface AdminAnalyticsGetFileResponse {
    ok?:                boolean;
    error?:             string;
    needed?:            string;
    provided?:          string;
    response_metadata?: ResponseMetadata;
    warning?:           string;
}

export interface ResponseMetadata {
    messages?: string[];
}

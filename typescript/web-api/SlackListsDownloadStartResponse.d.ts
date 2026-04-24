export interface SlackListsDownloadStartResponse {
    ok?:                boolean;
    job_id?:            string;
    response_metadata?: ResponseMetadata;
    error?:             string;
    needed?:            string;
    provided?:          string;
    warning?:           string;
}

export interface ResponseMetadata {
    messages?: string[];
}

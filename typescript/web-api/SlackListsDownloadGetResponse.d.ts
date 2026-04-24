export interface SlackListsDownloadGetResponse {
    ok?:                boolean;
    status?:            string;
    download_url?:      string;
    response_metadata?: ResponseMetadata;
    error?:             string;
    needed?:            string;
    provided?:          string;
    warning?:           string;
}

export interface ResponseMetadata {
    messages?: string[];
}

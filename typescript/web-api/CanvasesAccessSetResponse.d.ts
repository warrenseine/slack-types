export interface CanvasesAccessSetResponse {
    ok?:                           boolean;
    error?:                        string;
    failed_to_update_channel_ids?: string[];
    failed_to_update_user_ids?:    string[];
    response_metadata?:            ResponseMetadata;
    needed?:                       string;
    provided?:                     string;
    warning?:                      string;
}

export interface ResponseMetadata {
}

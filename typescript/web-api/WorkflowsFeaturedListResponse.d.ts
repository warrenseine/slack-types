export interface WorkflowsFeaturedListResponse {
    ok?:                  boolean;
    error?:               string;
    needed?:              string;
    provided?:            string;
    warning?:             string;
    invalid_channel_ids?: string[];
}

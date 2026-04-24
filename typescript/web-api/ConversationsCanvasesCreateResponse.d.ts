export interface ConversationsCanvasesCreateResponse {
    ok?:                boolean;
    canvas_id?:         string;
    detail?:            string;
    error?:             string;
    response_metadata?: ResponseMetadata;
    needed?:            string;
    provided?:          string;
    warning?:           string;
}

export interface ResponseMetadata {
    messages?: string[];
}

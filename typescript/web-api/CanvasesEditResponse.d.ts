export interface CanvasesEditResponse {
    ok?:                boolean;
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

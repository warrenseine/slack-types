export interface AppsManifestValidateResponse {
    ok?:                boolean;
    error?:             string;
    response_metadata?: ResponseMetadata;
    needed?:            string;
    provided?:          string;
    errors?:            Error[];
    warning?:           string;
}

export interface Error {
    code?:              string;
    message?:           string;
    pointer?:           string;
    related_component?: string;
}

export interface ResponseMetadata {
    messages?: string[];
}

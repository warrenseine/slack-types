export interface CanvasesSectionsLookupResponse {
    ok?:                boolean;
    error?:             string;
    sections?:          Section[];
    response_metadata?: ResponseMetadata;
    needed?:            string;
    provided?:          string;
    warning?:           string;
}

export interface ResponseMetadata {
    messages?: string[];
}

export interface Section {
    id?: string;
}

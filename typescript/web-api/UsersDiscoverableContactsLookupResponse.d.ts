export interface UsersDiscoverableContactsLookupResponse {
    ok?:                boolean;
    error?:             string;
    needed?:            string;
    provided?:          string;
    response_metadata?: ResponseMetadata;
    is_discoverable?:   boolean;
}

export interface ResponseMetadata {
    messages?: string[];
}

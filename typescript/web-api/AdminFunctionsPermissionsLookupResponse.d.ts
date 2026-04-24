export interface AdminFunctionsPermissionsLookupResponse {
    ok?:                boolean;
    permissions?:       { [key: string]: Permission };
    errors?:            Errors;
    error?:             string;
    needed?:            string;
    provided?:          string;
    response_metadata?: ResponseMetadata;
    metadata?:          { [key: string]: Errors };
    warning?:           string;
}

export interface Errors {
}

export interface Permission {
    distribution?:     AllowedByAdmin;
    allowed_entities?: AllowedEntities;
    allowed_by_admin?: AllowedByAdmin;
}

export interface AllowedByAdmin {
    type?:     string;
    user_ids?: string[];
}

export interface AllowedEntities {
    type?:        string;
    user_ids?:    string[];
    team_ids?:    string[];
    org_ids?:     string[];
    channel_ids?: string[];
}

export interface ResponseMetadata {
    messages?: string[];
}

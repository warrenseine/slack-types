export interface AdminAppsConfigLookupResponse {
    ok?:                boolean;
    error?:             string;
    response_metadata?: ResponseMetadata;
    needed?:            string;
    provided?:          string;
    configs?:           Config[];
    warning?:           string;
}

export interface Config {
    app_id?:                 string;
    workflow_auth_strategy?: string;
    domain_restrictions?:    DomainRestrictions;
}

export interface DomainRestrictions {
    emails?: string[];
    urls?:   string[];
}

export interface ResponseMetadata {
    messages?: string[];
}

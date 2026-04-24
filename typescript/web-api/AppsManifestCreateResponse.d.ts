export interface AppsManifestCreateResponse {
    ok?:                  boolean;
    error?:               string;
    response_metadata?:   ResponseMetadata;
    needed?:              string;
    provided?:            string;
    errors?:              Error[];
    app_id?:              string;
    credentials?:         Credentials;
    oauth_authorize_url?: string;
    team_id?:             string;
    team_domain?:         string;
    warning?:             string;
}

export interface Credentials {
    client_id?:          string;
    client_secret?:      string;
    verification_token?: string;
    signing_secret?:     string;
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

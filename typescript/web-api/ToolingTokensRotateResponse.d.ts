export interface ToolingTokensRotateResponse {
    ok?:                boolean;
    error?:             string;
    response_metadata?: ResponseMetadata;
    needed?:            string;
    provided?:          string;
    token?:             string;
    refresh_token?:     string;
    team_id?:           string;
    user_id?:           string;
    iat?:               number;
    exp?:               number;
}

export interface ResponseMetadata {
    messages?: string[];
}

export interface ConversationsKickResponse {
    ok?:       boolean;
    error?:    string;
    needed?:   string;
    provided?: string;
    errors?:   Errors;
    warning?:  string;
}

export interface Errors {
}

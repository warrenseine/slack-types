export interface ApiTestResponse {
    ok?:       boolean;
    error?:    string;
    args?:     Args;
    needed?:   string;
    provided?: string;
    warning?:  string;
}

export interface Args {
    error?: string;
    foo?:   string;
}

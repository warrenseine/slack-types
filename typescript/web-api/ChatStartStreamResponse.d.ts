export interface ChatStartStreamResponse {
    ok?:       boolean;
    ts?:       string;
    error?:    string;
    needed?:   string;
    provided?: string;
    channel?:  string;
    warning?:  string;
}

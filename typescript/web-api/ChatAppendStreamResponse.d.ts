export interface ChatAppendStreamResponse {
    ok?:       boolean;
    error?:    string;
    needed?:   string;
    provided?: string;
    channel?:  string;
    ts?:       string;
    warning?:  string;
}

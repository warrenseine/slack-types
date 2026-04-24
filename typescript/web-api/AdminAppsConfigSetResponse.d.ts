export interface AdminAppsConfigSetResponse {
    ok?:       boolean;
    error?:    string;
    needed?:   string;
    provided?: string;
    warning?:  string;
}

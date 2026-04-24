export interface AppsManifestDeleteResponse {
    ok?:       boolean;
    error?:    string;
    needed?:   string;
    provided?: string;
    warning?:  string;
}

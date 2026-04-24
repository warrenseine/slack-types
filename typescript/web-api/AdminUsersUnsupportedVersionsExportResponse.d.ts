export interface AdminUsersUnsupportedVersionsExportResponse {
    ok?:       boolean;
    error?:    string;
    needed?:   string;
    provided?: string;
    warning?:  string;
}

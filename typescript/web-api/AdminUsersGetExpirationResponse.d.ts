export interface AdminUsersGetExpirationResponse {
    ok?:       boolean;
    error?:    string;
    needed?:   string;
    provided?: string;
    user?:     User;
}

export interface User {
    id?:                  string;
    email?:               string;
    is_restricted?:       boolean;
    is_ultra_restricted?: boolean;
    expiration_ts?:       number;
}

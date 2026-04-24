export interface AppsManifestUpdateResponse {
    ok?:                  boolean;
    app_id?:              string;
    permissions_updated?: boolean;
    error?:               string;
    needed?:              string;
    provided?:            string;
    warning?:             string;
}

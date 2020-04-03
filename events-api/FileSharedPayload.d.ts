export interface FileSharedPayload {
    token?:         string;
    team_id?:       string;
    enterprise_id?: string;
    api_app_id?:    string;
    event?:         Event;
    type?:          string;
    event_id?:      string;
    event_time?:    number;
    authed_users?:  string[];
}

export interface Event {
    type?:       string;
    channel_id?: string;
    file_id?:    string;
    user_id?:    string;
    file?:       File;
    event_ts?:   string;
}

export interface File {
    id?: string;
}

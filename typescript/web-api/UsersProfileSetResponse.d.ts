export interface UsersProfileSetResponse {
    profile?:  Profile;
    ok?:       boolean;
    username?: string;
    error?:    string;
    needed?:   string;
    provided?: string;
    warning?:  string;
}

export interface Profile {
    title?:                      string;
    phone?:                      string;
    skype?:                      string;
    real_name?:                  string;
    real_name_normalized?:       string;
    display_name?:               string;
    display_name_normalized?:    string;
    fields?:                     { [key: string]: Field };
    status_text?:                string;
    status_emoji?:               string;
    status_expiration?:          number;
    avatar_hash?:                string;
    image_original?:             string;
    is_custom_image?:            boolean;
    email?:                      string;
    first_name?:                 string;
    last_name?:                  string;
    image_24?:                   string;
    image_32?:                   string;
    image_48?:                   string;
    image_72?:                   string;
    image_192?:                  string;
    image_512?:                  string;
    image_1024?:                 string;
    status_text_canonical?:      string;
    status_emoji_url?:           string;
    pronouns?:                   string;
    huddle_state?:               string;
    huddle_state_expiration_ts?: number;
    status_emoji_display_info?:  StatusEmojiDisplayInfo[];
    start_date?:                 string;
    status_clear_on_focus_end?:  boolean;
}

export interface Field {
    value?: string;
    alt?:   string;
}

export interface StatusEmojiDisplayInfo {
    emoji_name?:    string;
    display_alias?: string;
    display_url?:   string;
    unicode?:       string;
}

export interface ConversationsOpenResponse {
    ok?:           boolean;
    channel?:      Channel;
    no_op?:        boolean;
    already_open?: boolean;
    error?:        string;
    needed?:       string;
    provided?:     string;
}

export interface Channel {
    id?:                   string;
    created?:              number;
    is_archived?:          boolean;
    is_im?:                boolean;
    is_org_shared?:        boolean;
    user?:                 string;
    last_read?:            string;
    latest?:               Latest;
    unread_count?:         number;
    unread_count_display?: number;
    is_open?:              boolean;
    priority?:             number;
}

export interface Latest {
    type?:          string;
    subtype?:       string;
    text?:          string;
    ts?:            string;
    bot_id?:        string;
    blocks?:        Block[];
    client_msg_id?: string;
    user?:          string;
    team?:          string;
    bot_profile?:   BotProfile;
}

export interface Block {
    type?:                     string;
    block_id?:                 string;
    elements?:                 Accessory[];
    text?:                     Hint;
    accessory?:                Accessory;
    call_id?:                  string;
    api_decoration_available?: boolean;
    call?:                     Call;
    external_id?:              string;
    source?:                   string;
    fallback?:                 string;
    image_url?:                string;
    image_width?:              number;
    image_height?:             number;
    image_bytes?:              number;
    alt_text?:                 string;
    title?:                    Hint;
    fields?:                   Hint[];
    label?:                    Hint;
    element?:                  Accessory;
    dispatch_action?:          boolean;
    hint?:                     Hint;
    optional?:                 boolean;
}

export interface Accessory {
    type?:                            string;
    action_id?:                       string;
    options?:                         Option[];
    min_query_length?:                number;
    text?:                            Hint;
    url?:                             string;
    value?:                           string;
    style?:                           string;
    confirm?:                         Confirm;
    accessibility_label?:             string;
    initial_options?:                 Option[];
    focus_on_load?:                   boolean;
    initial_option?:                  Option;
    placeholder?:                     Hint;
    initial_channel?:                 string;
    response_url_enabled?:            boolean;
    initial_channels?:                string[];
    max_selected_items?:              number;
    initial_conversation?:            string;
    default_to_current_conversation?: boolean;
    filter?:                          Filter;
    initial_conversations?:           string[];
    initial_date?:                    string;
    initial_time?:                    string;
    image_url?:                       string;
    alt_text?:                        string;
    fallback?:                        string;
    image_width?:                     number;
    image_height?:                    number;
    image_bytes?:                     number;
    option_groups?:                   OptionGroup[];
    initial_user?:                    string;
    initial_users?:                   string[];
}

export interface Confirm {
    title?:   Hint;
    text?:    Hint;
    confirm?: Hint;
    deny?:    Hint;
    style?:   string;
}

export interface Hint {
    type?:     string;
    text?:     string;
    emoji?:    boolean;
    verbatim?: boolean;
}

export interface Filter {
    include?:                          string[];
    exclude_external_shared_channels?: boolean;
    exclude_bot_users?:                boolean;
}

export interface Option {
    text?:        Hint;
    value?:       string;
    description?: Hint;
    url?:         string;
}

export interface OptionGroup {
    label?:   Hint;
    options?: Option[];
}

export interface Call {
    v1?:                 V1;
    media_backend_type?: string;
}

export interface V1 {
    id?:                   string;
    app_id?:               string;
    app_icon_urls?:        AppIconUrls;
    date_start?:           number;
    active_participants?:  Participant[];
    all_participants?:     Participant[];
    display_id?:           string;
    join_url?:             string;
    desktop_app_join_url?: string;
    name?:                 string;
    created_by?:           string;
    date_end?:             number;
    channels?:             string[];
    is_dm_call?:           boolean;
    was_rejected?:         boolean;
    was_missed?:           boolean;
    was_accepted?:         boolean;
    has_ended?:            boolean;
}

export interface Participant {
    slack_id?:     string;
    external_id?:  string;
    display_name?: string;
    avatar_url?:   string;
}

export interface AppIconUrls {
    image_32?:       string;
    image_36?:       string;
    image_48?:       string;
    image_64?:       string;
    image_72?:       string;
    image_96?:       string;
    image_128?:      string;
    image_192?:      string;
    image_512?:      string;
    image_1024?:     string;
    image_original?: string;
}

export interface BotProfile {
    id?:      string;
    deleted?: boolean;
    name?:    string;
    updated?: number;
    app_id?:  string;
    icons?:   Icons;
    team_id?: string;
}

export interface Icons {
    image_36?: string;
    image_48?: string;
    image_72?: string;
}

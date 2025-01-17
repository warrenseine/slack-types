export interface FilesListResponse {
    ok?:       boolean;
    files?:    File[];
    paging?:   Paging;
    error?:    string;
    needed?:   string;
    provided?: string;
}

export interface File {
    id?:                        string;
    created?:                   number;
    timestamp?:                 number;
    name?:                      string;
    title?:                     string;
    mimetype?:                  string;
    filetype?:                  string;
    pretty_type?:               string;
    user?:                      string;
    editable?:                  boolean;
    size?:                      number;
    mode?:                      string;
    is_external?:               boolean;
    external_type?:             string;
    is_public?:                 boolean;
    public_url_shared?:         boolean;
    display_as_bot?:            boolean;
    username?:                  string;
    url_private?:               string;
    url_private_download?:      string;
    permalink?:                 string;
    permalink_public?:          string;
    edit_link?:                 string;
    preview?:                   string;
    preview_highlight?:         string;
    lines?:                     number;
    lines_more?:                number;
    preview_is_truncated?:      boolean;
    channels?:                  string[];
    groups?:                    string[];
    ims?:                       string[];
    comments_count?:            number;
    media_display_type?:        string;
    thumb_64?:                  string;
    thumb_80?:                  string;
    thumb_360?:                 string;
    thumb_360_w?:               number;
    thumb_360_h?:               number;
    thumb_160?:                 string;
    original_w?:                number;
    original_h?:                number;
    thumb_tiny?:                string;
    thumb_480?:                 string;
    thumb_480_w?:               number;
    thumb_480_h?:               number;
    thumb_360_gif?:             string;
    thumb_480_gif?:             string;
    deanimate?:                 string;
    deanimate_gif?:             string;
    thumb_720?:                 string;
    thumb_720_w?:               number;
    thumb_720_h?:               number;
    thumb_800?:                 string;
    thumb_800_w?:               number;
    thumb_800_h?:               number;
    thumb_960?:                 string;
    thumb_960_w?:               number;
    thumb_960_h?:               number;
    thumb_1024?:                string;
    thumb_1024_w?:              number;
    thumb_1024_h?:              number;
    image_exif_rotation?:       number;
    subject?:                   string;
    non_owner_editable?:        boolean;
    editor?:                    string;
    last_editor?:               string;
    updated?:                   number;
    original_attachment_count?: number;
    external_id?:               string;
    external_url?:              string;
    app_id?:                    string;
    app_name?:                  string;
    thumb_64_gif?:              string;
    thumb_64_w?:                string;
    thumb_64_h?:                string;
    thumb_80_gif?:              string;
    thumb_80_w?:                string;
    thumb_80_h?:                string;
    thumb_160_gif?:             string;
    thumb_160_w?:               string;
    thumb_160_h?:               string;
    thumb_720_gif?:             string;
    thumb_800_gif?:             string;
    thumb_960_gif?:             string;
    thumb_1024_gif?:            string;
    thumb_video?:               string;
    thumb_gif?:                 string;
    thumb_pdf?:                 string;
    thumb_pdf_w?:               string;
    thumb_pdf_h?:               string;
    converted_pdf?:             string;
    pjpeg?:                     string;
    has_rich_preview?:          boolean;
    plain_text?:                string;
    preview_plain_text?:        string;
    has_more?:                  boolean;
    sent_to_self?:              boolean;
    shares?:                    Shares;
    to?:                        Cc[];
    from?:                      Cc[];
    cc?:                        Cc[];
    channel_actions_ts?:        string;
    channel_actions_count?:     number;
    headers?:                   Headers;
    simplified_html?:           string;
    bot_id?:                    string;
    initial_comment?:           InitialComment;
    num_stars?:                 number;
    is_starred?:                boolean;
    pinned_to?:                 string[];
    reactions?:                 Reaction[];
    blocks?:                    Block[];
}

export interface Block {
    type?:                     string;
    elements?:                 Accessory[];
    block_id?:                 string;
    call_id?:                  string;
    api_decoration_available?: boolean;
    call?:                     Call;
    external_id?:              string;
    source?:                   string;
    text?:                     Hint;
    fallback?:                 string;
    image_url?:                string;
    image_width?:              number;
    image_height?:             number;
    image_bytes?:              number;
    alt_text?:                 string;
    title?:                    Hint;
    fields?:                   Hint[];
    accessory?:                Accessory;
    label?:                    Hint;
    element?:                  Accessory;
    dispatch_action?:          boolean;
    hint?:                     Hint;
    optional?:                 boolean;
}

export interface Accessory {
    type?:                            string;
    text?:                            Hint;
    action_id?:                       string;
    url?:                             string;
    value?:                           string;
    style?:                           string;
    confirm?:                         Confirm;
    accessibility_label?:             string;
    options?:                         Option[];
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
    min_query_length?:                number;
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

export interface Cc {
    address?:  string;
    name?:     string;
    original?: string;
}

export interface Headers {
    date?:        string;
    in_reply_to?: string;
    reply_to?:    string;
    message_id?:  string;
}

export interface InitialComment {
    id?:        string;
    created?:   number;
    timestamp?: number;
    user?:      string;
    comment?:   string;
    channel?:   string;
    is_intro?:  boolean;
}

export interface Reaction {
    name?:  string;
    count?: number;
    users?: string[];
    url?:   string;
}

export interface Shares {
    public?:  { [key: string]: Private[] };
    private?: { [key: string]: Private[] };
}

export interface Private {
    share_user_id?:     string;
    reply_users?:       string[];
    reply_users_count?: number;
    reply_count?:       number;
    ts?:                string;
    thread_ts?:         string;
    latest_reply?:      string;
    channel_name?:      string;
    team_id?:           string;
}

export interface Paging {
    count?: number;
    total?: number;
    page?:  number;
    pages?: number;
}

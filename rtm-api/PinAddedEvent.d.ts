export interface PinAddedEvent {
    type?:        string;
    user?:        string;
    channel_id?:  string;
    item?:        Item;
    item_user?:   string;
    pin_count?:   number;
    pinned_info?: PinnedInfo;
    event_ts?:    string;
}

export interface Item {
    type?:       string;
    channel?:    string;
    created_by?: string;
    created?:    number;
    message?:    Message;
    file?:       File;
    comment?:    Comment;
}

export interface Comment {
    id?:        string;
    created?:   number;
    timestamp?: number;
    user?:      string;
    comment?:   string;
    channel?:   string;
    is_intro?:  boolean;
}

export interface File {
    id?:                        string;
    created?:                   number;
    timestamp?:                 number;
    name?:                      string;
    title?:                     string;
    subject?:                   string;
    mimetype?:                  string;
    filetype?:                  string;
    pretty_type?:               string;
    user?:                      string;
    mode?:                      string;
    editable?:                  boolean;
    non_owner_editable?:        boolean;
    editor?:                    string;
    last_editor?:               string;
    updated?:                   number;
    original_attachment_count?: number;
    is_external?:               boolean;
    external_type?:             string;
    external_id?:               string;
    external_url?:              string;
    username?:                  string;
    size?:                      number;
    url_private?:               string;
    url_private_download?:      string;
    app_id?:                    string;
    app_name?:                  string;
    thumb_64?:                  string;
    thumb_64_gif?:              string;
    thumb_64_w?:                string;
    thumb_64_h?:                string;
    thumb_80?:                  string;
    thumb_80_gif?:              string;
    thumb_80_w?:                string;
    thumb_80_h?:                string;
    thumb_160?:                 string;
    thumb_160_gif?:             string;
    thumb_160_w?:               string;
    thumb_160_h?:               string;
    thumb_360?:                 string;
    thumb_360_gif?:             string;
    thumb_360_w?:               string;
    thumb_360_h?:               string;
    thumb_480?:                 string;
    thumb_480_gif?:             string;
    thumb_480_w?:               string;
    thumb_480_h?:               string;
    thumb_720?:                 string;
    thumb_720_gif?:             string;
    thumb_720_w?:               string;
    thumb_720_h?:               string;
    thumb_800?:                 string;
    thumb_800_gif?:             string;
    thumb_800_w?:               string;
    thumb_800_h?:               string;
    thumb_960?:                 string;
    thumb_960_gif?:             string;
    thumb_960_w?:               string;
    thumb_960_h?:               string;
    thumb_1024?:                string;
    thumb_1024_gif?:            string;
    thumb_1024_w?:              string;
    thumb_1024_h?:              string;
    thumb_video?:               string;
    thumb_gif?:                 string;
    thumb_pdf?:                 string;
    thumb_pdf_w?:               string;
    thumb_pdf_h?:               string;
    thumb_tiny?:                string;
    converted_pdf?:             string;
    image_exif_rotation?:       number;
    original_w?:                string;
    original_h?:                string;
    deanimate?:                 string;
    deanimate_gif?:             string;
    pjpeg?:                     string;
    permalink?:                 string;
    permalink_public?:          string;
    edit_link?:                 string;
    has_rich_preview?:          boolean;
    media_display_type?:        string;
    preview_is_truncated?:      boolean;
    preview?:                   string;
    preview_highlight?:         string;
    plain_text?:                string;
    preview_plain_text?:        string;
    has_more?:                  boolean;
    sent_to_self?:              boolean;
    lines?:                     number;
    lines_more?:                number;
    is_public?:                 boolean;
    public_url_shared?:         boolean;
    display_as_bot?:            boolean;
    channels?:                  any[];
    groups?:                    any[];
    ims?:                       any[];
    shares?:                    Shares;
    to?:                        any[];
    from?:                      any[];
    cc?:                        any[];
    channel_actions_ts?:        string;
    channel_actions_count?:     number;
    headers?:                   Headers;
    simplified_html?:           string;
    bot_id?:                    string;
    initial_comment?:           Comment;
    num_stars?:                 number;
    is_starred?:                boolean;
    pinned_to?:                 any[];
    reactions?:                 any[];
    comments_count?:            number;
    attachments?:               any[];
    blocks?:                    any[];
}

export interface Headers {
    date?:        string;
    in_reply_to?: string;
    reply_to?:    string;
    message_id?:  string;
}

export interface Shares {
}

export interface Message {
    client_msg_id?: string;
    type?:          string;
    app_id?:        string;
    team?:          string;
    user?:          string;
    bot_id?:        string;
    bot_profile?:   BotProfile;
    text?:          string;
    blocks?:        Block[];
    attachments?:   Attachment[];
    ts?:            string;
    pinned_to?:     string[];
    permalink?:     string;
}

export interface Attachment {
    msg_subtype?:           string;
    fallback?:              string;
    callback_id?:           string;
    color?:                 string;
    pretext?:               string;
    service_url?:           string;
    service_name?:          string;
    service_icon?:          string;
    author_id?:             string;
    author_name?:           string;
    author_link?:           string;
    author_icon?:           string;
    from_url?:              string;
    original_url?:          string;
    author_subname?:        string;
    channel_id?:            string;
    channel_name?:          string;
    id?:                    number;
    bot_id?:                string;
    indent?:                boolean;
    is_msg_unfurl?:         boolean;
    is_reply_unfurl?:       boolean;
    is_thread_root_unfurl?: boolean;
    is_app_unfurl?:         boolean;
    app_unfurl_url?:        string;
    title?:                 string;
    title_link?:            string;
    text?:                  string;
    fields?:                Field[];
    image_url?:             string;
    image_width?:           number;
    image_height?:          number;
    image_bytes?:           number;
    thumb_url?:             string;
    thumb_width?:           number;
    thumb_height?:          number;
    video_url?:             string;
    video_html?:            string;
    video_html_width?:      number;
    video_html_height?:     number;
    footer?:                string;
    footer_icon?:           string;
    ts?:                    string;
    mrkdwn_in?:             string[];
    actions?:               Action[];
    blocks?:                any[];
    files?:                 any[];
    filename?:              string;
    size?:                  number;
    mimetype?:              string;
    url?:                   string;
    metadata?:              Metadata;
}

export interface Action {
    id?:               string;
    name?:             string;
    text?:             string;
    style?:            string;
    type?:             string;
    value?:            string;
    confirm?:          ActionConfirm;
    options?:          SelectedOptionElement[];
    selected_options?: SelectedOptionElement[];
    data_source?:      string;
    min_query_length?: number;
    option_groups?:    ActionOptionGroup[];
    url?:              string;
}

export interface ActionConfirm {
    title?:        string;
    text?:         string;
    ok_text?:      string;
    dismiss_text?: string;
}

export interface ActionOptionGroup {
    text?:    string;
    options?: SelectedOptionElement[];
}

export interface SelectedOptionElement {
    text?:  string;
    value?: string;
}

export interface Field {
    title?: string;
    value?: string;
    short?: boolean;
}

export interface Metadata {
    thumb_64?:    boolean;
    thumb_80?:    boolean;
    thumb_160?:   boolean;
    original_w?:  number;
    original_h?:  number;
    thumb_360_w?: number;
    thumb_360_h?: number;
    format?:      string;
    extension?:   string;
    rotation?:    number;
    thumb_tiny?:  string;
}

export interface Block {
    type?:         string;
    elements?:     Accessory[];
    block_id?:     string;
    fallback?:     string;
    image_url?:    string;
    image_width?:  number;
    image_height?: number;
    image_bytes?:  number;
    alt_text?:     string;
    title?:        Text;
    text?:         Text;
    fields?:       Text[];
    accessory?:    Accessory;
}

export interface Accessory {
    type?:                            string;
    image_url?:                       string;
    alt_text?:                        string;
    fallback?:                        string;
    image_width?:                     number;
    image_height?:                    number;
    image_bytes?:                     number;
    text?:                            Text;
    action_id?:                       string;
    url?:                             string;
    value?:                           string;
    style?:                           string;
    confirm?:                         AccessoryConfirm;
    accessibility_label?:             string;
    options?:                         InitialOptionElement[];
    initial_options?:                 InitialOptionElement[];
    focus_on_load?:                   boolean;
    initial_option?:                  InitialOptionElement;
    placeholder?:                     Text;
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
    option_groups?:                   AccessoryOptionGroup[];
    initial_user?:                    string;
    initial_users?:                   string[];
}

export interface AccessoryConfirm {
    title?:   Text;
    text?:    Text;
    confirm?: Text;
    deny?:    Text;
    style?:   string;
}

export interface Text {
    type?:     Type;
    text?:     string;
    emoji?:    boolean;
    verbatim?: boolean;
}

export enum Type {
    Mrkdwn = "mrkdwn",
    PlainText = "plain_text",
}

export interface Filter {
    include?:                          any[];
    exclude_external_shared_channels?: boolean;
    exclude_bot_users?:                boolean;
}

export interface InitialOptionElement {
    text?:        Text;
    value?:       string;
    description?: Text;
    url?:         string;
}

export interface AccessoryOptionGroup {
    label?:   Text;
    options?: InitialOptionElement[];
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

export interface PinnedInfo {
    channel?:   string;
    pinned_by?: string;
    pinned_ts?: number;
}

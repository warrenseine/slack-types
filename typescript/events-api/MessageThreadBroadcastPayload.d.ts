export interface MessageThreadBroadcastPayload {
    token?:                 string;
    enterprise_id?:         string;
    team_id?:               string;
    api_app_id?:            string;
    type?:                  string;
    authed_users?:          string[];
    authed_teams?:          string[];
    authorizations?:        Authorization[];
    is_ext_shared_channel?: boolean;
    event_id?:              string;
    event_time?:            number;
    event_context?:         string;
    event?:                 Event;
}

export interface Authorization {
    enterprise_id?:         string;
    team_id?:               string;
    user_id?:               string;
    is_bot?:                boolean;
    is_enterprise_install?: boolean;
}

export interface Event {
    client_msg_id?: string;
    type?:          string;
    subtype?:       string;
    channel?:       string;
    user?:          string;
    root?:          Root;
    text?:          string;
    blocks?:        Block[];
    attachments?:   Attachment[];
    ts?:            string;
    thread_ts?:     string;
    event_ts?:      string;
    channel_type?:  string;
}

export interface Attachment {
    msg_subtype?:           string;
    fallback?:              string;
    callback_id?:           string;
    color?:                 string;
    hide_color?:            boolean;
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
    channel_team?:          string;
    id?:                    number;
    app_id?:                string;
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
    preview?:               Preview;
    file_id?:               string;
    list_record_id?:        string;
    list_record?:           ListRecord;
    hide_border?:           boolean;
    list_view_id?:          string;
    list?:                  List;
    list_view?:             ListView;
    filename?:              string;
    size?:                  number;
    mimetype?:              string;
    url?:                   string;
    metadata?:              Metadata;
    is_file_attachment?:    boolean;
}

export interface Action {
    id?:               string;
    name?:             string;
    text?:             string;
    style?:            string;
    type?:             string;
    value?:            string;
    confirm?:          ActionConfirm;
    options?:          any[];
    selected_options?: any[];
    data_source?:      string;
    min_query_length?: number;
    url?:              string;
}

export interface ActionConfirm {
    title?:        string;
    text?:         string;
    ok_text?:      string;
    dismiss_text?: string;
}

export interface Field {
    title?: string;
    value?: string;
    short?: boolean;
}

export interface List {
    id?:                                      string;
    created?:                                 number;
    timestamp?:                               number;
    name?:                                    string;
    title?:                                   string;
    mimetype?:                                string;
    filetype?:                                string;
    external_type?:                           string;
    pretty_type?:                             string;
    user?:                                    string;
    user_team?:                               string;
    editable?:                                boolean;
    size?:                                    number;
    mode?:                                    string;
    is_external?:                             boolean;
    is_public?:                               boolean;
    public_url_shared?:                       boolean;
    display_as_bot?:                          boolean;
    username?:                                string;
    list_metadata?:                           ListMetadata;
    list_limits?:                             ListLimits;
    url_private?:                             string;
    url_private_download?:                    string;
    permalink?:                               string;
    permalink_public?:                        string;
    last_editor?:                             string;
    updated?:                                 number;
    comments_count?:                          number;
    shares?:                                  Shares;
    has_more_shares?:                         boolean;
    private_channels_with_file_access_count?: number;
    private_file_with_access_count?:          number;
    has_rich_preview?:                        boolean;
    file_access?:                             string;
}

export interface ListLimits {
    over_row_maximum?:         boolean;
    row_count_limit?:          number;
    row_count?:                number;
    over_column_maximum?:      boolean;
    column_count?:             number;
    column_count_limit?:       number;
    over_view_maximum?:        boolean;
    view_count?:               number;
    view_count_limit?:         number;
    max_attachments_per_cell?: number;
}

export interface ListMetadata {
    icon?:            string;
    icon_url?:        string;
    icon_team_id?:    string;
    description?:     string;
    is_trial?:        boolean;
    creation_source?: CreationSource;
}

export interface CreationSource {
    type?:                 string;
    reference_id?:         string;
    workflow_function_id?: string;
}

export interface Shares {
}

export interface ListRecord {
    record?: Record;
}

export interface Record {
    record_id?: string;
}

export interface ListView {
    id?:                   string;
    name?:                 string;
    type?:                 string;
    is_locked?:            boolean;
    position?:             string;
    date_created?:         number;
    created_by?:           string;
    stick_column_left?:    boolean;
    is_all_items_view?:    boolean;
    default_view_key?:     string;
    show_completed_items?: boolean;
    grouping?:             Grouping;
}

export interface Grouping {
    group_by?:           string;
    group_by_column_id?: string;
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

export interface Preview {
    type?:       string;
    can_remove?: boolean;
    title?:      Text;
    subtitle?:   Text;
    icon_url?:   string;
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

export interface Block {
    type?:         string;
    elements?:     Element[];
    block_id?:     string;
    fallback?:     string;
    image_url?:    string;
    image_width?:  number;
    image_height?: number;
    image_bytes?:  number;
    is_animated?:  boolean;
    slack_file?:   SlackFile;
    alt_text?:     string;
    title?:        Text;
    text?:         Text;
    fields?:       Text[];
    accessory?:    Accessory;
}

export interface Accessory {
    type?:         string;
    image_url?:    string;
    alt_text?:     string;
    fallback?:     string;
    image_width?:  number;
    image_height?: number;
    image_bytes?:  number;
    slack_file?:   SlackFile;
}

export interface SlackFile {
    id?:  string;
    url?: string;
}

export interface Element {
    type?:                            string;
    text?:                            Text;
    action_id?:                       string;
    url?:                             string;
    value?:                           string;
    style?:                           string;
    confirm?:                         ElementConfirm;
    accessibility_label?:             string;
    placeholder?:                     Text;
    initial_channel?:                 string;
    response_url_enabled?:            boolean;
    focus_on_load?:                   boolean;
    max_selected_items?:              number;
    initial_conversation?:            string;
    default_to_current_conversation?: boolean;
    filter?:                          Filter;
    initial_date?:                    string;
    initial_option?:                  InitialOption;
    min_query_length?:                number;
    image_url?:                       string;
    alt_text?:                        string;
    fallback?:                        string;
    image_width?:                     number;
    image_height?:                    number;
    image_bytes?:                     number;
    slack_file?:                      SlackFile;
    initial_user?:                    string;
}

export interface ElementConfirm {
    title?:   Text;
    text?:    Text;
    confirm?: Text;
    deny?:    Text;
    style?:   string;
}

export interface Filter {
    include?:                          string[];
    exclude_external_shared_channels?: boolean;
    exclude_bot_users?:                boolean;
}

export interface InitialOption {
    text?:        Text;
    value?:       string;
    description?: Text;
    url?:         string;
}

export interface Root {
    text?:              string;
    user?:              string;
    parent_user_id?:    string;
    username?:          string;
    team?:              string;
    bot_id?:            string;
    mrkdwn?:            boolean;
    type?:              string;
    subtype?:           string;
    thread_ts?:         string;
    icons?:             RootIcons;
    bot_profile?:       BotProfile;
    edited?:            Edited;
    reply_count?:       number;
    reply_users_count?: number;
    latest_reply?:      string;
    subscribed?:        boolean;
    last_read?:         string;
    unread_count?:      number;
    ts?:                string;
    room?:              Room;
    no_notifications?:  boolean;
}

export interface BotProfile {
    id?:      string;
    deleted?: boolean;
    name?:    string;
    updated?: number;
    app_id?:  string;
    icons?:   BotProfileIcons;
    team_id?: string;
}

export interface BotProfileIcons {
    image_36?: string;
    image_48?: string;
    image_72?: string;
}

export interface Edited {
    user?: string;
    ts?:   string;
}

export interface RootIcons {
    emoji?:    string;
    image_36?: string;
    image_48?: string;
    image_64?: string;
    image_72?: string;
}

export interface Room {
    id?:                 string;
    name?:               string;
    media_server?:       string;
    created_by?:         string;
    date_start?:         number;
    date_end?:           number;
    canvas_thread_ts?:   string;
    thread_root_ts?:     string;
    is_dm_call?:         boolean;
    was_rejected?:       boolean;
    was_missed?:         boolean;
    was_accepted?:       boolean;
    has_ended?:          boolean;
    background_id?:      string;
    canvas_background?:  string;
    is_prewarmed?:       boolean;
    is_scheduled?:       boolean;
    media_backend_type?: string;
    display_id?:         string;
    external_unique_id?: string;
    app_id?:             string;
    call_family?:        string;
    recording?:          Recording;
    huddle_link?:        string;
}

export interface Recording {
    transcript?:         boolean;
    summary?:            boolean;
    notetaking?:         boolean;
    summary_status?:     string;
    can_record_summary?: string;
}

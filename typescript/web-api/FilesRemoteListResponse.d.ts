export interface FilesRemoteListResponse {
    ok?:                boolean;
    files?:             File[];
    response_metadata?: ResponseMetadata;
    error?:             string;
    needed?:            string;
    provided?:          string;
}

export interface File {
    id?:                                      string;
    created?:                                 number;
    timestamp?:                               number;
    name?:                                    string;
    title?:                                   string;
    subject?:                                 string;
    mimetype?:                                string;
    filetype?:                                string;
    pretty_type?:                             string;
    user?:                                    string;
    user_team?:                               string;
    source_team?:                             string;
    mode?:                                    string;
    editable?:                                boolean;
    non_owner_editable?:                      boolean;
    editor?:                                  string;
    last_editor?:                             string;
    updated?:                                 number;
    file_access?:                             string;
    editors?:                                 string[];
    edit_timestamp?:                          number;
    alt_txt?:                                 string;
    subtype?:                                 string;
    transcription?:                           Transcription;
    mp4?:                                     string;
    mp4_low?:                                 string;
    vtt?:                                     string;
    hls?:                                     string;
    hls_embed?:                               string;
    duration_ms?:                             number;
    thumb_video_w?:                           number;
    thumb_video_h?:                           number;
    original_attachment_count?:               number;
    is_external?:                             boolean;
    external_type?:                           string;
    external_id?:                             string;
    external_url?:                            string;
    username?:                                string;
    size?:                                    number;
    url_private?:                             string;
    url_private_download?:                    string;
    url_static_preview?:                      string;
    app_id?:                                  string;
    app_name?:                                string;
    thumb_64?:                                string;
    thumb_64_gif?:                            string;
    thumb_64_w?:                              string;
    thumb_64_h?:                              string;
    thumb_80?:                                string;
    thumb_80_gif?:                            string;
    thumb_80_w?:                              string;
    thumb_80_h?:                              string;
    thumb_160?:                               string;
    thumb_160_gif?:                           string;
    thumb_160_w?:                             string;
    thumb_160_h?:                             string;
    thumb_360?:                               string;
    thumb_360_gif?:                           string;
    thumb_360_w?:                             string;
    thumb_360_h?:                             string;
    thumb_480?:                               string;
    thumb_480_gif?:                           string;
    thumb_480_w?:                             string;
    thumb_480_h?:                             string;
    thumb_720?:                               string;
    thumb_720_gif?:                           string;
    thumb_720_w?:                             string;
    thumb_720_h?:                             string;
    thumb_800?:                               string;
    thumb_800_gif?:                           string;
    thumb_800_w?:                             string;
    thumb_800_h?:                             string;
    thumb_960?:                               string;
    thumb_960_gif?:                           string;
    thumb_960_w?:                             string;
    thumb_960_h?:                             string;
    thumb_1024?:                              string;
    thumb_1024_gif?:                          string;
    thumb_1024_w?:                            string;
    thumb_1024_h?:                            string;
    thumb_video?:                             string;
    thumb_gif?:                               string;
    thumb_pdf?:                               string;
    thumb_pdf_w?:                             string;
    thumb_pdf_h?:                             string;
    thumb_tiny?:                              string;
    converted_pdf?:                           string;
    image_exif_rotation?:                     number;
    original_w?:                              string;
    original_h?:                              string;
    deanimate?:                               string;
    deanimate_gif?:                           string;
    pjpeg?:                                   string;
    permalink?:                               string;
    permalink_public?:                        string;
    edit_link?:                               string;
    has_rich_preview?:                        boolean;
    media_display_type?:                      string;
    preview_is_truncated?:                    boolean;
    preview?:                                 string;
    preview_highlight?:                       string;
    plain_text?:                              string;
    preview_plain_text?:                      string;
    has_more?:                                boolean;
    sent_to_self?:                            boolean;
    lines?:                                   number;
    lines_more?:                              number;
    is_public?:                               boolean;
    public_url_shared?:                       boolean;
    display_as_bot?:                          boolean;
    channels?:                                string[];
    groups?:                                  string[];
    ims?:                                     string[];
    shares?:                                  Shares;
    has_more_shares?:                         boolean;
    to?:                                      Cc[];
    from?:                                    Cc[];
    cc?:                                      Cc[];
    channel_actions_ts?:                      string;
    channel_actions_count?:                   number;
    headers?:                                 Headers;
    simplified_html?:                         string;
    media_progress?:                          MediaProgress;
    saved?:                                   Saved;
    quip_thread_id?:                          string;
    is_channel_space?:                        boolean;
    linked_channel_id?:                       string;
    access?:                                  string;
    teams_shared_with?:                       any[];
    last_read?:                               number;
    title_blocks?:                            Block[];
    private_channels_with_file_access_count?: number;
    private_file_with_access_count?:          number;
    dm_mpdm_users_with_file_access?:          DmMpdmUsersWithFileAccess[];
    org_or_workspace_access?:                 string;
    update_notification?:                     number;
    canvas_template_mode?:                    string;
    template_conversion_ts?:                  number;
    template_name?:                           string;
    template_title?:                          string;
    template_description?:                    string;
    template_icon?:                           string;
    team_pref_version_history_enabled?:       boolean;
    show_badge?:                              boolean;
    favorites?:                               Favorite[];
    list_metadata?:                           ListMetadata;
    list_limits?:                             ListLimits;
    list_csv_download_url?:                   string;
    can_toggle_canvas_lock?:                  boolean;
    is_restricted_sharing_enabled?:           boolean;
    canvas_printing_enabled?:                 boolean;
    bot_id?:                                  string;
    initial_comment?:                         InitialComment;
    num_stars?:                               number;
    is_starred?:                              boolean;
    pinned_to?:                               string[];
    reactions?:                               Reaction[];
    comments_count?:                          number;
}

export interface Cc {
    address?:  string;
    name?:     string;
    original?: string;
}

export interface DmMpdmUsersWithFileAccess {
    user_id?: string;
    access?:  string;
}

export interface Favorite {
    collection_id?:   string;
    collection_name?: string;
    position?:        string;
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
    icon?:               string;
    icon_url?:           string;
    icon_team_id?:       string;
    description?:        string;
    is_trial?:           boolean;
    creation_source?:    CreationSource;
    schema?:             Schema[];
    views?:              View[];
    integrations?:       string[];
    description_blocks?: Block[];
}

export interface CreationSource {
    type?:                 string;
    reference_id?:         string;
    workflow_function_id?: string;
}

export interface Block {
    type?:                         string;
    elements?:                     Accessory[];
    block_id?:                     string;
    fallback?:                     string;
    image_url?:                    string;
    image_width?:                  number;
    image_height?:                 number;
    image_bytes?:                  number;
    is_animated?:                  boolean;
    slack_file?:                   SlackFile;
    alt_text?:                     string;
    title?:                        Text | string;
    text?:                         Text;
    fields?:                       Text[];
    accessory?:                    Accessory;
    expand?:                       boolean;
    title_url?:                    string;
    description?:                  Text | string;
    video_url?:                    string;
    thumbnail_url?:                string;
    author_name?:                  string;
    provider_name?:                string;
    provider_icon_url?:            string;
    function_trigger_id?:          string;
    app_id?:                       string;
    is_workflow_app?:              boolean;
    sales_home_workflow_app_type?: number;
    app_collaborators?:            string[];
    button_label?:                 string;
    bot_user_id?:                  string;
    url?:                          string;
    owning_team_id?:               string;
    workflow_id?:                  string;
    developer_trace_id?:           string;
    trigger_type?:                 string;
    trigger_subtype?:              string;
    share_url?:                    string;
}

export interface Accessory {
    type?:                            string;
    image_url?:                       string;
    alt_text?:                        string;
    fallback?:                        string;
    image_width?:                     number;
    image_height?:                    number;
    image_bytes?:                     number;
    slack_file?:                      SlackFile;
    text?:                            Text;
    action_id?:                       string;
    url?:                             string;
    value?:                           string;
    style?:                           string;
    confirm?:                         Confirm;
    accessibility_label?:             string;
    workflow?:                        Workflow;
    options?:                         Option[];
    initial_options?:                 Option[];
    focus_on_load?:                   boolean;
    initial_option?:                  Option;
    placeholder?:                     Text;
    initial_channel?:                 string;
    response_url_enabled?:            boolean;
    initial_channels?:                string[];
    max_selected_items?:              number;
    initial_conversation?:            string;
    default_to_current_conversation?: boolean;
    filter?:                          AccessoryFilter;
    initial_conversations?:           string[];
    initial_date?:                    string;
    initial_time?:                    string;
    timezone?:                        string;
    initial_date_time?:               number;
    min_query_length?:                number;
    option_groups?:                   OptionGroup[];
    initial_user?:                    string;
    initial_users?:                   string[];
    elements?:                        AccessoryElement[];
    indent?:                          number;
    offset?:                          number;
    border?:                          number;
}

export interface Confirm {
    title?:   Text;
    text?:    Text;
    confirm?: Text;
    deny?:    Text;
    style?:   string;
}

export interface Text {
    type?:     TextType;
    text?:     string;
    emoji?:    boolean;
    verbatim?: boolean;
}

export enum TextType {
    Mrkdwn = "mrkdwn",
    PlainText = "plain_text",
}

export interface AccessoryElement {
    type?:     FluffyType;
    elements?: PurpleElement[];
    style?:    string;
    indent?:   number;
    offset?:   number;
    border?:   number;
}

export interface PurpleElement {
    type?:         PurpleType;
    range?:        string;
    style?:        Style;
    text?:         string;
    channel_id?:   string;
    value?:        string;
    timestamp?:    number;
    format?:       string;
    url?:          string;
    fallback?:     string;
    unsafe?:       boolean;
    team_id?:      string;
    user_id?:      string;
    usergroup_id?: string;
    name?:         string;
    skin_tone?:    number;
    unicode?:      string;
}

export interface Style {
    bold?:             boolean;
    italic?:           boolean;
    strike?:           boolean;
    highlight?:        boolean;
    client_highlight?: boolean;
    unlink?:           boolean;
    code?:             boolean;
}

export enum PurpleType {
    Broadcast = "broadcast",
    Channel = "channel",
    Color = "color",
    Date = "date",
    Emoji = "emoji",
    Link = "link",
    Team = "team",
    Text = "text",
    User = "user",
    Usergroup = "usergroup",
}

export enum FluffyType {
    RichTextList = "rich_text_list",
    RichTextPreformatted = "rich_text_preformatted",
    RichTextQuote = "rich_text_quote",
    RichTextSection = "rich_text_section",
}

export interface AccessoryFilter {
    include?:                          any[];
    exclude_external_shared_channels?: boolean;
    exclude_bot_users?:                boolean;
}

export interface Option {
    text?:        Text;
    value?:       string;
    description?: Text;
    url?:         string;
}

export interface OptionGroup {
    label?:   Text;
    options?: Option[];
}

export interface SlackFile {
    id?:  string;
    url?: string;
}

export interface Workflow {
    trigger?: Trigger;
}

export interface Trigger {
    url?:                           string;
    customizable_input_parameters?: CustomizableInputParameter[];
}

export interface CustomizableInputParameter {
    name?:  string;
    value?: string;
}

export interface Schema {
    id?:                string;
    name?:              string;
    key?:               string;
    type?:              string;
    is_primary_column?: boolean;
    options?:           Options;
}

export interface Options {
    choices?:                    Choice[];
    format?:                     string;
    default_value?:              string;
    default_value_typed?:        DefaultValueTyped;
    emoji?:                      string;
    max?:                        number;
    precision?:                  number;
    show_member_name?:           boolean;
    date_format?:                string;
    time_format?:                string;
    currency_format?:            string;
    emoji_team_id?:              string;
    currency?:                   string;
    rounding?:                   string;
    mark_as_done_when_checked?:  boolean;
    for_assignment?:             boolean;
    notify_users?:               boolean;
    linked_to?:                  string[];
    canvas_id?:                  string;
    canvas_placeholder_mapping?: CanvasPlaceholderMapping[];
}

export interface CanvasPlaceholderMapping {
    variable?: string;
    column?:   string;
}

export interface Choice {
    value?: string;
    label?: string;
    color?: string;
}

export interface DefaultValueTyped {
    select?: string[];
}

export interface View {
    id?:                   string;
    name?:                 string;
    type?:                 string;
    is_locked?:            boolean;
    position?:             string;
    columns?:              Column[];
    date_created?:         number;
    created_by?:           string;
    stick_column_left?:    boolean;
    is_all_items_view?:    boolean;
    default_view_key?:     string;
    show_completed_items?: boolean;
    grouping?:             Grouping;
    filters?:              FilterElement[];
}

export interface Column {
    visible?:  boolean;
    key?:      string;
    id?:       string;
    position?: string;
    width?:    number;
}

export interface FilterElement {
    key?:          string;
    operator?:     string;
    values?:       string[];
    typed_values?: any[];
    column_id?:    string;
}

export interface Grouping {
    group_by?:           string;
    group_by_column_id?: string;
}

export interface MediaProgress {
    offset_ms?:     number;
    max_offset_ms?: number;
    duration_ms?:   number;
    media_watched?: boolean;
}

export interface Reaction {
    name?:  string;
    count?: number;
    users?: string[];
    url?:   string;
}

export interface Saved {
    is_archived?:    boolean;
    date_completed?: number;
    date_due?:       number;
    state?:          string;
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
    access?:            string;
    source?:            string;
    date_last_shared?:  number;
}

export interface Transcription {
    status?:  string;
    locale?:  string;
    preview?: Preview;
}

export interface Preview {
    content?:  string;
    has_more?: boolean;
}

export interface ResponseMetadata {
    next_cursor?: string;
}

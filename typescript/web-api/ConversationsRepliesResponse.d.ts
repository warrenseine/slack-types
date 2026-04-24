export interface ConversationsRepliesResponse {
    messages?:          MessageElement[];
    has_more?:          boolean;
    ok?:                boolean;
    response_metadata?: ResponseMetadata;
    error?:             string;
    needed?:            string;
    provided?:          string;
}

export interface MessageElement {
    bot_id?:               string;
    type?:                 string;
    text?:                 string;
    user?:                 string;
    ts?:                   string;
    team?:                 string;
    bot_profile?:          BotProfile;
    thread_ts?:            string;
    reply_count?:          number;
    reply_users_count?:    number;
    latest_reply?:         string;
    reply_users?:          string[];
    subscribed?:           boolean;
    parent_user_id?:       string;
    is_locked?:            boolean;
    last_read?:            string;
    upload?:               boolean;
    display_as_bot?:       boolean;
    app_id?:               string;
    x_files?:              string[];
    edited?:               Edited;
    reactions?:            Reaction[];
    metadata?:             FluffyMetadata;
    blocks?:               AssistantAppThreadBlock[];
    attachments?:          Attachment[];
    files?:                FileElement[];
    assistant_app_thread?: AssistantAppThread;
}

export interface AssistantAppThread {
    title?:                   string;
    title_blocks?:            AssistantAppThreadBlock[];
    first_user_thread_reply?: string;
}

export interface AssistantAppThreadBlock {
    type?:                         BlockType;
    elements?:                     Accessory[];
    block_id?:                     string;
    call_id?:                      string;
    api_decoration_available?:     boolean;
    call?:                         Call;
    external_id?:                  string;
    source?:                       string;
    file_id?:                      string;
    file?:                         FileElement;
    text?:                         DescriptionElement;
    fallback?:                     string;
    image_url?:                    string;
    image_width?:                  number;
    image_height?:                 number;
    image_bytes?:                  number;
    is_animated?:                  boolean;
    slack_file?:                   SlackFile;
    alt_text?:                     string;
    title?:                        DescriptionElement;
    title_url?:                    string;
    description?:                  DescriptionElement;
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
    fields?:                       DescriptionElement[];
    accessory?:                    Accessory;
    expand?:                       boolean;
    label?:                        DescriptionElement;
    element?:                      Accessory;
    dispatch_action?:              boolean;
    hint?:                         DescriptionElement;
    optional?:                     boolean;
}

export interface Accessory {
    type?:                            AccessoryType;
    text?:                            DescriptionElement;
    action_id?:                       string;
    url?:                             string;
    value?:                           string;
    style?:                           string;
    confirm?:                         AccessoryConfirm;
    accessibility_label?:             string;
    workflow?:                        Workflow;
    options?:                         InitialOptionElement[];
    initial_options?:                 InitialOptionElement[];
    focus_on_load?:                   boolean;
    initial_option?:                  InitialOptionElement;
    placeholder?:                     DescriptionElement;
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
    image_url?:                       string;
    alt_text?:                        string;
    fallback?:                        string;
    image_width?:                     number;
    image_height?:                    number;
    image_bytes?:                     number;
    slack_file?:                      SlackFile;
    option_groups?:                   AccessoryOptionGroup[];
    initial_user?:                    string;
    initial_users?:                   string[];
    elements?:                        AccessoryElement[];
    indent?:                          number;
    offset?:                          number;
    border?:                          number;
}

export interface AccessoryConfirm {
    title?:   DescriptionElement;
    text?:    DescriptionElement;
    confirm?: DescriptionElement;
    deny?:    DescriptionElement;
    style?:   string;
}

export interface DescriptionElement {
    type?:     DescriptionType;
    text?:     string;
    emoji?:    boolean;
    verbatim?: boolean;
}

export enum DescriptionType {
    Mrkdwn = "mrkdwn",
    PlainText = "plain_text",
}

export interface AccessoryElement {
    type?:     AccessoryType;
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

export enum AccessoryType {
    Button = "button",
    ChannelsSelect = "channels_select",
    Checkboxes = "checkboxes",
    ConversationsSelect = "conversations_select",
    Datepicker = "datepicker",
    Datetimepicker = "datetimepicker",
    ExternalSelect = "external_select",
    Image = "image",
    MultiChannelsSelect = "multi_channels_select",
    MultiConversationsSelect = "multi_conversations_select",
    MultiExternalSelect = "multi_external_select",
    MultiStaticSelect = "multi_static_select",
    MultiUsersSelect = "multi_users_select",
    Overflow = "overflow",
    RadioButtons = "radio_buttons",
    RichTextList = "rich_text_list",
    RichTextPreformatted = "rich_text_preformatted",
    RichTextQuote = "rich_text_quote",
    RichTextSection = "rich_text_section",
    StaticSelect = "static_select",
    Timepicker = "timepicker",
    UsersSelect = "users_select",
    WorkflowButton = "workflow_button",
}

export interface AccessoryFilter {
    include?:                          any[];
    exclude_external_shared_channels?: boolean;
    exclude_bot_users?:                boolean;
}

export interface InitialOptionElement {
    text?:        DescriptionElement;
    value?:       string;
    description?: DescriptionElement;
    url?:         string;
}

export interface AccessoryOptionGroup {
    label?:   DescriptionElement;
    options?: InitialOptionElement[];
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

export interface FileElement {
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
    title_blocks?:                            DescriptionBlockElement[];
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
    attachments?:                             any[];
    blocks?:                                  DescriptionBlockElement[];
}

export interface DescriptionBlockElement {
    type?:                         BlockType;
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
    title?:                        DescriptionElement | string;
    text?:                         DescriptionElement;
    fields?:                       DescriptionElement[];
    accessory?:                    Accessory;
    expand?:                       boolean;
    title_url?:                    string;
    description?:                  DescriptionElement | string;
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

export enum BlockType {
    Actions = "actions",
    Context = "context",
    Divider = "divider",
    Image = "image",
    RichText = "rich_text",
    Section = "section",
    ShareShortcut = "share_shortcut",
    Video = "video",
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
    description_blocks?: DescriptionBlockElement[];
}

export interface CreationSource {
    type?:                 string;
    reference_id?:         string;
    workflow_function_id?: string;
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
    preview?: TranscriptionPreview;
}

export interface TranscriptionPreview {
    content?:  string;
    has_more?: boolean;
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
    bot_team_id?:           string;
    indent?:                boolean;
    is_msg_unfurl?:         boolean;
    is_reply_unfurl?:       boolean;
    is_thread_root_unfurl?: boolean;
    is_app_unfurl?:         boolean;
    app_unfurl_url?:        string;
    title?:                 string;
    title_link?:            string;
    text?:                  string;
    fields?:                AttachmentField[];
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
    blocks?:                DescriptionBlockElement[];
    message_blocks?:        MessageBlock[];
    preview?:               AttachmentPreview;
    file_id?:               string;
    list_record_id?:        string;
    list_record?:           PurpleListRecord;
    list_records?:          ListRecordElement[];
    hide_border?:           boolean;
    list_view_id?:          string;
    list?:                  List;
    list_schema?:           Schema[];
    list_view?:             View;
    files?:                 FileElement[];
    filename?:              string;
    size?:                  number;
    mimetype?:              string;
    url?:                   string;
    metadata?:              AttachmentMetadata;
    is_file_attachment?:    boolean;
}

export interface Action {
    id?:               string;
    name?:             string;
    text?:             string;
    style?:            string;
    type?:             AccessoryType;
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

export interface AttachmentField {
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
    shares?:                                  EventPayload;
    channels?:                                string[];
    groups?:                                  string[];
    ims?:                                     string[];
    has_more_shares?:                         boolean;
    private_channels_with_file_access_count?: number;
    private_file_with_access_count?:          number;
    dm_mpdm_users_with_file_access?:          DmMpdmUsersWithFileAccess[];
    has_rich_preview?:                        boolean;
    file_access?:                             string;
}

export interface EventPayload {
}

export interface PurpleListRecord {
    record?: Record;
    schema?: Schema[];
}

export interface Record {
    record_id?: string;
    fields?:    RecordField[];
}

export interface RecordField {
    key?:        string;
    column_id?:  string;
    value?:      string;
    text?:       string;
    rich_text?:  any[];
    message?:    FieldMessage;
    number?:     any[];
    select?:     any[];
    date?:       any[];
    user?:       any[];
    attachment?: any[];
    checkbox?:   boolean;
    email?:      any[];
    phone?:      any[];
    channel?:    any[];
    rating?:     any[];
    timestamp?:  any[];
}

export interface FieldMessage {
    type?:                 string;
    subtype?:              string;
    team?:                 string;
    channel?:              string;
    user?:                 string;
    username?:             string;
    text?:                 string;
    blocks?:               DescriptionBlockElement[];
    attachments?:          any[];
    ts?:                   string;
    thread_ts?:            string;
    is_intro?:             boolean;
    is_starred?:           boolean;
    wibblr?:               boolean;
    pinned_to?:            any[];
    reactions?:            any[];
    app_id?:               string;
    bot_id?:               string;
    bot_link?:             string;
    display_as_bot?:       boolean;
    bot_profile?:          BotProfile;
    icons?:                MessageIcons;
    file?:                 PurpleFile;
    files?:                any[];
    upload?:               boolean;
    parent_user_id?:       string;
    inviter?:              string;
    client_msg_id?:        string;
    comment?:              Comment;
    topic?:                string;
    purpose?:              string;
    edited?:               Edited;
    unfurl_links?:         boolean;
    unfurl_media?:         boolean;
    is_thread_broadcast?:  boolean;
    is_locked?:            boolean;
    replies?:              any[];
    reply_count?:          number;
    reply_users?:          any[];
    reply_users_count?:    number;
    latest_reply?:         string;
    subscribed?:           boolean;
    x_files?:              any[];
    hidden?:               boolean;
    last_read?:            string;
    root?:                 Root;
    item_type?:            string;
    item?:                 Comment;
    metadata?:             PurpleMetadata;
    room?:                 Room;
    no_notifications?:     boolean;
    assistant_app_thread?: AssistantAppThread;
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

export interface Comment {
    id?:                   string;
    name?:                 string;
    title?:                string;
    created?:              string;
    timestamp?:            string;
    user?:                 string;
    username?:             string;
    is_intro?:             boolean;
    is_public?:            boolean;
    is_starred?:           boolean;
    public_url_shared?:    boolean;
    url_private?:          string;
    url_private_download?: boolean;
    permalink?:            string;
    permalink_public?:     boolean;
    edit_link?:            string;
    preview?:              string;
    preview_highlight?:    string;
    lines?:                number;
    lines_more?:           number;
    preview_is_truncated?: boolean;
    has_rich_preview?:     boolean;
    media_display_type?:   string;
    mimetype?:             string;
    filetype?:             string;
    pretty_type?:          string;
    is_external?:          boolean;
    external_type?:        string;
    editable?:             boolean;
    display_as_bot?:       boolean;
    size?:                 number;
    mode?:                 string;
    comment?:              string;
}

export interface Edited {
    user?: string;
    ts?:   string;
}

export interface PurpleFile {
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
    editors?:                                 any[];
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
    channels?:                                any[];
    groups?:                                  any[];
    ims?:                                     any[];
    shares?:                                  EventPayload;
    has_more_shares?:                         boolean;
    to?:                                      any[];
    from?:                                    any[];
    cc?:                                      any[];
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
    title_blocks?:                            any[];
    private_channels_with_file_access_count?: number;
    private_file_with_access_count?:          number;
    dm_mpdm_users_with_file_access?:          any[];
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
    favorites?:                               any[];
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
    pinned_to?:                               any[];
    reactions?:                               any[];
    comments_count?:                          number;
    attachments?:                             any[];
    blocks?:                                  any[];
}

export interface MessageIcons {
    emoji?:    string;
    image_36?: string;
    image_48?: string;
    image_64?: string;
    image_72?: string;
}

export interface PurpleMetadata {
    event_type?: string;
}

export interface Room {
    id?:                           string;
    name?:                         string;
    media_server?:                 string;
    created_by?:                   string;
    date_start?:                   number;
    date_end?:                     number;
    participants?:                 any[];
    participant_history?:          any[];
    participants_camera_on?:       any[];
    participants_camera_off?:      any[];
    participants_screenshare_on?:  any[];
    participants_screenshare_off?: any[];
    canvas_thread_ts?:             string;
    thread_root_ts?:               string;
    channels?:                     any[];
    is_dm_call?:                   boolean;
    was_rejected?:                 boolean;
    was_missed?:                   boolean;
    was_accepted?:                 boolean;
    has_ended?:                    boolean;
    background_id?:                string;
    canvas_background?:            string;
    is_prewarmed?:                 boolean;
    is_scheduled?:                 boolean;
    attached_file_ids?:            any[];
    media_backend_type?:           string;
    display_id?:                   string;
    external_unique_id?:           string;
    app_id?:                       string;
    call_family?:                  string;
    recording?:                    Recording;
    huddle_link?:                  string;
}

export interface Recording {
    transcript?:         boolean;
    summary?:            boolean;
    notetaking?:         boolean;
    summary_status?:     string;
    can_record_summary?: string;
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
    icons?:             MessageIcons;
    bot_profile?:       BotProfile;
    edited?:            Edited;
    replies?:           any[];
    reply_count?:       number;
    reply_users?:       any[];
    reply_users_count?: number;
    latest_reply?:      string;
    subscribed?:        boolean;
    last_read?:         string;
    unread_count?:      number;
    ts?:                string;
    room?:              Room;
    no_notifications?:  boolean;
}

export interface ListRecordElement {
    id?:                string;
    list_id?:           string;
    fields?:            RecordField[];
    date_created?:      number;
    created_by?:        string;
    thread_ts?:         string;
    position?:          string;
    updated_timestamp?: string;
    updated_by?:        string;
    platform_refs?:     PlatformRefs;
    is_subscribed?:     boolean;
    saved?:             Saved;
}

export interface PlatformRefs {
    bot_created_by?: string;
    bot_updated_by?: string;
    bot_deleted_by?: string;
}

export interface MessageBlock {
    team?:    string;
    channel?: string;
    ts?:      string;
    message?: FieldMessage;
}

export interface AttachmentMetadata {
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

export interface AttachmentPreview {
    type?:       string;
    can_remove?: boolean;
    title?:      DescriptionElement;
    subtitle?:   DescriptionElement;
    icon_url?:   string;
}

export interface FluffyMetadata {
    event_payload?: EventPayload;
    event_type?:    string;
}

export interface ResponseMetadata {
    next_cursor?: string;
}

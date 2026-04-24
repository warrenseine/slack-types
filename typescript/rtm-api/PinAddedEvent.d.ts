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
    message?:    ItemMessage;
    file?:       ItemFile;
    comment?:    InitialCommentClass;
}

export interface InitialCommentClass {
    id?:        string;
    created?:   number;
    timestamp?: number;
    user?:      string;
    comment?:   string;
    channel?:   string;
    is_intro?:  boolean;
}

export interface ItemFile {
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
    shares?:                                  PurpleShares;
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
    bot_id?:                                  string;
    initial_comment?:                         InitialCommentClass;
    num_stars?:                               number;
    is_starred?:                              boolean;
    pinned_to?:                               any[];
    reactions?:                               any[];
    comments_count?:                          number;
    attachments?:                             any[];
    blocks?:                                  any[];
}

export interface Headers {
    date?:        string;
    in_reply_to?: string;
    reply_to?:    string;
    message_id?:  string;
}

export interface MediaProgress {
    offset_ms?:     number;
    max_offset_ms?: number;
    duration_ms?:   number;
}

export interface Saved {
    is_archived?:    boolean;
    date_completed?: number;
    date_due?:       number;
    state?:          string;
}

export interface PurpleShares {
}

export interface Transcription {
    status?: string;
    locale?: string;
}

export interface ItemMessage {
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
    blocks?:                Block[];
    message_blocks?:        MessageBlock[];
    preview?:               Preview;
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

export interface Block {
    type?:                         BlockType;
    elements?:                     Accessory[];
    block_id?:                     string;
    fallback?:                     string;
    image_url?:                    string;
    image_width?:                  number;
    image_height?:                 number;
    image_bytes?:                  number;
    alt_text?:                     string;
    title?:                        Text | string;
    text?:                         Text;
    fields?:                       Text[];
    accessory?:                    Accessory;
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
    text?:                            Text;
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
    timezone?:                        string;
    initial_date_time?:               number;
    min_query_length?:                number;
    option_groups?:                   AccessoryOptionGroup[];
    initial_user?:                    string;
    initial_users?:                   string[];
    elements?:                        AccessoryElement[];
    indent?:                          number;
    offset?:                          number;
    border?:                          number;
}

export interface AccessoryConfirm {
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
    url?:          string;
    team_id?:      string;
    user_id?:      string;
    usergroup_id?: string;
    name?:         string;
    skin_tone?:    number;
    unicode?:      string;
}

export interface Style {
    bold?:   boolean;
    italic?: boolean;
    strike?: boolean;
    code?:   boolean;
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

export interface Field {
    title?: string;
    value?: string;
    short?: boolean;
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
    shares?:                                  FluffyShares;
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
    bot_id?:                                  string;
    initial_comment?:                         InitialCommentClass;
    num_stars?:                               number;
    is_starred?:                              boolean;
    pinned_to?:                               string[];
    reactions?:                               Reaction[];
    comments_count?:                          number;
    attachments?:                             any[];
    blocks?:                                  Block[];
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

export interface Reaction {
    name?:  string;
    count?: number;
    users?: string[];
    url?:   string;
}

export interface FluffyShares {
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

export interface MessageBlock {
    team?:    string;
    channel?: string;
    ts?:      string;
    message?: MessageBlockMessage;
}

export interface MessageBlockMessage {
    type?:                string;
    subtype?:             string;
    team?:                string;
    channel?:             string;
    user?:                string;
    username?:            string;
    text?:                string;
    blocks?:              Block[];
    attachments?:         any[];
    ts?:                  string;
    thread_ts?:           string;
    is_intro?:            boolean;
    is_starred?:          boolean;
    wibblr?:              boolean;
    pinned_to?:           any[];
    reactions?:           any[];
    app_id?:              string;
    bot_id?:              string;
    bot_link?:            string;
    display_as_bot?:      boolean;
    bot_profile?:         BotProfile;
    icons?:               MessageIcons;
    file?:                ItemFile;
    files?:               any[];
    upload?:              boolean;
    parent_user_id?:      string;
    inviter?:             string;
    client_msg_id?:       string;
    comment?:             ItemClass;
    topic?:               string;
    purpose?:             string;
    edited?:              Edited;
    unfurl_links?:        boolean;
    unfurl_media?:        boolean;
    is_thread_broadcast?: boolean;
    is_locked?:           boolean;
    replies?:             any[];
    reply_count?:         number;
    reply_users?:         any[];
    reply_users_count?:   number;
    latest_reply?:        string;
    subscribed?:          boolean;
    x_files?:             any[];
    hidden?:              boolean;
    last_read?:           string;
    root?:                Root;
    item_type?:           string;
    item?:                ItemClass;
    metadata?:            MessageMetadata;
    room?:                Room;
    no_notifications?:    boolean;
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

export interface ItemClass {
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

export interface MessageIcons {
    emoji?:    string;
    image_36?: string;
    image_48?: string;
    image_64?: string;
    image_72?: string;
}

export interface MessageMetadata {
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

export interface Preview {
    type?:       string;
    can_remove?: boolean;
    title?:      Text;
    subtitle?:   Text;
    icon_url?:   string;
}

export interface PinnedInfo {
    channel?:   string;
    pinned_by?: string;
    pinned_ts?: number;
}

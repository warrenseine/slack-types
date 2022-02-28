export interface RtmStartResponse {
    ok?:                          boolean;
    self?:                        Self;
    team?:                        Team;
    accept_tos_url?:              string;
    latest_event_ts?:             string;
    channels?:                    Channel[];
    groups?:                      Group[];
    ims?:                         Im[];
    cache_ts?:                    number;
    mobile_app_requires_upgrade?: boolean;
    read_only_channels?:          string[];
    non_threadable_channels?:     string[];
    thread_only_channels?:        string[];
    can_manage_shared_channels?:  boolean;
    subteams?:                    Subteams;
    dnd?:                         Dnd;
    users?:                       User[];
    cache_version?:               string;
    cache_ts_version?:            string;
    bots?:                        Bot[];
    url?:                         string;
    is_europe?:                   boolean;
    links?:                       Links;
    response_metadata?:           ResponseMetadata;
    error?:                       string;
    needed?:                      string;
    provided?:                    string;
}

export interface Bot {
    id?:              string;
    deleted?:         boolean;
    name?:            string;
    updated?:         number;
    app_id?:          string;
    icons?:           BotIcons;
    is_workflow_bot?: boolean;
    team_id?:         string;
}

export interface BotIcons {
    image_36?: string;
    image_48?: string;
    image_72?: string;
}

export interface Channel {
    id?:                         string;
    name?:                       string;
    is_channel?:                 boolean;
    is_group?:                   boolean;
    is_im?:                      boolean;
    is_mpim?:                    boolean;
    is_private?:                 boolean;
    created?:                    number;
    is_archived?:                boolean;
    is_general?:                 boolean;
    unlinked?:                   number;
    name_normalized?:            string;
    is_shared?:                  boolean;
    is_org_shared?:              boolean;
    is_pending_ext_shared?:      boolean;
    pending_shared?:             string[];
    creator?:                    string;
    is_ext_shared?:              boolean;
    shared_team_ids?:            string[];
    pending_connected_team_ids?: string[];
    has_pins?:                   boolean;
    is_member?:                  boolean;
    last_read?:                  string;
    topic?:                      Purpose;
    purpose?:                    Purpose;
    previous_names?:             string[];
    priority?:                   number;
    internal_team_ids?:          string[];
    connected_team_ids?:         string[];
    connected_limited_team_ids?: string[];
    conversation_host_id?:       string;
}

export interface Purpose {
    value?:    string;
    creator?:  string;
    last_set?: number;
}

export interface Dnd {
    dnd_enabled?:       boolean;
    next_dnd_start_ts?: number;
    next_dnd_end_ts?:   number;
    snooze_enabled?:    boolean;
}

export interface Group {
    id?:                   string;
    name?:                 string;
    name_normalized?:      string;
    is_group?:             boolean;
    created?:              number;
    creator?:              string;
    is_archived?:          boolean;
    is_mpim?:              boolean;
    is_open?:              boolean;
    is_read_only?:         boolean;
    is_thread_only?:       boolean;
    members?:              string[];
    parent_group?:         string;
    topic?:                Purpose;
    purpose?:              Purpose;
    last_read?:            string;
    latest?:               Latest;
    unread_count?:         number;
    unread_count_display?: number;
    priority?:             number;
}

export interface Latest {
    client_msg_id?:  string;
    type?:           string;
    subtype?:        string;
    team?:           string;
    user?:           string;
    username?:       string;
    parent_user_id?: string;
    text?:           string;
    topic?:          string;
    attachments?:    Attachment[];
    blocks?:         Block[];
    files?:          File[];
    reactions?:      string[];
    root?:           Root;
    upload?:         boolean;
    display_as_bot?: boolean;
    bot_id?:         string;
    bot_link?:       string;
    bot_profile?:    Bot;
    thread_ts?:      string;
    ts?:             string;
    icons?:          LatestIcons;
    x_files?:        string[];
    edited?:         Edited;
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
    blocks?:                Block[];
    files?:                 File[];
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
    confirm?:                         AccessoryConfirm;
    accessibility_label?:             string;
    options?:                         InitialOptionElement[];
    initial_options?:                 InitialOptionElement[];
    focus_on_load?:                   boolean;
    initial_option?:                  InitialOptionElement;
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
    option_groups?:                   AccessoryOptionGroup[];
    initial_user?:                    string;
    initial_users?:                   string[];
}

export interface AccessoryConfirm {
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

export interface InitialOptionElement {
    text?:        Hint;
    value?:       string;
    description?: Hint;
    url?:         string;
}

export interface AccessoryOptionGroup {
    label?:   Hint;
    options?: InitialOptionElement[];
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

export interface Field {
    title?: string;
    value?: string;
    short?: boolean;
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
    channels?:                  string[];
    groups?:                    string[];
    ims?:                       string[];
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
    comments_count?:            number;
    blocks?:                    Block[];
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

export interface Edited {
    user?: string;
    ts?:   string;
}

export interface LatestIcons {
    emoji?:    string;
    image_36?: string;
    image_48?: string;
    image_64?: string;
    image_72?: string;
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
    icons?:             LatestIcons;
    bot_profile?:       Bot;
    edited?:            Edited;
    replies?:           Edited[];
    reply_count?:       number;
    reply_users?:       string[];
    reply_users_count?: number;
    latest_reply?:      string;
    subscribed?:        boolean;
    last_read?:         string;
    unread_count?:      number;
    ts?:                string;
}

export interface Im {
    id?:            string;
    created?:       number;
    is_archived?:   boolean;
    is_im?:         boolean;
    is_org_shared?: boolean;
    user?:          string;
    last_read?:     string;
    is_open?:       boolean;
    has_pins?:      boolean;
    priority?:      number;
}

export interface Links {
    domains_ts?: number;
}

export interface ResponseMetadata {
    messages?: string[];
}

export interface Self {
    id?:              string;
    name?:            string;
    prefs?:           SelfPrefs;
    created?:         number;
    first_login?:     number;
    manual_presence?: string;
}

export interface SelfPrefs {
    underline_links?:                                           boolean;
    user_colors?:                                               string;
    color_names_in_list?:                                       boolean;
    email_alerts?:                                              string;
    email_alerts_sleep_until?:                                  number;
    email_tips?:                                                boolean;
    email_weekly?:                                              boolean;
    email_offers?:                                              boolean;
    email_research?:                                            boolean;
    email_developer?:                                           boolean;
    welcome_message_hidden?:                                    boolean;
    search_sort?:                                               string;
    search_file_sort?:                                          string;
    search_channel_sort?:                                       string;
    search_people_sort?:                                        string;
    expand_inline_imgs?:                                        boolean;
    expand_internal_inline_imgs?:                               boolean;
    expand_snippets?:                                           boolean;
    posts_formatting_guide?:                                    boolean;
    seen_welcome_2?:                                            boolean;
    seen_ssb_prompt?:                                           boolean;
    spaces_new_xp_banner_dismissed?:                            boolean;
    search_only_my_channels?:                                   boolean;
    search_only_current_team?:                                  boolean;
    search_hide_my_channels?:                                   boolean;
    search_only_show_online?:                                   boolean;
    search_hide_deactivated_users?:                             boolean;
    emoji_mode?:                                                string;
    emoji_use?:                                                 string;
    emoji_use_org?:                                             string;
    has_invited?:                                               boolean;
    has_uploaded?:                                              boolean;
    has_created_channel?:                                       boolean;
    has_created_channel_section?:                               boolean;
    has_searched?:                                              boolean;
    search_exclude_channels?:                                   string;
    messages_theme?:                                            string;
    webapp_spellcheck?:                                         boolean;
    no_joined_overlays?:                                        boolean;
    no_created_overlays?:                                       boolean;
    dropbox_enabled?:                                           boolean;
    seen_domain_invite_reminder?:                               boolean;
    seen_member_invite_reminder?:                               boolean;
    mute_sounds?:                                               boolean;
    arrow_history?:                                             boolean;
    tab_ui_return_selects?:                                     boolean;
    obey_inline_img_limit?:                                     boolean;
    require_at?:                                                boolean;
    ssb_space_window?:                                          string;
    mac_ssb_bounce?:                                            string;
    mac_ssb_bullet?:                                            boolean;
    expand_non_media_attachments?:                              boolean;
    show_typing?:                                               boolean;
    pagekeys_handled?:                                          boolean;
    last_snippet_type?:                                         string;
    display_real_names_override?:                               number;
    display_display_names?:                                     boolean;
    time24?:                                                    boolean;
    enter_is_special_in_tbt?:                                   boolean;
    msg_input_send_btn?:                                        boolean;
    msg_input_send_btn_auto_set?:                               boolean;
    msg_input_sticky_composer?:                                 boolean;
    composer_nux?:                                              string;
    graphic_emoticons?:                                         boolean;
    convert_emoticons?:                                         boolean;
    ss_emojis?:                                                 boolean;
    seen_onboarding_start?:                                     boolean;
    onboarding_cancelled?:                                      boolean;
    seen_onboarding_slackbot_conversation?:                     boolean;
    seen_onboarding_channels?:                                  boolean;
    seen_onboarding_direct_messages?:                           boolean;
    seen_onboarding_invites?:                                   boolean;
    seen_onboarding_search?:                                    boolean;
    seen_onboarding_recent_mentions?:                           boolean;
    seen_onboarding_starred_items?:                             boolean;
    seen_onboarding_private_groups?:                            boolean;
    seen_onboarding_banner?:                                    boolean;
    onboarding_slackbot_conversation_step?:                     number;
    set_tz_automatically?:                                      boolean;
    suppress_link_warning?:                                     boolean;
    suppress_external_invites_from_compose_warning?:            boolean;
    seen_emoji_pack_cta?:                                       number;
    seen_emoji_pack_dialog?:                                    boolean;
    seen_schedule_send_coachmark?:                              boolean;
    emoji_packs_most_recent_available_time?:                    number;
    emoji_packs_clicked_picker_cta?:                            boolean;
    emoji_packs_clicked_picker_post_install_cta?:               boolean;
    emoji_packs_clicked_collection_cta?:                        boolean;
    dnd_enabled?:                                               boolean;
    dnd_start_hour?:                                            string;
    dnd_end_hour?:                                              string;
    dnd_before_monday?:                                         string;
    dnd_after_monday?:                                          string;
    dnd_enabled_monday?:                                        string;
    dnd_before_tuesday?:                                        string;
    dnd_after_tuesday?:                                         string;
    dnd_enabled_tuesday?:                                       string;
    dnd_before_wednesday?:                                      string;
    dnd_after_wednesday?:                                       string;
    dnd_enabled_wednesday?:                                     string;
    dnd_before_thursday?:                                       string;
    dnd_after_thursday?:                                        string;
    dnd_enabled_thursday?:                                      string;
    dnd_before_friday?:                                         string;
    dnd_after_friday?:                                          string;
    dnd_enabled_friday?:                                        string;
    dnd_before_saturday?:                                       string;
    dnd_after_saturday?:                                        string;
    dnd_enabled_saturday?:                                      string;
    dnd_before_sunday?:                                         string;
    dnd_after_sunday?:                                          string;
    dnd_enabled_sunday?:                                        string;
    dnd_days?:                                                  string;
    dnd_weekdays_off_allday?:                                   boolean;
    reminder_notification_time?:                                string;
    dnd_custom_new_badge_seen?:                                 boolean;
    dnd_notification_schedule_new_badge_seen?:                  boolean;
    notification_center_filters?:                               string;
    calls_survey_last_seen?:                                    string;
    huddle_survey_last_seen?:                                   string;
    sidebar_behavior?:                                          string;
    channel_sort?:                                              string;
    separate_private_channels?:                                 boolean;
    separate_shared_channels?:                                  boolean;
    sidebar_theme?:                                             string;
    sidebar_theme_custom_values?:                               string;
    no_invites_widget_in_sidebar?:                              boolean;
    no_omnibox_in_channels?:                                    boolean;
    k_key_omnibox_auto_hide_count?:                             number;
    show_sidebar_quickswitcher_button?:                         boolean;
    ent_org_wide_channels_sidebar?:                             boolean;
    mark_msgs_read_immediately?:                                boolean;
    start_scroll_at_oldest?:                                    boolean;
    snippet_editor_wrap_long_lines?:                            boolean;
    ls_disabled?:                                               boolean;
    f_key_search?:                                              boolean;
    k_key_omnibox?:                                             boolean;
    prompted_for_email_disabling?:                              boolean;
    no_macelectron_banner?:                                     boolean;
    no_macssb1_banner?:                                         boolean;
    no_macssb2_banner?:                                         boolean;
    no_winssb1_banner?:                                         boolean;
    hide_user_group_info_pane?:                                 boolean;
    mentions_exclude_at_user_groups?:                           boolean;
    mentions_exclude_reactions?:                                boolean;
    privacy_policy_seen?:                                       boolean;
    enterprise_migration_seen?:                                 boolean;
    search_exclude_bots?:                                       boolean;
    load_lato_2?:                                               boolean;
    fuller_timestamps?:                                         boolean;
    last_seen_at_channel_warning?:                              number;
    emoji_autocomplete_big?:                                    boolean;
    two_factor_auth_enabled?:                                   boolean;
    hide_hex_swatch?:                                           boolean;
    show_jumper_scores?:                                        boolean;
    enterprise_mdm_custom_msg?:                                 string;
    client_logs_pri?:                                           string;
    flannel_server_pool?:                                       string;
    mentions_exclude_at_channels?:                              boolean;
    confirm_clear_all_unreads?:                                 boolean;
    confirm_user_marked_away?:                                  boolean;
    box_enabled?:                                               boolean;
    seen_single_emoji_msg?:                                     boolean;
    confirm_sh_call_start?:                                     boolean;
    preferred_skin_tone?:                                       string;
    show_all_skin_tones?:                                       boolean;
    whats_new_read?:                                            number;
    help_modal_open_timestamp?:                                 number;
    help_modal_consult_banner_dismissed?:                       boolean;
    help_flexpane_slack_connect_card_seen?:                     boolean;
    help_flexpane_clips_card_seen?:                             boolean;
    help_menu_open_timestamp?:                                  number;
    frecency_jumper?:                                           string;
    frecency_ent_jumper?:                                       string;
    jumbomoji?:                                                 boolean;
    newxp_seen_last_message?:                                   number;
    show_memory_instrument?:                                    boolean;
    enable_unread_view?:                                        boolean;
    seen_unread_view_coachmark?:                                boolean;
    seen_connect_dm_coachmark?:                                 boolean;
    seen_connect_section_coachmark?:                            boolean;
    should_show_connect_section?:                               boolean;
    enable_react_emoji_picker?:                                 boolean;
    seen_custom_status_badge?:                                  boolean;
    seen_custom_status_callout?:                                boolean;
    seen_custom_status_expiration_badge?:                       boolean;
    used_custom_status_kb_shortcut?:                            boolean;
    seen_guest_admin_slackbot_announcement?:                    boolean;
    seen_threads_notification_banner?:                          boolean;
    seen_name_tagging_coachmark?:                               boolean;
    all_unreads_sort_order?:                                    string;
    all_unreads_section_filter?:                                string;
    locale?:                                                    string;
    seen_intl_channel_names_coachmark?:                         boolean;
    seen_p3_locale_change_message_ko_kr?:                       number;
    seen_toast_new_locale_launch?:                              string;
    seen_toast_new_locale_launch_ts?:                           number;
    seen_locale_change_message?:                                number;
    seen_japanese_locale_change_message?:                       boolean;
    seen_shared_channels_coachmark?:                            boolean;
    seen_shared_channels_opt_in_change_message?:                boolean;
    has_recently_shared_a_channel?:                             boolean;
    seen_channel_browser_admin_coachmark?:                      boolean;
    seen_administration_menu?:                                  boolean;
    seen_drafts_section_coachmark?:                             boolean;
    seen_emoji_update_overlay_coachmark?:                       boolean;
    seen_sonic_deluxe_toast?:                                   number;
    seen_wysiwyg_deluxe_toast?:                                 boolean;
    seen_markdown_paste_toast?:                                 number;
    seen_markdown_paste_shortcut?:                              number;
    seen_ia_education?:                                         boolean;
    show_ia_tour_relaunch?:                                     number;
    plain_text_mode?:                                           boolean;
    show_shared_channels_education_banner?:                     boolean;
    ia_slackbot_survey_timestamp_48h?:                          number;
    ia_slackbot_survey_timestamp_7d?:                           number;
    enable_streamline_view?:                                    boolean;
    enable_sent_view?:                                          boolean;
    allow_calls_to_set_current_status?:                         boolean;
    in_interactive_mas_migration_flow?:                         boolean;
    sunset_interactive_message_views?:                          number;
    shdep_promo_code_submitted?:                                boolean;
    seen_shdep_slackbot_message?:                               boolean;
    seen_calls_interactive_coachmark?:                          boolean;
    allow_cmd_tab_iss?:                                         boolean;
    join_calls_device_settings?:                                string;
    calls_disconnect_on_lock?:                                  boolean;
    seen_workflow_builder_deluxe_toast?:                        boolean;
    workflow_builder_intro_modal_clicked_through?:              boolean;
    workflow_builder_coachmarks?:                               string;
    seen_gdrive_coachmark?:                                     boolean;
    seen_first_install_coachmark?:                              boolean;
    seen_existing_install_coachmark?:                           boolean;
    seen_link_unfurl_coachmark?:                                boolean;
    file_picker_variant?:                                       number;
    open_quip_doc_in_flexpane?:                                 boolean;
    saved_searches?:                                            string;
    huddles_variant?:                                           number;
    huddles_cc_by_default?:                                     boolean;
    huddles_mute_by_default?:                                   boolean;
    huddles_global_mute?:                                       boolean;
    huddles_mini_panel?:                                        boolean;
    huddles_set_status?:                                        boolean;
    huddles_show_shouty_rooster?:                               boolean;
    huddles_disconnect_on_lock?:                                boolean;
    huddles_play_music_when_last?:                              boolean;
    huddles_allow_smart_notif?:                                 boolean;
    huddles_reactions_play_sound?:                              boolean;
    huddles_reactions_read_out_loud?:                           boolean;
    huddles_chime_new_endpoints_check_completed?:               number;
    xws_sidebar_variant?:                                       number;
    inbox_views_workspace_filter?:                              string;
    overloaded_message_enabled?:                                boolean;
    seen_highlights_coachmark?:                                 boolean;
    seen_highlights_arrows_coachmark?:                          boolean;
    seen_highlights_warm_welcome?:                              boolean;
    seen_new_search_ui?:                                        boolean;
    seen_channel_search?:                                       boolean;
    seen_people_search?:                                        boolean;
    seen_people_search_count?:                                  number;
    dismissed_scroll_search_tooltip_count?:                     number;
    last_dismissed_scroll_search_tooltip_timestamp?:            number;
    has_used_quickswitcher_shortcut?:                           boolean;
    seen_quickswitcher_shortcut_tip_count?:                     number;
    browsers_dismissed_channels_low_results_education?:         boolean;
    browsers_seen_initial_channels_education?:                  boolean;
    browsers_dismissed_people_low_results_education?:           boolean;
    browsers_seen_initial_people_education?:                    boolean;
    browsers_dismissed_user_groups_low_results_education?:      boolean;
    browsers_seen_initial_user_groups_education?:               boolean;
    browsers_dismissed_files_low_results_education?:            boolean;
    browsers_seen_initial_files_education?:                     boolean;
    browsers_dismissed_initial_drafts_education?:               boolean;
    browsers_seen_initial_drafts_education?:                    boolean;
    browsers_dismissed_initial_activity_education?:             boolean;
    browsers_seen_initial_activity_education?:                  boolean;
    browsers_dismissed_initial_saved_education?:                boolean;
    browsers_seen_initial_saved_education?:                     boolean;
    seen_edit_mode?:                                            boolean;
    seen_edit_mode_edu?:                                        boolean;
    xws_dismissed_education?:                                   boolean;
    xws_seen_education?:                                        number;
    sidebar_pref_dismissed_tip?:                                boolean;
    a11y_dyslexic?:                                             boolean;
    a11y_animations?:                                           boolean;
    seen_keyboard_shortcuts_coachmark?:                         boolean;
    needs_initial_password_set?:                                boolean;
    lessons_enabled?:                                           boolean;
    tractor_enabled?:                                           boolean;
    tractor_experiment_group?:                                  string;
    opened_slackbot_dm?:                                        boolean;
    newxp_seen_help_message?:                                   number;
    newxp_suggested_channels?:                                  string;
    onboarding_complete?:                                       boolean;
    welcome_place_state?:                                       string;
    has_received_threaded_message?:                             boolean;
    joiner_notifications_muted?:                                boolean;
    invite_accepted_notifications_muted?:                       boolean;
    joiner_message_suggestion_dismissed?:                       boolean;
    dismissed_fullscreen_download_ssb_prompt?:                  boolean;
    dismissed_banner_download_ssb_prompt?:                      boolean;
    onboarding_state?:                                          number;
    whocanseethis_dm_mpdm_badge?:                               boolean;
    highlight_words?:                                           string;
    threads_everything?:                                        boolean;
    no_text_in_notifications?:                                  boolean;
    push_show_preview?:                                         boolean;
    growls_enabled?:                                            boolean;
    all_channels_loud?:                                         boolean;
    push_dm_alert?:                                             boolean;
    push_mention_alert?:                                        boolean;
    push_everything?:                                           boolean;
    push_idle_wait?:                                            number;
    push_sound?:                                                string;
    new_msg_snd?:                                               string;
    huddle_invite_sound?:                                       string;
    push_loud_channels?:                                        string;
    push_mention_channels?:                                     string;
    push_loud_channels_set?:                                    string;
    loud_channels?:                                             string;
    never_channels?:                                            string;
    loud_channels_set?:                                         string;
    at_channel_suppressed_channels?:                            string;
    push_at_channel_suppressed_channels?:                       string;
    muted_channels?:                                            string;
    all_notifications_prefs?:                                   string;
    growth_msg_limit_approaching_cta_count?:                    number;
    growth_msg_limit_approaching_cta_ts?:                       number;
    growth_msg_limit_reached_cta_count?:                        number;
    growth_msg_limit_reached_cta_last_ts?:                      number;
    growth_msg_limit_long_reached_cta_count?:                   number;
    growth_msg_limit_long_reached_cta_last_ts?:                 number;
    growth_msg_limit_sixty_day_banner_cta_count?:               number;
    growth_msg_limit_sixty_day_banner_cta_last_ts?:             number;
    growth_all_banners_prefs?:                                  string;
    analytics_upsell_coachmark_seen?:                           boolean;
    seen_app_space_coachmark?:                                  boolean;
    seen_app_space_tutorial?:                                   boolean;
    dismissed_app_launcher_welcome?:                            boolean;
    dismissed_app_launcher_limit?:                              boolean;
    dismissed_app_launcher_atlassian_promo?:                    boolean;
    enable_app_config_redesign?:                                boolean;
    dismissed_app_config_redesign_coachmark?:                   boolean;
    dismissed_app_manifest_description?:                        boolean;
    dismissed_app_manifest_coachmark?:                          boolean;
    purchaser?:                                                 boolean;
    seen_channel_email_tooltip?:                                boolean;
    show_ent_onboarding?:                                       boolean;
    folders_enabled?:                                           boolean;
    folder_data?:                                               string;
    seen_corporate_export_alert?:                               boolean;
    show_autocomplete_help?:                                    number;
    deprecation_toast_last_seen?:                               number;
    deprecation_modal_last_seen?:                               number;
    deprecation_banner_last_seen?:                              number;
    iap1_lab?:                                                  number;
    ia_top_nav_theme?:                                          string;
    ia_platform_actions_lab?:                                   number;
    activity_view?:                                             string;
    saved_view?:                                                string;
    seen_floating_sidebar_coachmark?:                           boolean;
    desktop_client_ids?:                                        string;
    failover_proxy_check_completed?:                            number;
    chime_access_check_completed?:                              number;
    mx_calendar_type?:                                          string;
    edge_upload_proxy_check_completed?:                         number;
    app_subdomain_check_completed?:                             number;
    add_prompt_interacted?:                                     boolean;
    add_apps_prompt_dismissed?:                                 boolean;
    add_channel_prompt_dismissed?:                              boolean;
    channel_sidebar_hide_invite?:                               boolean;
    channel_sidebar_hide_browse_dms_link?:                      boolean;
    in_prod_surveys_enabled?:                                   boolean;
    connect_dm_early_access?:                                   boolean;
    dismissed_installed_app_dm_suggestions?:                    string;
    seen_contextual_message_shortcuts_modal?:                   boolean;
    seen_message_navigation_educational_toast?:                 boolean;
    contextual_message_shortcuts_modal_was_seen?:               boolean;
    message_navigation_toast_was_seen?:                         boolean;
    up_to_browse_kb_shortcut?:                                  boolean;
    set_a11y_prefs_new_user?:                                   boolean;
    a11y_play_sound_for_incoming_dm?:                           boolean;
    a11y_play_sound_for_sent_dm?:                               boolean;
    a11y_read_out_incoming_dm?:                                 boolean;
    a11y_screen_reader_message_label_date_time_first?:          boolean;
    should_show_contextual_help_for_conversation_navigation?:   boolean;
    should_show_contextual_help_for_jump_to_conversation?:      boolean;
    should_show_contextual_help_for_section_navigation?:        boolean;
    should_show_contextual_help_for_thread_navigation?:         boolean;
    should_show_unsend_message_confirmation?:                   boolean;
    channel_sections?:                                          string;
    show_quick_reactions?:                                      boolean;
    user_customized_quick_reactions_display_feature?:           number;
    user_customized_quick_reactions_has_customized?:            boolean;
    user_customized_quick_reactions_use_frequently_used_emoji?: boolean;
    reaction_notifications?:                                    string;
    has_received_mention_or_reaction?:                          boolean;
    has_starred_item?:                                          boolean;
    has_drafted_message?:                                       boolean;
    enable_mentions_and_reactions_view?:                        boolean;
    enable_reminders_view?:                                     boolean;
    enable_saved_items_view?:                                   boolean;
    enable_hq_view?:                                            boolean;
    enable_all_dms_view?:                                       boolean;
    enable_channel_browser_view?:                               boolean;
    enable_file_browser_view?:                                  boolean;
    enable_people_browser_view?:                                boolean;
    enable_app_browser_view?:                                   boolean;
    reached_all_dms_disclosure?:                                boolean;
    enable_slack_connect_view?:                                 boolean;
    enable_slack_connect_view_2?:                               number;
    has_acknowledged_shortcut_speedbump?:                       boolean;
    enable_media_captions?:                                     boolean;
    media_playback_speed?:                                      number;
    media_muted?:                                               boolean;
    media_volume?:                                              number;
    dismissed_connect_auto_approval_modal?:                     string;
    tasks_view?:                                                string;
    show_sidebar_avatars?:                                      boolean;
    has_dismissed_google_directory_coachmark?:                  boolean;
    seen_sc_page_banner?:                                       boolean;
    seen_sc_menu_coachmark?:                                    boolean;
    seen_sc_page?:                                              boolean;
    dismissed_scdm_education?:                                  boolean;
    seen_bookmarks_intro?:                                      boolean;
    scdm_trial_offer_banner?:                                   string;
    identity_links_prefs?:                                      string;
    identity_links_global_prefs?:                               string;
    seen_sections_unreads_only_prompt_count?:                   number;
    last_seen_sections_unreads_only_prompt_timestamp?:          number;
    notifications_view?:                                        string;
    progressive_disclosure_state?:                              string;
    suggestions_request_id?:                                    string;
    allowed_unfurl_senders?:                                    string;
    ia_details_coachmark_seen?:                                 boolean;
    hide_external_members_sharing_speed_bump?:                  boolean;
    who_can_share_contact_card?:                                string;
    slack_connect_invite_should_badge_sidebar?:                 boolean;
    phc_dismissed?:                                             string;
    dismissed_gov_slack_first_time_popup?:                      boolean;
    mobile_channel_list_sort?:                                  string;
    user_expectations_survey_last_trigger_attempt?:             number;
    tz?:                                                        string;
    locales_enabled?:                                           LocalesEnabled;
    phc_viewed?:                                                string;
    seen_a11y_pref_setup_coachmark?:                            boolean;
    enable_file_browser_view_for_docs?:                         boolean;
    enable_shortcuts_view?:                                     boolean;
    show_gov_slack_context_bar_banner?:                         boolean;
    who_can_see_account_by_searching_email?:                    string;
    contextual_help_reset_count?:                               number;
}

export interface LocalesEnabled {
    "de-DE"?: string;
    "en-GB"?: string;
    "en-US"?: string;
    "es-ES"?: string;
    "es-LA"?: string;
    "fr-FR"?: string;
    "it-IT"?: string;
    "pt-BR"?: string;
    "ru-RU"?: string;
    "ja-JP"?: string;
    "zh-CN"?: string;
    "zh-TW"?: string;
    "ko-KR"?: string;
}

export interface Subteams {
    self?: string[];
    all?:  All[];
}

export interface All {
    id?:                    string;
    team_id?:               string;
    is_usergroup?:          boolean;
    is_subteam?:            boolean;
    name?:                  string;
    description?:           string;
    handle?:                string;
    is_external?:           boolean;
    date_create?:           number;
    date_update?:           number;
    date_delete?:           number;
    auto_provision?:        boolean;
    enterprise_subteam_id?: string;
    created_by?:            string;
    updated_by?:            string;
    prefs?:                 AllPrefs;
    user_count?:            number;
    channel_count?:         number;
}

export interface AllPrefs {
    channels?: string[];
    groups?:   Group[];
}

export interface Team {
    id?:                    string;
    name?:                  string;
    url?:                   string;
    email_domain?:          string;
    domain?:                string;
    msg_edit_window_mins?:  number;
    prefs?:                 TeamPrefs;
    icon?:                  Icon;
    over_storage_limit?:    boolean;
    messages_count?:        number;
    plan?:                  string;
    onboarding_channel_id?: string;
    date_create?:           number;
    limit_ts?:              number;
    is_verified?:           boolean;
    avatar_base_url?:       string;
}

export interface Icon {
    image_102?:      string;
    image_132?:      string;
    image_230?:      string;
    image_34?:       string;
    image_44?:       string;
    image_68?:       string;
    image_88?:       string;
    image_original?: string;
}

export interface TeamPrefs {
    default_channels?:                                   string[];
    allow_calls?:                                        boolean;
    display_email_addresses?:                            boolean;
    gdrive_enabled_team?:                                boolean;
    all_users_can_purchase?:                             boolean;
    enable_shared_channels?:                             number;
    can_receive_shared_channels_invites?:                boolean;
    invited_user_preset?:                                InvitedUserPreset;
    dropbox_legacy_picker?:                              boolean;
    app_whitelist_enabled?:                              boolean;
    who_can_manage_integrations?:                        SlackConnectAllowedWorkspaces;
    welcome_place_enabled?:                              boolean;
    msg_edit_window_mins?:                               number;
    allow_message_deletion?:                             boolean;
    display_external_email_addresses?:                   boolean;
    joiner_notifications_enabled?:                       boolean;
    received_esc_route_to_channel_awareness_message?:    boolean;
    who_can_create_channels?:                            string;
    who_can_archive_channels?:                           string;
    who_can_create_groups?:                              string;
    who_can_manage_channel_posting_prefs?:               string;
    who_can_kick_channels?:                              string;
    who_can_kick_groups?:                                string;
    locale?:                                             string;
    display_pronouns?:                                   boolean;
    admin_customized_quick_reactions?:                   string[];
    allow_admin_retention_override?:                     number;
    allow_audio_clip_sharing_slack_connect?:             boolean;
    allow_audio_clips?:                                  boolean;
    allow_box_cfs?:                                      boolean;
    allow_calls_interactive_screen_sharing?:             boolean;
    allow_clip_downloads?:                               string;
    allow_huddles?:                                      boolean;
    allow_huddles_transcriptions?:                       boolean;
    allow_media_transcriptions?:                         boolean;
    allow_retention_override?:                           boolean;
    allow_sponsored_slack_connections?:                  boolean;
    allow_video_clip_sharing_slack_connect?:             boolean;
    allow_video_clips?:                                  boolean;
    app_dir_only?:                                       boolean;
    app_management_apps?:                                string[];
    block_file_download?:                                boolean;
    box_app_installed?:                                  boolean;
    calls_apps?:                                         CallsApps;
    calls_locations?:                                    string[];
    can_accept_slack_connect_channel_invites?:           boolean;
    can_create_external_limited_invite?:                 boolean;
    can_create_slack_connect_channel_invite?:            boolean;
    channel_email_addresses_enabled?:                    boolean;
    compliance_export_start?:                            number;
    content_review_enabled?:                             boolean;
    created_with_google?:                                boolean;
    custom_status_default_emoji?:                        string;
    custom_status_presets?:                              Array<string[]>;
    default_channel_creation_enabled?:                   boolean;
    default_rxns?:                                       string[];
    disable_email_ingestion?:                            boolean;
    disable_file_deleting?:                              boolean;
    disable_file_editing?:                               boolean;
    disable_file_uploads?:                               string;
    disable_sidebar_connect_prompts?:                    string[];
    disable_sidebar_install_prompts?:                    string[];
    disallow_public_file_urls?:                          boolean;
    discoverable?:                                       string;
    display_default_phone?:                              boolean;
    display_name_pronunciation?:                         boolean;
    display_real_names?:                                 boolean;
    dm_retention_duration?:                              number;
    dm_retention_type?:                                  number;
    dnd_days?:                                           string;
    enable_connect_dm_early_access?:                     boolean;
    enable_domain_allowlist_for_cea?:                    boolean;
    enable_info_barriers?:                               boolean;
    enable_mpdm_to_private_channel_conversion?:          boolean;
    enterprise_default_channels?:                        string[];
    enterprise_has_corporate_exports?:                   boolean;
    enterprise_intune_enabled?:                          boolean;
    enterprise_mandatory_channels?:                      string[];
    enterprise_mdm_date_enabled?:                        number;
    enterprise_mdm_disable_file_download?:               boolean;
    enterprise_mdm_level?:                               number;
    enterprise_mobile_device_check?:                     boolean;
    enterprise_team_creation_request?:                   EnterpriseTeamCreationRequest;
    file_limit_whitelisted?:                             boolean;
    file_retention_duration?:                            number;
    file_retention_type?:                                number;
    filepicker_app_first_install?:                       boolean;
    gg_enabled?:                                         boolean;
    group_retention_duration?:                           number;
    group_retention_type?:                               number;
    has_compliance_export?:                              boolean;
    has_hipaa_compliance?:                               boolean;
    has_seen_partner_promo?:                             boolean;
    hermes_has_accepted_tos?:                            boolean;
    hermes_triggers_trippable_by_slack_connected_teams?: boolean;
    hide_gsuite_invite_option?:                          boolean;
    hide_referers?:                                      boolean;
    invite_requests_enabled?:                            boolean;
    invites_only_admins?:                                boolean;
    loud_channel_mentions_limit?:                        number;
    member_analytics_disabled?:                          boolean;
    ml_opt_out?:                                         boolean;
    mobile_passcode_timeout_in_seconds?:                 number;
    notification_redaction_type?:                        string;
    notify_pending_enabled?:                             boolean;
    ntlm_credential_domains?:                            string;
    onedrive_app_installed?:                             boolean;
    onedrive_enabled_team?:                              boolean;
    private_channel_membership_limit?:                   number;
    retention_duration?:                                 number;
    retention_type?:                                     number;
    search_feedback_opt_out?:                            boolean;
    self_serve_select?:                                  boolean;
    session_duration?:                                   number;
    session_duration_type?:                              number;
    show_join_leave?:                                    boolean;
    show_legacy_paid_benefits_page?:                     boolean;
    sign_in_with_slack_disabled?:                        boolean;
    single_user_exports?:                                boolean;
    slack_connect_allowed_workspaces?:                   SlackConnectAllowedWorkspaces;
    slack_connect_approval_type?:                        string;
    slack_connect_dm_only_verified_orgs?:                boolean;
    slack_connect_file_upload_sharing_enabled?:          boolean;
    slackbot_responses_disabled?:                        boolean;
    sso_disable_emails?:                                 boolean;
    sso_optional?:                                       boolean;
    sso_signup_restrictions?:                            number;
    sso_sync_with_provider?:                             boolean;
    subteams_auto_create_admin?:                         boolean;
    subteams_auto_create_owner?:                         boolean;
    use_browser_picker?:                                 boolean;
    uses_customized_custom_status_presets?:              boolean;
    warn_before_at_channel?:                             string;
    who_can_accept_slack_connect_channel_invites?:       SlackConnectAllowedWorkspaces;
    who_can_at_channel?:                                 string;
    who_can_at_everyone?:                                string;
    who_can_change_team_profile?:                        string;
    who_can_create_delete_user_groups?:                  string;
    who_can_create_external_limited_invite?:             SlackConnectAllowedWorkspaces;
    who_can_create_shared_channels?:                     string;
    who_can_create_slack_connect_channel_invite?:        SlackConnectAllowedWorkspaces;
    who_can_dm_anyone?:                                  SlackConnectAllowedWorkspaces;
    who_can_edit_user_groups?:                           string;
    who_can_manage_ext_shared_channels?:                 SlackConnectAllowedWorkspaces;
    who_can_manage_guests?:                              SlackConnectAllowedWorkspaces;
    who_can_manage_private_channels?:                    WhoCanManageP;
    who_can_manage_private_channels_at_workspace_level?: WhoCanManageP;
    who_can_manage_public_channels?:                     WhoCanManageP;
    who_can_manage_shared_channels?:                     SlackConnectAllowedWorkspaces;
    who_can_post_general?:                               string;
    who_can_post_in_shared_channels?:                    SlackConnectAllowedWorkspaces;
    who_can_request_ext_shared_channels?:                SlackConnectAllowedWorkspaces;
    who_can_review_flagged_content?:                     SlackConnectAllowedWorkspaces;
    who_can_view_message_activity?:                      SlackConnectAllowedWorkspaces;
    workflow_builder_enabled?:                           boolean;
    workflow_extension_steps_beta_opt_in?:               boolean;
    dnd_enabled?:                                        boolean;
    dnd_start_hour?:                                     string;
    dnd_end_hour?:                                       string;
    dnd_before_monday?:                                  string;
    dnd_after_monday?:                                   string;
    dnd_before_tuesday?:                                 string;
    dnd_after_tuesday?:                                  string;
    dnd_before_wednesday?:                               string;
    dnd_after_wednesday?:                                string;
    dnd_before_thursday?:                                string;
    dnd_after_thursday?:                                 string;
    dnd_before_friday?:                                  string;
    dnd_after_friday?:                                   string;
    dnd_before_saturday?:                                string;
    dnd_after_saturday?:                                 string;
    dnd_before_sunday?:                                  string;
    dnd_after_sunday?:                                   string;
    dnd_enabled_monday?:                                 string;
    dnd_enabled_tuesday?:                                string;
    dnd_enabled_wednesday?:                              string;
    dnd_enabled_thursday?:                               string;
    dnd_enabled_friday?:                                 string;
    dnd_enabled_saturday?:                               string;
    dnd_enabled_sunday?:                                 string;
    dnd_weekdays_off_allday?:                            boolean;
    auth_mode?:                                          string;
    who_can_create_workflows?:                           SlackConnectAllowedWorkspaces;
    workflows_webhook_trigger_enabled?:                  boolean;
    workflow_extension_steps_enabled?:                   boolean;
    workflows_export_csv_enabled?:                       boolean;
    who_can_use_hermes?:                                 SlackConnectAllowedWorkspaces;
    who_can_create_channel_email_addresses?:             SlackConnectAllowedWorkspaces;
    identity_links_prefs?:                               EnterpriseTeamCreationRequest;
    magic_unfurls_enabled?:                              boolean;
    invites_limit?:                                      boolean;
    show_mobile_promos?:                                 boolean;
    dm_retention_redaction_duration?:                    number;
    private_retention_redaction_duration?:               number;
    public_retention_redaction_duration?:                number;
}

export interface CallsApps {
    video?: Video[];
    audio?: string[];
}

export interface Video {
    id?:    string;
    name?:  string;
    image?: string;
}

export interface EnterpriseTeamCreationRequest {
    is_enabled?: boolean;
}

export interface InvitedUserPreset {
    enable_invited_user?: boolean;
}

export interface SlackConnectAllowedWorkspaces {
    type?: string[];
}

export interface WhoCanManageP {
    user?: string[];
    type?: string[];
}

export interface User {
    id?:                         string;
    team_id?:                    string;
    name?:                       string;
    deleted?:                    boolean;
    color?:                      string;
    real_name?:                  string;
    tz?:                         string;
    tz_label?:                   string;
    tz_offset?:                  number;
    profile?:                    Profile;
    is_admin?:                   boolean;
    is_owner?:                   boolean;
    is_primary_owner?:           boolean;
    is_restricted?:              boolean;
    is_ultra_restricted?:        boolean;
    is_bot?:                     boolean;
    is_app_user?:                boolean;
    updated?:                    number;
    is_email_confirmed?:         boolean;
    who_can_share_contact_card?: string;
    presence?:                   string;
    is_workflow_bot?:            boolean;
}

export interface Profile {
    title?:                     string;
    phone?:                     string;
    skype?:                     string;
    real_name?:                 string;
    real_name_normalized?:      string;
    display_name?:              string;
    display_name_normalized?:   string;
    fields?:                    Fields;
    status_text?:               string;
    status_emoji?:              string;
    status_emoji_display_info?: StatusEmojiDisplayInfo[];
    status_expiration?:         number;
    avatar_hash?:               string;
    image_original?:            string;
    is_custom_image?:           boolean;
    email?:                     string;
    pronouns?:                  string;
    first_name?:                string;
    last_name?:                 string;
    image_24?:                  string;
    image_32?:                  string;
    image_48?:                  string;
    image_72?:                  string;
    image_192?:                 string;
    image_512?:                 string;
    image_1024?:                string;
    status_text_canonical?:     string;
    team?:                      string;
    api_app_id?:                string;
    bot_id?:                    string;
    always_active?:             boolean;
    guest_invited_by?:          string;
}

export interface Fields {
    Xf019LT13Z16?: Xf019LT13Z16;
}

export interface Xf019LT13Z16 {
    value?: string;
    alt?:   string;
}

export interface StatusEmojiDisplayInfo {
    emoji_name?:    string;
    display_alias?: string;
    display_url?:   string;
}

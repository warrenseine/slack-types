export interface RtmStartResponse {
    ok?:                         boolean;
    self?:                       Self;
    team?:                       Team;
    latest_event_ts?:            string;
    channels?:                   Channel[];
    groups?:                     Group[];
    ims?:                        Im[];
    cache_ts?:                   number;
    read_only_channels?:         string[];
    non_threadable_channels?:    string[];
    thread_only_channels?:       string[];
    can_manage_shared_channels?: boolean;
    subteams?:                   Subteams;
    dnd?:                        Dnd;
    users?:                      User[];
    cache_version?:              string;
    cache_ts_version?:           string;
    bots?:                       Bot[];
    url?:                        string;
    error?:                      string;
    needed?:                     string;
    provided?:                   string;
}

export interface Bot {
    id?:              string;
    deleted?:         boolean;
    name?:            string;
    updated?:         number;
    app_id?:          string;
    icons?:           Icons;
    is_workflow_bot?: boolean;
}

export interface Icons {
    image_36?: string;
    image_48?: string;
    image_72?: string;
}

export interface Channel {
    id?:                         string;
    name?:                       string;
    is_channel?:                 boolean;
    created?:                    number;
    is_archived?:                boolean;
    is_general?:                 boolean;
    unlinked?:                   number;
    creator?:                    string;
    name_normalized?:            string;
    is_shared?:                  boolean;
    is_org_shared?:              boolean;
    has_pins?:                   boolean;
    is_member?:                  boolean;
    is_private?:                 boolean;
    is_mpim?:                    boolean;
    last_read?:                  string;
    members?:                    string[];
    topic?:                      Purpose;
    purpose?:                    Purpose;
    previous_names?:             string[];
    priority?:                   number;
    is_group?:                   boolean;
    is_im?:                      boolean;
    is_ext_shared?:              boolean;
    shared_team_ids?:            string[];
    internal_team_ids?:          string[];
    connected_team_ids?:         string[];
    pending_shared?:             string[];
    pending_connected_team_ids?: string[];
    is_pending_ext_shared?:      boolean;
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
    id?:              string;
    name?:            string;
    is_group?:        boolean;
    created?:         number;
    creator?:         string;
    is_archived?:     boolean;
    name_normalized?: string;
    is_read_only?:    boolean;
    is_thread_only?:  boolean;
    is_mpim?:         boolean;
    has_pins?:        boolean;
    is_open?:         boolean;
    last_read?:       string;
    members?:         string[];
    topic?:           Purpose;
    purpose?:         Purpose;
    priority?:        number;
}

export interface Im {
    id?:            string;
    created?:       number;
    is_archived?:   boolean;
    is_im?:         boolean;
    is_org_shared?: boolean;
    user?:          string;
    has_pins?:      boolean;
    last_read?:     string;
    is_open?:       boolean;
    priority?:      number;
}

export interface Self {
    id?:              string;
    name?:            string;
    prefs?:           SelfPrefs;
    created?:         number;
    manual_presence?: string;
}

export interface SelfPrefs {
    user_colors?:                                   string;
    color_names_in_list?:                           boolean;
    email_alerts?:                                  string;
    email_alerts_sleep_until?:                      number;
    email_tips?:                                    boolean;
    email_weekly?:                                  boolean;
    email_offers?:                                  boolean;
    email_research?:                                boolean;
    email_developer?:                               boolean;
    welcome_message_hidden?:                        boolean;
    search_sort?:                                   string;
    search_file_sort?:                              string;
    search_channel_sort?:                           string;
    search_people_sort?:                            string;
    expand_inline_imgs?:                            boolean;
    expand_internal_inline_imgs?:                   boolean;
    expand_snippets?:                               boolean;
    posts_formatting_guide?:                        boolean;
    seen_welcome_2?:                                boolean;
    seen_ssb_prompt?:                               boolean;
    spaces_new_xp_banner_dismissed?:                boolean;
    search_only_my_channels?:                       boolean;
    search_only_current_team?:                      boolean;
    search_hide_my_channels?:                       boolean;
    search_only_show_online?:                       boolean;
    search_hide_deactivated_users?:                 boolean;
    emoji_mode?:                                    string;
    emoji_use?:                                     string;
    has_invited?:                                   boolean;
    has_uploaded?:                                  boolean;
    has_created_channel?:                           boolean;
    has_searched?:                                  boolean;
    search_exclude_channels?:                       string;
    messages_theme?:                                string;
    webapp_spellcheck?:                             boolean;
    no_joined_overlays?:                            boolean;
    no_created_overlays?:                           boolean;
    dropbox_enabled?:                               boolean;
    seen_domain_invite_reminder?:                   boolean;
    seen_member_invite_reminder?:                   boolean;
    mute_sounds?:                                   boolean;
    arrow_history?:                                 boolean;
    tab_ui_return_selects?:                         boolean;
    obey_inline_img_limit?:                         boolean;
    require_at?:                                    boolean;
    ssb_space_window?:                              string;
    mac_ssb_bounce?:                                string;
    mac_ssb_bullet?:                                boolean;
    expand_non_media_attachments?:                  boolean;
    show_typing?:                                   boolean;
    pagekeys_handled?:                              boolean;
    last_snippet_type?:                             string;
    display_real_names_override?:                   number;
    display_display_names?:                         boolean;
    time24?:                                        boolean;
    enter_is_special_in_tbt?:                       boolean;
    msg_input_send_btn?:                            boolean;
    msg_input_send_btn_auto_set?:                   boolean;
    graphic_emoticons?:                             boolean;
    convert_emoticons?:                             boolean;
    ss_emojis?:                                     boolean;
    seen_onboarding_start?:                         boolean;
    onboarding_cancelled?:                          boolean;
    seen_onboarding_slackbot_conversation?:         boolean;
    seen_onboarding_channels?:                      boolean;
    seen_onboarding_direct_messages?:               boolean;
    seen_onboarding_invites?:                       boolean;
    seen_onboarding_search?:                        boolean;
    seen_onboarding_recent_mentions?:               boolean;
    seen_onboarding_starred_items?:                 boolean;
    seen_onboarding_private_groups?:                boolean;
    seen_onboarding_banner?:                        boolean;
    onboarding_slackbot_conversation_step?:         number;
    set_tz_automatically?:                          boolean;
    dnd_enabled?:                                   boolean;
    dnd_start_hour?:                                string;
    dnd_end_hour?:                                  string;
    dnd_before_monday?:                             string;
    dnd_after_monday?:                              string;
    dnd_enabled_monday?:                            string;
    dnd_before_tuesday?:                            string;
    dnd_after_tuesday?:                             string;
    dnd_enabled_tuesday?:                           string;
    dnd_before_wednesday?:                          string;
    dnd_after_wednesday?:                           string;
    dnd_enabled_wednesday?:                         string;
    dnd_before_thursday?:                           string;
    dnd_after_thursday?:                            string;
    dnd_enabled_thursday?:                          string;
    dnd_before_friday?:                             string;
    dnd_after_friday?:                              string;
    dnd_enabled_friday?:                            string;
    dnd_before_saturday?:                           string;
    dnd_after_saturday?:                            string;
    dnd_enabled_saturday?:                          string;
    dnd_before_sunday?:                             string;
    dnd_after_sunday?:                              string;
    dnd_enabled_sunday?:                            string;
    dnd_days?:                                      string;
    dnd_custom_new_badge_seen?:                     boolean;
    dnd_notification_schedule_new_badge_seen?:      boolean;
    sidebar_behavior?:                              string;
    channel_sort?:                                  string;
    separate_private_channels?:                     boolean;
    separate_shared_channels?:                      boolean;
    sidebar_theme?:                                 string;
    sidebar_theme_custom_values?:                   string;
    no_invites_widget_in_sidebar?:                  boolean;
    no_omnibox_in_channels?:                        boolean;
    k_key_omnibox_auto_hide_count?:                 number;
    show_sidebar_quickswitcher_button?:             boolean;
    ent_org_wide_channels_sidebar?:                 boolean;
    mark_msgs_read_immediately?:                    boolean;
    start_scroll_at_oldest?:                        boolean;
    snippet_editor_wrap_long_lines?:                boolean;
    ls_disabled?:                                   boolean;
    f_key_search?:                                  boolean;
    k_key_omnibox?:                                 boolean;
    prompted_for_email_disabling?:                  boolean;
    no_macelectron_banner?:                         boolean;
    no_macssb1_banner?:                             boolean;
    no_macssb2_banner?:                             boolean;
    no_winssb1_banner?:                             boolean;
    hide_user_group_info_pane?:                     boolean;
    mentions_exclude_at_user_groups?:               boolean;
    mentions_exclude_reactions?:                    boolean;
    privacy_policy_seen?:                           boolean;
    enterprise_migration_seen?:                     boolean;
    search_exclude_bots?:                           boolean;
    load_lato_2?:                                   boolean;
    fuller_timestamps?:                             boolean;
    last_seen_at_channel_warning?:                  number;
    emoji_autocomplete_big?:                        boolean;
    two_factor_auth_enabled?:                       boolean;
    hide_hex_swatch?:                               boolean;
    show_jumper_scores?:                            boolean;
    enterprise_mdm_custom_msg?:                     string;
    client_logs_pri?:                               string;
    flannel_server_pool?:                           string;
    mentions_exclude_at_channels?:                  boolean;
    confirm_clear_all_unreads?:                     boolean;
    confirm_user_marked_away?:                      boolean;
    box_enabled?:                                   boolean;
    seen_single_emoji_msg?:                         boolean;
    confirm_sh_call_start?:                         boolean;
    preferred_skin_tone?:                           string;
    show_all_skin_tones?:                           boolean;
    whats_new_read?:                                number;
    frecency_jumper?:                               string;
    frecency_ent_jumper?:                           string;
    frecency_ent_jumper_backup?:                    string;
    jumbomoji?:                                     boolean;
    newxp_seen_last_message?:                       number;
    show_memory_instrument?:                        boolean;
    enable_unread_view?:                            boolean;
    seen_unread_view_coachmark?:                    boolean;
    enable_react_emoji_picker?:                     boolean;
    seen_custom_status_badge?:                      boolean;
    seen_custom_status_callout?:                    boolean;
    seen_custom_status_expiration_badge?:           boolean;
    used_custom_status_kb_shortcut?:                boolean;
    seen_guest_admin_slackbot_announcement?:        boolean;
    seen_threads_notification_banner?:              boolean;
    seen_name_tagging_coachmark?:                   boolean;
    all_unreads_sort_order?:                        string;
    locale?:                                        string;
    seen_intl_channel_names_coachmark?:             boolean;
    seen_p2_locale_change_message?:                 number;
    seen_locale_change_message?:                    number;
    seen_japanese_locale_change_message?:           boolean;
    seen_shared_channels_coachmark?:                boolean;
    seen_shared_channels_opt_in_change_message?:    boolean;
    has_recently_shared_a_channel?:                 boolean;
    seen_channel_browser_admin_coachmark?:          boolean;
    seen_administration_menu?:                      boolean;
    seen_drafts_section_coachmark?:                 boolean;
    seen_emoji_update_overlay_coachmark?:           boolean;
    seen_sonic_deluxe_toast?:                       number;
    allow_calls_to_set_current_status?:             boolean;
    in_interactive_mas_migration_flow?:             boolean;
    sunset_interactive_message_views?:              number;
    shdep_promo_code_submitted?:                    boolean;
    seen_shdep_slackbot_message?:                   boolean;
    seen_calls_interactive_coachmark?:              boolean;
    allow_cmd_tab_iss?:                             boolean;
    workflow_builder_coachmarks?:                   string;
    seen_gdrive_coachmark?:                         boolean;
    overloaded_message_enabled?:                    boolean;
    seen_highlights_coachmark?:                     boolean;
    seen_highlights_arrows_coachmark?:              boolean;
    seen_highlights_warm_welcome?:                  boolean;
    seen_new_search_ui?:                            boolean;
    seen_channel_search?:                           boolean;
    seen_people_search?:                            boolean;
    a11y_animations?:                               boolean;
    seen_keyboard_shortcuts_coachmark?:             boolean;
    needs_initial_password_set?:                    boolean;
    lessons_enabled?:                               boolean;
    tractor_enabled?:                               boolean;
    tractor_experiment_group?:                      string;
    opened_slackbot_dm?:                            boolean;
    newxp_suggested_channels?:                      string;
    onboarding_complete?:                           boolean;
    welcome_place_state?:                           string;
    whocanseethis_dm_mpdm_badge?:                   boolean;
    highlight_words?:                               string;
    threads_everything?:                            boolean;
    no_text_in_notifications?:                      boolean;
    push_show_preview?:                             boolean;
    growls_enabled?:                                boolean;
    all_channels_loud?:                             boolean;
    push_dm_alert?:                                 boolean;
    push_mention_alert?:                            boolean;
    push_everything?:                               boolean;
    push_idle_wait?:                                number;
    push_sound?:                                    string;
    new_msg_snd?:                                   string;
    push_loud_channels?:                            string;
    push_mention_channels?:                         string;
    push_loud_channels_set?:                        string;
    loud_channels?:                                 string;
    never_channels?:                                string;
    loud_channels_set?:                             string;
    at_channel_suppressed_channels?:                string;
    push_at_channel_suppressed_channels?:           string;
    muted_channels?:                                string;
    all_notifications_prefs?:                       string;
    growth_msg_limit_approaching_cta_count?:        number;
    growth_msg_limit_approaching_cta_ts?:           number;
    growth_msg_limit_reached_cta_count?:            number;
    growth_msg_limit_reached_cta_last_ts?:          number;
    growth_msg_limit_long_reached_cta_count?:       number;
    growth_msg_limit_long_reached_cta_last_ts?:     number;
    growth_msg_limit_sixty_day_banner_cta_count?:   number;
    growth_msg_limit_sixty_day_banner_cta_last_ts?: number;
    growth_all_banners_prefs?:                      string;
    analytics_upsell_coachmark_seen?:               boolean;
    seen_app_space_coachmark?:                      boolean;
    seen_app_space_tutorial?:                       boolean;
    purchaser?:                                     boolean;
    app_action_picker?:                             string;
    show_ent_onboarding?:                           boolean;
    folders_enabled?:                               boolean;
    folder_data?:                                   string;
    seen_corporate_export_alert?:                   boolean;
    show_autocomplete_help?:                        number;
    deprecation_toast_last_seen?:                   number;
    deprecation_modal_last_seen?:                   number;
    failover_proxy_check_completed?:                number;
    edge_upload_proxy_check_completed?:             number;
    app_subdomain_check_completed?:                 number;
    add_apps_prompt_dismissed?:                     boolean;
    add_channel_prompt_dismissed?:                  boolean;
    channel_sidebar_hide_invite?:                   boolean;
    in_prod_surveys_enabled?:                       boolean;
    dismissed_installed_app_dm_suggestions?:        string;
    tz?:                                            string;
    locales_enabled?:                               LocalesEnabled;
    msg_input_sticky_composer?:                     boolean;
    seen_workflow_builder_deluxe_toast?:            boolean;
    workflow_builder_intro_modal_clicked_through?:  boolean;
    has_received_threaded_message?:                 boolean;
    iap1_lab?:                                      number;
    seen_people_search_count?:                      number;
    dismissed_app_launcher_welcome?:                boolean;
    dismissed_app_launcher_limit?:                  boolean;
    dismissed_scroll_search_tooltip_count?:         number;
    seen_contextual_message_shortcuts_modal?:       boolean;
    seen_message_navigation_educational_toast?:     boolean;
    show_shared_channels_education_banner?:         boolean;
    seen_wysiwyg_deluxe_toast?:                     boolean;
}

export interface LocalesEnabled {
    "de-DE"?: string;
    "en-GB"?: string;
    "en-US"?: string;
    "es-ES"?: string;
    "es-LA"?: string;
    "fr-FR"?: string;
    "pt-BR"?: string;
    "ja-JP"?: string;
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
}

export interface AllPrefs {
    channels?: string[];
    groups?:   string[];
}

export interface Team {
    id?:                    string;
    name?:                  string;
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
    avatar_base_url?:       string;
}

export interface Icon {
    image_34?:       string;
    image_44?:       string;
    image_68?:       string;
    image_88?:       string;
    image_102?:      string;
    image_132?:      string;
    image_230?:      string;
    image_original?: string;
}

export interface TeamPrefs {
    default_channels?:                           string[];
    allow_calls?:                                boolean;
    display_email_addresses?:                    boolean;
    gdrive_enabled_team?:                        boolean;
    all_users_can_purchase?:                     boolean;
    enable_shared_channels?:                     number;
    can_receive_shared_channels_invites?:        boolean;
    dropbox_legacy_picker?:                      boolean;
    locale?:                                     string;
    slackbot_responses_disabled?:                boolean;
    hide_referers?:                              boolean;
    msg_edit_window_mins?:                       number;
    allow_message_deletion?:                     boolean;
    calling_app_name?:                           string;
    allow_calls_interactive_screen_sharing?:     boolean;
    display_real_names?:                         boolean;
    who_can_at_everyone?:                        string;
    who_can_at_channel?:                         string;
    who_can_create_channels?:                    string;
    who_can_archive_channels?:                   string;
    who_can_create_groups?:                      string;
    who_can_manage_channel_posting_prefs?:       string;
    who_can_post_general?:                       string;
    who_can_kick_channels?:                      string;
    who_can_kick_groups?:                        string;
    retention_type?:                             number;
    retention_duration?:                         number;
    group_retention_type?:                       number;
    group_retention_duration?:                   number;
    dm_retention_type?:                          number;
    dm_retention_duration?:                      number;
    file_retention_type?:                        number;
    file_retention_duration?:                    number;
    allow_retention_override?:                   boolean;
    default_rxns?:                               string[];
    compliance_export_start?:                    number;
    warn_before_at_channel?:                     string;
    disallow_public_file_urls?:                  boolean;
    who_can_create_delete_user_groups?:          string;
    who_can_edit_user_groups?:                   string;
    who_can_change_team_profile?:                string;
    subteams_auto_create_owner?:                 boolean;
    subteams_auto_create_admin?:                 boolean;
    discoverable?:                               string;
    dnd_days?:                                   string;
    invites_only_admins?:                        boolean;
    invite_requests_enabled?:                    boolean;
    disable_file_uploads?:                       string;
    disable_file_editing?:                       boolean;
    disable_file_deleting?:                      boolean;
    file_limit_whitelisted?:                     boolean;
    uses_customized_custom_status_presets?:      boolean;
    disable_email_ingestion?:                    boolean;
    who_can_manage_guests?:                      WhoCan;
    who_can_create_shared_channels?:             string;
    who_can_manage_shared_channels?:             WhoCan;
    who_can_post_in_shared_channels?:            WhoCan;
    allow_shared_channel_perms_override?:        boolean;
    who_can_manage_ext_shared_channels?:         WhoCan;
    onedrive_enabled_team?:                      boolean;
    enterprise_default_channels?:                string[];
    enterprise_mandatory_channels?:              string[];
    enterprise_mdm_disable_file_download?:       boolean;
    mobile_passcode_timeout_in_seconds?:         number;
    has_hipaa_compliance?:                       boolean;
    self_serve_select?:                          boolean;
    loud_channel_mentions_limit?:                number;
    show_join_leave?:                            boolean;
    enterprise_mobile_device_check?:             boolean;
    disable_sidebar_connect_prompts?:            string[];
    disable_sidebar_install_prompts?:            string[];
    block_file_download?:                        boolean;
    dnd_enabled?:                                boolean;
    dnd_start_hour?:                             string;
    dnd_end_hour?:                               string;
    dnd_before_monday?:                          string;
    dnd_after_monday?:                           string;
    dnd_before_tuesday?:                         string;
    dnd_after_tuesday?:                          string;
    dnd_before_wednesday?:                       string;
    dnd_after_wednesday?:                        string;
    dnd_before_thursday?:                        string;
    dnd_after_thursday?:                         string;
    dnd_before_friday?:                          string;
    dnd_after_friday?:                           string;
    dnd_before_saturday?:                        string;
    dnd_after_saturday?:                         string;
    dnd_before_sunday?:                          string;
    dnd_after_sunday?:                           string;
    dnd_enabled_monday?:                         string;
    dnd_enabled_tuesday?:                        string;
    dnd_enabled_wednesday?:                      string;
    dnd_enabled_thursday?:                       string;
    dnd_enabled_friday?:                         string;
    dnd_enabled_saturday?:                       string;
    dnd_enabled_sunday?:                         string;
    custom_status_presets?:                      Array<string[]>;
    custom_status_default_emoji?:                string;
    auth_mode?:                                  string;
    who_can_manage_integrations?:                WhoCan;
    app_whitelist_enabled?:                      boolean;
    invites_limit?:                              boolean;
    onedrive_app_installed?:                     boolean;
    workflow_builder_enabled?:                   boolean;
    box_app_installed?:                          boolean;
    who_can_approve_ext_shared_channel_invites?: WhoCan;
    who_can_create_workflows?:                   WhoCan;
    invite_requests_admin_apis?:                 boolean;
    who_can_create_ext_shared_channel_invites?:  WhoCan;
    gg_enabled?:                                 boolean;
}

export interface WhoCan {
    type?: string[];
}

export interface User {
    id?:                  string;
    team_id?:             string;
    name?:                string;
    deleted?:             boolean;
    color?:               string;
    real_name?:           string;
    tz?:                  string;
    tz_label?:            string;
    tz_offset?:           number;
    profile?:             Profile;
    is_admin?:            boolean;
    is_owner?:            boolean;
    is_primary_owner?:    boolean;
    is_restricted?:       boolean;
    is_ultra_restricted?: boolean;
    is_bot?:              boolean;
    is_app_user?:         boolean;
    updated?:             number;
    presence?:            string;
    is_workflow_bot?:     boolean;
}

export interface Profile {
    title?:                   string;
    phone?:                   string;
    skype?:                   string;
    real_name?:               string;
    real_name_normalized?:    string;
    display_name?:            string;
    display_name_normalized?: string;
    fields?:                  Fields;
    status_text?:             string;
    status_emoji?:            string;
    status_expiration?:       number;
    avatar_hash?:             string;
    image_original?:          string;
    email?:                   string;
    first_name?:              string;
    last_name?:               string;
    image_24?:                string;
    image_32?:                string;
    image_48?:                string;
    image_72?:                string;
    image_192?:               string;
    image_512?:               string;
    image_1024?:              string;
    status_text_canonical?:   string;
    team?:                    string;
    is_custom_image?:         boolean;
    bot_id?:                  string;
    api_app_id?:              string;
    always_active?:           boolean;
    guest_channels?:          string;
    guest_invited_by?:        string;
}

export interface Fields {
    Xf0DAGNXHT?: Xf0DAGNXHT;
}

export interface Xf0DAGNXHT {
    value?: string;
    alt?:   string;
}

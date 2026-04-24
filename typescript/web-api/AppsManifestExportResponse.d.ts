export interface AppsManifestExportResponse {
    ok?:       boolean;
    manifest?: Manifest;
    error?:    string;
    needed?:   string;
    provided?: string;
    warning?:  string;
}

export interface Manifest {
    _metadata?:           Metadata;
    display_information?: DisplayInformation;
    settings?:            Settings;
    features?:            Features;
    oauth_config?:        OauthConfig;
    functions?:           { [key: string]: Function };
}

export interface Metadata {
    major_version?: number;
    minor_version?: number;
}

export interface DisplayInformation {
    name?:             string;
    long_description?: string;
    description?:      string;
    background_color?: string;
}

export interface Features {
    app_home?:       AppHome;
    bot_user?:       BotUser;
    shortcuts?:      Shortcut[];
    slash_commands?: SlashCommand[];
    unfurl_domains?: string[];
}

export interface AppHome {
    home_tab_enabled?:               boolean;
    messages_tab_enabled?:           boolean;
    messages_tab_read_only_enabled?: boolean;
}

export interface BotUser {
    display_name?:  string;
    always_online?: boolean;
}

export interface Shortcut {
    type?:        string;
    callback_id?: string;
    name?:        string;
    description?: string;
}

export interface SlashCommand {
    command?:       string;
    description?:   string;
    usage_hint?:    string;
    url?:           string;
    should_escape?: boolean;
}

export interface Function {
    title?:             string;
    description?:       string;
    input_parameters?:  { [key: string]: PutParameter };
    output_parameters?: { [key: string]: PutParameter };
}

export interface PutParameter {
    type?:        string;
    name?:        string;
    is_required?: boolean;
    description?: string;
    title?:       string;
    hint?:        string;
    minLength?:   number;
    maxLength?:   number;
    minimum?:     number;
    maximum?:     number;
}

export interface OauthConfig {
    scopes?:                   Scopes;
    redirect_urls?:            string[];
    token_management_enabled?: boolean;
    pkce_enabled?:             boolean;
}

export interface Scopes {
    bot?:  string[];
    user?: string[];
}

export interface Settings {
    description?:               string;
    long_description?:          string;
    background_color?:          string;
    event_subscriptions?:       EventSubscriptions;
    interactivity?:             Interactivity;
    allowed_ip_address_ranges?: string[];
    org_deploy_enabled?:        boolean;
    socket_mode_enabled?:       boolean;
    token_rotation_enabled?:    boolean;
    hermes_app_type?:           string;
    function_runtime?:          string;
    is_mcp_enabled?:            boolean;
}

export interface EventSubscriptions {
    bot_events?:  string[];
    user_events?: string[];
    request_url?: string;
}

export interface Interactivity {
    is_enabled?:               boolean;
    request_url?:              string;
    message_menu_options_url?: string;
}

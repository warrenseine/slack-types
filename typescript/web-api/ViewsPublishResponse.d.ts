export interface ViewsPublishResponse {
    ok?:                boolean;
    warning?:           string;
    error?:             string;
    needed?:            string;
    provided?:          string;
    view?:              View;
    response_metadata?: ResponseMetadata;
}

export interface ResponseMetadata {
    messages?: string[];
    warnings?: any[];
}

export interface View {
    id?:                    string;
    team_id?:               string;
    type?:                  string;
    title?:                 Close;
    submit?:                Close;
    close?:                 Close;
    blocks?:                Block[];
    private_metadata?:      string;
    callback_id?:           string;
    external_id?:           string;
    state?:                 State;
    hash?:                  string;
    clear_on_close?:        boolean;
    notify_on_close?:       boolean;
    submit_disabled?:       boolean;
    root_view_id?:          string;
    previous_view_id?:      string;
    app_id?:                string;
    app_installed_team_id?: string;
    bot_id?:                string;
    entity_url?:            string;
    external_ref?:          ExternalRef;
    app_unfurl_url?:        string;
    message_ts?:            string;
    thread_ts?:             string;
    channel?:               string;
}

export interface Block {
    type?:            string;
    block_id?:        string;
    label?:           Close;
    element?:         BlockElement;
    dispatch_action?: boolean;
    hint?:            Close;
    optional?:        boolean;
}

export interface BlockElement {
    type?:                   string;
    action_id?:              string;
    initial_value?:          InitialValueClass | string;
    dispatch_action_config?: DispatchActionConfig;
    focus_on_load?:          boolean;
    placeholder?:            Close;
    multiline?:              boolean;
    min_length?:             number;
    max_length?:             number;
}

export interface DispatchActionConfig {
    trigger_actions_on?: string[];
}

export interface InitialValueClass {
    type?:     string;
    elements?: InitialValueElement[];
    block_id?: string;
}

export interface InitialValueElement {
    type?:     string;
    elements?: PurpleElement[];
    style?:    string;
    indent?:   number;
    offset?:   number;
    border?:   number;
}

export interface PurpleElement {
    type?:     string;
    elements?: FluffyElement[];
    style?:    string;
    indent?:   number;
    offset?:   number;
    border?:   number;
}

export interface FluffyElement {
    type?:  string;
    range?: string;
    style?: Style;
    text?:  string;
}

export interface Style {
    bold?:             boolean;
    italic?:           boolean;
    strike?:           boolean;
    highlight?:        boolean;
    client_highlight?: boolean;
    underline?:        boolean;
    unlink?:           boolean;
    code?:             boolean;
}

export interface Close {
    type?:  string;
    text?:  string;
    emoji?: boolean;
}

export interface ExternalRef {
    id?:   string;
    type?: string;
}

export interface State {
}

export interface SlackListsItemsInfoResponse {
    ok?:                boolean;
    list?:              List;
    record?:            Record;
    subtasks?:          Record[];
    response_metadata?: ResponseMetadata;
    error?:             string;
    needed?:            string;
    provided?:          string;
    warning?:           string;
}

export interface List {
    id?:                            string;
    created?:                       number;
    timestamp?:                     number;
    name?:                          string;
    title?:                         string;
    mimetype?:                      string;
    filetype?:                      string;
    pretty_type?:                   string;
    user?:                          string;
    user_team?:                     string;
    editable?:                      boolean;
    size?:                          number;
    mode?:                          string;
    is_external?:                   boolean;
    external_type?:                 string;
    is_public?:                     boolean;
    public_url_shared?:             boolean;
    display_as_bot?:                boolean;
    username?:                      string;
    list_metadata?:                 ListMetadata;
    list_limits?:                   ListLimits;
    url_private?:                   string;
    url_private_download?:          string;
    permalink?:                     string;
    permalink_public?:              string;
    last_editor?:                   string;
    list_csv_download_url?:         string;
    updated?:                       number;
    is_starred?:                    boolean;
    skipped_shares?:                boolean;
    teams_shared_with?:             string[];
    is_restricted_sharing_enabled?: boolean;
    has_rich_preview?:              boolean;
    file_access?:                   string;
    access?:                        string;
    org_or_workspace_access?:       string;
    is_ai_suggested?:               boolean;
}

export interface ListLimits {
    over_row_maximum?:         boolean;
    row_count_limit?:          number;
    row_count?:                number;
    archived_row_count?:       number;
    over_column_maximum?:      boolean;
    column_count?:             number;
    column_count_limit?:       number;
    over_view_maximum?:        boolean;
    view_count?:               number;
    view_count_limit?:         number;
    max_attachments_per_cell?: number;
}

export interface ListMetadata {
    schema?:             Schema[];
    views?:              View[];
    integrations?:       string[];
    icon?:               string;
    description?:        string;
    description_blocks?: DescriptionBlock[];
    is_trial?:           boolean;
    subtask_schema?:     SubtaskSchema[];
    creation_source?:    CreationSource;
    todo_mode?:          boolean;
    default_view?:       string;
}

export interface CreationSource {
    type?:         string;
    reference_id?: string;
}

export interface DescriptionBlock {
    type?:     string;
    block_id?: string;
    elements?: DescriptionBlockElement[];
}

export interface DescriptionBlockElement {
    type?:     string;
    elements?: ElementElementClass[];
}

export interface ElementElementClass {
    type?: string;
    text?: string;
}

export interface Schema {
    id?:                string;
    name?:              string;
    key?:               string;
    type?:              string;
    is_primary_column?: boolean;
    options?:           SchemaOptions;
}

export interface SchemaOptions {
    format?:           string;
    show_member_name?: boolean;
    choices?:          Choice[];
}

export interface Choice {
    value?: string;
    label?: string;
    color?: string;
}

export interface SubtaskSchema {
    id?:                string;
    name?:              string;
    key?:               string;
    type?:              string;
    is_primary_column?: boolean;
    options?:           SubtaskSchemaOptions;
}

export interface SubtaskSchemaOptions {
    format?:           string;
    show_member_name?: boolean;
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
}

export interface Column {
    visible?:  boolean;
    key?:      string;
    id?:       string;
    position?: string;
}

export interface Record {
    id?:                string;
    list_id?:           string;
    date_created?:      number;
    created_by?:        string;
    updated_by?:        string;
    fields?:            Field[];
    updated_timestamp?: string;
    is_subscribed?:     boolean;
}

export interface Field {
    key?:       string;
    value?:     boolean;
    checkbox?:  boolean;
    column_id?: string;
}

export interface ResponseMetadata {
    messages?: string[];
}

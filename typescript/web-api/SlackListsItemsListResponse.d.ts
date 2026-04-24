export interface SlackListsItemsListResponse {
    ok?:                boolean;
    items?:             Item[];
    response_metadata?: ResponseMetadata;
    error?:             string;
    needed?:            string;
    provided?:          string;
    warning?:           string;
}

export interface Item {
    id?:                string;
    list_id?:           string;
    date_created?:      number;
    created_by?:        string;
    updated_by?:        string;
    fields?:            Field[];
    updated_timestamp?: string;
}

export interface Field {
    key?:       string;
    column_id?: string;
    value?:     boolean | string;
    rich_text?: RichText[];
    checkbox?:  boolean;
    text?:      string;
}

export interface RichText {
    type?:     string;
    block_id?: string;
    elements?: RichTextElement[];
}

export interface RichTextElement {
    type?:     string;
    elements?: ElementElementClass[];
}

export interface ElementElementClass {
    text?: string;
    type?: string;
}

export interface ResponseMetadata {
    next_cursor?: string;
    messages?:    string[];
}

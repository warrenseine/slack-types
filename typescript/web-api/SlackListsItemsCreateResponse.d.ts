export interface SlackListsItemsCreateResponse {
    ok?:                boolean;
    item?:              Item;
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
    value?:     string;
    rich_text?: RichText[];
    checkbox?:  boolean;
}

export interface RichText {
    type?:     string;
    elements?: RichTextElement[];
}

export interface RichTextElement {
    type?:     string;
    elements?: ElementElementClass[];
}

export interface ElementElementClass {
    type?: string;
    text?: string;
}

export interface ResponseMetadata {
    messages?: string[];
}

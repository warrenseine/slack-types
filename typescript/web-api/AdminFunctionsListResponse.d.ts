export interface AdminFunctionsListResponse {
    ok?:                boolean;
    error?:             string;
    response_metadata?: ResponseMetadata;
    needed?:            string;
    provided?:          string;
    functions?:         Function[];
    warning?:           string;
}

export interface Function {
    id?:                         string;
    callback_id?:                string;
    title?:                      string;
    description?:                string;
    type?:                       string;
    input_parameters?:           PutParameter[];
    output_parameters?:          PutParameter[];
    app_id?:                     string;
    date_created?:               number;
    date_updated?:               number;
    date_deleted?:               number;
    form_enabled?:               boolean;
    date_released?:              number;
    category_id?:                string;
    category_label?:             string;
    product_level_availability?: ProductLevelAvailability;
}

export interface PutParameter {
    type?:        string;
    name?:        string;
    title?:       string;
    is_required?: boolean;
    description?: string;
}

export interface ProductLevelAvailability {
    is_available?: boolean;
    available_to?: string;
}

export interface ResponseMetadata {
    messages?:    string[];
    next_cursor?: string;
}

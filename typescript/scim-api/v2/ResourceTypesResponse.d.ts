export interface ResourceTypesResponse {
    schemas?:   string[];
    Resources?: Resource[];
}

export interface Resource {
    schemas?:          string[];
    id?:               string;
    name?:             string;
    endpoint?:         string;
    description?:      string;
    schema?:           string;
    meta?:             Meta;
    schemaExtensions?: SchemaExtension[];
}

export interface Meta {
    location?:     string;
    resourceType?: string;
}

export interface SchemaExtension {
    schema?:   string;
    required?: boolean;
}

export interface TeamBillableInfoResponse {
    ok?:                boolean;
    billable_info?:     { [key: string]: BillableInfo };
    error?:             string;
    needed?:            string;
    provided?:          string;
    response_metadata?: ResponseMetadata;
    warning?:           string;
}

export interface BillableInfo {
    billing_active?: boolean;
}

export interface ResponseMetadata {
    next_cursor?: string;
}

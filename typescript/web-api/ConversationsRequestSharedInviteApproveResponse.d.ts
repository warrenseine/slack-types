export interface ConversationsRequestSharedInviteApproveResponse {
    ok?:        boolean;
    error?:     string;
    needed?:    string;
    provided?:  string;
    invite_id?: string;
}

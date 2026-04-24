export interface ConversationsRequestSharedInviteDenyResponse {
    ok?:        boolean;
    error?:     string;
    needed?:    string;
    provided?:  string;
    invite_id?: string;
}

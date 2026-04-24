export interface AdminConversationsGetConversationPrefsResponse {
    ok?:       boolean;
    prefs?:    Prefs;
    error?:    string;
    needed?:   string;
    provided?: string;
}

export interface Prefs {
    who_can_post?:      CanThread;
    can_thread?:        CanThread;
    membership_limit?:  MembershipLimit;
    can_huddle?:        CanHuddle;
    enable_at_channel?: CanHuddle;
    enable_at_here?:    CanHuddle;
}

export interface CanHuddle {
    enabled?: boolean;
}

export interface CanThread {
    type?: string[];
    user?: string[];
}

export interface MembershipLimit {
    value?: number;
}

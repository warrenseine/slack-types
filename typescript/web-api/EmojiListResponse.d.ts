export interface EmojiListResponse {
    ok?:                 boolean;
    emoji?:              { [key: string]: string };
    cache_ts?:           string;
    error?:              string;
    needed?:             string;
    provided?:           string;
    categories_version?: string;
    categories?:         Category[];
    warning?:            string;
}

export interface Category {
    name?:        string;
    emoji_names?: string[];
}

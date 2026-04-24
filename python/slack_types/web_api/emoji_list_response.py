# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = emoji_list_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, Dict, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Category:
    name: Optional[str] = None
    emoji_names: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Category':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        emoji_names = from_union([lambda x: from_list(from_str, x), from_none], obj.get("emoji_names"))
        return Category(name, emoji_names)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["emoji_names"] = from_union([lambda x: from_list(from_str, x), from_none], self.emoji_names)
        return result


@dataclass
class EmojiListResponse:
    categories_version: Optional[int] = None
    ok: Optional[bool] = None
    emoji: Optional[Dict[str, str]] = None
    cache_ts: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    categories: Optional[List[Category]] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EmojiListResponse':
        assert isinstance(obj, dict)
        categories_version = from_union([from_none, lambda x: int(from_str(x))], obj.get("categories_version"))
        ok = from_union([from_bool, from_none], obj.get("ok"))
        emoji = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("emoji"))
        cache_ts = from_union([from_str, from_none], obj.get("cache_ts"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        categories = from_union([lambda x: from_list(Category.from_dict, x), from_none], obj.get("categories"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return EmojiListResponse(categories_version, ok, emoji, cache_ts, error, needed, provided, categories, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["categories_version"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.categories_version)
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["emoji"] = from_union([lambda x: from_dict(from_str, x), from_none], self.emoji)
        result["cache_ts"] = from_union([from_str, from_none], self.cache_ts)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["categories"] = from_union([lambda x: from_list(lambda x: to_class(Category, x), x), from_none], self.categories)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def emoji_list_response_from_dict(s: Any) -> EmojiListResponse:
    return EmojiListResponse.from_dict(s)


def emoji_list_response_to_dict(x: EmojiListResponse) -> Any:
    return to_class(EmojiListResponse, x)

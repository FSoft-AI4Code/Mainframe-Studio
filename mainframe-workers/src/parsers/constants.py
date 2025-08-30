from typing import TypedDict, List


class CommentTokenFilter(TypedDict):
    DNP: List[str]
    IBM: List[str]
    UNISYS: List[str]


COMMENT_TOKEN_FILTER: CommentTokenFilter = {
    "DNP": [
        "COMMENTLINE",
        "COMMENTLINE2",
        "COMMENTLINE_2",
        "COMMENTLINE_3",
        "COMMENTLINE_4",
    ],
    "IBM": [
        "COMMENTLINE",
        "COMMENTLINE2",
        "COMMENTLINE_2",
        "COMMENTLINE_3",
        "COMMENTLINE_4",
    ],
    "UNISYS": ["COMMENTLINE", "COMMENTLINE2"],
}

# Default values to skip when searching program names through variable
DEFAULT_VALUES_TO_SKIP = ["SPACE", "SPACES"]

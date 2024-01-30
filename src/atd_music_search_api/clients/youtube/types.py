from typing import TypedDict


class SearchVideoResponseItemId(TypedDict):
    videoId: str


class SearchVideoResponseItem(TypedDict):
    id: SearchVideoResponseItemId


class SearchVideoResponse(TypedDict):
    items: list[SearchVideoResponseItem]

from typing import TypedDict


class SearchTrackResponseTrack(TypedDict):
    link: str
    type: str


class SearchTrackResponse(TypedDict):
    data: list[SearchTrackResponseTrack]

from typing import TypedDict


class SearchTrackResponseResponseHitResult(TypedDict):
    url: str


class SearchTrackResponseResponseHit(TypedDict):
    result: SearchTrackResponseResponseHitResult


class SearchTrackResponseResponse(TypedDict):
    hits: list[SearchTrackResponseResponseHit]


class SearchTrackResponse(TypedDict):
    response: SearchTrackResponseResponse

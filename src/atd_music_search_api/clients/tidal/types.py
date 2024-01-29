from typing import TypedDict


class TokenResponse(TypedDict):
    access_token: str


class SearchTrackResponseTrack(TypedDict):
    id: str


class SearchTrackResponse(TypedDict):
    tracks: list[SearchTrackResponseTrack]


class TrackResponseTrackResource(TypedDict):
    tidalUrl: str


class TrackResponse(TypedDict):
    resource: TrackResponseTrackResource

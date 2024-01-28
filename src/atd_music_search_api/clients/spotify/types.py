from typing import TypedDict


class TokenResponse(TypedDict):
    access_token: str
    token_type: str
    expires_in: int


class SearchTrackResponseTracksItemsExternalURLs(TypedDict):
    spotify: str


class SearchTrackResponseTracksItem(TypedDict):
    external_urls: SearchTrackResponseTracksItemsExternalURLs


class SearchTrackResponseTracks(TypedDict):
    items: list[SearchTrackResponseTracksItem]


class SearchTrackResponse(TypedDict):
    tracks: SearchTrackResponseTracks

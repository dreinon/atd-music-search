from typing import TypedDict


class TokenResponse(TypedDict):
    access_token: str


class SearchTrackResponseTracksItemExternalURLs(TypedDict):
    spotify: str


class SearchTrackResponseTracksItem(TypedDict):
    external_urls: SearchTrackResponseTracksItemExternalURLs


class SearchTrackResponseTracks(TypedDict):
    items: list[SearchTrackResponseTracksItem]


class SearchTrackResponse(TypedDict):
    tracks: SearchTrackResponseTracks

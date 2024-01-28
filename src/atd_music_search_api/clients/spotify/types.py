from typing import TypedDict


class TokenResponse(TypedDict):
    access_token: str


class SearchTrackResponseTracksItemsExternalURLs(TypedDict):
    spotify: str


class SearchTrackResponseTracksItem(TypedDict):
    external_urls: SearchTrackResponseTracksItemsExternalURLs


class SearchTrackResponseTracks(TypedDict):
    items: list[SearchTrackResponseTracksItem]


class SearchTrackResponse(TypedDict):
    tracks: SearchTrackResponseTracks

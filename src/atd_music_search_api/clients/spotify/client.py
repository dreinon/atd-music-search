import httpx
from httpx import Client

from ...config import CONFIG
from .types import SearchTrackResponse, TokenResponse


def get_access_token():
    """
    Get access token from Spotify API
    """
    response = httpx.post(
        f"{CONFIG.spotify.auth_url}/token",
        data={
            "grant_type": "client_credentials",
            "client_id": CONFIG.spotify.client_id,
            "client_secret": CONFIG.spotify.client_secret,
        },
    )

    return TokenResponse(**response.json())["access_token"]


class SpotifyClient(Client):
    """
    Spotify API Client
    """

    def __init__(self, *args, **kwargs):
        token = get_access_token()
        headers = {"Authorization": f"Bearer {token}"}
        super().__init__(
            base_url=CONFIG.spotify.api_url, headers=headers, *args, **kwargs
        )

    def search(self, query: str):
        """
        Search Spotify API
        """
        response = self.get("/search", params={"q": query, "type": "track", "limit": 1})
        response.raise_for_status()

        data = SearchTrackResponse(**response.json())
        return data["tracks"]["items"][0]["external_urls"]["spotify"]


__all__ = ["SpotifyClient"]

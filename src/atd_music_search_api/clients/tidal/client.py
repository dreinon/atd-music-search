import httpx
from httpx import AsyncClient

from ...config import CONFIG
from ..helpers import create_dependency
from .types import SearchTrackResponse, TokenResponse, TrackResponse


def get_access_token():
    """
    Get access token from Tidal API
    """
    response = httpx.post(
        f"{CONFIG.tidal.auth_url}/oauth2/token",
        data={
            "grant_type": "client_credentials",
            "client_id": CONFIG.tidal.client_id,
            "client_secret": CONFIG.tidal.client_secret,
        },
    )

    return TokenResponse(**response.json())["access_token"]


class TidalClient(AsyncClient):
    """
    Tidal API Client
    """

    def __init__(self, *args, **kwargs):
        token = get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.tidal.v1+json",
            "Content-Type": "application/vnd.tidal.v1+json",
        }
        params = {"countryCode": "ES"}
        super().__init__(
            base_url=CONFIG.tidal.api_url,
            headers=headers,
            params=params,
            *args,
            **kwargs,
        )

    async def search(self, query: str):
        """
        Search Tidal API
        """
        search_response = await self.get(
            "/search",
            params={
                "query": query,
                "type": "TRACKS",
                "limit": 1,
                "popularity": "COUNTRY",
            },
        )
        search_response.raise_for_status()

        search_data = SearchTrackResponse(**search_response.json())
        id = search_data["tracks"][0]["id"]

        track_response = await self.get(f"/tracks/{id}")
        track_response.raise_for_status()

        track_data = TrackResponse(**track_response.json())
        return track_data["resource"]["tidalUrl"]


get_tidal_client = create_dependency(TidalClient)

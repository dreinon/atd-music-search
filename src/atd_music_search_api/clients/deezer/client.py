import httpx
from httpx import AsyncClient

from ...config import CONFIG
from ..helpers import create_dependency
from .types import SearchTrackResponse


def get_access_token():
    """
    Get access token from Deezer API
    """
    authorization_response = httpx.post(
        CONFIG.deezer.auth_url,
        data={
            "client_id": CONFIG.deezer.client_id,
            "client_secret": CONFIG.deezer.client_secret,
            "grant_type": "client_credentials",
        },
    )
    data = authorization_response.text
    access_token_chunk = data.split("&")[0]
    access_token = access_token_chunk.split("=")[1]
    return access_token


class DeezerClient(AsyncClient):
    """
    Deezer API Client
    """

    def __init__(self, *args, **kwargs):
        token = get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
        }
        super().__init__(
            base_url=CONFIG.deezer.api_url,
            headers=headers,
            *args,
            **kwargs,
        )

    async def search(self, query: str):
        """
        Search Deezer API
        """
        search_response = await self.get(
            "/search",
            params={"q": query},
        )
        search_response.raise_for_status()

        search_data = SearchTrackResponse(**search_response.json())
        track_data = [
            element for element in search_data["data"] if element["type"] == "track"
        ][0]

        return track_data["link"]


get_deezer_client = create_dependency(DeezerClient)

from httpx import AsyncClient

from ...config import CONFIG
from ..helpers import create_dependency
from .types import SearchTrackResponse


class GeniusClient(AsyncClient):
    """
    Genius API Client
    """

    def __init__(self, *args, **kwargs):
        headers = {
            "Authorization": f"Bearer {CONFIG.genius.access_token}",
        }
        super().__init__(
            base_url=CONFIG.genius.api_url,
            headers=headers,
            *args,
            **kwargs,
        )

    async def search(self, query: str):
        """
        Search Genius API
        """
        search_response = await self.get(
            "/search",
            params={"q": query},
        )
        search_response.raise_for_status()

        search_data = SearchTrackResponse(**search_response.json())
        return search_data["response"]["hits"][0]["result"]["url"]


get_genius_client = create_dependency(GeniusClient)

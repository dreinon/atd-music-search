from httpx import AsyncClient

from ...config import CONFIG
from ..helpers import create_dependency
from .types import SearchVideoResponse


class YoutubeClient(AsyncClient):
    """
    Youtube API Client
    """

    def __init__(self, *args, **kwargs):
        params = {"key": CONFIG.youtube.api_key}
        super().__init__(
            base_url=CONFIG.youtube.api_url,
            params=params,
            *args,
            **kwargs,
        )

    @staticmethod
    def construct_video_url(id: str):
        return f"https://www.youtube.com/watch?v={id}"

    async def search(self, query: str):
        """
        Search Youtube API
        """
        search_response = await self.get(
            "/search",
            params={
                "part": "snippet",
                "q": f"musica {query}",
                "type": "video",
            },
        )
        search_response.raise_for_status()

        search_data = SearchVideoResponse(**search_response.json())
        id = search_data["items"][0]["id"]["videoId"]

        return self.construct_video_url(id)


get_youtube_client = create_dependency(YoutubeClient)

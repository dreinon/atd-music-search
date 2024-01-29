from typing import Annotated

from fastapi import APIRouter, Depends, Security

from ..auth import JWTBearer
from ..clients.spotify import SpotifyClient, get_spotify_client

router = APIRouter(
    prefix="/search", tags=["search"], dependencies=[Security(JWTBearer())]
)


@router.get("/spotify")
async def spotify(
    query: str,
    spotify_client: Annotated[SpotifyClient, Depends(get_spotify_client)],
):
    return await spotify_client.search(query=query)

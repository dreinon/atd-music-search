from asyncio import gather
from typing import Annotated

from fastapi import APIRouter, Depends, Security

from ..auth import JWTBearer
from ..clients.spotify import SpotifyClient, get_spotify_client
from ..clients.tidal import TidalClient, get_tidal_client
from .models import SearchResponse

router = APIRouter(
    prefix="/search", tags=["search"], dependencies=[Security(JWTBearer())]
)


@router.get("/")
async def search(
    query: str,
    spotify_client: Annotated[SpotifyClient, Depends(get_spotify_client)],
    tidal_client: Annotated[TidalClient, Depends(get_tidal_client)],
) -> SearchResponse:
    spotify_coroutine = spotify_client.search(query=query)
    tidal_coroutine = tidal_client.search(query=query)

    [spotify, tidal] = await gather(spotify_coroutine, tidal_coroutine)
    return {"spotify": spotify, "tidal": tidal}


@router.get("/spotify")
async def spotify(
    query: str,
    spotify_client: Annotated[SpotifyClient, Depends(get_spotify_client)],
):
    return await spotify_client.search(query=query)


@router.get("/tidal")
async def tidal(
    query: str,
    tidal_client: Annotated[TidalClient, Depends(get_tidal_client)],
):
    return await tidal_client.search(query=query)

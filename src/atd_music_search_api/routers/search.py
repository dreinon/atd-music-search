from asyncio import gather
from typing import Annotated

from fastapi import APIRouter, Depends, Security

from ..auth import JWTBearer
from ..clients.deezer import DeezerClient, get_deezer_client
from ..clients.genius import GeniusClient, get_genius_client
from ..clients.spotify import SpotifyClient, get_spotify_client
from ..clients.tidal import TidalClient, get_tidal_client
from ..clients.youtube import YoutubeClient, get_youtube_client
from .models import SearchResponse

router = APIRouter(
    prefix="/search", tags=["search"], dependencies=[Security(JWTBearer())]
)


@router.get("/spotify")
async def search_song_in_spotify(
    query: str,
    spotify_client: Annotated[SpotifyClient, Depends(get_spotify_client)],
) -> str:
    return await spotify_client.search(query=query)


@router.get("/tidal")
async def search_song_in_tidal(
    query: str,
    tidal_client: Annotated[TidalClient, Depends(get_tidal_client)],
) -> str:
    return await tidal_client.search(query=query)


@router.get("/deezer")
async def search_song_in_deezer(
    query: str, deezer_client: Annotated[DeezerClient, Depends(get_deezer_client)]
) -> str:
    return await deezer_client.search(query=query)


@router.get("/youtube")
async def search_song_in_youtube(
    query: str, youtube_client: Annotated[YoutubeClient, Depends(get_youtube_client)]
) -> str:
    return await youtube_client.search(query=query)


@router.get("/genius")
async def search_song_in_genius(
    query: str, genius_client: Annotated[GeniusClient, Depends(get_genius_client)]
) -> str:
    return await genius_client.search(query=query)


@router.get("/")
async def search_in_all_platforms(
    query: str,
    spotify_client: Annotated[SpotifyClient, Depends(get_spotify_client)],
    tidal_client: Annotated[TidalClient, Depends(get_tidal_client)],
    deezer_client: Annotated[DeezerClient, Depends(get_deezer_client)],
    youtube_client: Annotated[YoutubeClient, Depends(get_youtube_client)],
    genius_client: Annotated[GeniusClient, Depends(get_genius_client)],
) -> SearchResponse:
    spotify_coroutine = search_song_in_spotify(query, spotify_client)
    tidal_coroutine = search_song_in_tidal(query, tidal_client)
    deezer_coroutine = search_song_in_deezer(query, deezer_client)
    youtube_coroutine = search_song_in_youtube(query, youtube_client)
    genius_coroutine = search_song_in_genius(query, genius_client)

    [spotify, tidal, deezer, youtube, genius] = await gather(
        spotify_coroutine,
        tidal_coroutine,
        deezer_coroutine,
        youtube_coroutine,
        genius_coroutine,
    )
    return SearchResponse(
        spotify=spotify, tidal=tidal, deezer=deezer, youtube=youtube, genius=genius
    )

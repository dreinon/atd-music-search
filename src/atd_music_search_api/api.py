from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .clients import SpotifyClient

app = FastAPI(title="ATD Music Search API")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> str:
    return "Welcome to ATD Music Search API!"

@app.get("/search")
async def search(query: str):
    with SpotifyClient() as spotify_client:
        return spotify_client.search(query=query)
    
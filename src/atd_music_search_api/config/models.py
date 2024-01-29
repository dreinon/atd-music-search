from pydantic import BaseModel


class AtdMusicSearchAPI(BaseModel):
    secret: str


class Spotify(BaseModel):
    auth_url: str
    api_url: str
    client_id: str
    client_secret: str


class Tidal(BaseModel):
    auth_url: str
    api_url: str
    client_id: str
    client_secret: str


class ConfigType(BaseModel):
    atd_music_search_api: AtdMusicSearchAPI
    spotify: Spotify
    tidal: Tidal

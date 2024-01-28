from pydantic import BaseModel


class AtdMusicSearchAPI(BaseModel):
    secret: str


class ConfigType(BaseModel):
    atd_music_search_api: AtdMusicSearchAPI

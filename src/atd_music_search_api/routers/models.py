from pydantic import BaseModel


class SearchResponse(BaseModel):
    spotify: str
    tidal: str
    deezer: str
    youtube: str
    genius: str

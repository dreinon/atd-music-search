from pydantic import BaseModel


class SearchResponse(BaseModel):
    spotify: str
    tidal: str

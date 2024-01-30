from enum import Enum


class Platform(Enum):
    Spotify = "spotify"
    Tidal = "tidal"
    Deezer = "deezer"
    Youtube = "youtube"
    Genius = "genius"


PlatformColors = {
    Platform.Spotify: "bright_green",
    Platform.Tidal: "white",
    Platform.Deezer: "purple",
    Platform.Youtube: "bright_red",
    Platform.Genius: "bright_yellow",
}

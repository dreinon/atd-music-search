import time
from typing import Optional

import httpx
import typer
from jose import jwt
from rich import print

from .config import CONFIG
from .helpers import color_platform
from .types import Platform


def generate_jwt() -> str:
    now = int(time.time())
    tomorrow = now + 24 * 3600
    payload = {
        "iss": "atd-music-search-cli",
        "iat": now,
        "exp": tomorrow,
    }
    return jwt.encode(
        payload, key=CONFIG.atd_music_search_api.secret, algorithm="HS256"
    )


def call_api(
    query: str, platform: Optional[Platform] = None, verbose=True
) -> dict[Platform, str]:
    if verbose:
        print(
            f"Searching {query}{ f' on {color_platform(platform)}' if platform else ''}...\n"
        )

    platform_path = f"/{platform.value}" if platform else ""

    try:
        response = httpx.get(
            f"{CONFIG.atd_music_search_api.url}/search{platform_path}/",
            params={"query": query},
            headers={"Authorization": f"Bearer {generate_jwt()}"},
        )
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        typer.echo(f"Error: {e}")
        raise typer.Exit(code=1)

    if platform:
        return {platform: response.json()}

    return {Platform(k): v for k, v in response.json().items()}


def print_response(response: dict[Platform, str]):
    for platform, result in response.items():
        print(f"{color_platform(platform)}: {result}")

import logging
import time
from typing import Any, cast

from jose import JWTError, jwt

from atd_music_search_api.config import CONFIG

ALGORITHM = "HS256"


def decode_token(token: str) -> dict[Any, Any]:
    JWT_SECRET = CONFIG.atd_music_search_api.secret

    try:
        return cast(dict[Any, Any], jwt.decode(token, JWT_SECRET, algorithms=ALGORITHM))
    except JWTError:
        logging.debug("Bearer token couldn't be decoded")
        return {}


def create_token(subject: str, secret: str | None = None, expiration: int | None = None) -> str:
    JWT_SECRET = CONFIG.atd_music_search_api.secret if not secret else secret
    now = int(time.time())
    tomorrow = now + 24 * 3600
    payload = {
        "iss": "atd-music-search-api",
        "sub": subject,
        "iat": now,
        "exp": tomorrow if not expiration else expiration,
    }
    return cast(str, jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM))

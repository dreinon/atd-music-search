import os
from logging import DEBUG

import uvicorn


def export_config(override_env_with: str | None = None) -> None:
    env = override_env_with or os.getenv("ENV")
    with open(f"config/api/{env}.json", encoding="utf-8") as f:
        os.environ["API_CONFIG"] = f.read()


if __name__ == "__main__":
    export_config()

    uvicorn.run(
        "src.atd_music_search_api.api:app",
        port=8080,
        log_level=DEBUG,
        reload=True,
        reload_dirs=["src/atd_music_search_api"],
    )

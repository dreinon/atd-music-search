from logging import DEBUG

import uvicorn

from .utils import export_config

if __name__ == "__main__":
    export_config()

    uvicorn.run(
        "src.atd_music_search_api.api:app",
        port=8080,
        log_level=DEBUG,
        reload=True,
        reload_dirs=["src/atd_music_search_api"],
    )

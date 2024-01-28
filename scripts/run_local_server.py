import logging
import os
import sys

from loguru import logger
from uvicorn import Config, Server

from .utils import export_config

LOG_LEVEL = logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG"))
JSON_LOGS = os.environ.get("JSON_LOGS", "0") == "1"


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1
        message = record.getMessage()

        logger.opt(depth=depth, exception=record.exc_info).log(level, message)


def setup_logging():
    # intercept everything at the root logger
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(LOG_LEVEL)

    # remove every other logger's handlers
    # and propagate to root logger
    logging_manager = logging.root.manager
    for name in logging_manager.loggerDict.keys():  # pylint: disable=no-member
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    # configure loguru
    logger.configure(handlers=[{"sink": sys.stdout, "serialize": JSON_LOGS}])


if __name__ == "__main__":
    export_config()
    server = Server(
        Config("src.atd_music_search_api.api:app", port=8080, log_level=LOG_LEVEL, reload=True),
    )

    # setup logging last, to make sure no library overwrites it
    # (they shouldn't, but it happens)
    setup_logging()

    server.run()

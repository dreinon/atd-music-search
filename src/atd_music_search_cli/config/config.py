import os

from .models import ConfigType


def import_config():
    return ConfigType.model_validate_json(os.environ["CLI_CONFIG"])

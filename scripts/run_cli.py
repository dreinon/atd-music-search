import os
import sys


def export_config(override_env_with: str | None = None) -> None:
    env = override_env_with or os.getenv("ENV")
    with open(f"config/cli/{env}.json", encoding="utf-8") as f:
        os.environ["CLI_CONFIG"] = f.read()


if __name__ == "__main__":
    export_config()

    args_string = " ".join([f'"{arg}"' if " " in arg else arg for arg in sys.argv[1:]])
    cmd = f"python -m src.atd_music_search_cli.cli {args_string}"
    os.system(cmd)

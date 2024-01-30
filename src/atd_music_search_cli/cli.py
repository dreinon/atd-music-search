from typing import Optional

import typer
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from rich import print

from .api import call_api, print_response
from .helpers import color_platform
from .types import Platform

cli = typer.Typer(name="ATD Music Search CLI")

platform_arg = typer.Argument(
    ...,
    help="Platform to search into",
    case_sensitive=False,
)

song_arg = typer.Argument(
    ...,
    help="Song to search",
)

open_flag = typer.Option(
    False,
    "--open",
    "-o",
    help="Open the link in the browser",
)


@cli.command(help="Search in a specific platform", no_args_is_help=True)
def platform(
    platform: Platform = platform_arg, song: str = song_arg, open: bool = open_flag
):
    response = call_api(song, platform)

    print_response(response)

    if open:
        print(f"Opening {color_platform(platform)}...")
        typer.launch(response[platform])


@cli.command(help="Search in all platforms", no_args_is_help=True)
def all(song: str = song_arg):
    response = call_api(song)
    return print_response(response)


def main_interactive():
    song = inquirer.text(
        message=("Write the name of the song " "you want to search 🔎")
    ).execute()
    platform: Optional[Platform] = inquirer.select(
        message="Select a platform to search into:",
        choices=[
            *[Choice(name=platform.name, value=platform) for platform in Platform],
            Choice(name="All", value=None),
        ],
        default=None,
    ).execute()

    response = call_api(song, platform)
    print_response(response)

    if platform:
        open = inquirer.confirm(
            message=f"Do you want to open the link?",
            default=False,
        ).execute()
        if open:
            print(f"Opening {color_platform(platform)}...")
            typer.launch(response[platform])


@cli.callback(no_args_is_help=True, invoke_without_command=True)
def main(
    interactive: bool = typer.Option(
        False, "--interactive", "-i", help="Interactive mode"
    ),
):
    """
    ATD Music Search CLI
    """
    if interactive:
        return main_interactive()


if __name__ == "__main__":
    cli()

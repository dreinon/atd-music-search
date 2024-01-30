from .types import Platform, PlatformColors


def color_platform(platform: Platform) -> str:
    color = PlatformColors[platform]
    return f"[{color}]{platform.name}[/{color}]"

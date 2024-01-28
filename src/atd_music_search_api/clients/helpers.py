from typing import Type

import httpx


def create_dependency(client_constructor: Type[httpx.Client]):
    def dependency():
        with client_constructor() as client:
            yield client

    return dependency

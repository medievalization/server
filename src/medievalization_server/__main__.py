#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medievalization Server

Launcher
"""
import asyncio
import os
import sys
import traceback
from typing import NoReturn

from websockets.server import serve

from medievalization_server import server


async def start() -> None:
    """Start server."""
    async with serve(server, "localhost", 8765):
        print("Running on localhost:8765")
        await asyncio.Future()


def main() -> NoReturn:
    """Launch the server."""
    try:
        asyncio.run(start())
        sys.exit(os.EX_OK)
    except Exception as exception:  # pylint: disable=broad-exception-caught
        traceback.print_exception(exception)
        try:
            if isinstance(exception, OSError):
                sys.exit(exception.errno)
            else:
                raise exception
        except Exception:  # pylint: disable=broad-exception-caught
            sys.exit(os.EX_SOFTWARE)


if __name__ == "__main__":
    main()

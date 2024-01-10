#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medievalization Server

Launcher
"""
import asyncio

from websockets.server import serve

from server import server


async def main() -> None:
    """Start server."""
    async with serve(server, "localhost", 8765):
        print("Running on localhost:8765")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())

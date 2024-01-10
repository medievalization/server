# -*- coding: utf-8 -*-
"""
Medievalization Server

Main
"""
import json
from typing import TypedDict, TypeAlias, Union

from websockets.server import WebSocketServerProtocol

JSONValue: TypeAlias = Union[str, int, float, bool, None, list["JSONValue"], "JSONData"]
JSONData: TypeAlias = dict[str, JSONValue]


class Message(TypedDict):
    """A message from the socket."""

    type: str
    data: JSONData


def board(width: int, height: int) -> list[list[int]]:
    """Makes a checkerboard."""
    return [[int(i % 2 != j % 2) for i in range(width)] for j in range(height)]


async def server(websocket: WebSocketServerProtocol) -> None:
    """
    Server
    """
    async for message in websocket:
        data: Message = json.loads(message)

        # Indev Part
        if data["type"] == "tile":
            print("tile")
            await websocket.send(json.dumps({"type": "tile", "data": board(16, 9)}))

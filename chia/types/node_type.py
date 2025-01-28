from __future__ import annotations

from enum import IntEnum


class NodeType(IntEnum):
    FULL_NODE = 1
    HARVESTER = 2
    FARMER = 3
    TIMELORD = 4
    INTRODUCER = 5
    WALLET = 6
    DATA_LAYER = 7

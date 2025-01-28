from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, SupportsBytes, Union

from chia.protocols.protocol_message_types import ProtocolMessageTypes
from chia.types.node_type import NodeType  # TODO: remove this and change a lot of `import` statements
from chia.util.ints import uint8, uint16
from chia.util.streamable import Streamable, streamable

__all__ = ["Message", "NodeType", "make_msg"]


@streamable
@dataclass(frozen=True)
class Message(Streamable):
    type: uint8  # one of ProtocolMessageTypes
    # message id
    id: Optional[uint16]
    # Message data for that type
    data: bytes


def make_msg(msg_type: ProtocolMessageTypes, data: Union[bytes, SupportsBytes]) -> Message:
    return Message(uint8(msg_type.value), None, bytes(data))

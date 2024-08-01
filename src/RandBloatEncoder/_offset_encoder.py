from src.RandBloatEncoder.__internals.base_encoder import BaseEncoder
import random

class OffsetEncoder(BaseEncoder):

    def __init__(self, offset = None) -> None:
        self.offset = offset or random.randint(0, 255)
    
    def encodeBytes(self, message: bytes) -> bytes:
        output: bytearray = bytearray()
        output.extend(random.randbytes(self.offset))
        for byte in message:
            output.append(byte)
            output.extend(random.randbytes(self.offset))
            offset = random.randint(1, 255)
            output.append(offset)
            output.extend(random.randbytes(offset))
        return bytes(output)

    def decodeBytes(self, encoded_message: bytes) -> bytes:
        output: bytearray = bytearray()
        index: int = self.offset
        while index < len(encoded_message):
            output.append(encoded_message[index])
            index += self.offset
            index += 1
            index += encoded_message[index]
            index += 1
        return bytes(output)
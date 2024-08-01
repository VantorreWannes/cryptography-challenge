from src.RandBloatEncoder.__internals.base_encoder import BaseEncoder
import random

class SimpleEncoder(BaseEncoder):

    def encodeBytes(self, message: bytes) -> bytes:
        output: bytearray = bytearray()
        for byte in message:
            output.append(byte)
            offset = random.randint(1, 255)
            output.append(offset)
            output.extend(random.randbytes(offset))
        return bytes(output)
    
    def decodeBytes(self, encoded_message: bytes) -> bytes:
        output: bytearray = bytearray()
        index: int = 0
        while index < len(encoded_message):
            output.append(encoded_message[index])
            index += 1
            index += encoded_message[index]
            index += 1
        return bytes(output)
    
if __name__ == '__main__':
    pass
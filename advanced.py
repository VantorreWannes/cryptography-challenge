import random

class AdvancedEncoder:

    def __init__(self, offset = 0) -> None:
        self.index = offset

    def encodeBytes(self, message: bytes) -> bytes:
        output: bytearray = bytearray()
        output.extend(random.randbytes(self.index))
        for byte in message:
            output.append(byte)
            offset = random.randint(1, 255)
            output.append(offset)
            output.extend(random.randbytes(offset))
        return bytes(output)

    def decodeBytes(self, encoded_message: bytes) -> bytes:
        output: bytearray = bytearray()
        index: int = self.index
        while index < len(encoded_message):
            output.append(encoded_message[index])
            index += 1
            index += encoded_message[index]
            index += 1
        return bytes(output)

    def encodeString(self, message: str) -> bytes:
        message_bytes: bytes = message.encode('utf-8')
        return self.encodeBytes(message_bytes)
    
    def decodeString(self, encoded_message: bytes) -> str:
        decoded_message: bytes = self.decodeBytes(encoded_message)
        return decoded_message.decode('utf-8')

if __name__ == '__main__':
    MESSAGE = "HELLO"
    ENCODER = AdvancedEncoder()
    ENCODED_MESSAGE = ENCODER.encodeString(MESSAGE)
    DECODED_MESSAGE = ENCODER.decodeString(ENCODED_MESSAGE)
    print(DECODED_MESSAGE)

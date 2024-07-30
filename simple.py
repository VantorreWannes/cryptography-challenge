import random

class SimpleEncoder:

    def encodeBytes(message: bytes) -> bytes:
        output: bytearray = bytearray()
        for byte in message:
            output.append(byte)
            offset = random.randint(1, 255)
            output.append(offset)
            output.extend(random.randbytes(offset))
        return bytes(output)

    def decodeBytes(encoded_message: bytes) -> bytes:
        output: bytearray = bytearray()
        index: int = 0
        while index < len(encoded_message):
            output.append(encoded_message[index])
            index += 1
            index += encoded_message[index]
            index += 1
        return bytes(output)

    def encodeString(message: str) -> bytes:
        message_bytes: bytes = message.encode('utf-8')
        return SimpleEncoder.encodeBytes(message_bytes)
    
    def decodeString(encoded_message: bytes) -> str:
        decoded_message: bytes = SimpleEncoder.decodeBytes(encoded_message)
        return decoded_message.decode('utf-8')

if __name__ == '__main__':
    MESSAGE = "HELLO"
    ENCODED_MESSAGE = SimpleEncoder.encodeString(MESSAGE)
    DECODED_MESSAGE = SimpleEncoder.decodeString(ENCODED_MESSAGE)
    print(DECODED_MESSAGE)

import random

def encode(message: str, offset = 0) -> bytes:
    message_bytes = message.encode('utf-8')
    buffer_len = sum([byte for byte in message_bytes]) + offset * 2
    buffer = list(random.randbytes(buffer_len))
    positive_offset, negative_offset = offset, (buffer_len - offset - 1)
    for byte in message_bytes:
        buffer[positive_offset] = (byte + buffer[negative_offset]) % 256
        positive_offset += byte
        negative_offset -= byte
    return bytes(buffer)

def decode(encoded_buffer, offset = 0) -> str:
    message: list[str] = []
    buffer_len = len(encoded_buffer)
    positive_offset, negative_offset = offset, (buffer_len - offset - 1)
    while positive_offset < buffer_len - offset:
        decoded_byte = (encoded_buffer[positive_offset] - encoded_buffer[negative_offset]) % 256
        positive_offset += decoded_byte
        negative_offset -= decoded_byte
        message.append(chr(decoded_byte))
    return "".join(message)

if __name__ == '__main__':
    START_POS = 25
    encoded = encode("A 0 | Hello from me | 0 A", START_POS)
    decoded = decode(encoded, START_POS)
    with open('encoded.bin', 'wb') as f:
        f.write(encoded)
    print(decoded)
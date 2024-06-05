import random

def encode(secret_message: str, pos = 0) -> list[int]:
    secret_message = secret_message.encode('utf-8')
    rand_bytes = [int(i) for i in random.randbytes(len(secret_message)*(256+pos))]
    neg = (len(rand_bytes)-1) - pos
    for byte in secret_message:
        neg -= rand_bytes[neg]
        rand_bytes[pos] = (byte + rand_bytes[neg]) % 256
        pos += rand_bytes[pos+1]
    return rand_bytes

def decode(encoded: list[int], pos = 0) -> str:
    decoded: bytearray = []
    neg = (len(encoded)-1) - pos
    while pos+1 < len(encoded):
        neg -= encoded[neg]
        decoded_byte = (encoded[pos] - encoded[neg]) % 256
        decoded.append(decoded_byte)
        pos += encoded[pos+1]
    return "".join([chr(i) for i in bytes(decoded)])
    

if __name__ == '__main__':
    START_POS = 0
    encoded = encode("X 82 Hiya Uwo 28 x", START_POS)
    decoded = decode(encoded, START_POS)
    print(decoded)
    with open('encoded.bin', 'wb') as f:
        f.write(bytes(encoded))




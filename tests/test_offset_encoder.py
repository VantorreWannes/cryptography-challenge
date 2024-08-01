from src import OffsetEncoder

def test_encode_bytes():
    MESSAGE = bytes([0, 1, 2, 3])
    ENCODER = OffsetEncoder()
    ENCODED_MESSAGE = ENCODER.encodeBytes(MESSAGE)
    DECODED_MESSAGE = ENCODER.decodeBytes(ENCODED_MESSAGE)
    assert DECODED_MESSAGE == MESSAGE

def test_encode_string():
    MESSAGE = "HELLO WORLD"
    ENCODER = OffsetEncoder()
    ENCODED_MESSAGE = ENCODER.encodeString(MESSAGE)
    DECODED_MESSAGE = ENCODER.decodeString(ENCODED_MESSAGE)
    assert DECODED_MESSAGE == MESSAGE

if __name__ ==  '__main__':
    test_encode_bytes()
    test_encode_string()
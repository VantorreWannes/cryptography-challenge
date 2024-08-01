from abc import ABC, abstractmethod

class BaseEncoder(ABC):

    @abstractmethod
    def encodeBytes(self, message: bytes) -> bytes:
        pass

    @abstractmethod
    def decodeBytes(self, encoded_message: bytes) -> bytes:
        pass

    def encodeString(self, message: str) -> bytes:
        message_bytes: bytes = message.encode('utf-8')
        return self.encodeBytes(message_bytes)
    
    def decodeString(self, encoded_message: bytes) -> str:
        decoded_message: bytes = self.decodeBytes(encoded_message)
        return decoded_message.decode('utf-8')

if __name__ == '__main__':
    pass
class CaesarCypher:
    def __init__(self, offset: int):
        self.offset = offset

    def encrypt(self, message: str) -> str:
        return "".join([chr(ord(c) + self.offset) for c in message])

    def decrypt(self, message: str) -> str:
        return "".join([chr(ord(c) - self.offset) for c in message])
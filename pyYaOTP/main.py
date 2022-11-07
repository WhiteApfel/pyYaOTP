import base64
import hashlib
import hmac
import struct
import time


class YaOTP:
    def __init__(self, pin: str, secret: str):
        self.key = hashlib.sha256(pin.encode() + self.decode_secret(secret)).digest()

    @staticmethod
    def decode_secret(secret: str) -> bytes:
        last_block_width = len(secret) % 8
        if last_block_width != 0:
            secret += (8 - last_block_width) * "="
        return base64.b32decode(secret)

    @staticmethod
    def otp_to_yandex(otp: int) -> str:
        otp = otp % (26**8)
        code = ""
        while len(code) < 8:
            code += chr(ord("a") + (otp % 26))
            otp //= 26
        return code[::-1]

    @staticmethod
    def time_to_counter(timestamp: int | float) -> int:
        return int(timestamp) // 30

    def generate_code(self, counter: int = None) -> str:
        if counter is None:
            counter = int(time.time()) // 30

        hmac_hash = hmac.new(
            self.key, struct.pack(">q", counter), hashlib.sha256
        ).digest()
        offset = hmac_hash[len(hmac_hash) - 1] & 0xF
        otp = (
            struct.unpack(">q", hmac_hash[offset : offset + 8])[0] & 0x7FFFFFFFFFFFFFFF
        )  # max int64

        return self.otp_to_yandex(otp)

import pytest

from pyYaOTP import YaOTP


@pytest.mark.parametrize(
    "encoded, decoded",
    [
        ("RJPHNTVRAINQQ3GKVOMRX33QQU", b"\x8a^v\xce\xb1\x02\x1b\x08l\xca\xab\x99\x1b\xefp\x85"),
        ("RJPHROCKETBANKRDFOREFERQQU", b"\x8a^x\xb8J$\xc2\x06\xaa#+\xa2B\x920\x85"),
    ],
)
def test_valid_decode(encoded: str, decoded: bytes):
    assert YaOTP.decode_secret(secret=encoded) == decoded

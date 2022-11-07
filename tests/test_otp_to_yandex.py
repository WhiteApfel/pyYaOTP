import pytest

from pyYaOTP import YaOTP


@pytest.mark.parametrize(
    "otp, valid",
    [
        (3891851972300632616, "cyuoctwq"),
        (8418992669993802599, "lboprhnb"),
    ],
)
def test_valid_convert(otp: int, valid: str):
    assert YaOTP.otp_to_yandex(otp=otp) == valid

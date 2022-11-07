import pytest as pytest

from pyYaOTP import YaOTP


@pytest.mark.parametrize(
    "pin, secret, counter, valid",
    [
        ("5321", "RJPHNTVRAINQQ3GKVOMRX33QQU", 55594434, "uvsdaxwh"),
        ("3040", "RJPHAAGAYO6QQ3WHITEAPFELQU", 55594435, "rqrjddil"),
        ("5321304044087960", "RJPHMYLIFEISNULLANDVOIDQQU", 55594436, "vjgwjmxi"),
        ("5536913848639080", "RJPHROCKETBANKRDFOREFERQQU", 55594437, "fntewgax"),
    ],
)
def test_valid_pin_valid_secret_valid_counter(
    pin: str, secret: str, counter: int, valid: str
):
    yaotp = YaOTP(pin=pin, secret=secret)
    assert yaotp.generate_code(counter=counter) == valid


@pytest.mark.parametrize(
    "pin, secret, counter, valid",
    [
        ("4408", "RJPHNTVRAINQQ3GKVOMRX33QQU", 55594434, "uvsdaxwh"),
        ("7960", "RJPHAAGAYO6QQ3WHITEAPFELQU", 55594435, "rqrjddil"),
        ("4285130001982621", "RJPHMYLIFEISNULLANDVOIDQQU", 55594436, "vjgwjmxi"),
        ("5379653018710812", "RJPHROCKETBANKRDFOREFERQQU", 55594437, "fntewgax"),
    ],
)
def test_invalid_pin_valid_secret_invalid_counter(
    pin: str, secret: str, counter: int, valid: str
):
    yaotp = YaOTP(pin=pin, secret=secret)
    with pytest.raises(AssertionError):
        assert yaotp.generate_code(counter=counter) == valid


@pytest.mark.parametrize(
    "pin, secret, counter, valid",
    [
        ("5321", "RJPHAAGAYO6QQ3WHITEAPFELQU", 55594434, "uvsdaxwh"),
        ("3040", "RJPHNTVRAINQQ3GKVOMRX33QQU", 55594435, "rqrjddil"),
        ("5321304044087960", "RJPHROCKETBANKRDFOREFERQQU", 55594436, "vjgwjmxi"),
        ("5536913848639080", "RJPHMYLIFEISNULLANDVOIDQQU", 55594437, "fntewgax"),
    ],
)
def test_valid_pin_invalid_secret_valid_counter(
    pin: str, secret: str, counter: int, valid: str
):
    yaotp = YaOTP(pin=pin, secret=secret)
    with pytest.raises(AssertionError):
        assert yaotp.generate_code(counter=counter) == valid


@pytest.mark.parametrize(
    "pin, secret, counter, valid",
    [
        ("5321", "RJPHNTVRAINQQ3GKVOMRX33QQU", 55594435, "uvsdaxwh"),
        ("3040", "RJPHAAGAYO6QQ3WHITEAPFELQU", 55594436, "rqrjddil"),
        ("5321304044087960", "RJPHMYLIFEISNULLANDVOIDQQU", 55594437, "vjgwjmxi"),
        ("5536913848639080", "RJPHROCKETBANKRDFOREFERQQU", 55594438, "fntewgax"),
    ],
)
def test_valid_pin_valid_secret_invalid_counter(
    pin: str, secret: str, counter: int, valid: str
):
    yaotp = YaOTP(pin=pin, secret=secret)
    with pytest.raises(AssertionError):
        assert yaotp.generate_code(counter=counter) == valid

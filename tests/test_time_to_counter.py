import pytest

from pyYaOTP import YaOTP


@pytest.mark.parametrize(
    "timestamp, valid",
    [
        (1667834098.3083632, 55594469),
        (1667834098, 55594469),
        (1667834163.4830096, 55594472),
        (1667834163, 55594472),
    ],
)
def test_valid_convert(timestamp: int | float, valid: int):
    assert YaOTP.time_to_counter(timestamp=timestamp) == valid

# pyYaOTP

**Python implementation of Yandex OTP (Яндекс.Ключ) based on [KeeYaOtp](https://github.com/norblik/KeeYaOtp)**

## Installation

```shall
python -m pip install pyYaOTP
# or
python -m pip install git+https://github.com/WhiteApfel/pyYaOTP.git
# or
git clone https://github.com/WhiteApfel/pyYaOTP.git
cd pyYaOTP
python setup.py install
```

## How to use

```python
from pyYaOTP import YaOTP

yaotp = YaOTP(pin="<<pin>>", secret="<<secret>>")
print(yaotp.generate_code())
```

---

**keywords**: Яндекс.Ключ, Yandex.Key, Yandex OTP, YaOTP
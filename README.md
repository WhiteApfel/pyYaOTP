# pyYaOTP

**Python implementation of Yandex OTP (Яндекс.Ключ) based on [KeeYaOtp](https://github.com/norblik/KeeYaOtp)**

## Installation

```shall
python -m pip install pyYaOTP
# or
TAG_VERSION=git python -m pip install git+https://github.com/WhiteApfel/pyYaOTP.git
# or
git clone https://github.com/WhiteApfel/pyYaOTP.git
cd pyYaOTP
TAG_VERSION=local python setup.py install
```

## How to use

```python
from pyYaOTP import YaOTP

yaotp = YaOTP(pin="<<pin>>", secret="<<secret>>", login="me@asex.space")
print(yaotp.generate_code())

# QR (Magic) auth
if yaotp.magic_auth(track_id=input("Track ID >>> ")) is True:
    print("Success")
else:
    print("Error")
```

---

**keywords**: Яндекс.Ключ, Yandex.Key, Yandex OTP, YaOTP

from io import open
from os import environ

from setuptools import setup


def read(filename):
    with open(filename, encoding="utf-8") as file:
        return file.read()


def requirements():
    with open("requirements.txt", "r") as req:
        return [r for r in req.read().split("\n") if r]


setup(
    name="pyYaOTP",
    version=environ.get("TAG_VERSION").replace("v", ""),
    packages=[
        "pyYaOTP",
    ],
    url="https://github.com/WhiteApfel/pyYaOTP",
    license="Mozilla Public License 2.0",
    author="WhiteApfel",
    author_email="white@pfel.ru",
    description="Python implementation of Yandex OTP based on KeeYaOtp",
    install_requires=requirements(),
    project_urls={
        "Source code": "https://github.com/WhiteApfel/pyYaOTP",
        "Write me": "https://t.me/whiteapfel",
    },
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    keywords="yandex otp яндекс ключ yaotp",
)

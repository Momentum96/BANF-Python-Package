from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python package for BANF Co., Ltd.'

setup(
    name="banf",
    version=VERSION,
    description=DESCRIPTION,
    author="BANF Co., Ltd.",
    author_email="gwjeon@banf.co.kr",
    packages=find_packages(),
    install_requires=[],
    keywords='conversion',
    classifiers= [
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
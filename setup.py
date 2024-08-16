from setuptools import setup, find_packages
import codecs
import os

VERSION = '5.0.0'
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    LONG_DESCRIPTION = "\n" + fh.read()


# Setting up
setup(
    name="YnExchangePY",
    version=VERSION,
    author="Yasha Najafi(YN)",
    author_email="<najafiyasha@gmail.com>",
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'bs4','selenium','chromedriver'],
    keywords=['python', 'crypto', 'prices', 'crypto calculations', 'api', 'calculations'],
)

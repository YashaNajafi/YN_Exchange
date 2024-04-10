from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'See crypto prices and calculations crypto datas'
LONG_DESCRIPTION = 'View crypto prices and calculations crypto values to USD and IRT'

# Setting up
setup(
    name="YN_Exchange",
    version=VERSION,
    author="Yasha Najafi(YN)",
    author_email="<najafiyasha@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests', 'bs4'],
    keywords=['python', 'crypto', 'prices', 'crypto calculations', 'api', 'calculations'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

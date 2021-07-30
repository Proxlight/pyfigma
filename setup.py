from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.2'
DESCRIPTION = 'Automate GUI creation'
LONG_DESCRIPTION = 'A package that allows to scrape data from figma'

# Setting up
setup(
    name="pyfigma",
    version=VERSION,
    author="Proxlight (Pratyush Mishra)",
    author_email="<proxlight02@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests', 'Eel'],
    keywords=['python', 'GUI', 'Figma', 'Scraping', 'API', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

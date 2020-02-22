from setuptools import find_packages
from setuptools import setup
from bcoscli import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bcoscli",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    author="duanyongqiang",
    author_email="sysuduanyongqiang@163.com",
    description="A userful package to use 'FISCO-BCOS', the FISCO-BCOS sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yyonging/bcoscli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "cod>=0.0.3"
    ],
    entry_points={"console_scripts": ["bcoscli = bcoscli:init"]}
)

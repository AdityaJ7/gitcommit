# gitcommit_enhanced/setup.py
from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="gitcommit_enhanced",
    url="https://github.com/AdityaJ7/gitcommit_enhanced",
    description="Gitcommit enhanced is a tool for writing conventional commits in an easy way.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.1",
    author="Aditya Jetely",
    author_email="ajetely@gmail.com",
    license="public",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "gitcommit = gitcommit_enhanced.gitcommit:main",
        ],
    },
)

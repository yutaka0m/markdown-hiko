from setuptools import find_packages, setup

LONG_DESCRIPTION = """
[Mardown Hiko] is a cli that uploads Markdown images to AWS S3.
""".strip()

SHORT_DESCRIPTION = """
[Mardown Hiko] is a cli that uploads Markdown images to AWS S3.
""".strip()

VERSION = "0.2.2"

URL = "https://github.com/yutaka0m/markdown-hiko"

with open("requirements.txt") as f:
    REQUIRED = f.read().splitlines()

setup(
    name="markdown-hiko",
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    author="@yutaka0m",
    author_email="",
    license="MIT",
    packages=find_packages(),
    entry_points={"console_scripts": "markdown-hiko = src.cli:main"},
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
)

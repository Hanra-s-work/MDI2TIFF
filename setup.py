"""
File containing the required information to successfully build a python package
"""

import setuptools

with open("README.md", "r", encoding="utf-8", newline="\n") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mdi2img',
    version='1.0.0',
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    author="Henry Letellier",
    author_email="henrysoftwarehouse@protonmail.com",
    description="A module that allows you to convert mdi files to tiff and other formats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hanra-s-work/MDI2IMG",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
)

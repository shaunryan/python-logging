import pathlib
from setuptools import setup
import os


# The directory containing this file
HERE = pathlib.Path(__file__).parent


# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="[loggingdemo]",
    version_config={
        "template": "{tag}",
        "dev_template": "{tag}.dev{ccount}",
        "dirty_template": "{tag}.dev{ccount}.dirty",
        "starting_version": "0.0.1",
        "version_callback": None,
        "version_file": None,
        "count_commits_from_version_file": False
    },
    setup_requires=['setuptools-git-versioning'],
    description="Logging pattern examples",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/shaunryan/python-logging",
    author="Shaun Ryan",
    author_email="shaun_chiburi@hotmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["loggingdemo"],
    install_requires=[
          'PyYAML'
      ],
    zip_safe=False
)
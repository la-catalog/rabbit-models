from pathlib import Path

from setuptools import find_packages, setup

long_description = Path("README.md").read_text()

setup(
    name="rabbit-models",
    version="0.0.1",
    description="Contains all models for queue messages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiagola92/rabbit-models",
    author="thiagola92",
    author_email="thiagola92@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords="rabbitmq, models",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    install_requires=["pydantic>=1.9.1"],
    python_requires=">=3.10",
)

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="spot-on_schema",
    url="https://github.com/GustafBengtsson/spot-on_schema",
    version="0.0.1",
    description="Shared SQLAlchemy schema models for spot-on projects",
    author="Gustaf B",
    author_email="gustaf.bengtsson@rise.se",
    packages=find_packages(),
    install_requires=[
        "SQLAlchemy>=1.4"
    ],
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
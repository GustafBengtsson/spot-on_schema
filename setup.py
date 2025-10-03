from setuptools import setup, find_packages

setup(
    name="spot_on_schema",
    version="1.0.0",
    description="Shared SQLAlchemy schema models for spot-on projects",
    author="Gustaf B",
    packages=find_packages(),
    install_requires=[
        "SQLAlchemy>=1.4"
    ],
    python_requires=">=3.8",
)
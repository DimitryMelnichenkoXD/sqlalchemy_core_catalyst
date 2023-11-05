import os

from setuptools import setup, find_packages

PWD = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
with open(os.path.join(PWD, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name='sqlalchemy_core_catalyst',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'greenlet==3.0.1',
        'pydantic==1.10.2',
        'SQLAlchemy==1.4.25',
        'typing_extensions==4.8.0',
    ],
    description='Library for easy interaction with SQLAlchemy and Pydantic.',
    long_description=long_description,
    long_description_content_type="text/markdown",
)

from setuptools import setup, find_packages

setup(
    name='sqlalchemy_core_catalyst',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'greenlet==3.0.1',
        'pydantic==1.10.2',
        'SQLAlchemy==1.4.25',
        'typing_extensions==4.8.0',
    ],
)

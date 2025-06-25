# setup.py

from setuptools import setup, find_packages

setup(
    name="python_calculator",  # This is the name of the package
    version="6.0",
    packages=find_packages(),
    install_requires=[],  # Any dependencies you want to include
    test_suite='tests',
    tests_require=[
        'pytest',  # Specify pytest for testing
    ],
    author="Fake Author",
    author_email="your.email@example.com",
    description="A simple calculator package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

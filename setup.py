from setuptools import setup, find_packages

with open("README.md","r") as f:
    description = f.read()

setup(
    name='topsis-3529',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.25.1',
        'pandas>=2.0.3'
    ],

    lond_description = description,
    long_description_content_type= "text/markdown",
)
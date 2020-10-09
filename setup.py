import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iwgproton",
    version="0.0.1",
    author="rodneymandap",
    author_email="rodneyjan.mandap@gmail.com",
    description="Python package to connect to IWG Proton API",
    long_description=long_description,
    url="https://github.com/rodneymandap/iwg-proton",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
from setuptools import setup

with open("README.md",  "r") as fh:
    long_description = fh.read()

setup(
    name = "Burclar",
    version = "0.0.1",
    author = "Special",
    author_email = "mert.special0@gmail.com",
    description = "Basit bir burc modulu.",
    long_description = long_description,
    py_modules = ["Burclar"],
    package_dir = {'' : 'src'},
    url ="https://github.com/The-Special/Burc-api",
    
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 2.7.15",
        "Programming Language :: Python :: 3.8",
        "Lisence :: OSI Approved :: MIT License",
        "Operating System :: OS Independent,"
    ],
    install_requires = [
        "requests" ,
        "beautifulsoup4",
    ]
)
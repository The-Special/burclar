import setuptools

with open("README.md",  "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "Burc-api",
    version = "0.0.1",
    author = "Special",
    author_email = "mert.special0@gmail.com",
    description = "Basit bir burç modülü.",
    long_description = long_description,
    long_description_content_type ="text/markdown",
    url = "https://github.com/The-Special/Burç-api",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
     ],
     python_requires = ['']

)
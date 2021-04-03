from setuptools import setup , find_packages

with open("README.md",  "r") as fh:
    long_description = fh.read()

setup(
    name = "Burclar",
    version = "0.0.1",
    author = "Special",
    author_email = "mert.twelvesky@gmail.com",
    description = "Basit bir burc modulu.",
    long_description = long_description,
    package_dir = {'' : 'src'},
    packages=find_packages(),
    keywords = ['burclar' , 'burcapi' , 'python' , 'BurcApi']
    url ="https://github.com/The-Special/Burc-api",
    license='MIT', 
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

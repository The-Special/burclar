from setuptools import setup , find_packages

with open("README.md",  "r") as fh:
    long_description = fh.read()

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
    name = "Burclar",
    version = "0.0.1",
    author = "Special",
    author_email = "mert.twelvesky@gmail.com",
    description = "Basit bir burc modulu.",
    long_description = long_description,
    packages=find_packages(),
    keywords = ['burclar' , 'burcapi' , 'python' , 'BurcApi'],
    url ="https://github.com/The-Special/Burc-api",
    license='MIT', 
    classifiers = classifiers,
    install_requires = [
        "requests" ,
        "beautifulsoup4",
    ]
)

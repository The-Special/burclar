from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='burclar',
  version='1.2.0',
  description='Basit bir burç modülü.',
  long_description_content_type="text/markdown",
  long_description=open('README.md').read(),
  url='https://github.com/The-Special/Burc-api', 
  author='Special',
  author_email='',
  license='MIT License', 
  classifiers=classifiers,
  keywords=['burçlar', 'python' , 'burc-api'], 
  packages=find_packages(),
  install_requires=['beautifulsoup4' , 'requests'] 
)

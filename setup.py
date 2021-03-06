import setuptools
from os import path
from foo import __version__

# Read the contents of README.md
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='samplepackage',
    version=__version__,
    description="This is a sample package",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Thanh-Truong/samplepackage',
    author='Thanh Truong',
    author_email='tcthanh@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires = ['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'samplepackage = foo.bar.main:main'
        ],
    }
)
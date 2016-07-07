from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sixelplot',
    version='0.0.3',
    description='thin-wrapper for pysixel and matplotlib.',
    long_description=long_description,
    url='https://github.com/kktk-KO/sixelplot',
    author='kktk',
    author_email='kktkko3579@gmail.com',
    license='CC0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Terminals',
    ],
    keywords='sixel terminal image',
    packages=find_packages(exclude=['tests*']),
    install_requires = [
        "pysixel",
        "matplotlib"
    ]
)

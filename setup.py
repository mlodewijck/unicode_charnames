# -*- coding: utf-8 -*-

from os import path
from setuptools import setup, find_packages

from unicode_charnames.release import __version__

here = path.abspath(path.dirname(__file__))
github = 'https://github.com/mlodewijck/unicode_charnames'

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='unicode_charnames',
    version=__version__,
    description='Look up Unicode character name or code point label and search in Unicode character names',
    long_description=long_description,
    url=github,
    author='Marc Lodewijck',
    author_email='mlodewijck@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Filters',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=['Unicode', 'character names'],
    packages=find_packages(exclude=('tools',)),
    python_requires='>=3.3',
    package_data={'unicode_charnames': ['*.txt']},
    project_urls={
        'Bug Reports': '{}/issues'.format(github),
        'Source': '{}/'.format(github),
    }
)

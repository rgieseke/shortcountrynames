"""
shortcountrynames
-----------------

Install using ::

    pip install shortcountrynames

See README.md and repository for details:
    https://github.com/rgieseke/shortcountrynames
"""

import os
from setuptools import setup

import versioneer

path = os.path.abspath(os.path.dirname(__file__))

cmdclass = versioneer.get_cmdclass()

with open(os.path.join(path, 'README.md'), "r") as f:
    readme = f.read()
    readme = readme.split("\n\n", 1)[1]

setup(
    name='shortcountrynames',
    version=versioneer.get_version(),
    description='Maps from two or three letter country codes to short names',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/rgieseke/shortcountrynames',
    author='Robert Gieseke',
    author_email='robert.gieseke@pik-potsdam.de',
    license='CC0',
    platforms='any',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=['country code'],
    cmdclass=cmdclass,
    packages=['shortcountrynames']
)

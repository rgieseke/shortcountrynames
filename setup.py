"""
shortcountrynames
-----------------

Install using ::

    pip install shortcountrynames

See README.md and repository for details:
    https://github.com/rgieseke/shortcountrynames
"""

from setuptools import setup


setup(
    name='shortcountrynames',
    version='0.1',
    description='Maps from three letter country codes to short names',
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
    packages=['shortcountrynames']
)

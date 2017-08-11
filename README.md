[![PyPI](https://img.shields.io/pypi/v/shortcountrynames.svg)](https://pypi.python.org/pypi/shortcountrynames/)
[![npm](https://img.shields.io/npm/v/shortcountrynames.svg)](https://www.npmjs.com/package/shortcountrynames)

## Data Package
Data Package with two and three-letter country codes and short
English country names based on the [country-codes](https://github.com/datasets/country-codes) Data Package with some
changes to the choice of short names.

## Python module

Install with

```
pip install shortcountrynames
```

Usage

```py
from shortcountrynames import to_name

assert to_name("DE") == "Germany"
assert to_name("DEU") == "Germany"
```

## JavaScript module

Install with

```
npm install shortcountrynames
```

Usage

```
var shortcountrynames = require("shortcountrynames")

// Define custom codes
shortcountrynames.names["TEST"] = 'test'

console.log(shortcountrynames.to_name("DEU")) // Germany
console.log(shortcountrynames.to_name("TEST")) // test
```

## Notes

Non-standard codes:
`EUU` - European Union
`XKX` - Kosovo

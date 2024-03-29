[![PyPI](https://img.shields.io/pypi/v/shortcountrynames.svg)](https://pypi.org/project/shortcountrynames/)
[![npm](https://img.shields.io/npm/v/shortcountrynames.svg)](https://www.npmjs.com/package/shortcountrynames)

“Do One Thing and Do It Well” - this package helps turning two or three letter
codes into short English names.

`shortcountrynames` is maintained by Robert Gieseke (<rob.g@web.de>).

## Data Package
[Data Package](http://frictionlessdata.io/), a simple
[CSV file](shortcountrynames.csv), with two and three-letter country
codes and short English country names based on the [country-codes](https://github.com/datasets/country-codes) Data Package with some
changes and additions to the choice of short names.

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

```js
import {names, to_name} from 'shortcountrynames'

// Define custom codes
names["TEST"] = 'test'

console.log(to_name("DEU")) // Germany
console.log(to_name("TEST")) // test
```

## Notes

Non-standard codes:

`EU`, `EUU` - European Union

`XK`, `XKX` - Kosovo

## License

CC0

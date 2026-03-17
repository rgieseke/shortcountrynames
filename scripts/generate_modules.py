# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas>=3.0.1",
# ]
# ///
from pathlib import Path

import pandas as pd

root = Path(__file__).parents[1]

df = pd.read_csv(root / "shortcountrynames.csv", keep_default_na=False)

# Python module header
py_out = '''"""
shortcountrynames
-----------------


"""

from importlib.metadata import version

__version__ = version("shortcountrynames")


names = {}

'''

# JS module header
js_out = """// Short Country Names

const names = {}
"""


for _, row in df.iterrows():
    line = f'names["{row.Code}"] = names["{row.Shortcode}"] = "{row.Name}"\n'
    py_out += line
    js_out += line

py_out += '''\n\ndef to_name(code):
    """Return short name for two or three letter code `code`.

    Non-standard codes: EU and EUU for European Union, XK and XKX for Kosovo"""
    return names[code]
'''

js_out += """\nconst to_name = function(code) {
  return names[code]
}

export {names, to_name}
"""

with open(str(root / "shortcountrynames/__init__.py"), "w") as f:
    f.write(py_out)

with open(str(root / "index.js"), "w") as f:
    f.write(js_out)

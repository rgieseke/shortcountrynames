from pathlib import Path
from pandas_datapackage_reader import read_datapackage


root = Path(__file__).parents[1]

df = read_datapackage(".")

# Python module header
py_out = '''"""
shortcountrynames
-----------------

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

"""


names = {}

'''

# JS module header
js_out = '''// Country Groups

exports.names = {}
var names = exports.names
'''


for code, row in df.iterrows():
    line = 'names["{}"] = names["{}"] = "{}"\n'.format(
        code, row.Shortcode, row.Name)
    py_out += line
    js_out += line

py_out += '''\n\ndef to_name(code):
    """Return short name for two or three letter code `code`.

    Non-standard codes: EU and EUU for European Union, XK and XKX for Kosovo"""
    return exports.names[code]
'''

js_out += '''\nexports.to_name = function(code) {
  return names[code]
}'''


with(open(str(root / "shortcountrynames/__init__.py"), "w")) as f:
    f.write(py_out)

with(open(str(root / "index.js"), "w")) as f:
    f.write(js_out)

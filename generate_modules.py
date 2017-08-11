from pandas_datapackage_reader import read_datapackage

df = read_datapackage(".")

py_out = '''"""
shortcountrynames
-----------------

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

"""


names = {}

'''

for code, row in df.iterrows():
    py_out += 'names["{}"] = names["{}"] = "{}"\n'.format(
        code, row.Shortcode, row.Name)

py_out += '''\n\ndef to_name(code):
    """Return short name for two or three letter code `code`.

    Non-standard codes: EU and EUU for European Union, XK and XKX for Kosovo"""
    return names[code]
'''

with(open("shortcountrynames/__init__.py", "w")) as f:
    f.write(py_out)

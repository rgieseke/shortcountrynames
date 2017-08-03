from pprint import pformat
from pandas_datapackage_reader import read_datapackage

df = read_datapackage(".")

py_out = '''"""
shortcountrynames
-----------------

"""


names = {
'''

py_out += " " + pformat(df["Name"].to_dict(), indent=4)[1:-1]

py_out += "\n}\n\n"
py_out += '''def to_name(code):
    """Return short name for three letter code `code`.

    Non-standard codes: EUU for European Union, XKX for Kosovo"""
    return names[code]
'''

with(open("shortcountrynames/__init__.py", "w")) as f:
    f.write(py_out)

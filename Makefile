all: shortcountrynames/__init__.py

shortcountrynames/__init__.py: shortcountrynames.csv generate_modules.py venv
	./venv/bin/python generate_modules.py

venv: requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur $<
	touch venv

clean:
	rm shortcountrynames/__init__.py

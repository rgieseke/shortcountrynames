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

publish-on-pypi:
	-rm build dist
	@status=$$(git status --porcelain); \
	if test "x$${status}" = x; then \
		python setup.py bdist_wheel --universal; \
		twine upload dist/*; \
	else \
		echo Working directory is dirty >&2; \
	fi;

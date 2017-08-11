all: shortcountrynames/__init__.py

shortcountrynames/__init__.py: shortcountrynames.csv scripts/generate_modules.py venv
	./venv/bin/python scripts/generate_modules.py

venv: requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur $<
	touch venv

clean:
	rm shortcountrynames/__init__.py

publish:
	-rm -rf build dist
	./scripts/create_tag.sh
	@status=$$(git status --porcelain); \
	if test "x$${status}" = x; then \
		python setup.py bdist_wheel --universal; \
		twine upload dist/*; \
		npm publish; \
	else \
		echo Working directory is dirty >&2; \
	fi;

PHONY: clean publish

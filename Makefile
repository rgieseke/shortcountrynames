all: shortcountrynames/__init__.py

shortcountrynames/__init__.py: shortcountrynames.csv scripts/generate_modules.py
	uv run scripts/generate_modules.py

clean:
	rm shortcountrynames/__init__.py
	rm index.js
	
update-version:
	-rm -rf build dist
	./scripts/create_tag.sh
	
PHONY: clean publish

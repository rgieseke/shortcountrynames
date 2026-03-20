all: shortcountrynames/__init__.py

shortcountrynames/__init__.py: shortcountrynames.csv scripts/generate_modules.py
	uv run scripts/generate_modules.py

sort:
	head -n 1 shortcountrynames.csv > tmp.csv
	tail -n +2 shortcountrynames.csv | sort -t, -k3,3 >> tmp.csv
	mv tmp.csv shortcountrynames.csv

clean:
	rm shortcountrynames/__init__.py
	rm index.js
	
update-version:
	-rm -rf build dist
	./scripts/create_tag.sh

PHONY: clean sort

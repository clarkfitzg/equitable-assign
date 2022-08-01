test: test.py equiassign.py
	python3 $<

upload: dist/*
	python3 -m twine upload --repository testpypi dist/*

build: src/*
	python3 -m build

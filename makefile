test: test.py equiassign.py
	python3 $<

up: dist/*
	python3 -m twine upload dist/*

test_up: dist/*
	python3 -m twine upload --repository testpypi dist/*

build: src/*
	rm dist/*
	python3 -m build

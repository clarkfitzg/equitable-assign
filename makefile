test: test.py equiassign.py
	python3 $<

build: src/*
	python3 -m build

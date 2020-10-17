hello:
	echo "hello World!"

install:
	pip install -r requirements.txt

remove:
	pip uninstall -r requirements.txt

test:
	python -m pytest -vv test_hello.py

help:
	echo "usage: make {hello|test|install|remove}"

all: hello install
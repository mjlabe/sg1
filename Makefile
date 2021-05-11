.PHONY: start
start:
	python3 sg1.manage.py start test

.PHONY: render
render:
	python3 ./sg1/manage.py render

PHONY: urls
urls:
	python3 sg1/manage.py urls

.PHONY: dist
dist:
	python3 setup.py bdist_wheel
	pip install ./dist/sg1-0.1-py3-none-any.whl --force-reinstall

.PHONY: build
build:
	python3 -m build

.PHONY: install
install:
	python3 setup.py bdist_wheel
	python3 setup.py sdist
	pip install ./dist/sg1-0.1.1-py3-none-any.whl --force-reinstall

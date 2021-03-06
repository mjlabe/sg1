.PHONY: render
render:
	sg1 render example

PHONY: urls
urls:
	sg1 urls example

.PHONY: dist
dist:
	python3 setup.py bdist_wheel
	python3 setup.py sdist

.PHONY: install
install:
	pip install ./dist/sg1-0.1.4-py3-none-any.whl --force-reinstall

.PHONY: update
update:
	python3 setup.py bdist_wheel
	python3 setup.py sdist
	pip install ./dist/sg1-0.1.4-py3-none-any.whl --force-reinstall

.PHOMY: upload
upload:
	twine upload dist/*

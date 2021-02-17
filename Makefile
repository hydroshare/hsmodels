.DEFAULT_GOAL := all
isort = isort hsmodels tests
black = black -S -l 120 --target-version py38 hsmodels tests

.PHONY: format
format:
	$(isort)
	$(black)

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: docs
docs:
	flake8 --max-line-length=80 docs/examples/
	python docs/build/main.py
	mkdocs build

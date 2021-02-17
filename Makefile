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
	python docs/generate_model_markdown.py
	mkdocs build

.PHONY: docs-serve
docs-serve:
	python docs/generate_model_markdown.py
	mkdocs serve

.PHONY: publish-docs
publish-docs:
	zip -r site.zip site

.PHONY: test
test:
	pytest tests

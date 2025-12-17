SHELL := /bin/bash

.PHONY: test tests lint-all

lint-all:
	pre-commit run --all-files

test:
	pytest ./tests

tests:
	pytest -q ./tests

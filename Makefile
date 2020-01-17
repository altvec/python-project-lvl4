lint:
	@poetry run flake8

requirements.txt: poetry.lock
	@poetry export --format requirements.txt --output requirements.txt

.PHONY: lint

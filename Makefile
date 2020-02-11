install: .env
	@poetry install

.env:
	@test ! -f .env && cp .env.example .env

start:
	@poetry run python manage.py runserver --noreload

shell:
	@poetry run python manage.py shell

migrations:
	@poetry run python manage.py makemigrations
	@poetry run python manage.py migrate

lint:
	@poetry run flake8

test:
	@poetry run python manage.py test

requirements.txt: poetry.lock
	@poetry export --format requirements.txt --output requirements.txt

.PHONY: install start lint shell migrations test

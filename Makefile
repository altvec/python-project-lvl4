install: .env
	@poetry install

.env:
	@test ! -f .env && cp .env.example .env

shell:
	@poetry run python manage.py shell

migrate:
	@poetry run python manage.py migrate

setup: migrate seed_statuses
	@echo Create a super user
	@poetry run python manage.py createsuperuser

start: migrate
	@poetry run python manage.py runserver 0.0.0.0:8000

lint:
	@poetry run flake8

seed_statuses:
	@echo Create initial task statuses
	@poetry run python manage.py loaddata ./fixtures/task_statuses.json

test:
	@poetry run coverage run --omit '.venv/*' --source '.' manage.py test

test-coverage-report: test
	@poetry run coverage report

test-coverage-report-xml:
	@poetry run coverage xml

requirements.txt: poetry.lock
	@poetry export --format requirements.txt --output requirements.txt

secretkey:
	@poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(64))'

.PHONY: install shell setup start lint seed_statuses test secretkey

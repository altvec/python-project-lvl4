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

seed_statuses:
	@poetry run python manage.py loaddata ./tasks/fixtures/task_statuses.json

test:
	@coverage run --omit '.venv/*' --source '.' manage.py test -v 2
	@coverage report
	@coverage xml

requirements.txt: poetry.lock
	@poetry export --format requirements.txt --output requirements.txt

.PHONY: install start lint seed_statuses shell migrations test

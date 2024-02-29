

.PHONY: install
install:
	poetry install

.PHONY: runserver
runserver:
	poetry run python3 -m core.manage runserver

.PHONY: migrations
migrations:
	poetry run python3 -m core.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python3 -m core.manage migrate

.PHONY: superuser
superuser:
	poetry run python3 -m core.manage createsuperuser

.PHONY: update
update: install migrate;
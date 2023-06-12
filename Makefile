.PHONY: setup
setup:
	poetry install

.PHONY: lint
lint:
	poetry run black .
	poetry run isort .
	poetry run ruff --fix .

.PHONY: test
test:
	poetry run python -m unittest

.PHONY: run
run:
	poetry run python -m project_planner project.yaml
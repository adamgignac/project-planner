.PHONY: setup
setup:
	poetry install

.PHONY: lint
lint:
	poetry run black project_planner/
	poetry run isort project_planner/
	poetry run ruff --fix project_planner/

.PHONY: test
test:
	poetry run python -m unittest

.PHONY: run
run:
	poetry run python -m project_planner project.yaml
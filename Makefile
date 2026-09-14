ROOT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
APP_DIR := $(ROOT)balance-system
UV := uv
DC := docker compose
WEB := $(DC) exec -T web
MANAGE := cd $(APP_DIR) && $(UV) run --project $(ROOT) python manage.py
CELERY_APP := config

.DEFAULT_GOAL := help

.PHONY: help
help: ## Show available targets
	@grep -E '^[a-zA-Z0-9_-]+:.*##' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*##"}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

.PHONY: sync
sync: ## Install project dependencies
	cd $(ROOT) && $(UV) sync

.PHONY: sync-dev
sync-dev: ## Install dependencies including dev group
	cd $(ROOT) && $(UV) sync --group dev

.PHONY: lint
lint: ## Run ruff linter
	$(UV) run ruff check $(APP_DIR)

.PHONY: format
format: ## Run ruff formatter
	$(UV) run ruff format $(APP_DIR)

.PHONY: lint-fix
lint-fix: ## Run ruff linter with autofix
	$(UV) run ruff check --fix $(APP_DIR)

.PHONY: pre-commit
pre-commit: ## Run pre-commit on all files
	$(UV) run pre-commit run --all-files

.PHONY: check
check: ## Run Django system checks
	$(MANAGE) check

.PHONY: test
test: ## Run Django tests
	$(MANAGE) test

.PHONY: main
main: ## Run manage.py with ARGS, e.g. make main ARGS="showmigrations"
	$(MANAGE) $(ARGS)

.PHONY: migrate
migrate: ## Apply database migrations
	$(MANAGE) migrate

.PHONY: makemigrations
makemigrations: ## Create new migrations
	$(MANAGE) makemigrations

.PHONY: make_migrate
make_migrate: makemigrations ## Alias for makemigrations

.PHONY: shell
shell: ## Open django-extensions shell_plus
	$(MANAGE) shell_plus --print-sql

.PHONY: admin
admin: ## Create Django superuser
	$(MANAGE) createsuperuser

.PHONY: celery
celery: ## Run Celery worker locally
	cd $(APP_DIR) && $(UV) run --project $(ROOT) celery -A $(CELERY_APP) worker -l INFO

.PHONY: up
up: ## Build and start Docker stack with seed data
	$(DC) up --build -d
	$(WEB) uv run --project /app python manage.py create_bank_in_system
	$(WEB) uv run --project /app python manage.py create_super_user

.PHONY: start
start: ## Start Docker stack
	$(DC) up -d

.PHONY: down
down: ## Stop and remove Docker stack
	$(DC) down

.PHONY: stop
stop: ## Stop Docker services
	$(DC) stop

.PHONY: logs
logs: ## Follow Docker logs
	$(DC) logs -f

.PHONY: ps
ps: ## Show Docker service status
	$(DC) ps

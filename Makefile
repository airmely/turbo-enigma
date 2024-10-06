# Makefile

PROJECT_NAME=balance_system
BASE_COMMAND=python3 manage.py

main:
	$(BASE_COMMAND) $(ARGS)

migrate:
	$(BASE_COMMAND) migrate

make_migrate:
	$(BASE_COMMAND) makemigrations

celery:
	celery -A $(PROJECT_NAME) worker -l INFO

stop:
	docker stop $$(docker ps -q) || true

start:
	docker-compose up -d

shell:
	$(BASE_COMMAND) shell_plus --print-sql

admin:
	$(BASE_COMMAND) createsuperuser

.PHONY: main start stop celery shell admin migrate make_migrate

FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry

RUN poetry install --no-root

COPY . .

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings

#RUN poetry run python manage.py migrate \
#    && poetry run python manage.py create_bank_in_system \
#    && poetry run python manage.py create_super_user

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
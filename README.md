---

# Banking System

## Tech Stack

- **Python 3.12+**
- **Django**
- **django-modern-rest (DMR)**
- **PostgreSQL**
- **Redis**
- **Celery**
- **uv** — dependency management
- **ruff** — linting and formatting

## Getting Started

### First Steps

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:airmely/turbo-enigma.git
   cd turbo-enigma
   ```

2. **Set Up Configuration (optional):**
   ```bash
   cp balance-system/default_config.toml balance-system/config.toml
   ```
   The app loads `default_config.toml` and merges `config.toml` on top (local file, gitignored). For local dev (debug toolbar, django-extensions) copy `config/settings/local_settings.example.py` to `local_settings.py`.

3. **Start the Application with Docker:**
   ```bash
   make up
   ```
   If you don't have `make`, use:
   ```bash
   docker compose up --build -d
   docker compose exec -T web uv run --project /app python manage.py create_bank_in_system
   docker compose exec -T web uv run --project /app python manage.py create_super_user
   ```

4. **For subsequent launches:**
   ```bash
   make start
   ```
   Or:
   ```bash
   docker compose up -d
   ```

5. **Stop containers:**
   ```bash
   make stop
   ```
   Or:
   ```bash
   docker compose stop
   ```

6. **Remove containers:**
   ```bash
   make down
   docker compose down --volumes
   ```

### Local Development (without Docker)

1. Install [uv](https://docs.astral.sh/uv/).
2. Copy config and local settings:
   ```bash
   cp balance-system/default_config.toml balance-system/config.toml
   cp balance-system/config/settings/local_settings.example.py balance-system/config/settings/local_settings.py
   ```
   Set `host = "localhost"` and redis URLs to `localhost` in `config.toml`.
3. Install dependencies:
   ```bash
   make sync-dev
   ```
4. Run migrations:
   ```bash
   make migrate
   ```
5. Start the dev server:
   ```bash
   make main ARGS="runserver"
   ```
6. Start Celery worker (separate terminal):
   ```bash
   make celery
   ```

### Makefile Commands

Run `make help` for the full list. Common targets:

| Command | Description |
|---|---|
| `make sync-dev` | Install dependencies (including dev group) |
| `make migrate` | Apply database migrations |
| `make makemigrations` | Create new migrations |
| `make lint` | Run ruff linter |
| `make format` | Run ruff formatter |
| `make check` | Run Django system checks |
| `make test` | Run Django tests |
| `make up` | Build and start Docker stack with seed data |
| `make logs` | Follow Docker logs |

### Accessing the Application

- **Swagger API Documentation:**
    - [http://localhost:8000/api/swagger/](http://localhost:8000/api/swagger/)

- **Django Admin Panel:**
    - [http://localhost:8000/admin/](http://localhost:8000/admin/)

### Admin Credentials

- **Username:** admin
- **Password:** 1234

---

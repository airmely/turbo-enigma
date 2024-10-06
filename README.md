
---

# Banking System

## Tech Stack
- **Python**
- **Django**
- **Django REST Framework (DRF)**
- **PostgreSQL**
- **Redis**
- **Celery**

## Getting Started

### First Steps

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:airmely/turbo-enigma.git
   ```

2. **Set Up Environment Variables:**
   ```bash
   cat env.example > .env
   ```

3. **Start the Application with Docker:**
   ```bash
   make up
   ```
   - If you don't have make, you can simply use these commands:
   ```bash
    docker-compose up --build -d
    docker exec balance_system-web-1 poetry run python manage.py create_bank_in_system
    docker exec balance_system-web-1 poetry run python manage.py create_super_user
   ```
   
4. **For subsequent launches, start with this command:**
    ```bash
    make start
    ```
   - Or:
   ```bash
   docker-compose up -d
   ```
5. **Stop containers:**
    ```bash
    make stop
    ```
   - Or:
   ```bash
   docker stop $$(docker ps -q) || true
   ```
6. **Remove containers:**
    ```bash
    docker-compose down
    docker-compose down --volumes
    docker container prune
   ```
### Accessing the Application

- **Swagger API Documentation:**
  - [http://localhost:8000/api/swagger/](http://localhost:8000/api/swagger/)

- **Django Admin Panel:**
  - [http://localhost:8000/admin/](http://localhost:8000/admin/)

### Admin Credentials

- **Username:** admin
- **Password:** 1234

---

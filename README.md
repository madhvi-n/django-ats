# Django ATS

A simple **Applicant Tracking System (ATS)*** for recruiters to manage candidate records, including **CRUD operations and search functionality.**

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.1-brightgreen?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django Rest Framework](https://img.shields.io/badge/Django_Rest_Framework-3.15-red)](https://www.django-rest-framework.org/)

## 🚀 Features

- **Candidate Management:** Create, Update, Delete candidates.
- **Search API:** Search candidates by name with relevance ranking.

## 🏗 Tech Stack

- Backend: Python 3.11, Django 5.1, Django REST Framework
- Database: SQLite (default) / PostgreSQL (optional)

## ⚙️ Installation & Setup

1. Clone the Repository

    ```bash
    git clone https://github.com/madhvi-n/django-ats.git
    cd django-ats
    ```

2. Set up a virtual environment

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3. Install Dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Apply Database Migrations

    ```bash
    python manage.py migrate
    ```

5. Create a Superuser

    ```bash
    python manage.py createsuperuser
    ```

6. Run the Development Server

    ```bash
    python manage.py runserver
    ```

    Access the application at: <http://127.0.0.1:8000>

## 📝 API Documentation

The API documentation is available via **Swagger**:

- **Swagger UI:** `http://127.0.0.1:8000/api/swagger/`
- **Redoc:** `http://127.0.0.1:8000/api/redoc/`

### API endpoints

- GET `api/v1/candidates` : Lists all candidates
- POST `api/v1/candidates` : Creates new candidate
- PUT `api/v1/candidates/{id}` : Updates candidate
- DELETE `api/v1/candidates/{id}`: Deletes candidates
- GET `api/v1/candidates/search?q={name}` : Searchs candidates with the given query

## ⚙️ Environment Variables *(Example .env file)*

```ini
SECRET_KEY=django-secret-key
DEBUG=True
```

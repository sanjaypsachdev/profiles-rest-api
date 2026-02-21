# Profiles REST API

A Django REST API project for managing user profiles. Built with Django 6 and Django REST Framework.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Setup

### Using uv (recommended)

```bash
# Clone the repository (if applicable)
# cd into the project directory

# Create virtual environment and install dependencies
uv sync

# Set the secret key (required). Copy .env.example to .env and set DJANGO_SECRET_KEY.
# Generate a key: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
cp .env.example .env
# Edit .env and set DJANGO_SECRET_KEY=your-generated-key
```

### Using pip

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -e .
```

## Running the project

```bash
# Run migrations (first time or after model changes)
uv run python manage.py migrate

# Start the development server
uv run python manage.py runserver
```

The API will be available at **http://127.0.0.1:8000/**.

## Project structure

```
├── manage.py              # Django CLI entry point
├── pyproject.toml         # Project metadata and dependencies
├── profiles_project/      # Main Django project
│   ├── settings.py        # Project settings
│   ├── urls.py            # Root URL configuration
│   ├── wsgi.py
│   └── asgi.py
└── profiles_api/          # Profiles API app
    ├── models.py
    ├── views.py
    ├── admin.py
    └── tests.py
```

## Tech stack

- **Django** 6.x – Web framework
- **Django REST Framework** – REST API toolkit
- **SQLite** – Default database (development)

## Troubleshooting

**`VIRTUAL_ENV` does not match the project environment:** You're in this project but another virtualenv is activated (e.g. a parent folder's `.venv`). Either:

- **Use this project's venv:** `source .venv/bin/activate` (then `VIRTUAL_ENV` will match and the warning goes away).
- **Or run without activating:** use `uv run …` as in the commands below; uv will use this project's `.venv` and you can `unset VIRTUAL_ENV` to silence the warning.

In Cursor/VS Code, ensure the interpreter is set to this workspace's `.venv` (e.g. **Python: Select Interpreter** → choose the one under this project).

## Useful commands

| Command | Description |
|---------|-------------|
| `uv run python manage.py runserver` | Start the dev server |
| `uv run python manage.py migrate` | Apply database migrations |
| `uv run python manage.py makemigrations profiles_api` | Create migrations from model changes (run from project root; only field/model changes are detected) |
| `uv run python manage.py createsuperuser` | Create an admin user |
| `uv run python manage.py shell` | Open Django shell |

## License

See project configuration for license details.

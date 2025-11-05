# fastapi-rest

A minimal, clean FastAPI REST API project scaffold in Python. It’s organized into clear layers (routes, schemas, models, services) with simple dependency injection and an optional Docker setup for local development.

- Language: Python (100%)
- Framework: FastAPI
- ASGI server: Uvicorn (dev)

## Features

- FastAPI app with automatic interactive docs (Swagger UI and ReDoc)
- Clear, modular structure:
  - `routes/` for API endpoints
  - `service/` for business logic (service layer)
  - `schemas/` for request/response validation
  - `models/` for persistence layer entities
  - `dependencies.py` for reusable DI helpers (e.g., database session)
  - `database.py` for database wiring
- Ready-to-run locally or with Docker Compose

## Project Structure

```
.
├── app/
│   ├── app.py              # Creates the FastAPI app and includes routers
│   ├── database.py         # Database configuration and session/engine setup
│   ├── dependencies.py     # Reusable dependencies (e.g., get_db)
│   ├── models/             # ORM models (e.g., SQLAlchemy models)
│   ├── routes/             # API routers/endpoints
│   ├── schemas/            # Pydantic schemas for request/response models
│   └── service/            # Service layer (business/domain logic)
├── main.py                 # Application entrypoint (uvicorn target)
├── docker-compose.yml      # Containerized local development
├── requirements.txt        # Python dependencies
└── .gitignore              # Git ignore rules
```

## Getting Started

### Prerequisites

- Python 3.10+ (recommended)
- pip (or uv, pipenv, poetry) for dependency management
- Optional: Docker and Docker Compose v2

### Install and run (local)

1. Create and activate a virtual environment:
   - macOS/Linux:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Start the server:
   ```
   uvicorn main:app --reload
   ```
   - API Docs (Swagger UI): http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### Run with Docker

Build and start:
```
docker compose up --build
```

Then open:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development Workflow

- Add an endpoint:
  1. Create a router under `app/routes/` (e.g., `items.py`).
  2. Add or update schemas in `app/schemas/`.
  3. Implement domain logic in `app/service/` (e.g., `item_service.py`).
  4. Add models in `app/models/` if persistence is needed.
  5. Include the router in `app/app.py`.

## Configuration

- Environment variables: If your app uses a database, define a connection string (e.g., `DATABASE_URL`) and read it in `app/database.py`.
- Secrets: Prefer `.env` files (with a library like `python-dotenv`) or environment variables. Never commit secrets to VCS.

## Testing

- Recommended setup: `pytest` for tests under a `tests/` folder, plus `httpx`/`pytest-asyncio` for async endpoints.
- Dependency overrides: Use FastAPI’s `app.dependency_overrides` in tests to stub database or external services.

## License

This repository currently does not include a license file. Consider adding one (MIT, Apache 2.0, etc.) to clarify usage.

## Further Reading

- FastAPI: https://fastapi.tiangolo.com/
- Pydantic: https://docs.pydantic.dev/
- Uvicorn: https://www.uvicorn.org/

---
If you want, I can also wire up a sample domain (e.g., a simple “CRM” entity) under `routes/`, `schemas/`, `models/`, and `service/` to demonstrate the full flow.

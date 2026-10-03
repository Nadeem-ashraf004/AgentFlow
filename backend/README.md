# AgentFlow Backend

The backend for AgentFlow, an agentic research platform designed to use LangGraph and specialized AI agents to conduct research and generate evidence-grounded reports.

## Technology Stack

* Python 3.10
* FastAPI
* Pydantic
* Pydantic Settings
* Pytest
* HTTPX

Planned technologies include PostgreSQL, Qdrant, Gemini, LangGraph, LangChain, and LangSmith.

## Architecture

The backend follows a layered architecture:

```text
HTTP Request
     |
     v
FastAPI Routes
     |
     v
Services
     |
     v
Business Logic
     |
     v
Response Schemas
```

### Main Components

* `app/api/routes/`: HTTP endpoints.
* `app/api/dependencies.py`: FastAPI dependencies.
* `app/core/`: Configuration, logging, and application exceptions.
* `app/schemas/`: Request and response validation.
* `app/services/`: Application service layer.
* `tests/`: Automated backend tests.

## Current Implementation

### Implemented

* FastAPI application setup.
* Environment-based application configuration.
* Centralized logging configuration.
* Application exception classes.
* Health endpoint connected to the service layer.
* Pydantic request and response schemas.
* Initial route groups for authentication, documents, research, conversations, and reports.

### Architectural Placeholders

Authentication, document management, research execution, conversation persistence, and report retrieval are not implemented yet. Their current API routes return HTTP 501.

These features will be implemented in their designated development phases.

## Environment Setup

Activate the virtual environment from Git Bash:

```bash
source .venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Backend

From the `backend` directory:

```bash
uvicorn app.main:app --reload
```

API base URL:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Health endpoint:

```text
http://127.0.0.1:8000/api/health
```

## Run Tests

```bash
pytest
```

## Development Roadmap

1. Project setup.
2. FastAPI backend architecture.
3. Authentication and authorization.
4. Database architecture.
5. Document management.
6. RAG and document intelligence.
7. LangGraph foundations.
8. Tools and agent orchestration.
9. Research planning and multi-agent workflows.
10. Evaluation, reliability, and observability.

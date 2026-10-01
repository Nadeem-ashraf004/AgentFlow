# AgentFlow Backend

This directory contains the backend API for the AgentFlow Agentic Research Platform.

## Technology

- Python
- FastAPI
- Pydantic
- PostgreSQL — planned
- Qdrant — planned
- Gemini — planned
- LangGraph — planned

## Backend Responsibilities

The backend will eventually handle:

- User authentication and authorization
- Document upload and processing
- Document retrieval
- Research tasks
- LangGraph agent orchestration
- Tool calling
- Multi-agent workflows
- Research reports
- Memory and checkpointing
- Evaluation
- API communication with the frontend

## Current Phase

### Phase 1 — Project Setup

Current Phase 1 components:

- FastAPI application
- Environment configuration
- Centralized logging
- Application exceptions
- Health endpoint
- Pydantic response schema
- Basic API dependency system
- Initial automated test setup

## Running the Backend

Activate the virtual environment:

```bash
source .venv/Scripts/activate
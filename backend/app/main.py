from fastapi import FastAPI

from app.api.routes.auth import router as auth_router
from app.api.routes.conversations import router as conversations_router
from app.api.routes.documents import router as documents_router
from app.api.routes.health import router as health_router
from app.api.routes.reports import router as reports_router
from app.api.routes.research import router as research_router
from app.core.config import settings

app = FastAPI(
title=settings.APP_NAME,
version=settings.APP_VERSION,
description=(
"Agentic research platform powered by LangGraph. "
"Some endpoints are architectural placeholders."
),
)

app.include_router(
health_router,
prefix=settings.API_PREFIX,
)

app.include_router(
auth_router,
prefix=settings.API_PREFIX,
)

app.include_router(
documents_router,
prefix=settings.API_PREFIX,
)

app.include_router(
research_router,
prefix=settings.API_PREFIX,
)

app.include_router(
conversations_router,
prefix=settings.API_PREFIX,
)

app.include_router(
reports_router,
prefix=settings.API_PREFIX,
)

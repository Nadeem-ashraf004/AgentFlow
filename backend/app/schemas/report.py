from datetime import datetime

from pydantic import BaseModel, Field


class Citation(BaseModel):
    title: str
    url: str | None = None
    document_id: str | None = None


class ReportResponse(BaseModel):
    id: str
    research_task_id: str
    title: str
    content: str
    citations: list[Citation] = Field(default_factory=list)
    version: int = 1
    created_at: datetime
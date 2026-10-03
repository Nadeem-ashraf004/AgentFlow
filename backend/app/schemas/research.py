from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field


ResearchStatus = Literal[
    "pending",
    "planning",
    "researching",
    "analysing",
    "writing",
    "reveiwing",
    "waiting_for_humman",
    "completed",
    "failed",
]

class ResearchRequest(BaseModel):
    query: str = Field(..., min_length=3, max_length=10000)
    document_id: list[str] = Field(default_factory=list)
    conversation_id: str | None = Field(default=None)

class ResearchResponse(BaseModel):
    id : str
    query : str
    status : ResearchStatus
    created_ad : datetime    

class ResearchResultResponse(BaseModel):
    task_id: str
    status: ResearchStatus
    message: str    

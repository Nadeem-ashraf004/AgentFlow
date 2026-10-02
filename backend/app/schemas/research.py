from datetime import datetime
from typing import literal 
from pydantic import BaseModel, field 


ResearchStatus = literal[
    "pending",
    "palanning",
    "researching",
    "analysing",
    "writing",
    "reveiwing",
    "waiting_for_humman",
    "completed",
    "failed",
]

class ResearchRequest(BaseModel):
    query: str = field(..., min_length=3, max_length=10000)
    document_id: list[str] = field(default_factory=list)
    conversation_id: str | None = None

class ResearchResponse(BaseModel):
    id : str
    query : str
    status : ResearchStatus
    created_ad : datetime    

class ResearchResultResponse(BaseModel):
    task_id: str
    status: ResearchStatus
    message: str    

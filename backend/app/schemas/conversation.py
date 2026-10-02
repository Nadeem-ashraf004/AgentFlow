from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


MessageRole = Literal["user", "assistant"]


class ConversationCreateRequest(BaseModel):
    title: str | None = Field(default=None, max_length=200)


class ConversationResponse(BaseModel):
    id: str
    title: str
    created_at: datetime
    updated_at: datetime


class MessageCreateRequest(BaseModel):
    content: str = Field(min_length=1, max_length=20000)


class MessageResponse(BaseModel):
    id: str
    role: MessageRole
    content: str
    created_at: datetime
from fastapi import APIRouter, HTTPException, status

from app.schemas.conversation import (
    ConversationCreateRequest,
    ConversationResponse,
    MessageCreateRequest,
    MessageResponse,
)

router = APIRouter(prefix="/conversations", tags=["Conversations"])


@router.post("", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def create_conversation(
    request: ConversationCreateRequest,
) -> ConversationResponse:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Conversation management will be implemented in a later phase.",
    )


@router.post(
    "/{conversation_id}/messages",
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
)
def create_message(
    conversation_id: str,
    request: MessageCreateRequest,
) -> MessageResponse:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Message management will be implemented in a later phase.",
    )
from fastapi import APIRouter, HTTPException, status

from app.schemas.document import DocumentResponse

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.get("/{document_id}", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def get_document(document_id: str) -> DocumentResponse:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Document management will be implemented in Phase 5.",
    )
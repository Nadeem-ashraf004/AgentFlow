from fastapi import APIRouter, HTTPException, status

from app.schemas.research import ResearchRequest, ResearchTaskResponse

router = APIRouter(prefix="/research", tags=["Research"])


@router.post(
    "",
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
)
def create_research_task(request: ResearchRequest) -> ResearchTaskResponse:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Research workflows will be implemented in later phases.",
    )


@router.get(
    "/{task_id}",
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
)
def get_research_task(task_id: str) -> ResearchTaskResponse:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Research task retrieval will be implemented in later phases.",
    )
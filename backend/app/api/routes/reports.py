from fastapi import APIRouter, HTTPException, status

from app.schemas.report import ReportResponse

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get(
    "/{report_id}",
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
)
def get_report(report_id: str) -> ReportResponse:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Report management will be implemented in a later phase.",
    )
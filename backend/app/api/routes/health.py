from datetime import datetime, timezone

from fastapi import APIRouter, Depends

from app.api.dependencies import get_app_settings
from app.core.config import Settings
from app.schemas.common import HealthResponse


router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("", response_model=HealthResponse)
def health_check(
    settings: Settings = Depends(get_app_settings),
) -> HealthResponse:
    return HealthResponse(
        status="ok",
        app_name=settings.APP_NAME,
        version=settings.APP_VERSION,
        timestamp=datetime.now(timezone.utc),
    )
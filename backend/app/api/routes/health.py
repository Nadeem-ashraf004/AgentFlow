from datetime import datetime, timezone

from fastapi import APIRouter, Depends

from app.api.dependencies import get_app_settings
from app.core.config import Settings
from app.schemas.common import HealthResponse
from app.services.health_service import get_health_info

router = APIRouter(
prefix="/health",
tags=["Health"],
)

@router.get("", response_model=HealthResponse)
def health_check(
settings: Settings = Depends(get_app_settings),
) -> HealthResponse:
    health_info = get_health_info(settings)


    return HealthResponse(
    **health_info,
    timestamp=datetime.now(timezone.utc),
)

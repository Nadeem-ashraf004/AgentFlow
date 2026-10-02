from app.core.config import Settings


def get_health_info(settings: Settings) -> dict:
    return {
        "status": "ok",
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }
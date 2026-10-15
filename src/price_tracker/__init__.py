import uvicorn

from price_tracker.config import get_settings


def main() -> None:
    settings = get_settings()
    uvicorn.run(
        "price_tracker.app:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )

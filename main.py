from dotenv import load_dotenv
from src.app import create_app

load_dotenv()
app, settings = create_app()

if __name__ == "__main__":
    import uvicorn  # noqa

    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        workers=2,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL,
    )

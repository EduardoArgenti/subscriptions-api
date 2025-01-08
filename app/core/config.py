from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My FastAPI App"
    database_url: str = "sqlite:///./test.db"

settings = Settings()
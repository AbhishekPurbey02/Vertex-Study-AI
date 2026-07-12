from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Vertex Study AI"
    app_description: str = "AI-powered study assistant using RAG and LLMs"
    app_version: str = "0.1.0"
    environment: str = "development"

    backend_cors_origins: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Vertex Study AI"
    app_description: str = "AI-powered study assistant using RAG and LLMs"
    app_version: str = "0.1.0"
    environment: str = "development"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
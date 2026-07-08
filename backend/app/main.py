from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(
    title="Vertex Study AI",
    description="AI-powered study assistant using RAG and LLMs",
    version="0.1.0",
)

app.include_router(health_router)
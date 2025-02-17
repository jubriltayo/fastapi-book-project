from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router import api_router
from api.routes.integration_conf import router as integration_router
from core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Router
app.include_router(api_router, prefix=settings.API_PREFIX)

# Integration Router
app.include_router(integration_router)


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}

from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on startup 
    print("starting")
    print(f"SAP URL: {settings.SAP_BASE_URL}")

    yield  #app running

    # on shutdown
    print("shutting down")

app = FastAPI(
    title="Fastbank Demo Data",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/health") #get health endpoint
def health():
    return { #automaticaly converts intoo json
        "status": "ok",
        "app_host": settings.APP_HOST,
        "app_port": settings.APP_PORT
    }
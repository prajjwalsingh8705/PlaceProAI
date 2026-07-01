from fastapi import FastAPI

from app.routes.auth import router as auth_router
from app.routes.resume import router as resume_router

app = FastAPI()

app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)

app.include_router(
    resume_router,
    prefix="/api/resume",
    tags=["Resume"]
)

@app.get("/")
def root():
    return {
        "message": "PlacePro AI Backend Running"
    }
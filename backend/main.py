from fastapi.middleware.cors import CORSMiddleware
import os

from fastapi import FastAPI

from app.routes.auth import router as auth_router
from app.routes.resume import router as resume_router

# Create uploads folder automatically
os.makedirs("uploads", exist_ok=True)

app = FastAPI(
    title="PlacePro AI API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
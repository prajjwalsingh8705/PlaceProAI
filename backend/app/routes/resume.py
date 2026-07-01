import os
import shutil
import uuid

from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.resume import Resume
from app.security.auth import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/upload")
def upload_resume(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    unique_filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join("uploads", unique_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume = Resume(
        user_id=current_user.id,
        file_name=file.filename,
        file_path=file_path
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return {
        "message": "Resume uploaded successfully",
        "resume_id": str(resume.id),
        "file_name": resume.file_name
    }
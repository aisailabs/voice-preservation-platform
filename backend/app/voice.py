from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, storage
from ..database import get_db
from ..utils import get_current_user

router = APIRouter(
    prefix="/voice",
    tags=["Voice"]
)

@router.post("/upload", response_model=schemas.VoiceUploadResponse)
def upload_voice(file: UploadFile = File(...), db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    s3_key = storage.upload_file_to_s3(file)
    recording = crud.save_voice_recording(db, user_id=current_user.id, filename=file.filename, s3_key=s3_key)
    file_url = storage.get_s3_file_url(s3_key)
    return {"message": "File uploaded successfully", "file_url": file_url}

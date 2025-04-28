from sqlalchemy.orm import Session
from . import models
from .utils import hash_password, verify_password

def create_user(db: Session, email: str, password: str):
    db_user = models.User(email=email, hashed_password=hash_password(password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def save_voice_recording(db: Session, user_id: int, filename: str, s3_key: str):
    recording = models.VoiceRecording(user_id=user_id, filename=filename, s3_key=s3_key)
    db.add(recording)
    db.commit()
    db.refresh(recording)
    return recording


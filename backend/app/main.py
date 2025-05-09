from fastapi import FastAPI
from . import models
from .database import engine
from .routers import auth, voice

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(voice.router)

@app.get("/")
def root():
    return {"message": "Voice Preservation Backend is Up!"}


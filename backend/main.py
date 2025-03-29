
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import models, utils, yt_dlp_handler
from .database import SessionLocal, engine
from .auth import authenticate_user, create_user, get_current_user
from pydantic import BaseModel

# Initialize database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": user.token, "token_type": "bearer"}

@app.post("/register")
def register_user(username: str, password: str):
    create_user(username, password)
    return {"message": "User created successfully!"}

@app.post("/download/")
def start_download(url: str, user: str = Depends(get_current_user)):
    command = yt_dlp_handler.get_yt_dlp_command(url)
    download_path = f"/downloads/{user.username}/{url.split('/')[-1]}.mp4"
    yt_dlp_handler.download_video(command, download_path)
    return {"message": "Download started!"}
    
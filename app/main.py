from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from .database import engine, get_db

app = FastAPI(title="FastAPI Medical Notes")

@app.get("/")
def root():
    return {"message": "🚀 FastAPI Medical Notes API is running!"}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

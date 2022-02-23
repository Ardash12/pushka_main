from fastapi import APIRouter, Depends, HTTPException
from api import logger, settings
from sqlalchemy.orm import Session
from api.db import SessionLocal, tarantool_db
from fastapi.responses import Response, JSONResponse
from typing import Optional, List
from api.utils import crud
from api.schemas import EventInfoSchema
import time

# initial router for api routes - '/api/v1'
router = APIRouter()


def get_postgres_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_taranrool_db():
    yield tarantool_db


# Путь для получения списка рекомендаций по айди и типу рекомендаций.
@router.get("/recommendations_by_id", response_model=List[EventInfoSchema])
async def get_recommendations(id: str = None, type: str = None, db: Session = Depends(get_taranrool_db)):
    try:
        return crud.get_recommendations_by_id(db, id, type)
    except:
        raise HTTPException(status_code=400, detail="Bad request. Recommendations were not found")


# Путь для получения списка рекомендаций по номеру телофона и типу рекомендаций.
@router.get("/recommendations_by_phone", response_model=List[EventInfoSchema])
async def get_recommendations_by_phone(phone: str = None, type: str = None, db: Session = Depends(get_taranrool_db)):
    try:
        return crud.get_recommendations_by_phone(db, phone, type)
    except:
        raise HTTPException(status_code=400, detail="Bad request. Recommendations were not found")
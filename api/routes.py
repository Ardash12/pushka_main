from fastapi import APIRouter, Depends, HTTPException
from api import logger, settings
from sqlalchemy.orm import Session
from .db import SessionLocal, tarantool_db
from fastapi.responses import Response, JSONResponse
from typing import Optional, List
from api.utils import crud
from.schemas import GetRecommendations
import time

# initial router for api routes - '/api/v1'
router = APIRouter(
    prefix='/api/v1',
    tags=["api"])


def get_postgres_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_taranrool_db():
    yield tarantool_db


# Путь для получения списка рекомендаций по айди и типу рекомендаций.
@router.get("/recommendations", response_model=List[GetRecommendations])
async def get_recommendations(id: str = None, type: str = None, db: Session = Depends(get_taranrool_db)):
    try:
        return crud.get_recommendations_by_id(db, id, type)
    except:
        raise HTTPException(status_code=400, detail="Bad request. Recommendations were not found")



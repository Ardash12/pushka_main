from fastapi import APIRouter, Depends, HTTPException
from api import logger, settings
from sqlalchemy.orm import Session
from api import logger
from .db import SessionLocal, tarantool_db

# initial router
router = APIRouter()

def get_postgres_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_taranrool_db():
    try:
        yield tarantool_db
    finally:
        tarantool_db.close()


@router.get("/")
async def test():
    logger.info('Request to test endpoint')
    return 'Welcome to the test endpoint'

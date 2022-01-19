from fastapi import APIRouter, Depends, HTTPException
from api import logger, settings
from sqlalchemy.orm import Session
from api import logger

# initial router
router = APIRouter()


@router.get("/")
async def test():
    logger.info('Request to test endpoint')
    return 'Welcome to the test endpoint'

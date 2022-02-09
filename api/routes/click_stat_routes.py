from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.db import SessionLocal
from api.schemas import ReferenceList, CreateReference
from starlette.requests import Request
from api.utils import crud


def get_db(request: Request):
    return request.state.db


router = APIRouter()


@router.get('/', response_model=List[ReferenceList])
def ref_list(db: Session = Depends(get_db)):
    return crud.get_reference_list(db)


@router.post('/')
def ref_list(item: CreateReference, db: Session = Depends(get_db)):
    return crud.post_reference(db, item)

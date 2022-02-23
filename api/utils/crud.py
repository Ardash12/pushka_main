import json
from sqlalchemy.orm import Session
from api.models import Reference
from api.schemas import CreateReference


def get_recommendations_by_id(db, id: str, type: str):
    connect = db.space(type)
    recommendations = dict(connect.select(id))
    return recommendations[id]


def get_recommendations_by_phone(db, phone: str, type: str):
    connect = db.space(type)
    recommendations = dict(connect.select(phone))
    return recommendations[phone]


from sqlalchemy.orm import Session
from api.models import Reference
from api.schemas import CreateReference


def get_reference_list(db: Session):
    """Забираем из БД все объекты для GET запроса"""
    return db.query(Reference).all()


def post_reference(db: Session, item: CreateReference):
    """Записываем в БД данные из post запроса"""
    ref = Reference(**item.dict())
    db.add(ref)
    db.commit()
    db.refresh(ref)
    return ref
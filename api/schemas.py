from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EventInfoSchema(BaseModel):
    id: int
    event_title: str
    score: float
    event_organizer_id: int
    event_organizer_title: str
    organization: Optional[object]
    organization_data: Optional[object]
    event_img: str
    event_buy_link: str
    event_additional_buy_link: str



class ReferenceBase(BaseModel):
    """Базовая схема построения данных для обращения к БД"""

    user_id: str
    event_id: int
    event_type: str
    date: datetime

    class Config:
        orm_mode = True


class ReferenceList(ReferenceBase):
    """Схема для GET запросов"""

    id: int


class CreateReference(ReferenceBase):
    """Схема для POST запросов"""

    pass



from pydantic import BaseModel
from datetime import datetime


class GetRecommendations(BaseModel):
    event_id: int
    score: float
    event_title: str
    event_organizer: str
    event_buy_link: str
    event_buy_link_additional: str



class ReferenceBase(BaseModel):
    """Базовая схема построения данных для обращения к БД"""

    user_id: int
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



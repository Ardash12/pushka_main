from api.db import Base
from sqlalchemy import Column, String, Integer, DateTime


class Reference(Base):
    """Модели для создания таблицы в БД"""

    __tablename__ = 'reference_stat'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id = Column(Integer)
    event_id = Column(Integer)
    event_type = Column(String)
    date = Column(DateTime)
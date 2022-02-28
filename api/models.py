from api.db import Base
from sqlalchemy import Column, String, Integer, DateTime, event, ForeignKey, column, Interval, Date, Float, Enum
from sqlalchemy.orm import relationship
import enum


class StatusEnum(enum.Enum):
    active = 'active'
    visited = 'visited'
    refunded = 'refunded'


class Reference(Base):
    """Модели для создания таблицы в БД"""

    __tablename__ = 'reference_stat'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id = Column(String)
    event_id = Column(Integer)
    event_type = Column(String)
    date = Column(DateTime)


class Organization(Base):
    """Модели для хранения информации об мероприятия"""

    __tablename__ = 'organization_info'
    id = Column(Integer, primary_key=True, index=False, unique=True)
    organization_title = Column(String)
    address = Column(String)
    category = Column(String)
    events = relationship("Event", backref='organization_info')


class Event(Base):
    """Модели для хранения информации об мероприятия"""

    __tablename__ = 'events_info'
    id = Column(Integer, primary_key=True, index=False, unique=True)
    event_title = Column(String)
    event_organizer_title = Column(String)
    event_organizer_id = Column(Integer, ForeignKey('organization_info.id'), nullable=True)
    event_buy_link = Column(String)
    event_additional_buy_link = Column(String, nullable=True)
    event_img = Column(String)
    organization_data = relationship('Organization', backref='events_info')


class UsersInfo(Base):
    """Модели для хранения информации о юзерах от заказчика"""

    __tablename__ = 'users_info'
    id = Column(String, primary_key=True, index=False, unique=True)
    create_date = Column(Interval)
    user_birth = Column(Date)


class ClickInfo(Base):
    """Модели для хранения информации о кликах от заказчика"""

    __tablename__ = 'click_info'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    create_time = Column(DateTime)
    create_date = Column(Date)
    user_phone_details = Column(String)
    buyer_mobile_phone = Column(String)
    user_id = Column(String)
    url = Column(String)


class ClickUniqInfo(Base):
    """Модели для хранения информации о уникальных кликах от заказчика"""

    __tablename__ = 'click_uniq_info'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    create_date = Column(Date)
    user_phone_details = Column(String)
    buyer_mobile_phone = Column(String)
    user_id = Column(String)


class Regions(Base):
    """Модели для хранения информации о регионах """

    __tablename__ = 'regions'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    region_name = Column(String, unique=True)


class UserRegions(Base):
    """Модели для хранения информации о регионах юзеров от заказчика"""

    __tablename__ = 'user_region'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id = Column(String, ForeignKey('users_info.id'))
    region = Column(String(length=100), ForeignKey('regions.region_name'))


class Tickets(Base):
    """Модели для хранения информации о билетах"""

    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    refund_ticket_price = Column(Float, nullable=True)
    refund_date = Column(Integer)
    payment_amount = Column(Float, nullable=True)
    refund_reason = Column(String, nullable=True)
    visitor_first_name = Column(String)
    visit_date = Column(Interval)
    session_organization_id = Column(Integer)
    status = Column(Enum(StatusEnum))
    create_date = Column(Interval)
    payment_ticket_price = Column(Float, nullable=True)
    payment_date = Column(Interval)
    owner = Column(Integer)
    buyer_mobile_phone = Column(String(55))
    session_event_id = Column(Integer)
    comment = Column(String(255))
    session_date = Column(Integer)
    session_params = Column(String)

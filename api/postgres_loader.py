from sqlalchemy import inspect
from api.models import Organization, Event, UsersInfo, ClickInfo, ClickUniqInfo, Regions, UserRegions, Tickets
from api.db import SessionLocal, engine
from api import logger
import csv
import dateutil.parser

db = SessionLocal()


def table_exists(engine, name):
    ins = inspect(engine)
    ret = ins.dialect.has_table(engine.connect(), name)
    print('Table "{}" exists: {}'.format(name, ret))
    return ret


# Загрузка в БД данных по мероприятиям

def add_event_data():
    exist_table = table_exists(engine, 'events_info')  # Проверка наличия таблицы
    if not exist_table:
        with open('.\\api\\rec_files\\original_files\\events.csv', encoding='utf-8') as data:
            reader = csv.reader(data, delimiter=';')
            for row in reader:
                try:
                    org_id = db.query(Organization).filter(Organization.organization_title == row[2]).first()

                    try:
                        event = Event(id=int(row[0]),
                                      event_title=row[1],
                                      event_organizer_title=row[2],
                                      event_organizer_id=org_id.id,
                                      event_buy_link=row[3],
                                      event_additional_buy_link=row[4],
                                      event_img=''
                                      )
                        db.add(event)
                    except:
                        event = Event(id=int(row[0]),
                                      event_title=row[1],
                                      event_organizer_title=row[2],
                                      event_organizer_id=None,
                                      event_buy_link=row[3],
                                      event_additional_buy_link=row[4],
                                      event_img=''
                                      )
                        db.add(event)

                    try:
                        db.commit()
                        db.refresh(event)
                    except:
                        db.rollback()
                    finally:
                        db.close()

                except Exception as e:
                    logger.error(e)
                    pass
    else:
        pass

# Загрузка в БД данных по организациям

def add_organization_data():
    exist_table = table_exists(engine, 'organization_info')  # Проверка наличия таблицы
    if not exist_table:
        with open('.\\api\\rec_files\\original_files\\organizations.csv', encoding='utf-8') as data:
            reader = csv.reader(data, delimiter=';')
            for row in reader:
                try:
                    org = Organization(id=int(row[0]), organization_title=row[1], address=row[2], category=row[4])
                    db.add(org)
                    db.commit()
                    db.refresh(org)

                except Exception as e:
                    logger.error(e)
                    pass
    else:
        pass

# # Загрузка в БД данных из файла организаторов по кликам
#
# def add_click_data():
#     with open('.\\api\\rec_files\\original_files\\click.txt', encoding='utf-8') as data:
#         reader = csv.reader(data, delimiter=';')
#         id_item = 0
#         for row in reader:
#             id_item += 1
#             try:
#                 parsed_datetime = dateutil.parser.parse(row[0])
#             except:
#                 pass
#
#             try:
#                 click = ClickInfo(
#                     id=id_item,
#                     create_time=parsed_datetime,
#                     create_date=row[1],
#                     user_phone_details=row[2],
#                     buyer_mobile_phone=row[3],
#                     user_id=row[4],
#                     url=row[5],
#                 )
#                 db.add(click)
#                 db.commit()
#                 db.refresh(click)
#                 print(id_item, 'ok')
#
#             except Exception as e:
#                 print(e)
#
#
# # Загрузка в БД данных из файла организаторов по уникальным кликам
#
# def add_click_unique_data():
#     with open('.\\api\\rec_files\\original_files\\uniq.txt', encoding='utf-8') as data:
#         reader = csv.reader(data, delimiter=';')
#         id_item = 0
#         for row in reader:
#             id_item += 1
#             try:
#                 parsed_datetime = dateutil.parser.parse(row[0])
#             except:
#                 pass
#             try:
#                 click = ClickUniqInfo(
#                     id=id_item,
#                     create_date=parsed_datetime,
#                     user_phone_details=row[1],
#                     buyer_mobile_phone=row[2],
#                     user_id=row[3],
#                 )
#                 db.add(click)
#                 db.commit()
#                 db.refresh(click)
#                 print(id_item, 'ok')
#             except Exception as e:
#                 print(e)

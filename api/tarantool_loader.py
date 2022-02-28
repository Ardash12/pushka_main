import tarantool
import json
from .db import tarantool_db
from api import logger
from api.models import Event
from api.db import SessionLocal


postgres_db = SessionLocal()


# Проверка наличия спейса для типа рекомендаций
def check_creating_spaces(spaces):
    for elem in spaces:
        space, json_file = elem
        try:
            check = tarantool_db.space(space)
            logger.info(f'Space {space} is exist')
        except:
            logger.info(f'Space {space} was not found')
            space_class = RecommendationSpace(tarantool_db, space, json_file)
            space_class.create_tarantool_space()
            space_class.load_data_to_tarantool_space()
            logger.info(f'Creating of space {space} have been completed')


class RecommendationSpace():
    """Экземпляр спейса рекомендации"""

    def __init__(self, db, space_name, json_file):
        self.db = db
        self.space_name = space_name
        self.json_file = json_file

    def create_tarantool_space(self):
        """Создание спейса"""

        logger.info(f'Create {self.space_name} space')
        self.db.call('box.cfg', [{'memtx_memory': 38654705667}])
        schema = [
            {'name': 'id', 'type': 'string'},
            {'name': 'event_ids', 'type': 'any'}
        ]
        try:
            self.db.call('box.schema.space.create', [f'{self.space_name}', {'format': schema}])
            logger.info(f'{self.space_name} space have created')
        except tarantool.error.DatabaseError:
            self.db.call(f'box.space.{self.space_name}:create_index', ['primary'])
            logger.info(f'{self.space_name} index have added')

    # def get_event_info_from_csv(self):
    #     """Загрузка данных по мероприятиям из csv"""
    #
    #     logger.info(f'Start load {self.csv_file}')
    #     with open(f'.\\api\\rec_files\\{self.csv_file}', encoding='utf-8') as data:
    #         reader = csv.reader(data, delimiter=';')
    #         for row in reader:
    #             id = str(row[0])
    #             events_info = {
    #                 'event_title': row[1],
    #                 'event_organizer': row[2],
    #                 'event_buy_link': row[3],
    #                 'event_buy_link_additional': row[4],
    #                 'event_img': ''
    #             }
    #             self.events_data[id] = events_info
    #         data.close()
    #     logger.info(f'Loading data from {self.csv_file} have been completed')

    def load_data_to_tarantool_space(self):
        """Загрузка в спейс тарантула рекомендаций"""

        logger.info(f'Load recommendations data from {self.json_file} to tarantool')

        with open(f'.\\api\\rec_files\\{self.json_file}', 'r') as file:
            parsed_string = json.loads(file.read())
            connect = tarantool_db.space(self.space_name)
            count_of_user = len(parsed_string)
            current_count = 0

            for key, value in parsed_string.items():
                item_data = []
                try:
                    for id, score in value.items():
                        try:
                            event = {
                                'score': score,
                            }
                            event_data = postgres_db.query(Event).get(int(id))
                            event.update(event_data.__dict__)
                            event.pop('_sa_instance_state')
                            try:
                                org_dict = event_data.organization_data.__dict__

                                org_dict.pop('_sa_instance_state')
                                org = {'organization': org_dict}
                                event.update(org)
                            except KeyError:
                                org_dict = event_data.organization_data.__dict__
                                org = {'organization': org_dict}
                                event['organization_data'] = org_dict
                                event.update(org)

                            except AttributeError:
                                org = {'organization': {
                                    'category': '',
                                    'address': '',
                                    'organization_title': '',
                                    'id': None
                                }}
                                event.update(org)

                            item_data.append(event)
                        # если нет данных по event_id
                        except AttributeError:
                            event = {
                                'id': int(id),
                                'score': float(score),
                                'event_title': '',
                                'event_organizer_title': '',
                                'event_organizer_id': int(),
                                'event_buy_link': '',
                                'event_buy_link_additional': '',
                                'event_img': ''
                            }
                            item_data.append(event)
                    print(key)
                    connect.insert((key, item_data))
                    current_count += 1
                    logger.info(f'added recs for {current_count} of {count_of_user} users ')

                # если в value не dict

                except AttributeError:
                    try:
                        for id in value:
                            try:
                                event_data = postgres_db.query(Event).get(int(id))
                                event = {
                                    'score': 0,
                                }
                                event.update(event_data.__dict__)
                                event.pop('_sa_instance_state')
                                try:
                                    org_dict = event_data.organization_data.__dict__

                                    org_dict.pop('_sa_instance_state')
                                    org = {'organization': org_dict}
                                    event.update(org)
                                except KeyError:
                                    org_dict = event_data.organization_data.__dict__
                                    org = {'organization': org_dict}
                                    event['organization_data'] = org_dict
                                    event.update(org)

                                except AttributeError:
                                    org = {'organization': {
                                        'category': '',
                                        'address': '',
                                        'organization_title': '',
                                        'id': None
                                    }}
                                    event.update(org)
                                item_data.append(event)

                            # если нет данных по event_id
                            except AttributeError:
                                try:
                                    event = {
                                        'id': int(id),
                                        'score': float(),
                                        'event_title': '',
                                        'event_organizer_title': '',
                                        'event_organizer_id': int(),
                                        'event_buy_link': '',
                                        'event_buy_link_additional': '',
                                        'event_img': ''
                                    }
                                except ValueError:
                                    pass
                                item_data.append(event)
                            except ValueError:
                                pass
                    # если выпадает NoneType
                    except TypeError:
                        pass
                    print(key)
                    connect.insert((key, item_data))
                    current_count += 1
                    logger.info(f'added recs for {current_count} of {count_of_user} users ')

            logger.info(f'recommendations data from {self.json_file} to tarantool have been completed')
            file.close()

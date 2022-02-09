import tarantool
import json
import csv
from .db import tarantool_db
from api import logger

# Проверка наличия спейса для типа рекомендаций
def check_creating_spaces(spaces):
    for elem in spaces:
        space, csv_file, json_file = elem
        try:
            check = tarantool_db.space(space)
            logger.info(f'Space {space} is exist')
        except:
            logger.info(f'Space {space} was not found')
            space_class = RecommendationSpace(tarantool_db, space, csv_file, json_file)
            space_class.create_tarantool_space()
            space_class.get_event_info_from_csv()
            space_class.load_data_to_tarantool_space()
            logger.info(f'Creating of space {space} have been completed')


class RecommendationSpace():
    """Экземпляр спейса рекомендации"""

    def __init__(self, db, space_name, csv_file, json_file):
        self.db = db
        self.space_name = space_name
        self.csv_file = csv_file
        self.json_file = json_file
        self.events_data = {}

    def create_tarantool_space(self):
        """Создание спейса"""

        logger.info(f'Create {self.space_name} space')
        self.db.call('box.cfg', [{'memtx_memory': 25769803778 }])
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

    def get_event_info_from_csv(self):
        """Загрузка данных по мероприятиям из csv"""

        logger.info(f'Start load {self.csv_file}')
        with open(f'.\\api\\rec_files\\{self.csv_file}', encoding='utf-8') as data:
            reader = csv.reader(data, delimiter=';')
            for row in reader:
                id = str(row[0])
                events_info = {
                    'event_title': row[1],
                    'event_organizer': row[2],
                    'event_buy_link': row[3],
                    'event_buy_link_additional': row[4],
                    'event_img': ''
                }
                self.events_data[id] = events_info
            data.close()
        logger.info(f'Loading data from {self.csv_file} have been completed')

    def load_data_to_tarantool_space(self):
        """Загрузка в спейс тарантула рекомендаций"""

        logger.info(f'Load recommendations data from {self.json_file} to tarantool')

        with open(f'.\\api\\rec_files\\{self.json_file}', 'r') as file:
            parsed_string = json.loads(file.read())
            connect = tarantool_db.space(self.space_name)

            for key, value in parsed_string.items():
                item_data = []
                try:
                    for id, score in value.items():
                        try:
                            event_data = self.events_data[str(id)]
                            event = {
                                'event_id': id,
                                'score': score,
                            }
                            event.update(event_data)
                            item_data.append(event)
                        # если нет данных по event_id
                        except KeyError:
                            event = {
                                'event_id': int(id),
                                'score': float(score),
                                'event_title': '',
                                'event_organizer': '',
                                'event_buy_link': '',
                                'event_buy_link_additional': '',
                                'event_img': ''
                            }
                            item_data.append(event)

                    connect.insert((key, item_data))
                # если в value не dict
                except AttributeError:
                    try:
                        for id in value:
                            try:
                                event_data = self.events_data[str(id)]
                                event = {
                                    'event_id': int(id),
                                    'score': 0,
                                }
                                event.update(event_data)
                                item_data.append(event)
                            # если нет данных по event_id
                            except KeyError:
                                try:
                                    event = {
                                        'event_id': int(id),
                                        'score': 0,
                                        'event_title': '',
                                        'event_organizer': '',
                                        'event_buy_link': '',
                                        'event_buy_link_additional': '',
                                    }
                                except ValueError:
                                    pass
                                item_data.append(event)
                    # если выпадает NoneType
                    except TypeError:
                        pass

                    connect.insert((key, item_data))



            logger.info(f'recommendations data from {self.json_file} to tarantool have been completed')
            file.close()







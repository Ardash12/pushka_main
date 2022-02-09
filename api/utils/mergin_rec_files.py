import json
from api import logger
import os

FINAL_FILE = '.\\api\\rec_files\\regional_rec.json'


def merging_files(rec_list):
    if os.path.exists(FINAL_FILE):
        pass
    else:
        final_data = {}
        try:
            for rec in rec_list:
                with open(f'.\\api\\rec_files\\original_files\\{rec}', 'r', encoding='utf-8', ) as file:
                    logger.info('Start merging of {}'.format(rec))
                    parsed_string = json.loads(file.read())
                    for key, value in parsed_string.items():
                        final_data[key] = value
                    logger.info('End merging of {}'.format(rec))

            with open(FINAL_FILE, 'w') as fp:
                json.dump(final_data, fp)
                logger.info('merging of regional rec files has been ended')
                fp.close()
        except Exception as e:
            raise Exception('Merging ended with error {}'.format(e))
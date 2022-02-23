import requests

from api import settings as s


class TestRegionalRecs:
    id = '005bbb70559ac82250d8099760f7df50'
    fail_id = '13322'
    type_rec = 'regional_rec'
    fail_type_rec = 'regional_rec_2'
    if s.status == 'DEV':
        URL = f'{s.dev_host}:{s.dev_port}/api/v1/recommendations_by_id?id={id}&type={type_rec}'
        FAIL_URL_BY_ID = f'{s.dev_host}:{s.dev_port}/api/v1/recommendations_by_id?id={fail_id}&type={type_rec}'
        FAIL_URL_BY_TYPE = f'{s.dev_host}:{s.dev_port}/api/v1/recommendations_by_id?id={id}&type={fail_type_rec}'
    elif s.status == 'TEST':
        URL = f'{s.test_host}:{s.test_port}/api/v1/recommendations_by_id?id={id}&type={type_rec}'
        FAIL_URL_BY_ID = f'{s.test_host}:{s.test_port}/api/v1/recommendations_by_id?id={fail_id}&type={type_rec}'
        FAIL_URL_BY_TYPE = f'{s.test_host}:{s.test_port}/api/v1/recommendations_by_id?id={id}&type={fail_type_rec}'
    else:
        URL = f'{s.prod_host}:{s.prod_port}/api/v1/recommendations_by_id?id={id}&type={type_rec}'
        FAIL_URL_BY_ID = f'{s.prod_host}:{s.prod_port}/api/v1/recommendations_by_id?id={fail_id}&type={type_rec}'
        FAIL_URL_BY_TYPE = f'{s.prod_host}:{s.prod_port}/api/v1/recommendations_by_id?id={id}&type={fail_type_rec}'

    def test_response_code(self):
        res = requests.get(self.URL)
        assert res.status_code == 200

    def test_headers(self):
        res = requests.get(self.URL)
        assert res.headers['content-type'] == 'application/json'

    def test_id_not_exist(self):
        res = requests.get(self.FAIL_URL_BY_ID)
        assert res.status_code == 400

    def test_wrong_type(self):
        res = requests.get(self.FAIL_URL_BY_TYPE)
        assert res.status_code == 400


class Test3dayRecsFromFilteredEvent:
    phone = '6a4816fe848efbd8c8fb8e8760d7cbd1'
    fail_phone = '133'
    type_rec = '3day_recs_from_filtered_events'
    fail_type_rec = '3day_recs_from_filtered_events_1asdfsf'
    if s.status == 'DEV':
        URL = f'{s.dev_host}:{s.dev_port}/api/v1/recommendations_by_phone?phone={phone}&type={type_rec}'
        FAIL_URL_BY_ID = f'{s.dev_host}:{s.dev_port}/api/v1/recommendations_by_phone?phone={fail_phone}&type={type_rec}'
        FAIL_URL_BY_TYPE = f'{s.dev_host}:{s.dev_port}/api/v1/recommendations_by_phone?phone={phone}&type={fail_type_rec}'
    elif s.status == 'TEST':
        URL = f'{s.test_host}:{s.test_port}/api/v1/recommendations_by_phone?phone={phone}&type={type_rec}'
        FAIL_URL_BY_ID = f'{s.test_host}:{s.test_port}/api/v1/recommendations_by_phone?phone={fail_phone}&type={type_rec}'
        FAIL_URL_BY_TYPE = f'{s.test_host}:{s.test_port}/api/v1/recommendations_by_phone?phone={phone}&type={fail_type_rec}'
    else:
        URL = f'{s.prod_host}:{s.prod_port}/api/v1/recommendations_by_phone?phone={phone}&type={type_rec}'
        FAIL_URL_BY_ID = f'{s.prod_host}:{s.prod_port}/api/v1/recommendations_by_phone?phone={fail_phone}&type={type_rec}'
        FAIL_URL_BY_TYPE = f'{s.prod_host}:{s.prod_port}/api/v1/recommendations_by_phone?phone={phone}&type={fail_type_rec}'

    def test_response_code(self):
        res = requests.get(self.URL)
        assert res.status_code == 200

    def test_headers(self):
        res = requests.get(self.URL)
        assert res.headers['content-type'] == 'application/json'

    def test_id_not_exist(self):
        res = requests.get(self.FAIL_URL_BY_ID)
        assert res.status_code == 400

    def test_wrong_type(self):
        res = requests.get(self.FAIL_URL_BY_TYPE)
        assert res.status_code == 400


class Test3dayRecsFromFilteredTop:
    phone = '160e3490b932ca55fc133b11e74c100e'
    fail_phone = '133'
    type_rec = '3day_recs_from_filtered_top'
    fail_type_rec = '3day_recs_from_filtered_2sdfsf'
    if s.status == 'DEV':
        URL = f'{s.dev_host}:{s.dev_port}/api/v1/recommendations_by_phone?phone={phone}&type={type_rec}'
        FAIL_URL_BY_ID = f'{s.dev_host}:{s.dev_port}/api/v1/recommendations_by_phone?phone={fail_phone}&type={type_rec}'
        FAIL_URL_BY_TYPE = f'{s.dev_host}:{s.dev_port}/api/v1/recommendations_by_phone?phone={phone}&type={fail_type_rec}'
    elif s.status == 'TEST':
        URL = f'{s.test_host}:{s.test_port}/api/v1/recommendations_by_phone?phone={phone}&type={type_rec}'
        FAIL_URL_BY_ID = f'{s.test_host}:{s.test_port}/api/v1/recommendations_by_phone?phone={fail_phone}&type={type_rec}'
        FAIL_URL_BY_TYPE = f'{s.test_host}:{s.test_port}/api/v1/recommendations_by_phone?phone={phone}&type={fail_type_rec}'
    else:
        URL = f'{s.prod_host}:{s.prod_port}/api/v1/recommendations_by_phone?phone={phone}&type={type_rec}'
        FAIL_URL_BY_ID = f'{s.prod_host}:{s.prod_port}/api/v1/recommendations_by_phone?phone={fail_phone}&type={type_rec}'
        FAIL_URL_BY_TYPE = f'{s.prod_host}:{s.prod_port}/api/v1/recommendations_by_phone?phone={phone}&type={fail_type_rec}'

    def test_response_code(self):
        res = requests.get(self.URL)
        assert res.status_code == 200

    def test_headers(self):
        res = requests.get(self.URL)
        assert res.headers['content-type'] == 'application/json'

    def test_id_not_exist(self):
        res = requests.get(self.FAIL_URL_BY_ID)
        assert res.status_code == 400

    def test_wrong_type(self):
        res = requests.get(self.FAIL_URL_BY_TYPE)
        assert res.status_code == 400


class TestUserRecWithoutFilter:
    phone = '920c30cd8c7dc4139e44fca6141c9b70'
    fail_phone = '133'
    type_rec = 'user_rec_without_filter'
    fail_type_rec = 'user_rec_without_filter_fail'
    if s.status == 'DEV':
        URL = f'{s.dev_host}:{s.dev_port}/api/v1/recommendations_by_phone?phone={phone}&type={type_rec}'
        FAIL_URL_BY_ID = f'{s.dev_host}:{s.dev_port}/api/v1/recommendations_by_phone?phone={fail_phone}&type={type_rec}'
        FAIL_URL_BY_TYPE = f'{s.dev_host}:{s.dev_port}/api/v1/recommendations_by_phone?phone={phone}&type={fail_type_rec}'
    elif s.status == 'TEST':
        URL = f'{s.test_host}:{s.test_port}/api/v1/recommendations_by_phone?phone={phone}&type={type_rec}'
        FAIL_URL_BY_ID = f'{s.test_host}:{s.test_port}/api/v1/recommendations_by_phone?phone={fail_phone}&type={type_rec}'
        FAIL_URL_BY_TYPE = f'{s.test_host}:{s.test_port}/api/v1/recommendations_by_phone?phone={phone}&type={fail_type_rec}'
    else:
        URL = f'{s.prod_host}:{s.prod_port}/api/v1/recommendations_by_phone?phone={phone}&type={type_rec}'
        FAIL_URL_BY_ID = f'{s.prod_host}:{s.prod_port}/api/v1/recommendations_by_phone?phone={fail_phone}&type={type_rec}'
        FAIL_URL_BY_TYPE = f'{s.prod_host}:{s.prod_port}/api/v1/recommendations_by_phone?phone={phone}&type={fail_type_rec}'

    def test_response_code(self):
        res = requests.get(self.URL)
        assert res.status_code == 200

    def test_headers(self):
        res = requests.get(self.URL)
        assert res.headers['content-type'] == 'application/json'

    def test_id_not_exist(self):
        res = requests.get(self.FAIL_URL_BY_ID)
        assert res.status_code == 400

    def test_wrong_type(self):
        res = requests.get(self.FAIL_URL_BY_TYPE)
        assert res.status_code == 400

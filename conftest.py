import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.patch_object import PartialUpdateObject
from endpoints.delete_object import DeleteObject

base_url = 'https://api.restful-api.dev/objects'

# Фикстура для создания объекта для тестирования
@pytest.fixture(scope='module')
def obj_id():
    create_object = CreateObject()
    payload = {
        "name": "Redmi Note 14 Pro 12",
        "data": {
            "year": 2024,
            "price": 399.88,
            "CPU model": "Helio G100-Ultra",
            "Hard disk size": "256 GB"
        }
    }

    create_object.new_object(payload)
    yield create_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_object(create_object.response_json['id'])
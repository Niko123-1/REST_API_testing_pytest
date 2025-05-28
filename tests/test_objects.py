import requests
import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.patch_object import PartialUpdateObject
from endpoints.delete_object import DeleteObject



def test_create_object():
    # Создаем объект

    new_object_endpoint = CreateObject()
    payload = {
        "name": "New equip",
        "data": {
            "year": 2023,
            "price": 3399.88,
            "CPU model": "CPU",
            "Hard disk size": "256 GB"
        }
    }
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_status_code_is_200()
    new_object_endpoint.check_name(payload['name'])

def test_get_object_by_obj_id(obj_id):
    # Получаем информацию о созданном объекте

    get_object_endpoint = GetObject()
    get_object_endpoint.get_object(obj_id)
    get_object_endpoint.check_status_code_is_200()
    get_object_endpoint.check_response_id(obj_id)


def test_update_object(obj_id):
    # Меняем созданный объект

    update_object_endpoint = UpdateObject()
    payload = {
        "name": "Apple Honor 17",
        "data": {
            "year": 2025,
            "price": 49.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    update_object_endpoint.update_object(obj_id,payload=payload)
    update_object_endpoint.check_status_code_is_200()
    update_object_endpoint.check_name(payload['name'])
    update_object_endpoint.check_data(payload['data'])


def test_patch_object(obj_id):
    # Меняем некоторые поля объекта

    patch_object_endpoint = PartialUpdateObject()
    payload = {
        "name": "Apple Honor 17 NEW NEW NEW",
        "data": {
            "price": 249.99
        }
    }

    patch_object_endpoint.partial_update_object(obj_id, payload=payload)
    patch_object_endpoint.check_status_code_is_200()
    patch_object_endpoint.check_name(payload['name'])
    patch_object_endpoint.check_data(payload['data'])


def test_delete_object(obj_id):
    # Удаляем созданный объект

    delete_object_endpoint = DeleteObject()

    delete_object_endpoint.delete_object(obj_id)
    delete_object_endpoint.check_status_code_is_200()
    delete_object_endpoint.check_deletion_message(obj_id)

    # Проверяем, что объект действительно удален
    get_object_endpoint = GetObject()
    get_object_endpoint.get_object(obj_id)
    get_object_endpoint.check_status_code_is_404()
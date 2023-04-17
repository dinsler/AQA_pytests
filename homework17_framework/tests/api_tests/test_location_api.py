from http import HTTPStatus

from homework17_framework.api_collections.location_api import LocationAPI
from homework17_framework.data_objects.location_data import LocationData


def test_get_location(env, location_mock):
    expected_location = location_mock
    response = LocationAPI(env).get_location(1)
    response_data = response.json()
    actual_location = LocationData.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, 'Status code is not as expected'
    assert actual_location == expected_location, 'Character Data is not as expected'


def test_get_non_existent_location(env):
    response = LocationAPI(env).get_location(1123)
    assert response.status_code == HTTPStatus.NOT_FOUND, 'Status code is not as expected'
    assert response.json().get('error') == 'Location not found'

import pytest
from homework17_framework.data_objects.character_data import CharacterData
from homework17_framework.data_objects.location_data import LocationData


@pytest.fixture()
def character_mock():
    return CharacterData()


@pytest.fixture()
def location_mock():
    return LocationData()

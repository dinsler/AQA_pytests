import pytest
from homework15_pytest.human import Human

#
# @pytest.fixture()
# def generate_human_data(faker):
#     name = faker.name()
#     yield name


@pytest.fixture()
def average_human():
    return Human('Alex', 34, 'male')


@pytest.fixture()
def old_human():
    return Human('Mona', 100, 'female')


@pytest.fixture()
def dead_human():
    return Human('Paul', 104, 'male')


@pytest.fixture()
def human_with_params():
    def __create_human(name: str, age: int, gender: str):
        return Human(name, age, gender)
    yield __create_human


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "positive: for positive tests"
    )
    config.addinivalue_line(
        "markers", "negative: for negative tests"
    )

import pytest
from homework17_framework.page_objects.main_page import MainPage
from homework17_framework.utilities.config_reader import get_application_url, get_browser_id, get_user_creds,\
    get_search_item
from homework17_framework.utilities.driver_factory import driver_factory


@pytest.fixture()
def create_browser():
    driver = driver_factory(get_browser_id())
    driver.maximize_window()
    driver.get(get_application_url())
    yield driver
    driver.quit()


@pytest.fixture()
def open_main_page(create_browser):
    return MainPage(create_browser)


@pytest.fixture()
def open_login_page(open_main_page):
    return open_main_page.click_login_button()


@pytest.fixture()
def open_my_account_page(open_login_page):
    return open_login_page.login(get_user_creds()[0], get_user_creds()[1])


@pytest.fixture()
def open_found_product_page(open_main_page):
    return open_main_page.found_product(get_search_item()[0])


@pytest.fixture()
def open_cart_page(open_found_product_page):
    return open_found_product_page.click_buy_button().click_go_to_cart_button()


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: for smoke tests"
    )
    config.addinivalue_line(
        "markers", "regression: for regression tests"
    )
from selenium.webdriver import Chrome, ChromeOptions, Firefox
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.firefox.service import Service as firefox_service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

__CHROME = 1
__FIRE_FOX = 2


def driver_factory(driver_id: int):
    if int(driver_id) == __CHROME:
        options = ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--disable-site-isolation-trials")
        return Chrome(chrome_options=options, service=chrome_service(ChromeDriverManager().install()))
    elif int(driver_id) == __FIRE_FOX:
        return Firefox(service=firefox_service(GeckoDriverManager().install()))
    else:
        return Chrome(service=chrome_service(ChromeDriverManager().install()))

from selenium.webdriver.common.by import By
from homework17_framework.utilities.web_ui.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __cart_page = (By.XPATH, '//div[@id="app"]//h1')
    __remove_product_from_cart_button = (By.XPATH, '//a[@title="видалити продукт"]')
    __my_product_in_cart = (By.XPATH, '//span[text()="Kringle Candle"]/parent::a/parent::div/../..')
    __eco_wrapping_checkbox = (By.XPATH, '//div[@class="sc-hOzowv bhdFLN sc-fyBusP fhgWEU ecoWrapping"]//input'
                                         '[@type="checkbox"]')
    __gift_wrapping_checkbox = (By.XPATH, '//input[@type="checkbox" and @disabled]')
    __discount_code_input = (By.XPATH, '//input[@type="text"]')
    __submit_discount_code_button = (By.XPATH, '//span[text()="OK"]/../../parent::button')
    __input_error_message = (By.XPATH, '//label[@data-testid="input-error"]')
    __back_to_shop_button = (By.XPATH, '//span[text()="Назад до магазину"]/../../parent::button')
    __order_button = (By.XPATH, '//span[text()="Замовити"]/../../parent::button')
    __order_steps_chain = (By.XPATH, '//div[@class="sc-cabOPr kHEcYW stepChain"]')
    __categories_of_products_links = (By.XPATH, '//*[@id="categoryLinks"]')

    def get_cart_page_text(self):
        return self._get_text(self.__cart_page)

    def click_remove_product_from_cart_button(self):
        self._click(self.__remove_product_from_cart_button)
        return self

    def is_my_product_in_cart_invisible(self):
        return self._wait_until_element_invisible(self.__my_product_in_cart)

    def set_invalid_discount_code_input(self, discount_code: str):
        self._send_keys(locator=self.__discount_code_input, value=discount_code)
        return self

    def click_submit_discount_code_button(self):
        self._click_with_js_execute(self.__submit_discount_code_button)
        return self

    def is_input_error_message_displayed(self):
        element = self._wait_until_element_visible(self.__input_error_message)
        return element.is_displayed

    def select_eco_wrapping_checkbox(self):
        self._click_with_js_execute(self.__eco_wrapping_checkbox)
        return self

    def is_gift_wrapping_checkbox_invisible(self):
        return self._wait_until_element_invisible(self.__gift_wrapping_checkbox)

    def click_back_to_shop_button(self):
        self._click_with_js_execute(self.__back_to_shop_button)
        return self

    def is_categories_of_products_links_displayed(self):
        element = self._wait_until_element_located(self.__categories_of_products_links)
        return element.is_displayed

    def click_order_button(self):
        self._click_with_js_execute(self.__order_button)
        return self

    def is_order_steps_chain_displayed(self):
        element = self._wait_until_element_located(self.__order_steps_chain)
        return element.is_displayed

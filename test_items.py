from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.webdriver import WebDriver 
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestOrders:
    def test_order_button_is_available(self, browser: WebDriver):
        browser.get(link)
        order_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        
        actual = order_button.is_displayed()
        expected = True
        assert actual == expected, "Кнопка \"Добавить в корзину\" должна присутствовать на странице" 
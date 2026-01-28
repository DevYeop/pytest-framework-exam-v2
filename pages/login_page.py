from selenium.webdriver.common.by import By
from core.ui.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"
    USER_INPUT = (By.ID, "user-name")
    PW_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.type(self.USER_INPUT, username)
        self.type(self.PW_INPUT, password)
        self.click(self.LOGIN_BTN)

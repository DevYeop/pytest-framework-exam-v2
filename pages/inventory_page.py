from selenium.webdriver.common.by import By
from core.ui.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")

    def get_title(self):
        return self.find(self.TITLE).text

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_saucedemo_login(browser):
    login = LoginPage(browser)
    inventory = InventoryPage(browser)

    login.open()
    login.login("standard_user", "secret_sauce")
    
    assert inventory.get_title() == "Products"

from Data.credentials import user,admin
import pytest
import allure
from Locators.locators import NavigationMenuLocators
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException


locator = NavigationMenuLocators

def credentials():
    lst = [[user['email'], user['password']], [admin['email'], admin['password']]]
    return lst

@allure.link("http://localhost:57690/home/events?page=1", name='Click me')
@allure.feature('Login User')
@allure.story('"Actors" login to site EventExpress ')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('data', credentials())
def test_authorization(app, data, screenshot_on_failure):
    app.auth.click_on_login_button()
    app.auth.clean_login_field( )
    app.auth.type_login(data[0])
    app.auth.clean_password_field( )
    app.auth.type_pass(data[1])
    app.auth.press_button_signin()
    assert app.base.check_if_element_exists( locator.PROFILE )
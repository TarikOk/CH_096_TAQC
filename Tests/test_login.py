from Tests.test_main import TestInit
from Pages.LoginPage import LoginPage
from Data.TestData import TestData
 

class TestLogin(TestInit):

    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()


    def login_if_user_entered(self):
        self.login = LoginPage(self.driver)
        self.login.login_user(TestData.LOGIN_USER, TestData.PASSWORD_USER)

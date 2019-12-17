from Tests.test_init import TestInit

from Data.credentials import user



class TestLogin(TestInit):

    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()



    def test_authorization(self):
        self.exec.auth.click_on_login_button()
        self.exec.auth.clean_login_field()
        self.exec.auth.type_login( user['email'])
        self.exec.auth.clean_password_field( )
        self.exec.auth.type_pass(user['password'])
        self.exec.auth.press_button_signin()














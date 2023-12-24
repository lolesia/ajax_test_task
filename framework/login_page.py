from .page import Page
from .element_constant import *


class LoginPage(Page):
    """
    A class to implement the simulation of
    the required action on the login page
    """

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.click_element(ELEMENT_AUTH_BUTTON)
        self.send_keys(ELEMENT_EMAIL, username)
        self.send_keys(ELEMENT_PASSWORD, password)
        self.click_element(ELEMENT_AUTH_BUTTON_SECOND_SCREEN)
        return self

    def login_second_screen(self, username, password):
        self.send_keys(ELEMENT_EMAIL, username)
        self.send_keys(ELEMENT_PASSWORD, password)
        self.click_element(ELEMENT_AUTH_BUTTON_SECOND_SCREEN)
        return self

    def is_logged_in(self):

        success_login_element = self.wait_for_element_to_be_present(ELEMENT_ADD_HUB)
        return success_login_element.is_displayed()

    def authentication_error(self):
        error_login_element = self.wait_for_element_to_be_present(ELEMENT_INVALID_AUTH_MESSAGE)
        return error_login_element.text

    def logout(self):
        self.click_element(ELEMENT_MENU)
        self.click_element(ELEMENT_SETTINGS_APP)
        self.click_element(ELEMENT_LOGOUT)


from conftest import user_login_fixture
import logging

logging.basicConfig(level=logging.INFO)


class TestLogin:
    """
    Class to implement testing of
    basic authentication functions
    """

    def test_user_login_positive(self, user_login_fixture):
        login = 'qa.ajax.app.automation@gmail.com'
        password = 'qa_automation_password'
        login_page = user_login_fixture.login(login, password)

        try:
            assert login_page.is_logged_in() is True
        except AssertionError as e:
            logging.error(f"Assertion error: {e}")
            raise
        finally:
            login_page.logout()

    def test_user_login_invalid_mail_format(self, user_login_fixture):
        login = 'qa.ajax.app.automation'
        password = 'qa_automation_password'
        try:
            assert user_login_fixture.login(login, password).authentication_error() == 'Неверный формат электронной почты'
        except AssertionError as e:
            logging.error(f"Assertion error: {e}")
            raise

    def test_user_login_invalid_login_data(self, user_login_fixture):
        login = 'invalid_login_automation@gmail.com'
        password = 'invalid_password'
        try:
            assert user_login_fixture.login_second_screen(login, password).authentication_error() == 'Неверный логин или пароль'
        except AssertionError as e:
            logging.error(f"Assertion error: {e}")
            raise






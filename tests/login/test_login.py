from conftest import user_login_fixture
import logging
import pytest
logging.basicConfig(level=logging.INFO)

class TestLogin:
    """
    Class to implement testing of
    basic authentication functions
    """

    @pytest.mark.parametrize("login, password, login_method, expected_error", [
        ('qa.ajax.app.automation@gmail.com', 'qa_automation_password', 'login', None),
        ('qa.ajax.app.automation', 'qa_automation_password', 'login', 'Неверный формат электронной почты'),
        ('invalid_login_automation@gmail.com', 'invalid_password', 'login_second_screen', 'Неверный логин или пароль'),
    ])
    def test_user_login(self, user_login_fixture, login, password, login_method, expected_error):
        login_page = getattr(user_login_fixture, login_method)(login, password)

        try:
            if expected_error is None:
                assert login_page.is_logged_in() is True
                login_page.logout()
            else:
                assert login_page.authentication_error() == expected_error
        except AssertionError as e:
            logging.error(f"Ошибка проверки: {e}")
            raise




from conftest import user_login_fixture
import logging
import pytest
logging.basicConfig(level=logging.INFO)


# class TestLogin:
#     """
#     Class to implement testing of
#     basic authentication functions
#     """
#
#     def test_user_login_positive(self, user_login_fixture):
#         login = 'qa.ajax.app.automation@gmail.com'
#         password = 'qa_automation_password'
#         login_page = user_login_fixture.login(login, password)
#
#         try:
#             assert login_page.is_logged_in() is True
#         except AssertionError as e:
#             logging.error(f"Assertion error: {e}")
#             raise
#         finally:
#             login_page.logout()
#
#     def test_user_login_invalid_mail_format(self, user_login_fixture):
#         login = 'qa.ajax.app.automation'
#         password = 'qa_automation_password'
#         try:
#             assert user_login_fixture.login(login, password).authentication_error() == 'Неверный формат электронной почты'
#         except AssertionError as e:
#             logging.error(f"Assertion error: {e}")
#             raise
#
#     def test_user_login_invalid_login_data(self, user_login_fixture):
#         login = 'invalid_login_automation@gmail.com'
#         password = 'invalid_password'
#         error_message = user_login_fixture.login_second_screen(login, password).authentication_error()
#         try:
#             assert error_message == 'Неверный логин или пароль' or error_message == 'Подождите, идет синхронизация с сервером'
#         except AssertionError as e:
#             logging.error(f"Assertion error: {e}")
#             raise


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




from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    """
    Class to implement simulation of standard
    required actions on the application page
    """

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def find_element(self, xpath):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            return element
        except NoSuchElementException as e:
            self.logger.error(f'Element with XPath={xpath} not found: {e}')
            raise

    def click_element(self, xpath):
        try:
            element = self.find_element(xpath)
            element.click()
        except NoSuchElementException as e:
            self.logger.error(f'Element with XPath={xpath} not found: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element with XPath={xpath} not interactable: {e}')
            raise

    def send_keys(self, xpath, text,  clear_first=True):
        try:
            element = self.find_element(xpath)
            if clear_first:
                element.clear()
            element.send_keys(text)
        except ElementNotInteractableException as e:
            self.logger.error(f'Element with XPath={xpath} not found: {e}')
            raise

    def wait_for_element_to_be_present(self, xpath, timeout=5000):
        try:
            element_present = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element_present
        except TimeoutException:
            self.logger.error(f'Element with XPath={xpath} did not appear within {timeout} seconds.')
            raise

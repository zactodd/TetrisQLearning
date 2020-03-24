from tetris_ql.utils import get_chrome_driver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


DRIVER = get_chrome_driver()
URL = "https://tetris.com/play-tetris"


class Page:
    def __init__(self, url, browser=DRIVER):
        self.browser = self._browser_initialise(url, browser)

    @staticmethod
    def _browser_initialise(url, browser):
        """
        Initialise the browser.
        :param browser: The browser prior to being initialise.
        :return: The browser.
        """
        browser.get(url)
        return browser


def google_login(email, password, driver=DRIVER):
    login_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'identifierId')))
    login_field.send_keys(email)
    driver.find_element_by_id('identifierNext').click()
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    password_field = password_field.find_element_by_tag_name('input')
    password_field.send_keys(password)
    driver.find_element_by_id('passwordNext').click()

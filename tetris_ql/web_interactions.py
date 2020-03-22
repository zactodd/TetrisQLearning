from tetris_ql.utils import get_chrome_driver

DRIVER = get_chrome_driver()
URL = "https://tetris.com/play-tetris"


class Page:
    def __init__(self, browser=DRIVER):
        self.browser = self._browser_initialise(browser)

    @staticmethod
    def _browser_initialise(browser):
        """
        Initialise the browser.
        :param browser: The browser prior to being initialise.
        :return: The browser.
        """
        browser.get(URL)
        return browser

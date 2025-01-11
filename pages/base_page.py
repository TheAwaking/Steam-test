from selenium.webdriver.support.ui import WebDriverWait as Wait
from config_reader import ConfigReader


class BasePage:
    def __init__(self, driver, config_reader):
        self.driver = driver
        self.timeout = config_reader.get_value('timeout')
        self.base_url = config_reader.get_value('base_url')
        self.wait = Wait(driver, self.timeout)

    def open(self):
        self.driver.get(self.base_url)

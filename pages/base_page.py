from selenium.webdriver.support.ui import WebDriverWait as Wait
from config_reader import ConfigReader


class BasePage:
    def __init__(self, driver, config_reader):
        self.driver = driver
        self.timeout = config_reader.get_value('timeout')
        self.wait = Wait(driver, self.timeout)

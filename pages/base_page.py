from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    def __init__(self, driver, config_reader):
        self.driver = driver
        self.timeout = config_reader.get('timeout')
        self.wait = Wait(driver, self.timeout)


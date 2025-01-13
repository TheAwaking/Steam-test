from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    CHECK_PAGE = (By.XPATH, "//div[@class='label' and contains(text(), 'Sort')]")

    def __init__(self, driver):
        super().__init__(driver)

    def page_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.CHECK_PAGE))

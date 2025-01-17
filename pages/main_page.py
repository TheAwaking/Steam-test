from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):
    CHECK_PAGE = (By.XPATH, "//div[@class='label' and contains(text(), 'Sort')]")
    SEARCH_FIELD = (By.ID, "store_nav_search_term")

    def wait_if_page_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.CHECK_PAGE))
            return True
        except TimeoutException:
            return False

    def enter_game_name_and_search(self, game):
        search_field = self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELD))
        search_field.send_keys(game)
        search_field.send_keys(Keys.RETURN)

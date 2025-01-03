from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    SEARCH_FIELD = (By.ID, "store_nav_search_term")
    SORT_BY = (By.ID, "sort_by_trigger")
    FILTER_BY = (By.ID, "Price_ASC")
    CHECK_PAGE = (By.XPATH, "//div[@class='label' and contains(text(), 'Sort')]")
    SEARCH_RESULTS = (By.ID, "search_results_filtered_warning_persistent")


class TestMainPage(BasePage):
    def __init__(self, driver, config_reader):
        super().__init__(driver)
        self.base_url = config_reader.get('base_url')

    def open(self):
        self.driver.get(self.base_url)

    def page_displayed(self):
        self.wait.until(EC.visibility_of_element_located(Locators.CHECK_PAGE))

    def home_page(self, game):
        search_field = self.wait.until(EC.visibility_of_element_located(Locators.SEARCH_FIELD))
        search_field.send_keys(game)
        search_field.send_keys(Keys.RETURN)

    def sort_by_trigger(self):
        sort_by = self.wait.until(EC.element_to_be_clickable(Locators.SORT_BY))
        sort_by.click()

    def filter_by_trigger(self):
        filter_by = self.wait.until(EC.element_to_be_clickable(Locators.FILTER_BY))
        filter_by.click()

    def sort_displayed(self):
        self.wait.until(EC.visibility_of_element_located(Locators.SEARCH_RESULTS))

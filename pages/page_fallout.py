from locators.Locators_steam import Locators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    def test_page(self):
        search_field = self.is_visible(Locators.SEARCH_FIELD)
        search_field.send_keys('Fallout')
        search_field.send_keys(Keys.RETURN)

    def check_page(self):
        self.is_presence(Locators.SEARCH_FIELD)

    def sort_by_trigger(self):
        sort_by = self.is_clickable(Locators.SORT_BY)
        sort_by.click()

    def filter_by_trigger(self):
        filter_by = self.is_clickable(Locators.FILTER_BY)
        filter_by.click()

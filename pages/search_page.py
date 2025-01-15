from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re


class SearchPage(BasePage):
    SEARCH_FIELD = (By.ID, "store_nav_search_term")
    SORT_BY = (By.ID, "sort_by_trigger")
    FILTER_BY = (By.ID, "Price_ASC")
    CONTAINER = (By.XPATH, "//*[contains(@id, 'search_result_container') and contains(@style, 'opacity')]")
    SEARCH_RESULTS = (By.XPATH, "//*[@class='discount_final_price']")
    PRICES = (By.XPATH, "(//*[@class='discount_final_price'])[position() <= {n}]")

    def enter_game_name_and_search(self, game):
        search_field = self.wait.until(EC.visibility_of_element_located(self.SEARCH_FIELD))
        search_field.send_keys(game)
        search_field.send_keys(Keys.RETURN)

    def sort_by_trigger(self):
        sort_by = self.wait.until(EC.element_to_be_clickable(self.SORT_BY))
        sort_by.click()

    def checking_gray_screen(self):
        self.wait.until(EC.invisibility_of_element_located(self.CONTAINER))

    def filter_by_trigger(self):
        filter_by = self.wait.until(EC.element_to_be_clickable(self.FILTER_BY))
        filter_by.click()

    def sort_displayed(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_RESULTS))

    def sort_n_prices(self, n):
        price_element = self.wait.until(EC.presence_of_all_elements_located(self.PRICES)).format(n)
        prices = [price.text.strip() for price in price_element]
        return prices

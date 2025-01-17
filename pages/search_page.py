from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(BasePage):
    SORT_BY = (By.ID, "sort_by_trigger")
    FILTER_BY = (By.ID, "Price_ASC")
    CONTAINER = (By.XPATH, "//*[contains(@id, 'search_result_container') and contains(@style, 'opacity')]")
    SEARCH_RESULTS = (By.XPATH, "//*[@class='discount_final_price']")
    POSITION = (By.XPATH, "(//*[@class='discount_final_price'])[position() <= {n}]")
    PRICES = (By.XPATH, "//div[@class='discount_final_price' and contains(text(), '')]")

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

    def sort_n_positions(self, n):
        self.wait.until(EC.presence_of_all_elements_located(self.POSITION)).format(n)

    def sorted_prices(self):
        price_elements = self.wait.until(EC.presence_of_all_elements_located(self.PRICES))
        prices = []
        for element in price_elements:
            price_text = element.text.replace('руб', '').replace(' ', '').strip()
            price_value = float(price_text)
            prices.append(price_value)
        sorted_prices = sorted(prices)
        return sorted_prices


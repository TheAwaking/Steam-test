from selenium.webdriver.common.by import By


class Locators:
    SEARCH_FIELD = (By.ID, "store_nav_search_term")
    SORT_BY = (By.ID, "sort_by_trigger")
    FILTER_BY = (By.ID, "Price_ASC")
    CHECK_PAGE = (By.XPATH, "//div[@class='label' and contains(text(), 'Sort')]")

from tests.conftest import driver
from pages.page_the_witcher import MainPage
from pages.page_fallout import MainPage


class TestSearchPage:
    def test_search_for_game(self, driver):
        main_page = MainPage(driver, 'https://store.steampowered.com/')
        main_page.open()
        main_page.test_page()
        main_page.sort_by_trigger()
        main_page.filter_by_trigger()

    def test_search_for_another_game(self, driver):
        main_page = MainPage(driver, 'https://store.steampowered.com/')
        main_page.open()
        main_page.test_page()
        main_page.sort_by_trigger()
        main_page.filter_by_trigger()

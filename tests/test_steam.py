from tests.conftest import driver
from pages.main_page import MainPage
from pages.main_page import SearchPage
import pytest
from config_reader import ConfigReader

config_reader = ConfigReader('../config.json')


@pytest.mark.parametrize("game, n", [
    ("The Witcher", 10),
    ("Fallout", 20)
])
class TestSearchPage:
    def test_search_for_game(self, driver, game, n):
        base_url = config_reader.get_value(self)
        main_page = MainPage(driver, base_url)
        search_page = SearchPage(driver, base_url)
        main_page.open()
        assert main_page.page_displayed(), "page is not displayed"
        search_page.enter_game_name_and_search(game)
        search_page.sort_by_trigger()
        assert search_page.gray_screen(), "gray screen is visible"
        search_page.filter_by_trigger()
        assert search_page.sort_displayed(), "price is not displayed"



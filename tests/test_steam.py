from tests.conftest import driver
from pages.main_page import MainPage
from pages.search_page import SearchPage
import pytest
from config_reader import ConfigReader


@pytest.mark.parametrize("game, n", [
    ("The Witcher", 10),
    ("Fallout", 20)
])
class TestSearchPage:
    def __init__(self, config_path):
        self.config_reader = ConfigReader(config_path)

    def test_search_for_game(self, driver, game, n):
        base_url = self.config_reader.get_value('base_url')
        main_page = MainPage(driver, base_url)
        search_page = SearchPage(driver, base_url)
        assert main_page.page_displayed(), "page is not displayed"
        search_page.enter_game_name_and_search(game)
        search_page.sort_by_trigger()
        assert search_page.checking_gray_screen(), "gray screen is visible"
        assert search_page.sort_n_prices(n)
        assert search_page.filter_by_trigger(), "not sorted"
        assert search_page.sort_displayed(), "price is not displayed"

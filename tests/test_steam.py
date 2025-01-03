from tests.conftest import driver
from pages.page_the_witcher import TestMainPage
import pytest
from config_reader import ConfigReader

config_reader = ConfigReader('../config.json')


@pytest.mark.parametrize("game, n", [
    ("The Witcher", 10),
    ("Fallout", 20)
])
class TestSearchPage:
    def test_search_for_game(self, driver, game, n):
        base_url = config_reader.get_base_url()
        main_page = TestMainPage(driver, base_url)
        main_page.open()
        assert main_page.page_displayed()
        main_page.home_page()
        main_page.sort_by_trigger()
        main_page.filter_by_trigger()
        assert main_page.sort_displayed()
        search_result = main_page.home_page(game)
        assert search_result == game

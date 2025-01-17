from tests.conftest import driver
from pages.main_page import MainPage
from pages.search_page import SearchPage
import pytest


@pytest.mark.parametrize("game, n", [
    ("The Witcher", 10),
    ("Fallout", 20)
])
class TestSearchPage:

    def test_search_for_game(self, driver, config_reader, game, n):
        main_page = MainPage(driver, config_reader)
        search_page = SearchPage(driver, config_reader)
        assert main_page.wait_if_page_displayed(), "page is not displayed"
        main_page.enter_game_name_and_search(game)
        search_page.sort_by_trigger()
        search_page.checking_gray_screen()
        assert search_page.filter_by_trigger(), "not sorted"
        assert search_page.sort_displayed(), "price is not displayed"
        assert search_page.sort_n_positions(n), "sorting is not correct"
        search_page.sorted_prices()
        original_prices = search_page.sorted_prices()
        assert original_prices == sorted(original_prices), "price is not sorted"

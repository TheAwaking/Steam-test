from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    chrome_browser = webdriver.Chrome()
    chrome_browser.maximize_window()
    yield chrome_browser
    chrome_browser.quit()

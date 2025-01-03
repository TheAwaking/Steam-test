from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    chrome_browser = webdriver.Chrome()
    yield chrome_browser
    chrome_browser.quit()

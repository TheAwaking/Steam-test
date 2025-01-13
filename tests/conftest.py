import json
from selenium import webdriver
import pytest
from config_reader import ConfigReader


@pytest.fixture()
def driver():
    chrome_browser = webdriver.Chrome()
    yield chrome_browser
    chrome_browser.quit()


@pytest.fixture()
def open_url(driver):
    config_reader = ConfigReader('../config.json')
    url = config_reader.get_value("base_url")
    driver.get(url)

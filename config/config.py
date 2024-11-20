# config.py
import logging
import pytest
from selenium import webdriver

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Fixture for initializing the WebDriver (Chrome in this case)
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver

def test_basic_auth(driver):
    # Use the URL with embedded credentials to bypass the Basic Auth prompt
    username = "admin"
    password = "admin"
    url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"

    # Open the page directly with the credentials embedded in the URL
    driver.get(url)

    # Wait for the page to load and verify authentication was successful
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    assert "Congratulations" in driver.page_source
    print("Basic Authentication test passed successfully!")


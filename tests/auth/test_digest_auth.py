import requests
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver

def test_digest_auth(driver):
    # URL for Digest Authentication
    url = "https://the-internet.herokuapp.com/digest_auth"

    # Navigate to the Digest Auth URL
    auth_url = f"https://admin:admin@the-internet.herokuapp.com/digest_auth"
    driver.get(auth_url)

    # Wait until the page is loaded and check if the element that confirms the login is present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))

    # Verify that the authentication was successful (e.g., check for the "Congratulations" message)
    assert "Congratulations" in driver.page_source
    logger.info("Digest Authentication test passed successfully!")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver
import pytest


def test_status_codes(driver):
    # Go to the status codes page
    driver.get("https://the-internet.herokuapp.com/status_codes")

    # List of status code links
    status_codes = ["200", "301", "404", "500"]

    for code in status_codes:
        # Find the link corresponding to the status code
        link = driver.find_element(By.LINK_TEXT, code)
        logger.info(f"Clicking on status code: {code}")

        # Click the link to navigate to the status code page
        link.click()

        # Wait for the URL to change to the expected status code page
        WebDriverWait(driver, 10).until(
            EC.url_contains(f"status_codes/{code}")
        )
        logger.info(f"Page URL is now: {driver.current_url}")

        # Check for the correct status code message in the page body
        page_body = driver.find_element(By.TAG_NAME, "body").text
        logger.info(f"Page body: {page_body}")

        # Verify the correct status code message is present in the body
        expected_message = f"This page returned a {code} status code."
        assert expected_message in page_body, f"Expected message '{expected_message}' in body, but got: {page_body}"

        # Log the successful test for the current status code
        logger.info(f"Status code {code} test passed.")

        # Navigate back to the status codes page to test the next link
        driver.back()

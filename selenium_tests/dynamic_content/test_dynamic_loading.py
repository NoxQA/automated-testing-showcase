import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver


def test_dynamic_loading(driver):
    """
    Test to verify dynamically loaded page elements.
    Covers two examples:
    1. An element that is hidden and becomes visible.
    2. An element that is not present initially and gets rendered after an action.
    """
    base_url = "https://the-internet.herokuapp.com/dynamic_loading"

    # Helper function to handle loading and visibility checks
    def verify_loading_and_content(example_number, expected_text):
        try:
            # Construct URL for the example
            page_url = f"{base_url}/{example_number}"

            # Navigate to the page
            driver.get(page_url)
            logger.info(f"Navigated to: {page_url}")

            # Locate and click the 'Start' button
            start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
            start_button.click()
            logger.info(f"Clicked 'Start' button for Example {example_number}.")

            # Wait for the loading to complete by checking for visibility of result text
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
            )

            # Verify the expected text is displayed
            result_text = driver.find_element(By.CSS_SELECTOR, "#finish h4").text
            assert result_text == expected_text, f"Expected '{expected_text}', but got '{result_text}'."
            logger.info(f"Example {example_number} loaded successfully with text: {result_text}")

        except Exception as e:
            logger.error(f"An error occurred in Example {example_number}: {str(e)}")
            raise

    # Test for Example 1: Element on the page that is hidden
    verify_loading_and_content(1, "Hello World!")

    # Test for Example 2: Element rendered after the fact
    verify_loading_and_content(2, "Hello World!")

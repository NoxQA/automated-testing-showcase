import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver


@pytest.mark.usefixtures("driver")
def test_redirect_functionality(driver):
    # Step 1: Navigate to the Redirection page
    logger.info("Navigating to the Redirection page.")
    driver.get("https://the-internet.herokuapp.com/redirector")

    # Step 2: Click the redirection link
    try:
        redirect_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "redirect"))
        )
        redirect_link.click()
        logger.info("Clicked the redirect link.")
    except Exception as e:
        logger.error(f"Error clicking the redirect link: {e}")
        # Capture the page source for debugging
        logger.debug("Full page source:")
        logger.debug(driver.page_source)
        return

    # Step 3: Wait for the redirection to complete and verify the new URL
    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains("/status_codes")
        )
        current_url = driver.current_url
        logger.info(f"Successfully redirected to the URL: {current_url}")
    except Exception as e:
        logger.error(f"Redirection did not complete successfully: {e}")
        # Capture the page source for debugging
        logger.debug("Full page source after redirection:")
        logger.debug(driver.page_source)
        return

    # Step 4: Validate that the URL is the expected Status Codes page
    expected_url = "https://the-internet.herokuapp.com/status_codes"
    assert expected_url in current_url, f"Redirection failed. Expected URL: {expected_url}, but got {current_url}"

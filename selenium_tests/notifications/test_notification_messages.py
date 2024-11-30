import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import logger, driver  # Adjust imports as necessary
import time


def test_notification_message(driver):
    logger.info("Navigating to the Notification Message page.")
    driver.get("https://the-internet.herokuapp.com/notification_message_rendered")

    # Sleep for a moment to ensure the page is fully loaded
    time.sleep(3)

    # Click the hyperlink to trigger the notification
    try:
        trigger_link = driver.find_element(By.LINK_TEXT, "Click here")
        trigger_link.click()
        logger.info("Clicked the hyperlink to trigger the notification.")
    except Exception as e:
        logger.error(f"Error clicking the hyperlink: {e}")
        return

    # Wait for the notification element to become visible in the DOM
    def get_notification_text():
        try:
            # Wait until the notification element is present and visible
            notification_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "flash"))
            )
            logger.debug(f"Notification element HTML: {notification_element.get_attribute('outerHTML')}")
            return notification_element.text.strip()
        except Exception as e:
            logger.error(f"Notification element is not visible or not present in the DOM: {e}")
            # Capture the page source for debugging
            logger.debug("Full page source:")
            logger.debug(driver.page_source)
            return None

    # Retrieve the notification message
    initial_message = get_notification_text()
    if initial_message is None:
        logger.error("Initial notification message retrieval failed.")

    # Assert the initial message retrieval
    assert initial_message is not None, "Initial notification message could not be retrieved."




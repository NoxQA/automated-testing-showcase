import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver
import time

def test_infinite_scroll(driver):
    # Step 1: Open the Infinite Scroll page
    logger.info("Opening Infinite Scroll page.")
    driver.get("https://the-internet.herokuapp.com/infinite_scroll")

    # Step 2: Get the initial number of content elements
    initial_content = driver.find_elements(By.CLASS_NAME, "jscroll-added")
    initial_content_count = len(initial_content)
    logger.info(f"Initial content count: {initial_content_count}")

    # Step 3: Scroll until new content is loaded
    scroll_attempts = 3  # Adjust the number of scrolls if needed
    for attempt in range(scroll_attempts):
        logger.info(f"Scroll attempt {attempt + 1}/{scroll_attempts}")

        # Step 4: Scroll to the bottom of the page to trigger loading of new content
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Step 5: Wait for a moment for new content to load
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jscroll-added"))
        )

        # Optionally wait a bit more to ensure the content is fully loaded
        time.sleep(2)

    # Step 6: Verify that new content has loaded
    new_content = driver.find_elements(By.CLASS_NAME, "jscroll-added")
    new_content_count = len(new_content)
    logger.info(f"New content count after scrolling: {new_content_count}")

    # Assert that the new content count is greater than the initial count
    assert new_content_count > initial_content_count, "Content did not load after scrolling."

    logger.info("Infinite Scroll test passed successfully.")

import pytest
from selenium.webdriver.common.by import By
from config.config import logger, driver
import time

def test_dynamic_content(driver):
    """
    Test to verify the dynamic content changes on each page load.
    This includes both the text and images displayed on the page.
    """
    # Define the URL of the dynamic content page
    page_url = "https://the-internet.herokuapp.com/dynamic_content"

    try:
        # Navigate to the dynamic content page
        driver.get(page_url)
        logger.info(f"Navigated to the page: {page_url}")

        # Capture initial content (images and text)
        initial_images = [img.get_attribute("src") for img in driver.find_elements(By.CSS_SELECTOR, ".example img")]
        initial_texts = [element.text for element in driver.find_elements(By.CSS_SELECTOR, ".large-10.columns")]

        logger.info(f"Initial Images: {initial_images}")
        logger.info(f"Initial Texts: {initial_texts}")

        # Refresh the page to see if the content changes
        driver.refresh()
        time.sleep(2)  # Adding a slight delay to ensure the page loads new content

        # Capture new content after the page refresh
        new_images = [img.get_attribute("src") for img in driver.find_elements(By.CSS_SELECTOR, ".example img")]
        new_texts = [element.text for element in driver.find_elements(By.CSS_SELECTOR, ".large-10.columns")]

        logger.info(f"New Images: {new_images}")
        logger.info(f"New Texts: {new_texts}")

        # Check if content (either images or texts) changed after the refresh
        content_changed = (initial_images != new_images) or (initial_texts != new_texts)
        assert content_changed, "Dynamic content did not change after page refresh"
        logger.info("Dynamic content test passed: Content changed after page refresh.")

    except Exception as e:
        logger.error(f"An error occurred during the dynamic content test: {str(e)}")

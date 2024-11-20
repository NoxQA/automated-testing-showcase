import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver  # Make sure to import the logger from config.py


@pytest.mark.run(order=3)
def test_add_or_remove_elements(driver):
    logger.info("Navigating to the Add or Remove Elements Testing page...")
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    # Log the current page URL to ensure you're on the right page
    logger.info(f"Current URL: {driver.current_url}")

    # Wait until the 'Add Element' button is clickable and click it
    logger.info("Waiting for 'Add Element' button to be clickable...")
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Element']"))
    )
    logger.info("'Add Element' button found, clicking it...")
    add_button.click()

    # Log the state after clicking
    logger.info("Clicking the 'Delete' button on the newly added element...")

    # Wait for the delete button to be clickable and click it
    delete_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "added-manually"))
    )
    logger.info("'Delete' button found, clicking it...")
    delete_button.click()

    logger.info("Add/Remove elements test passed successfully!")

    # Adding a small delay to keep the browser open for observation
    logger.info("Pausing for 5 seconds to allow you to observe the browser...")
    time.sleep(5)  # You can adjust the time as needed

    # Log the state of the page after the actions
    logger.info(f"Current URL after interaction: {driver.current_url}")

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver


def test_dynamic_controls(driver):
    """
    Test to verify the functionality of dynamic controls.
    This includes adding/removing a checkbox and enabling/disabling an input field.
    """
    # Define the URL of the dynamic controls page
    page_url = "https://the-internet.herokuapp.com/dynamic_controls"

    try:
        # Navigate to the dynamic controls page
        driver.get(page_url)
        logger.info(f"Navigated to the page: {page_url}")

        # Remove/Add Checkbox Test
        checkbox_button = driver.find_element(By.CSS_SELECTOR, "#checkbox-example button")
        checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox input")

        # Remove the checkbox
        checkbox_button.click()
        logger.info("Clicked 'Remove' button for checkbox.")

        # Wait for the checkbox to be removed and check for the confirmation message
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "message"), "It's gone!")
        )
        logger.info("Checkbox removed successfully.")

        # Add the checkbox back
        checkbox_button.click()
        logger.info("Clicked 'Add' button for checkbox.")

        # Wait for the checkbox to be added back and check for the confirmation message
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "message"), "It's back!")
        )
        logger.info("Checkbox added successfully.")

        # Enable/Disable Input Field Test
        input_button = driver.find_element(By.CSS_SELECTOR, "#input-example button")
        input_field = driver.find_element(By.CSS_SELECTOR, "#input-example input")

        # Enable the input field
        input_button.click()
        logger.info("Clicked 'Enable' button for input field.")

        # Wait for the input field to be enabled and check the confirmation message
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "message"), "It's enabled!")
        )
        assert input_field.is_enabled(), "Input field is not enabled."
        logger.info("Input field enabled successfully.")

        # Disable the input field
        input_button.click()
        logger.info("Clicked 'Disable' button for input field.")

        # Wait for the input field to be disabled and check the confirmation message
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "message"), "It's disabled!")
        )
        assert not input_field.is_enabled(), "Input field is not disabled."
        logger.info("Input field disabled successfully.")

    except Exception as e:
        logger.error(f"An error occurred during the dynamic controls test: {str(e)}")
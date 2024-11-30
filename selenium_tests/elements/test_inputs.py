import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config.config import logger, driver


def test_input_number_field(driver):
    # Step 1: Open the Inputs page
    logger.info("Opening Inputs page.")
    driver.get("https://the-internet.herokuapp.com/inputs")

    # Step 2: Locate the number input field
    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

    # Step 3: Enter a number into the input field
    input_value = 42  # Example number to enter
    logger.info(f"Entering the number {input_value} into the input field.")
    input_field.clear()  # Clear any existing value in the input field
    input_field.send_keys(input_value)  # Enter the number

    # Step 4: Verify that the value is correctly entered
    entered_value = input_field.get_attribute("value")
    logger.info(f"Entered value is {entered_value}.")

    # Assert that the entered value matches the expected value
    assert entered_value == str(input_value), f"Expected value '{input_value}', but got '{entered_value}'."

    logger.info("Input number test passed successfully.")

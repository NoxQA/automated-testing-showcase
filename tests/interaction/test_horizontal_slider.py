import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver


def test_horizontal_slider(driver):
    # Step 1: Open the Horizontal Slider page
    logger.info("Opening Horizontal Slider page.")
    driver.get("https://the-internet.herokuapp.com/horizontal_slider")

    # Step 2: Locate the slider input element and the value span element
    slider = driver.find_element(By.CSS_SELECTOR, "input[type='range']")
    range_value = driver.find_element(By.ID, "range")

    # Step 3: Click on the slider to focus it
    logger.info("Clicking on the slider to focus it.")
    slider.click()

    # Step 4: Store the initial value of the slider
    initial_value = range_value.text
    logger.info(f"Initial value of slider: {initial_value}")

    # Step 5: Move the slider forward (right arrow to increase)
    logger.info("Using the right arrow key to move the slider forward.")
    slider.send_keys(Keys.ARROW_RIGHT)

    # Step 6: Wait for the value to change after moving forward
    WebDriverWait(driver, 3).until(
        lambda driver: range_value.text != initial_value
    )

    new_value = range_value.text
    logger.info(f"Slider value after moving forward: {new_value}")

    # Ensure the value has changed (not the same as initial value)
    assert new_value != initial_value, f"Expected value to change, but got {new_value}"

    # Step 7: Store the value after moving forward
    value_after_forward = new_value

    # Step 8: Move the slider backward (left arrow to decrease)
    logger.info("Using the left arrow key to move the slider backward.")
    slider.send_keys(Keys.ARROW_LEFT)

    # Step 9: Wait for the value to change again after moving backward
    WebDriverWait(driver, 3).until(
        lambda driver: range_value.text != value_after_forward
    )
    new_value = range_value.text
    logger.info(f"Slider value after moving backward: {new_value}")

    # Ensure the value has decreased (not the same as after moving forward)
    assert new_value != value_after_forward, f"Expected value to change, but got {new_value}"

    logger.info("Horizontal Slider test passed successfully.")

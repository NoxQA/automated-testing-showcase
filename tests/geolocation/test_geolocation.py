import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver  # Import logger and driver from config

# Test for Geolocation functionality
def test_geolocation(driver):
    # Step 1: Open the Geolocation page
    logger.info("Opening Geolocation page.")
    driver.get("https://the-internet.herokuapp.com/geolocation")

    # Step 2: Click the "Where am I?" button
    logger.info("Clicking the 'Where am I?' button.")
    button = driver.find_element(By.XPATH, "//button[contains(text(), 'Where am I?')]")
    button.click()

    # Step 3: Wait for the latitude and longitude to be displayed
    logger.info("Waiting for the geolocation data to appear.")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lat-value")))

    # Step 4: Get the latitude and longitude values
    latitude = driver.find_element(By.ID, "lat-value").text
    longitude = driver.find_element(By.ID, "long-value").text

    # Log the retrieved values
    logger.info(f"Latitude: {latitude}")
    logger.info(f"Longitude: {longitude}")

    # Step 5: Assert the values to ensure they match the expected geolocation
    assert latitude == "42.1593088", f"Expected latitude 42.1593088 but got {latitude}"
    assert longitude == "24.7496704", f"Expected longitude 24.7496704 but got {longitude}"

    logger.info("Geolocation test passed successfully.")
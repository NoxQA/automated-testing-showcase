from selenium.webdriver.common.by import By
import requests
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


def test_context_menu(driver):
    # Step 1: Navigate to the Context Menu page
    url = "https://the-internet.herokuapp.com/context_menu"
    logger.info(f"Navigating to {url}")
    driver.get(url)

    # Step 2: Locate the element where we need to right-click
    hotspot = driver.find_element(By.ID, "hot-spot")

    # Step 3: Perform a right-click action (context click) on the element
    logger.info("Right-clicking on the hotspot...")
    action = ActionChains(driver)
    action.context_click(hotspot).perform()

    # Step 4: Wait for the alert to appear
    time.sleep(2)  # Sleep to allow time for the alert to appear (better to use WebDriverWait in production)

    # Step 5: Switch to the alert and verify its text
    alert = Alert(driver)
    alert_text = alert.text
    logger.info(f"Alert text: {alert_text}")

    # Verify if the alert text is correct
    assert alert_text == "You selected a context menu", f"Expected alert text 'You selected a context menu', but got '{alert_text}'."

    # Step 6: Accept the alert
    alert.accept()
    logger.info("Alert accepted.")
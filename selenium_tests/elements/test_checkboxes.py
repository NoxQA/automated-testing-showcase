import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver

def test_checkboxes(driver):
    logger.info("Navigating to the Checkboxes Testing page...")
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # Step 2: Verify the initial state of the checkboxes
    checkbox_1 = driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
    checkbox_2 = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]")

    # Check the initial state of checkbox 1
    assert not checkbox_1.is_selected(), "Checkbox 1 should be unchecked initially."
    logger.info("Checkbox 1 is unchecked initially.")

    # Check the initial state of checkbox 2
    assert checkbox_2.is_selected(), "Checkbox 2 should be checked initially."
    logger.info("Checkbox 2 is checked initially.")

    # Step 3: Check checkbox 1 if it is unchecked
    if not checkbox_1.is_selected():
        logger.info("Checking Checkbox 1...")
        checkbox_1.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_selected(checkbox_1))
        logger.info("Checkbox 1 is checked.")

    # Step 4: Uncheck checkbox 2 if it is checked
    if checkbox_2.is_selected():
        logger.info("Unchecking Checkbox 2...")
        checkbox_2.click()
        # Wait for checkbox 2 to be unchecked
        WebDriverWait(driver, 10).until(lambda driver: not checkbox_2.is_selected())
        logger.info("Checkbox 2 is unchecked.")

    # Step 5: Verify the state after interacting with both checkboxes
    assert checkbox_1.is_selected(), "Checkbox 1 should be checked."
    logger.info("Verified Checkbox 1 is checked.")

    assert not checkbox_2.is_selected(), "Checkbox 2 should be unchecked."
    logger.info("Verified Checkbox 2 is unchecked.")

    # Step 6: Recheck checkbox 1 if it is unchecked
    if not checkbox_1.is_selected():
        logger.info("Rechecking Checkbox 1...")
        checkbox_1.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_selected(checkbox_1))
        logger.info("Checkbox 1 is rechecked.")

    # Step 7: Check checkbox 2 if it is unchecked
    if not checkbox_2.is_selected():
        logger.info("Checking Checkbox 2...")
        checkbox_2.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_selected(checkbox_2))
        logger.info("Checkbox 2 is checked.")

    # Step 8: Verify the final state after rechecking/unchecking
    assert checkbox_1.is_selected(), "Checkbox 1 should be checked after rechecking."
    logger.info("Verified Checkbox 1 is checked.")

    assert checkbox_2.is_selected(), "Checkbox 2 should be checked after rechecking."
    logger.info("Verified Checkbox 2 is checked.")
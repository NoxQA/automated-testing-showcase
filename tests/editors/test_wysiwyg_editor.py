import pytest
from config.config import logger, driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_tinymce_editor(driver):
    logger.info("Test started")

    # Navigate to the TinyMCE page
    driver.get('https://the-internet.herokuapp.com/tinymce')
    logger.info("Navigated to the TinyMCE page")

    # Locate the TinyMCE iframe
    iframe = driver.find_element(By.ID, "mce_0_ifr")

    # Switch to the iframe where the TinyMCE editor is located
    driver.switch_to.frame(iframe)

    # Locate the body of the TinyMCE editor
    editor_body = driver.find_element(By.CSS_SELECTOR, "body")

    # Clear any existing content in the editor and type new text
    editor_body.clear()  # Clear any pre-existing content
    editor_body.send_keys("Hello, TinyMCE!")

    # Now check if the text entered exists in the editor (validation)
    entered_text = editor_body.text
    assert "Hello, TinyMCE!" == entered_text, f"Expected 'Hello, TinyMCE!' but got {entered_text}"

    logger.info("Text was entered successfully into the editor.")

    # Clean up after the test
    driver.quit()
    logger.info("Test finished and browser closed")

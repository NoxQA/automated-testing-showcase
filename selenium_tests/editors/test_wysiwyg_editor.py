import pytest
from config.config import logger, driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_tinymce_editor(driver):
    logger.info("Test started")

    driver.get('https://the-internet.herokuapp.com/tinymce')
    logger.info("Navigated to the TinyMCE page")

    iframe = driver.find_element(By.ID, "mce_0_ifr")

    driver.switch_to.frame(iframe)

    editor_body = driver.find_element(By.CSS_SELECTOR, "body")

    editor_body.clear()  # Clear any pre-existing content
    editor_body.send_keys("Hello, TinyMCE!")

    entered_text = editor_body.text
    assert "Hello, TinyMCE!" == entered_text, f"Expected 'Hello, TinyMCE!' but got {entered_text}"

    logger.info("Text was entered successfully into the editor.")

    driver.quit()
    logger.info("Test finished and browser closed")

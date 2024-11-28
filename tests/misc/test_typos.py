from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver
import pytest


def test_typos(driver):
    # Go to the typos page
    driver.get("https://the-internet.herokuapp.com/typos")

    # Wait until the page content is loaded and visible
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "p"))
    )

    # Get the text of the second paragraph, which contains the typo
    page_text = driver.find_element(By.XPATH, "//div[@id='content']//p[2]").text
    logger.info(f"Page text: {page_text}")

    # Check if the typo "won,t" is present in the text
    assert "won,t" in page_text, f"Expected typo 'won,t' not found in page text: {page_text}"

    # Log success
    logger.info("Test passed: Typo found in the text.")

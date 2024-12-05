from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure
import pytest


def test_typos(driver):
    driver.get("https://the-internet.herokuapp.com/typos")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "p"))
    )

    page_text = driver.find_element(By.XPATH, "//div[@id='content']//p[2]").text
    logger.info(f"Page text: {page_text}")

    assert "won,t" in page_text, f"Expected typo 'won,t' not found in page text: {page_text}"

    logger.info("Test passed: Typo found in the text.")

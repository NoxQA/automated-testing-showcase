import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure  # Adjust imports as necessary


@pytest.mark.usefixtures("driver")
def test_large_and_deep_dom(driver):
    logger.info("Navigating to the Large & Deep DOM page.")
    driver.get("https://the-internet.herokuapp.com/large")

    logger.info("Verifying the 'No Siblings' section.")
    no_siblings_element = driver.find_element(By.ID, "no-siblings")
    assert no_siblings_element.is_displayed(), "'No Siblings' section is not visible"
    assert no_siblings_element.text == "No siblings", "'No Siblings' text is incorrect"

    logger.info("Verifying the 'Siblings' section.")

    for i in range(1, 6):
        sibling_id = f"sibling-{i}.{i}"
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, sibling_id)))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, sibling_id)))

            sibling = driver.find_element(By.ID, sibling_id)
            assert sibling.is_displayed(), f"Sibling {i}.{i} is not visible"
            logger.info(f"Sibling {i}.{i} is visible.")

        except Exception as e:
            logger.error(f"Error finding or verifying {sibling_id}: {e}")
            continue

    logger.info("Verifying the large table headers and first few columns.")
    for i in range(1, 6):
        try:
            header = driver.find_element(By.ID, f"header-{i}")
            assert header.is_displayed(), f"Header {i} is not visible"
            assert header.text.strip() == str(i), f"Header {i} text is incorrect"
            logger.info(f"Header {i} is visible and correct.")
        except Exception as e:
            logger.error(f"Error finding header {i}: {e}")
            continue

    logger.info("Verifying the first few rows of the table.")
    for row in range(1, 6):
        for col in range(1, 6):
            cell_selector = f".row-{row} .column-{col}"
            try:
                cell = driver.find_element(By.CSS_SELECTOR, cell_selector)
                assert cell.is_displayed(), f"Cell in row {row}, column {col} is not visible"
                expected_text = f"{row}.{col}"
                assert cell.text.strip() == expected_text, f"Cell in row {row}, column {col} text is incorrect (expected {expected_text}, got {cell.text.strip()})"
                logger.info(f"Cell in row {row}, column {col} is correct.")
            except Exception as e:
                logger.error(f"Error finding or verifying cell at row {row}, column {col}: {e}")
                continue

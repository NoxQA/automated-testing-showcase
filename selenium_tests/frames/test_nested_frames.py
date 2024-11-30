import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver  # Adjust imports as necessary

@pytest.mark.usefixtures("driver")
def test_nested_frames(driver):
    # Step 1: Navigate to the Nested Frames page
    logger.info("Navigating to the Nested Frames page.")
    driver.get("https://the-internet.herokuapp.com/nested_frames")

    # Step 2: Switch to the 'frame-top' and verify its content
    logger.info("Switching to the 'frame-top'.")
    driver.switch_to.frame("frame-top")

    # Step 3: Switch to the 'frame-left' and verify content
    try:
        logger.info("Switching to the 'frame-left'.")
        driver.switch_to.frame("frame-left")
        left_content = driver.find_element(By.TAG_NAME, "body").text
        assert "LEFT" in left_content, "Content of 'frame-left' is incorrect."
        logger.info("Content of 'frame-left' verified.")
    except Exception as e:
        logger.error(f"Error in 'frame-left': {e}")
        raise AssertionError("Error verifying content in 'frame-left'.")
    finally:
        # Go back to 'frame-top' level
        driver.switch_to.parent_frame()

    # Step 4: Switch to the 'frame-middle' and verify content
    try:
        logger.info("Switching to the 'frame-middle'.")
        driver.switch_to.frame("frame-middle")
        middle_content = driver.find_element(By.ID, "content").text
        assert "MIDDLE" in middle_content, "Content of 'frame-middle' is incorrect."
        logger.info("Content of 'frame-middle' verified.")
    except Exception as e:
        logger.error(f"Error in 'frame-middle': {e}")
        raise AssertionError("Error verifying content in 'frame-middle'.")
    finally:
        # Go back to 'frame-top' level
        driver.switch_to.parent_frame()

    # Step 5: Switch to the 'frame-right' and verify content
    try:
        logger.info("Switching to the 'frame-right'.")
        driver.switch_to.frame("frame-right")
        right_content = driver.find_element(By.TAG_NAME, "body").text
        assert "RIGHT" in right_content, "Content of 'frame-right' is incorrect."
        logger.info("Content of 'frame-right' verified.")
    except Exception as e:
        logger.error(f"Error in 'frame-right': {e}")
        raise AssertionError("Error verifying content in 'frame-right'.")
    finally:
        # Go back to the main page (exit frames)
        driver.switch_to.default_content()

    # Step 6: Switch to the 'frame-bottom' and verify content
    try:
        logger.info("Switching to the 'frame-bottom'.")
        driver.switch_to.frame("frame-bottom")
        bottom_content = driver.find_element(By.TAG_NAME, "body").text
        assert "BOTTOM" in bottom_content, "Content of 'frame-bottom' is incorrect."
        logger.info("Content of 'frame-bottom' verified.")
    except Exception as e:
        logger.error(f"Error in 'frame-bottom': {e}")
        raise AssertionError("Error verifying content in 'frame-bottom'.")
    finally:
        # Go back to the main page (exit frames)
        driver.switch_to.default_content()

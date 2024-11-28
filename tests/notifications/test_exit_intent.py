import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver

@pytest.mark.parametrize("page_url", ["https://the-internet.herokuapp.com/exit_intent"])
def test_exit_intent_modal(driver, page_url):
    """
    Test the behavior of the Exit Intent modal on mouseout.
    """

    try:
        # Step 1: Navigate to the Exit Intent page
        driver.get(page_url)
        logger.info(f"Navigated to: {page_url}")

        # Step 2: Wait for the modal to be hidden initially (because it should not be visible yet)
        try:
            modal = WebDriverWait(driver, 5).until(
                EC.invisibility_of_element_located((By.ID, "ouibounce-modal"))
            )
            logger.info("Exit Intent modal is initially invisible.")
        except Exception:
            logger.error("Exit Intent modal is unexpectedly visible on page load.")
            pytest.fail("Modal should not be visible on page load.")

        # Step 3: Simulate mouseout (moving the mouse out of the viewport)
        driver.execute_script("window.scrollTo(0, 0);")  # Ensure we're at the top of the page
        logger.info("Simulated mouse out of viewport.")

        # Step 4: Wait for the modal to appear (increased wait time)
        try:
            modal = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "ouibounce-modal"))
            )
            logger.info("Exit Intent modal appeared.")
        except Exception as e:
            logger.error(f"Modal failed to appear: {str(e)}")
            pytest.fail(f"Modal did not appear after mouse out event: {str(e)}")

        # Step 5: Close the modal by clicking the 'Close' button
        close_button = driver.find_element(By.CSS_SELECTOR, "#ouibounce-modal .modal-footer p")
        close_button.click()
        logger.info("Closed the exit intent modal.")

        # Step 6: Verify that the modal does not reappear
        try:
            # Reload the page to simulate a fresh session
            driver.refresh()
            WebDriverWait(driver, 5).until(
                EC.invisibility_of_element_located((By.ID, "ouibounce-modal"))
            )
            logger.info("Exit Intent modal is invisible after page reload. Test passed.")
        except Exception:
            logger.error("Exit Intent modal appeared again after page reload unexpectedly.")
            pytest.fail("Exit Intent modal should not reappear after being closed.")

    except Exception as e:
        logger.error(f"An error occurred during the Exit Intent test: {str(e)}")
        pytest.fail(f"Test failed due to: {str(e)}")
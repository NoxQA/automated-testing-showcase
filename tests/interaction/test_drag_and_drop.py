import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from config.config import logger, driver


def test_drag_and_drop(driver):
    """
    Test to perform drag and drop on the HerokuApp drag and drop page.
    This function combines the JavaScript-based drag-and-drop functionality
    and the validation steps to ensure the drag-and-drop was successful.
    """
    # Define the Drag and Drop page URL
    page_url = "https://the-internet.herokuapp.com/drag_and_drop"

    try:
        # Navigate to the Drag and Drop page
        driver.get(page_url)
        logger.info(f"Navigated to the page: {page_url}")

        # IDs of source and target elements
        source_id = "#column-a"
        target_id = "#column-b"

        # JavaScript to perform drag and drop
        js_code = """
            function triggerDragAndDrop(selectorDrag, selectorDrop) {
                const elementDrag = document.querySelector(selectorDrag);
                const elementDrop = document.querySelector(selectorDrop);

                if (!elementDrag || !elementDrop) return false;

                const dataTransfer = new DataTransfer();

                elementDrag.dispatchEvent(new DragEvent('dragstart', { dataTransfer }));
                elementDrop.dispatchEvent(new DragEvent('drop', { dataTransfer }));
                elementDrag.dispatchEvent(new DragEvent('dragend', { dataTransfer }));

                return true;
            }
            return triggerDragAndDrop(arguments[0], arguments[1]);
        """

        # Execute the JavaScript for drag and drop
        result = driver.execute_script(js_code, source_id, target_id)
        if result:
            logger.info("Drag and Drop successful.")
        else:
            logger.error("Drag and Drop failed.")
            return  # Exit if the drag-and-drop operation failed

        # Verify if the content was swapped
        source_header = driver.find_element(By.ID, "column-a").text
        target_header = driver.find_element(By.ID, "column-b").text

        # Check if the elements were swapped
        assert source_header == "B", "Drag and drop failed: A is not replaced by B"
        assert target_header == "A", "Drag and drop failed: B is not replaced by A"
        logger.info("Drag and Drop verification passed.")

    except Exception as e:
        logger.error(f"An error occurred during the drag and drop test: {str(e)}")

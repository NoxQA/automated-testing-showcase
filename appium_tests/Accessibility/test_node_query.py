import pytest
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.options.android import UiAutomator2Options
from config.appium_config import logger, enable_talkback, disable_talkback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TestAccessibility:
    """Test suite for accessibility features."""

    def test_open_accessibility_menu(self, appium_driver, wait):
        """Open the Accessibility menu."""
        logger.info("Starting test: Open Accessibility Menu")

        try:
            accessibility_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Accessibility']"))
            )
            assert accessibility_element.is_displayed(), "Accessibility menu item not displayed"
            logger.info("Accessibility menu item found and displayed")
            accessibility_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_open_accessibility_node_provider(self, appium_driver, wait):
        """Open the Accessibility Node Querying screen."""
        logger.info("Starting test: Open Accessibility Node Querying")

        try:
            node_provider_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Accessibility Node Querying']"))
            )
            assert node_provider_element.is_displayed(), "Accessibility Node Querying menu item not displayed"
            logger.info("Accessibility Node Querying menu item found and displayed")
            node_provider_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_title_text(self, appium_driver, wait):
        """Verify the title text on the Accessibility Node Querying screen."""
        logger.info("Starting test: Verify Title Text")

        try:
            title_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Accessibility/Accessibility Node Querying']"))
            )
            assert title_element.is_displayed(), "Title text not displayed"
            assert title_element.text == "Accessibility/Accessibility Node Querying", "Title text mismatch"
            logger.info(f"Title text verified: {title_element.text}")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_instruction_text(self, appium_driver, wait):
        """Verify instruction text and its content description."""
        logger.info("Starting test: Verify Instruction Text")

        try:
            instruction_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Enable QueryBack')]"))
            )
            assert instruction_element.is_displayed(), "Instruction text not displayed"
            content_desc = instruction_element.get_attribute("content-desc")
            assert content_desc == instruction_element.text, "Content description mismatch"
            logger.info(f"Instruction text verified: {instruction_element.text}, Content-desc: {content_desc}")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_interaction_with_task_list(self, appium_driver, wait):
        """Test interaction with task list items."""
        logger.info("Starting test: Interaction with Task List")

        try:
            task_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Take out Trash']"))
            )
            assert task_element.is_displayed(), "Task item not displayed"
            logger.info("Task item found and displayed")

            task_element.click()
            sleep(2)
            task_checkbox = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.CheckBox[@resource-id='io.appium.android.apis:id/tasklist_finished']"))
            )
            assert task_checkbox.is_displayed(), "Task checkbox not displayed"
            logger.info("Task checkbox found and displayed")
            task_checkbox.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_navigation_to_next_task(self, appium_driver, wait):
        """Navigate to the next task in the list."""
        logger.info("Starting test: Navigate to Next Task")

        try:
            next_task_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Do Laundry']"))
            )
            assert next_task_element.is_displayed(), "Next task item not displayed"
            logger.info("Next task item found and displayed")

            next_task_element.click()
            sleep(2)
            next_task_checkbox = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.CheckBox[@resource-id='io.appium.android.apis:id/tasklist_finished']"))
            )
            assert next_task_checkbox.is_displayed(), "Next task checkbox not displayed"
            logger.info("Next task checkbox found and displayed")
            next_task_checkbox.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise
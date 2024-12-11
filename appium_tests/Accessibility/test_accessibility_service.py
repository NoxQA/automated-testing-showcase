import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.appium_config import logger
from time import sleep


class TestAccessibilityService:
    """Test suite for Accessibility/Accessibility Service page."""

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

    def test_accessibility_service(self, appium_driver, wait):
        """Open the Accessibility Service screen."""
        logger.info("Starting test: Open Accessibility Service")

        try:
            accessibility_service_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Accessibility Service']"))
            )
            assert accessibility_service_element(), "Accessibility Service menu item not displayed"
            logger.info("Accessibility Service menu item found and displayed")
            accessibility_service_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_title_text(self, appium_driver, wait):
        """Verify the title text on the Accessibility Service page."""
        logger.info("Starting test: Verify Title Text")

        try:
            title_element = wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, "//android.widget.TextView[@text='Accessibility/Accessibility Service']"))
            )
            assert title_element.is_displayed(), "Title text not displayed"
            assert title_element.text == "Accessibility/Accessibility Service", "Title text mismatch"
            logger.info(f"Title text verified: {title_element.text}")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_instruction_text(self, appium_driver, wait):
        """Verify the instruction text and its content description."""
        logger.info("Starting test: Verify Instruction Text")

        try:
            # XPath query for the instruction text
            instruction_element = wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Enable TalkBack')]"))
            )
            assert instruction_element.is_displayed(), "Instruction text not displayed"

            # Verify the content description matches the text
            content_desc = instruction_element.get_attribute("content-desc")
            assert content_desc == instruction_element.text, "Content description mismatch"
            logger.info(f"Instruction text verified: {instruction_element.text}, Content-desc: {content_desc}")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_interact_with_button(self, appium_driver, wait):
        """Verify and interact with the clickable button."""
        logger.info("Starting test: Interact with Button")

        try:
            # XPath query for the button
            button_element = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/button"))
            )
            assert button_element.is_displayed(), "Button not displayed"
            logger.info("Button found and displayed")

            # Perform click action
            button_element.click()
            logger.info("Button clicked successfully")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

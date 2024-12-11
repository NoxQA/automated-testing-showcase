import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.appium_config import logger
from time import sleep


class TestCustomView:
    """Test suite for Accessibility/Custom View page."""

    def test_open_animations_menu(self, appium_driver, wait):
        """Open the Animations menu."""
        logger.info("Starting test: Open Animations Menu")

        try:
            animations_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Animation' and @resource-id='android:id/text1']"))
            )
            assert animations_element.is_displayed(), "Animations menu item not displayed"
            logger.info("Animations menu item found and displayed")
            animations_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

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

    def test_custom_view(self, appium_driver, wait):
        """Open the Custom View screen."""
        logger.info("Starting test: Open Custom View")

        try:
            custom_view_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Custom View']"))
            )
            assert custom_view_element.is_displayed(), "Accessibility Service menu item not displayed"
            logger.info("Accessibility Service menu item found and displayed")
            custom_view_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_title_text(self, appium_driver, wait):
        """Verify the title text on the Custom View page."""
        logger.info("Starting test: Verify Title Text")

        try:
            title_element = wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, "//android.widget.TextView[@text='Accessibility/Custom View']"))
            )
            assert title_element.is_displayed(), "Title text not displayed"
            assert title_element.text == "Accessibility/Custom View", "Title text mismatch"
            logger.info(f"Title text verified: {title_element.text}")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_instruction_text(self, appium_driver, wait):
        """Verify the instruction text and its content description."""
        logger.info("Starting test: Verify Instruction Text")

        try:
            instruction_element = wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Enable TalkBack')]"))
            )
            assert instruction_element.is_displayed(), "Instruction text not displayed"

            content_desc = instruction_element.get_attribute("content-desc")
            assert content_desc == instruction_element.text, "Content description mismatch"
            logger.info(f"Instruction text verified: {instruction_element.text}, Content-desc: {content_desc}")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_interact_with_buttons(self, appium_driver, wait):
        """Verify and interact with the clickable 'Off' buttons."""
        logger.info("Starting test: Interact with Buttons")

        try:
            first_button = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, "//android.view.View[@text='Off' and @bounds='[0,641][110,754]']"))
            )
            assert first_button.is_displayed(), "First button not displayed"
            logger.info("First button found and displayed")

            first_button.click()
            logger.info("First button clicked successfully")
            is_checked = first_button.get_attribute("checked") == "true"
            logger.info(f"First button state after click: {is_checked}")

            second_button = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, "//android.view.View[@text='Off' and @bounds='[0,754][110,867]']"))
            )
            assert second_button.is_displayed(), "Second button not displayed"
            logger.info("Second button found and displayed")

            second_button.click()
            logger.info("Second button clicked successfully")
            is_checked = second_button.get_attribute("checked") == "true"
            logger.info(f"Second button state after click: {is_checked}")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

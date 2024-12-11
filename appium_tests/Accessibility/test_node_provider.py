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
            sleep(2)  # Wait for the Accessibility menu to open
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_open_accessibility_node_provider(self, appium_driver, wait):
        """Open the Accessibility Node Provider screen."""
        logger.info("Starting test: Open Accessibility Node Provider")

        try:
            node_provider_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Accessibility Node Provider']"))
            )
            assert node_provider_element.is_displayed(), "Accessibility Node Provider menu item not displayed"
            logger.info("Accessibility Node Provider menu item found and displayed")
            node_provider_element.click()
            sleep(2)  # Wait for the Accessibility Node Provider screen to open
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_title_text(self, appium_driver, wait):
        """Verify the title text on the Accessibility Node Provider screen."""
        logger.info("Starting test: Verify Title Text")

        try:
            title_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Accessibility/Accessibility Node Provider']"))
            )
            assert title_element.is_displayed(), "Title text not displayed"
            assert title_element.text == "Accessibility/Accessibility Node Provider", "Title text mismatch"
            logger.info(f"Title text verified: {title_element.text}")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_instruction_text(self, appium_driver, wait):
        """Verify instruction text and its content description."""
        logger.info("Starting test: Verify Instruction Text")

        try:
            instruction_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Enable TalkBack and Explore-by-touch from accessibility settings. Then touch the colored squares.']"))
            )
            assert instruction_element.is_displayed(), "Instruction text not displayed"
            content_desc = instruction_element.get_attribute("content-desc")
            assert content_desc == instruction_element.text, "Content description mismatch"
            logger.info(f"Instruction text verified: {instruction_element.text}, Content-desc: {content_desc}")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_interaction_with_colored_square(self, appium_driver, wait):
        """Test interaction with a colored square."""
        logger.info("Starting test: Interaction with Colored Square")

        try:
            square_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.view.View[@bounds='[0,457][450,607]']"))
            )
            assert square_element.is_displayed(), "Colored square not displayed"
            logger.info("Colored square found and displayed")

            square_element.click()
            sleep(2)

        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise


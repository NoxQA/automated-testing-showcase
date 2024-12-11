import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.appium_config import logger
from time import sleep


class TestAnimationDefaultLayout:
    """Test suite for Animation/Default Layout Animations page."""

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

    def test_open_default_layout_animations_menu(self, appium_driver, wait):
        """Open the Default Layout Animations menu."""
        logger.info("Starting test: Open Default Layout Animations Menu")

        try:
            default_layout_animations_menu_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Default Layout Animations']"))
            )
            assert default_layout_animations_menu_element.is_displayed(), "Default Layout Animations menu item not displayed"
            logger.info("Default Layout Animations menu item found and displayed")
            default_layout_animations_menu_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_default_layout_animations_title(self, appium_driver, wait):
        """Verify the title text on the Animation/Default Layout Animations page."""
        logger.info("Starting test: Verify Title Text for Default Layout Animations")

        try:
            title_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Animation/Default Layout Animations']"))
            )
            assert title_element.is_displayed(), "Title text not displayed"
            assert title_element.text == "Animation/Default Layout Animations", "Title text mismatch"
            logger.info(f"Title text verified: {title_element.text}")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_click_add_button(self, appium_driver, wait):
        """Click the 'Add Button' to trigger the layout animation."""
        logger.info("Starting test: Click 'Add Button'")

        try:
            add_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/addNewButton"))
            )
            assert add_button.is_displayed(), "'Add Button' not displayed"
            logger.info("'Add Button' is displayed")
            add_button.click()
            logger.info("Clicked the 'Add Button'")
            sleep(2)  # Allow layout animation to take effect
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_new_button_added(self, appium_driver, wait):
        """Verify a new button has been added after clicking the 'Add Button'."""
        logger.info("Starting test: Verify New Button Added")

        try:
            # Wait for the grid layout to contain at least one button with a number
            new_button = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.GridLayout//android.widget.Button[starts-with(@text, '1')]"))
            )
            assert new_button.is_displayed(), "New Button not added"
            logger.info("New Button with text starting with '1' is added successfully")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise
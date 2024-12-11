import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.appium_config import logger
from time import sleep


class TestAnimationReversingPage:
    """Test suite for Animation/Reversing page."""

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

    def test_open_animation_reversing_menu(self, appium_driver, wait):
        """Open the Animation/Reversing menu."""
        logger.info("Starting test: Open Animation/Reversing Menu")

        try:
            animation_reversing_menu = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Reversing']"))
            )
            assert animation_reversing_menu.is_displayed(), "Animation/Reversing menu item not displayed"
            logger.info("Animation/Reversing menu item found and displayed")
            animation_reversing_menu.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_play_button_displayed(self, appium_driver, wait):
        """Verify the 'Play' button is displayed."""
        logger.info("Starting test: Verify Play Button Displayed")

        try:
            play_button = wait.until(
                EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/startButton"))
            )
            assert play_button.is_displayed(), "'Play' button not displayed"
            logger.info("'Play' button is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_reverse_button_displayed(self, appium_driver, wait):
        """Verify the 'Reverse' button is displayed."""
        logger.info("Starting test: Verify Reverse Button Displayed")

        try:
            reverse_button = wait.until(
                EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/reverseButton"))
            )
            assert reverse_button.is_displayed(), "'Reverse' button not displayed"
            logger.info("'Reverse' button is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_click_play_button(self, appium_driver, wait):
        """Click the 'Play' button and verify its functionality."""
        logger.info("Starting test: Click Play Button")

        try:
            play_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/startButton"))
            )
            assert play_button.is_displayed(), "'Play' button not displayed"
            logger.info("'Play' button is displayed")
            play_button.click()
            logger.info("Clicked the 'Play' button")
            sleep(2)

            # Verify animation started (this could be an animation change or screen change)
            animation_view = wait.until(
                EC.visibility_of_element_located((AppiumBy.CLASS_NAME, "android.view.View"))
            )
            assert animation_view.is_displayed(), "Expected animation or view not displayed after clicking 'Play'"
            logger.info("Animation or view displayed after clicking 'Play' button")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_click_reverse_button(self, appium_driver, wait):
        """Click the 'Reverse' button and verify the reversing functionality."""
        logger.info("Starting test: Click Reverse Button")

        try:
            reverse_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/reverseButton"))
            )
            assert reverse_button.is_displayed(), "'Reverse' button not displayed"
            logger.info("'Reverse' button is displayed")
            reverse_button.click()
            logger.info("Clicked the 'Reverse' button")
            sleep(2)

            # Verify reverse animation or effect
            reverse_view = wait.until(
                EC.visibility_of_element_located((AppiumBy.CLASS_NAME, "android.view.View"))
            )
            assert reverse_view.is_displayed(), "Expected reverse animation or view not displayed after clicking 'Reverse'"
            logger.info("Reverse animation or view displayed after clicking 'Reverse' button")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

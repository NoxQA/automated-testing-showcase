import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.appium_config import logger
from time import sleep


class TestAnimationEvents:
    """Test suite for Animation/Events page."""

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

    def test_open_animation_events_menu(self, appium_driver, wait):
        """Open the Animation/Events menu."""
        logger.info("Starting test: Open Animation/Events Menu")

        try:
            animation_events_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Animation/Events']"))
            )
            assert animation_events_element.is_displayed(), "Animation/Events menu item not displayed"
            logger.info("Animation/Events menu item found and displayed")
            animation_events_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_play_button_is_displayed(self, appium_driver, wait):
        """Verify the 'Play' button is displayed."""
        logger.info("Starting test: Verify Play Button")

        try:
            play_button = wait.until(
                EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/startButton"))
            )
            assert play_button.is_displayed(), "'Play' button not displayed"
            logger.info("'Play' button is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_click_play_button(self, appium_driver, wait):
        """Click the 'Play' button to trigger the animation."""
        logger.info("Starting test: Click Play Button")

        try:
            play_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/startButton"))
            )
            assert play_button.is_displayed(), "'Play' button not displayed"
            logger.info("'Play' button is displayed")
            play_button.click()
            logger.info("Clicked the 'Play' button")
            sleep(2)  # Allow animation to take effect
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_cancel_button_is_displayed(self, appium_driver, wait):
        """Verify the 'Cancel' button is displayed."""
        logger.info("Starting test: Verify Cancel Button")

        try:
            cancel_button = wait.until(
                EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/cancelButton"))
            )
            assert cancel_button.is_displayed(), "'Cancel' button not displayed"
            logger.info("'Cancel' button is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_click_cancel_button(self, appium_driver, wait):
        """Click the 'Cancel' button."""
        logger.info("Starting test: Click Cancel Button")

        try:
            cancel_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/cancelButton"))
            )
            assert cancel_button.is_displayed(), "'Cancel' button not displayed"
            logger.info("'Cancel' button is displayed")
            cancel_button.click()
            logger.info("Clicked the 'Cancel' button")
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_end_button_is_displayed(self, appium_driver, wait):
        """Verify the 'End' button is displayed."""
        logger.info("Starting test: Verify End Button")

        try:
            end_button = wait.until(
                EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/endButton"))
            )
            assert end_button.is_displayed(), "'End' button not displayed"
            logger.info("'End' button is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_click_end_button(self, appium_driver, wait):
        """Click the 'End' button."""
        logger.info("Starting test: Click End Button")

        try:
            end_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/endButton"))
            )
            assert end_button.is_displayed(), "'End' button not displayed"
            logger.info("'End' button is displayed")
            end_button.click()
            logger.info("Clicked the 'End' button")
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_end_immediately_checkbox_is_displayed(self, appium_driver, wait):
        """Verify the 'End Immediately' checkbox is displayed."""
        logger.info("Starting test: Verify End Immediately Checkbox")

        try:
            end_immediately_checkbox = wait.until(
                EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/endCB"))
            )
            assert end_immediately_checkbox.is_displayed(), "'End Immediately' checkbox not displayed"
            logger.info("'End Immediately' checkbox is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_toggle_end_immediately_checkbox(self, appium_driver, wait):
        """Toggle the 'End Immediately' checkbox."""
        logger.info("Starting test: Toggle End Immediately Checkbox")

        try:
            end_immediately_checkbox = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/endCB"))
            )
            assert end_immediately_checkbox.is_displayed(), "'End Immediately' checkbox not displayed"
            logger.info("'End Immediately' checkbox is displayed")
            end_immediately_checkbox.click()  # Toggle the checkbox
            logger.info("Toggled the 'End Immediately' checkbox")
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

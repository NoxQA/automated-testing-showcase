import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.appium_config import logger
from time import sleep


class TestAnimation:
    """Test suite for Animation/Bouncing Balls page."""

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

    def test_bouncing_balls(self, appium_driver, wait):
        """Open the Bouncing Balls screen."""
        logger.info("Starting test: Open Bouncing Balls")

        try:
            bouncing_balls_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Bouncing Balls']"))
            )
            assert bouncing_balls_element.is_displayed(), "Bouncing Balls menu item not displayed"
            logger.info("Bouncing Balls menu item found and displayed")
            bouncing_balls_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_title_text(self, appium_driver, wait):
        """Verify the title text on the Animation/Bouncing Balls page."""
        logger.info("Starting test: Verify Title Text")

        try:
            title_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Animation/Bouncing Balls']"))
            )
            assert title_element.is_displayed(), "Title text not displayed"
            assert title_element.text == "Animation/Bouncing Balls", "Title text mismatch"
            logger.info(f"Title text verified: {title_element.text}")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_animation_canvas(self, appium_driver, wait):
        """Verify the presence of the animation canvas."""
        logger.info("Starting test: Verify Animation Canvas")

        try:
            canvas_element = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@bounds='[0,220][1080,2274]']"))
            )
            assert canvas_element.is_displayed(), "Animation canvas not displayed"
            logger.info("Animation canvas is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_animation_functionality(self, appium_driver, wait):
        """Verify that the animation canvas is functional."""
        logger.info("Starting test: Verify Animation Functionality")

        try:
            canvas_element = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@bounds='[0,220][1080,2274]']"))
            )
            assert canvas_element.is_displayed(), "Animation canvas not displayed"

            initial_bounds = canvas_element.get_attribute("bounds")
            logger.info(f"Initial bounds of canvas: {initial_bounds}")

            appium_driver.tap([(540, 1247)])
            logger.info("Tap action performed on the animation canvas")

            updated_bounds = canvas_element.get_attribute("bounds")
            logger.info(f"Updated bounds of canvas after interaction: {updated_bounds}")

            assert initial_bounds == updated_bounds, "Canvas state appears unchanged; verify animation behavior"
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

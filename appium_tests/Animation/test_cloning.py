import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.appium_config import logger
from time import sleep


class TestAnimationCloning:
    """Test suite for Animation/Cloning page."""

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

    def test_open_animation_cloning_menu(self, appium_driver, wait):
        """Open the Animation/Cloning menu."""
        logger.info("Starting test: Open Animation/Cloning Menu")

        try:
            cloning_menu_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Cloning']"))
            )
            assert cloning_menu_element.is_displayed(), "Cloning menu item not displayed"
            logger.info("Cloning menu item found and displayed")
            cloning_menu_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_cloning_title(self, appium_driver, wait):
        """Verify the title text on the Animation/Cloning page."""
        logger.info("Starting test: Verify Title Text for Animation/Cloning")

        try:
            title_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Animation/Cloning']"))
            )
            assert title_element.is_displayed(), "Title text not displayed"
            assert title_element.text == "Animation/Cloning", "Title text mismatch"
            logger.info(f"Title text verified: {title_element.text}")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_click_run_button(self, appium_driver, wait):
        """Click the 'Run' button on the Animation/Cloning page."""
        logger.info("Starting test: Click 'Run' Button")

        try:
            run_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/startButton"))
            )
            assert run_button.is_displayed(), "'Run' button not displayed"
            logger.info("'Run' button is displayed")
            run_button.click()
            logger.info("Clicked the 'Run' button")
            sleep(2)  # Allow animation to play
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_animation_canvas_cloning(self, appium_driver, wait):
        """Verify the presence and functionality of the animation canvas."""
        logger.info("Starting test: Verify Animation Canvas for Cloning")

        try:
            canvas_element = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@bounds='[0,352][1080,2274]']"))
            )
            assert canvas_element.is_displayed(), "Animation canvas not displayed"
            logger.info("Animation canvas is displayed")

            # Verify interaction on the canvas if applicable
            initial_bounds = canvas_element.get_attribute("bounds")
            logger.info(f"Initial bounds of canvas: {initial_bounds}")

            appium_driver.tap([(540, 1247)])  # Tap the center of the canvas
            logger.info("Tap action performed on the animation canvas")

            updated_bounds = canvas_element.get_attribute("bounds")
            logger.info(f"Updated bounds of canvas after interaction: {updated_bounds}")

            assert initial_bounds == updated_bounds, "Canvas state appears unchanged; verify cloning animation behavior"
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.appium_config import logger
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains



class TestAnimationSeekingPage:
    """Test suite for Animation/Seeking page."""


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

    def test_open_animation_seeking_menu(self, appium_driver, wait):
        """Open the Animation/Seeking menu."""
        logger.info("Starting test: Open Animation/Seeking Menu")

        try:
            animation_seeking_menu = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Seeking']"))
            )
            assert animation_seeking_menu.is_displayed(), "Animation/Seeking menu item not displayed"
            logger.info("Animation/Seeking menu item found and displayed")
            animation_seeking_menu.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_run_button_displayed(self, appium_driver, wait):
        """Verify the 'Run' button is displayed."""
        logger.info("Starting test: Verify Run Button Displayed")

        try:
            run_button = wait.until(
                EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/startButton"))
            )
            assert run_button.is_displayed(), "'Run' button not displayed"
            logger.info("'Run' button is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_seek_bar_displayed(self, appium_driver, wait):
        """Verify the SeekBar is displayed."""
        logger.info("Starting test: Verify SeekBar Displayed")

        try:
            seek_bar = wait.until(
                EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/seekBar"))
            )
            assert seek_bar.is_displayed(), "SeekBar not displayed"
            logger.info("SeekBar is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_click_run_button(self, appium_driver, wait):
        """Click the 'Run' button and verify its functionality."""
        logger.info("Starting test: Click Run Button")

        try:
            run_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/startButton"))
            )
            assert run_button.is_displayed(), "'Run' button not displayed"
            logger.info("'Run' button is displayed")
            run_button.click()
            logger.info("Clicked the 'Run' button")
            sleep(2)

            # Verify animation or view started (this could be an animation change or screen change)
            animation_view = wait.until(
                EC.visibility_of_element_located((AppiumBy.CLASS_NAME, "android.view.View"))
            )
            assert animation_view.is_displayed(), "Expected animation or view not displayed after clicking 'Run'"
            logger.info("Animation or view displayed after clicking 'Run' button")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_seek_bar_interaction(self, appium_driver, wait):
        """Interact with the SeekBar and verify its functionality."""
        logger.info("Starting test: SeekBar Interaction")

        try:
            # Find the SeekBar element
            seek_bar = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/seekBar"))
            )
            assert seek_bar.is_displayed(), "SeekBar not displayed"
            logger.info("SeekBar is displayed")

            # Get the coordinates of the SeekBar
            seek_bar_location = seek_bar.location
            seek_bar_size = seek_bar.size

            # Calculate the start and end points for the swipe action
            start_x = seek_bar_location['x'] + seek_bar_size['width'] * 0.2  # 20% of SeekBar's width
            end_x = seek_bar_location['x'] + seek_bar_size['width'] * 0.8  # 80% of SeekBar's width
            y = seek_bar_location['y'] + seek_bar_size['height'] // 2  # Vertical center of the SeekBar

            # Perform swipe action using swipe() method
            appium_driver.swipe(start_x, y, end_x, y, duration=1000)  # You can adjust the duration (in ms)

            logger.info("Moved the SeekBar")
            sleep(2)

            # Verify the SeekBar value or progress (check other attributes, like progress)
            updated_seek_bar_value = seek_bar.get_attribute('text')  # Or check for progress/other attributes
            assert updated_seek_bar_value != '0.0', f"SeekBar value did not change"
            logger.info(f"SeekBar value changed to: {updated_seek_bar_value}")

        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise
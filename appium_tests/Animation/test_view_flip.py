import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.appium_config import logger
from time import sleep


class TestViewFlipPage:
    """Test suite for Animation/View Flip page."""

    def test_open_animation_menu(self, appium_driver, wait):
        """Open the Animation menu."""
        logger.info("Starting test: Open Animation Menu")

        try:
            animation_menu_item = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Animation' and @resource-id='android:id/text1']"))
            )
            assert animation_menu_item.is_displayed(), "Animation menu item not displayed"
            logger.info("Animation menu item is displayed")
            animation_menu_item.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_open_view_flip_menu(self, appium_driver, wait):
        """Open the View Flip menu."""
        logger.info("Starting test: Open View Flip Menu")

        try:
            view_flip_menu_item = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='View Flip']"))
            )
            assert view_flip_menu_item.is_displayed(), "View Flip menu item not displayed"
            logger.info("View Flip menu item is displayed")
            view_flip_menu_item.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_flip_button_and_verify_language(self, appium_driver, wait):
        """Click the Flip button and verify ListView switches between languages."""
        logger.info("Starting test: Flip Button and Verify Language")

        try:
            # Locate the Flip button
            flip_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/button"))
            )
            assert flip_button.is_displayed(), "Flip button not displayed"
            logger.info("Flip button is displayed")

            # Initial check for ListView in English
            list_view_en = wait.until(
                EC.presence_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/list_en"))
            )
            assert list_view_en.is_displayed(), "ListView in English not displayed"
            logger.info("ListView in English is displayed")

            # Verify English items
            english_items = ["One", "Two", "Three", "Four", "Five", "Six"]
            self.verify_list_items(appium_driver, english_items)
            logger.info("Verified English ListView items")

            # Click the Flip button
            flip_button.click()
            logger.info("Clicked the Flip button")
            sleep(2)

            # Check for ListView in French
            list_view_fr = wait.until(
                EC.presence_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/list_fr"))
            )
            assert list_view_fr.is_displayed(), "ListView in French not displayed"
            logger.info("ListView in French is displayed")

            # Verify French items
            french_items = ["Un", "Deux", "Trois", "Quatre", "Le Five", "Six"]
            self.verify_list_items(appium_driver, french_items)
            logger.info("Verified French ListView items")

        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def verify_list_items(self, appium_driver, expected_items):
        """Verify ListView contains the expected items."""
        # Locate the ListView
        list_view = appium_driver.find_elements(AppiumBy.ID, "android:id/text1")
        retrieved_items = [item.text for item in list_view]

        # Log retrieved items
        logger.info(f"Retrieved ListView items: {retrieved_items}")

        # Verify the number of items matches
        assert len(retrieved_items) == len(expected_items), (
            f"Expected {len(expected_items)} items, but found {len(retrieved_items)}"
        )

        # Verify each item matches
        for retrieved, expected in zip(retrieved_items, expected_items):
            assert retrieved == expected, f"Item mismatch: expected '{expected}', found '{retrieved}'"


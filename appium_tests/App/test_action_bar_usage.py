import pytest
from appium.webdriver.common.appiumby import AppiumBy
from config.appium_config import logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class TestActionBarUsage:
    """Test suite for Action Bar Usage functionality"""

    def test_open_app_menu(self, appium_driver, wait):
        """Open App menu"""
        logger.info("Starting test: Open App Menu")
        try:
            app_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='App']"))
            )
            assert app_element.is_displayed(), "App menu item is not displayed."
            logger.info("App menu item found and displayed.")
            app_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_open_action_bar_menu(self, appium_driver, wait):
        """Open the Action Bar menu"""
        logger.info("Open App/Action Bar menu")
        try:
            action_bar_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Action Bar']"))
            )
            assert action_bar_element.is_displayed(), "Action Bar menu is not displayed."
            logger.info("Action Bar menu item found and displayed.")
            action_bar_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_open_action_bar_tabs_menu(self, appium_driver, wait):
        """Open the Action Bar Usage menu"""
        logger.info("Open Action Bar Usage menu")
        try:
            action_bar_usage_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Action Bar Usage']"))
            )
            assert action_bar_tabs_usage.is_displayed(), "Action Bar Usage menu is not displayed."
            logger.info("Action Bar Usage menu item found and displayed.")
            action_bar_usage_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_click_edit_button(self, appium_driver, wait):
        """Click the Edit button and verify that the toast message appears"""
        logger.info("Starting test: Click Edit button")

        try:
            # Locate the "Edit" button using its accessibility ID
            edit_button_locator = (AppiumBy.ACCESSIBILITY_ID, "Edit")
            edit_button = wait.until(lambda driver: driver.find_element(*edit_button_locator))

            # Click the Edit button
            edit_button.click()
            logger.info("Tapped Edit button successfully.")

            # Verify that the toast message appears with the expected text "Selected Item: Edit"
            toast_locator = (AppiumBy.XPATH, "//android.widget.Toast[@text='Selected Item: Edit']")
            wait.until(lambda driver: driver.find_element(*toast_locator))
            logger.info("Toast message 'Selected Item: Edit' appeared successfully.")

        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_search_button_click(self, appium_driver, wait):
        """Click the Search button and verify that the search view works"""
        logger.info("Starting test: Click Search button")

        try:
            # Locate the Search button using its content description
            search_button_locator = (AppiumBy.ACCESSIBILITY_ID, "Search")
            search_button = wait.until(lambda driver: driver.find_element(*search_button_locator))

            # Click the Search button
            search_button.click()
            logger.info("Tapped Search button successfully.")

            # Verify the search view is visible
            search_view_locator = (AppiumBy.ID, "io.appium.android.apis:id/action_search")
            search_view = wait.until(lambda driver: driver.find_element(*search_view_locator))
            assert search_view.is_displayed(), "Search View is not displayed"
            logger.info("Search View is displayed successfully.")

        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_more_options_button_click(self, appium_driver, wait):
        """Click the More Options button and verify that it triggers the expected action"""
        logger.info("Starting test: Click More Options button")

        try:
            # Locate the More Options button using its content description
            more_options_button_locator = (AppiumBy.ACCESSIBILITY_ID, "More options")
            more_options_button = wait.until(lambda driver: driver.find_element(*more_options_button_locator))

            # Click the More Options button
            more_options_button.click()
            logger.info("Tapped More Options button successfully.")

            # Verify menu options appear after clicking More Options
            # Adjust the following locator to match the actual menu items
            menu_item_locator = (AppiumBy.XPATH, "//android.widget.TextView[@text='SomeMenuItem']")  # Example
            wait.until(lambda driver: driver.find_element(*menu_item_locator))
            logger.info("Menu item found after clicking More Options button.")

        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_search_input(self, appium_driver, wait):
        """Type in the Search View and verify the text input"""
        logger.info("Starting test: Search input")

        try:
            # Locate the Search View input field (inside the SearchView component)
            search_input_locator = (AppiumBy.ID, "android:id/search_src_text")
            search_input = wait.until(lambda driver: driver.find_element(*search_input_locator))

            # Create an ActionChains instance to simulate typing
            actions = ActionChains(appium_driver)

            # Type some search text using ActionChains
            search_text = "test search"
            actions.click(search_input).send_keys(search_text).perform()
            logger.info(f"Typed '{search_text}' into search input.")

            # Verify the typed text is in the search field
            assert search_input.get_attribute("text") == search_text, "Search text is not entered correctly"
            logger.info("Search input text entered successfully.")

        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

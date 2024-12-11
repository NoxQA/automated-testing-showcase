import pytest
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.appium_config import logger
from time import sleep


class TestTabActions:
    """Test suite for Tab Actions"""

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
        """Open the Action Bar Tabs menu"""
        logger.info("Open Action Bar Mechanics menu")
        try:
            action_bar_tabs_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Action Bar Tabs']"))
            )
            assert action_bar_tabs_element.is_displayed(), "Action Bar Tabs menu is not displayed."
            logger.info("Action Bar Tabs menu item found and displayed.")
            action_bar_tabs_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_add_new_tab(self, appium_driver, wait):
        """Click the Add new tab button and ensure it can be clicked"""
        logger.info("Starting test: Add New Tab")
        try:
            add_tab_button_locator = (AppiumBy.ACCESSIBILITY_ID, "Add new tab")
            add_tab_button = wait.until(lambda driver: driver.find_element(*add_tab_button_locator))

            # Simply click the Add new tab button
            add_tab_button.click()
            logger.info("Tapped Add new tab button successfully.")

            # Test passes if no errors are raised
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_remove_last_tab(self, appium_driver, wait):
        """Click the Remove last tab button and ensure it can be clicked"""
        logger.info("Starting test: Remove Last Tab")
        try:
            remove_last_tab_button_locator = (AppiumBy.ACCESSIBILITY_ID, "Remove last tab")
            remove_last_tab_button = wait.until(lambda driver: driver.find_element(*remove_last_tab_button_locator))

            # Simply click the Remove last tab button
            remove_last_tab_button.click()
            logger.info("Tapped Remove last tab button successfully.")

            # Test passes if no errors are raised
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_toggle_tab_mode(self, appium_driver, wait):
        """Click the Toggle tab mode button and ensure it can be clicked"""
        logger.info("Starting test: Toggle Tab Mode")
        try:
            toggle_tab_mode_button_locator = (AppiumBy.ACCESSIBILITY_ID, "Toggle tab mode")
            toggle_tab_mode_button = wait.until(lambda driver: driver.find_element(*toggle_tab_mode_button_locator))

            # Simply click the Toggle tab mode button
            toggle_tab_mode_button.click()
            logger.info("Tapped Toggle tab mode button successfully.")

            # Test passes if no errors are raised
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_remove_all_tabs(self, appium_driver, wait):
        """Click the Remove all tabs button and ensure it can be clicked"""
        logger.info("Starting test: Remove All Tabs")
        try:
            remove_all_tabs_button_locator = (AppiumBy.ACCESSIBILITY_ID, "Remove all tabs")
            remove_all_tabs_button = wait.until(lambda driver: driver.find_element(*remove_all_tabs_button_locator))

            # Simply click the Remove all tabs button
            remove_all_tabs_button.click()
            logger.info("Tapped Remove all tabs button successfully.")

            # Test passes if no errors are raised
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise
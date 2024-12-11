import pytest
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.appium_config import logger
from time import sleep


class TestAppEvents:
    """Test suite for App Events menu"""

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

    def test_open_action_bar_mechanics_menu(self, appium_driver, wait):
        """Open the Action Bar Mechanics menu"""
        logger.info("Open App/Action Bar Mechanics menu")
        try:
            action_bar_mechanics_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Action Bar Mechanics']"))
            )
            assert action_bar_mechanics_element.is_displayed(), "Action Bar Mechanics menu is not displayed."
            logger.info("Action Bar Mechanics menu item found and displayed.")
            action_bar_mechanics_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

        def test_action_button(self, appium_driver, wait):
            """Interact with the Action Button using W3C WebDriver Actions"""
            logger.info("Interacting with Action Button")
            try:
                action_button = wait.until(
                    EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Action Button"))
                )
                assert action_button.is_displayed(), "Action Button is not displayed."
                logger.info("Action Button found.")

                action_chains = ActionChains(appium_driver)
                action_chains.move_to_element(action_button).click().perform()
                logger.info("Tapped Action Button successfully.")

                notification_message = wait.until(
                    EC.visibility_of_element_located(
                        (AppiumBy.XPATH, "//*[@class='android.widget.Toast' and @text='Selected Item: Action Button']")
                    )
                )
                assert notification_message.is_displayed(), "Notification message is not displayed."
                logger.info("Notification message displayed correctly.")
            except Exception as e:
                logger.error(f"Test failed: {e}")
                raise

        def test_more_options_button(self, appium_driver, wait):
            """Interact with More Options Button using W3C WebDriver Actions"""
            logger.info("Interacting with More Options button")
            try:
                more_options_button = wait.until(
                    EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "More options"))
                )
                assert more_options_button.is_displayed(), "More options Button is not displayed."
                logger.info("More options button displayed correctly.")

                action_chains = ActionChains(appium_driver)
                action_chains.move_to_element(more_options_button).click().perform()
                logger.info("Tapped More Options Button successfully.")

                normal_item = wait.until(
                    EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Normal item']"))
                )
                normal_item.click()

                notification_message = wait.until(
                    EC.visibility_of_element_located(
                        (AppiumBy.XPATH, "//*[@class='android.widget.Toast' and @text='Selected Item: Normal item']")
                    )
                )
                assert notification_message.is_displayed(), "Notification message is not displayed."
                logger.info("Notification message displayed correctly.")
            except Exception as e:
                logger.error(f"Test failed: {e}")
                raise



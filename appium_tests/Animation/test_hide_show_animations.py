import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.appium_config import logger
from time import sleep


class TestHideShowAnimations:
    """Test suite for Hide-Show Animations page."""

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

    def test_open_hide_show_animations_menu(self, appium_driver, wait):
        """Open the Hide-Show Animations menu."""
        logger.info("Starting test: Open Hide-Show Animations Menu")

        try:
            hide_show_animations_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Hide-Show Animations']"))
            )
            assert hide_show_animations_element.is_displayed(), "Hide-Show Animations menu item not displayed"
            logger.info("Hide-Show Animations menu item found and displayed")
            hide_show_animations_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_show_buttons_button(self, appium_driver, wait):
        """Verify the 'Show Buttons' button is displayed."""
        logger.info("Starting test: Verify Show Buttons Button")

        try:
            show_buttons_button = wait.until(
                EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/addNewButton"))
            )
            assert show_buttons_button.is_displayed(), "'Show Buttons' button not displayed"
            logger.info("'Show Buttons' button is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_click_show_buttons_button(self, appium_driver, wait):
        """Click the 'Show Buttons' button to trigger the layout animation."""
        logger.info("Starting test: Click Show Buttons Button")

        try:
            show_buttons_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/addNewButton"))
            )
            assert show_buttons_button.is_displayed(), "'Show Buttons' button not displayed"
            logger.info("'Show Buttons' button is displayed")
            show_buttons_button.click()
            logger.info("Clicked the 'Show Buttons' button")
            sleep(2)  # Allow layout animation to take effect
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_checkboxes_displayed(self, appium_driver, wait):
        """Verify 'Custom Animations' and 'Hide (GONE)' checkboxes are displayed."""
        logger.info("Starting test: Verify Checkboxes Displayed")

        try:
            custom_anim_checkbox = wait.until(
                EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/customAnimCB"))
            )
            hide_gone_checkbox = wait.until(
                EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/hideGoneCB"))
            )

            assert custom_anim_checkbox.is_displayed(), "'Custom Animations' checkbox not displayed"
            assert hide_gone_checkbox.is_displayed(), "'Hide (GONE)' checkbox not displayed"

            logger.info("'Custom Animations' and 'Hide (GONE)' checkboxes are displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_toggle_custom_anim_checkbox(self, appium_driver, wait):
        """Toggle the 'Custom Animations' checkbox."""
        logger.info("Starting test: Toggle Custom Animations Checkbox")

        try:
            custom_anim_checkbox = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/customAnimCB"))
            )
            assert custom_anim_checkbox.is_displayed(), "'Custom Animations' checkbox not displayed"
            logger.info("'Custom Animations' checkbox is displayed")
            custom_anim_checkbox.click()  # Toggle the checkbox
            logger.info("Toggled the 'Custom Animations' checkbox")
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_toggle_hide_gone_checkbox(self, appium_driver, wait):
        """Toggle the 'Hide (GONE)' checkbox."""
        logger.info("Starting test: Toggle Hide (GONE) Checkbox")

        try:
            hide_gone_checkbox = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/hideGoneCB"))
            )
            assert hide_gone_checkbox.is_displayed(), "'Hide (GONE)' checkbox not displayed"
            logger.info("'Hide (GONE)' checkbox is displayed")
            hide_gone_checkbox.click()  # Toggle the checkbox
            logger.info("Toggled the 'Hide (GONE)' checkbox")
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_buttons_displayed(self, appium_driver, wait):
        """Verify that the buttons '0', '1', '2', and '3' are displayed."""
        logger.info("Starting test: Verify Buttons Displayed")

        try:
            button_0 = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='0']"))
            )
            button_1 = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='1']"))
            )
            button_2 = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='2']"))
            )
            button_3 = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='3']"))
            )

            assert button_0.is_displayed(), "'0' button not displayed"
            assert button_1.is_displayed(), "'1' button not displayed"
            assert button_2.is_displayed(), "'2' button not displayed"
            assert button_3.is_displayed(), "'3' button not displayed"

            logger.info("Buttons '0', '1', '2', and '3' are displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

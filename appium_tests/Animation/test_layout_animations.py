import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.appium_config import logger
from time import sleep


class TestLayoutAnimations:
    """Test suite for Layout Animations page."""

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

    def test_open_layout_animations_menu(self, appium_driver, wait):
        """Open the Layout Animations menu."""
        logger.info("Starting test: Open Layout Animations Menu")

        try:
            layout_animations_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Layout Animations']"))
            )
            assert layout_animations_element.is_displayed(), "Layout Animations menu item not displayed"
            logger.info("Layout Animations menu item found and displayed")
            layout_animations_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_show_button(self, appium_driver, wait):
        """Verify the 'Add Button' button is displayed."""
        logger.info("Starting test: Verify Add Button Button")

        try:
            add_button = wait.until(
                EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/addNewButton"))
            )
            assert add_button.is_displayed(), "'Add Button' button not displayed"
            logger.info("'Add Button' button is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_click_add_button(self, appium_driver, wait):
        """Click the 'Add Button' button to trigger the layout animation."""
        logger.info("Starting test: Click Add Button Button")

        try:
            add_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/addNewButton"))
            )
            assert add_button.is_displayed(), "'Add Button' button not displayed"
            logger.info("'Add Button' button is displayed")
            add_button.click()
            logger.info("Clicked the 'Add Button' button")
            sleep(2)  # Allow layout animation to take effect
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_custom_animations_checkbox(self, appium_driver, wait):
        """Verify 'Custom Animations' checkbox is displayed."""
        logger.info("Starting test: Verify Custom Animations Checkbox")

        try:
            custom_anim_checkbox = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.CheckBox[@resource-id='io.appium.android.apis:id/customAnimCB']"))
            )
            assert custom_anim_checkbox.is_displayed(), "'Custom Animations' checkbox not displayed"
            logger.info("'Custom Animations' checkbox is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_toggle_custom_anim_checkbox(self, appium_driver, wait):
        """Toggle the 'Custom Animations' checkbox."""
        logger.info("Starting test: Toggle Custom Animations Checkbox")

        try:
            custom_anim_checkbox = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.CheckBox[@resource-id='io.appium.android.apis:id/customAnimCB']"))
            )
            assert custom_anim_checkbox.is_displayed(), "'Custom Animations' checkbox not displayed"
            logger.info("'Custom Animations' checkbox is displayed")
            custom_anim_checkbox.click()  # Toggle the checkbox
            logger.info("Toggled the 'Custom Animations' checkbox")
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_in_checkbox(self, appium_driver, wait):
        """Verify the 'In' checkbox is displayed."""
        logger.info("Starting test: Verify In Checkbox")

        try:
            in_checkbox = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.CheckBox[@resource-id='io.appium.android.apis:id/appearingCB']"))
            )
            assert in_checkbox.is_displayed(), "'In' checkbox not displayed"
            logger.info("'In' checkbox is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_toggle_in_checkbox(self, appium_driver, wait):
        """Toggle the 'In' checkbox."""
        logger.info("Starting test: Toggle In Checkbox")

        try:
            in_checkbox = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.CheckBox[@resource-id='io.appium.android.apis:id/appearingCB']"))
            )
            assert in_checkbox.is_displayed(), "'In' checkbox not displayed"
            logger.info("'In' checkbox is displayed")
            in_checkbox.click()  # Toggle the checkbox
            logger.info("Toggled the 'In' checkbox")
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_out_checkbox(self, appium_driver, wait):
        """Verify the 'Out' checkbox is displayed."""
        logger.info("Starting test: Verify Out Checkbox")

        try:
            out_checkbox = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.CheckBox[@resource-id='io.appium.android.apis:id/disappearingCB']"))
            )
            assert out_checkbox.is_displayed(), "'Out' checkbox not displayed"
            logger.info("'Out' checkbox is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_toggle_out_checkbox(self, appium_driver, wait):
        """Toggle the 'Out' checkbox."""
        logger.info("Starting test: Toggle Out Checkbox")

        try:
            out_checkbox = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.CheckBox[@resource-id='io.appium.android.apis:id/disappearingCB']"))
            )
            assert out_checkbox.is_displayed(), "'Out' checkbox not displayed"
            logger.info("'Out' checkbox is displayed")
            out_checkbox.click()  # Toggle the checkbox
            logger.info("Toggled the 'Out' checkbox")
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_changing_in_checkbox(self, appium_driver, wait):
        """Verify the 'Changing-In' checkbox is displayed."""
        logger.info("Starting test: Verify Changing-In Checkbox")

        try:
            changing_in_checkbox = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.CheckBox[@resource-id='io.appium.android.apis:id/changingAppearingCB']"))
            )
            assert changing_in_checkbox.is_displayed(), "'Changing-In' checkbox not displayed"
            logger.info("'Changing-In' checkbox is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_toggle_changing_in_checkbox(self, appium_driver, wait):
        """Toggle the 'Changing-In' checkbox."""
        logger.info("Starting test: Toggle Changing-In Checkbox")

        try:
            changing_in_checkbox = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.CheckBox[@resource-id='io.appium.android.apis:id/changingAppearingCB']"))
            )
            assert changing_in_checkbox.is_displayed(), "'Changing-In' checkbox not displayed"
            logger.info("'Changing-In' checkbox is displayed")
            changing_in_checkbox.click()  # Toggle the checkbox
            logger.info("Toggled the 'Changing-In' checkbox")
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_toggle_changing_out_checkbox(self, appium_driver, wait):
        """Toggle the 'Changing-Out' checkbox."""
        logger.info("Starting test: Toggle Changing-Out Checkbox")

        try:
            changing_out_checkbox = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.CheckBox[@resource-id='io.appium.android.apis:id/changingDisappearingCB']"))
            )
            assert changing_out_checkbox.is_displayed(), "'Changing-Out' checkbox not displayed"
            logger.info("'Changing-Out' checkbox is displayed")
            changing_out_checkbox.click()  # Toggle the checkbox
            logger.info("Toggled the 'Changing-Out' checkbox")
            sleep(2)  # Wait for any animation to complete
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise
import logging
import subprocess
from time import sleep
from appium import webdriver
from appium.options.android import UiAutomator2Options


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger()

def enable_talkback():
    """Enable TalkBack programmatically using ADB."""
    logger.info("Enabling TalkBack via ADB...")
    subprocess.run(["adb", "shell", "settings", "put", "secure", "enabled_accessibility_services", "com.google.android.marvin.talkback/com.google.android.marvin.talkback.TalkBackService"])
    subprocess.run(["adb", "shell", "settings", "put", "secure", "accessibility_enabled", "1"])
    sleep(2)
    logger.info("TalkBack enabled successfully.")

def disable_talkback():
    """Disable TalkBack programmatically using ADB."""
    logger.info("Disabling TalkBack via ADB...")
    subprocess.run(["adb", "shell", "settings", "put", "secure", "enabled_accessibility_services", "null"])
    subprocess.run(["adb", "shell", "settings", "put", "secure", "accessibility_enabled", "0"])
    sleep(2)
    logger.info("TalkBack disabled successfully.")


def get_appium_driver():
    """Set up and return the Appium driver."""
    logger.info("Initializing Appium driver...")

    # Set up the Appium options
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Pixel_4a"
    options.platform_version = "15"  # Ensure that the version is valid
    options.app = "/media/bladerunner95/Fast/Portfolio/selenium-automation-showcase/pythonProject/appium_tests/apk/ApiDemos-debug.apk"  # Correct APK path
    options.automation_name = "UiAutomator2"

    # Set up the Appium driver using the correct endpoint for Appium v2
    driver = webdriver.Remote(
        command_executor="http://192.168.1.104:4723",  # Use the correct endpoint for Appium v2
        options=options
    )

    return driver

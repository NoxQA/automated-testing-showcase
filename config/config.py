import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Fixture for initializing the WebDriver (Chrome in this case)
@pytest.fixture(scope="function")
def driver():
    # Set up Chrome options
    chrome_options = Options()

    # Define preferences to configure the download directory and block prompts
    prefs = {
        "download.default_directory": "/tmp/selenium_downloads",  # Change this to your preferred path
        "download.prompt_for_download": False,  # Disable the download prompt
        "download.directory_upgrade": True,  # Enable upgrading the directory if necessary
        "safebrowsing.enabled": True,  # Enable safe browsing (optional)
        "download.extensions_to_open": "applications/pdf,text/plain"  # Automatically handle certain file types
    }

    # Apply the preferences to Chrome options
    chrome_options.add_experimental_option("prefs", prefs)

    # Initialize the WebDriver with the configured options
    driver = webdriver.Chrome(options=chrome_options)

    # Yield the driver to be used in the tests
    yield driver

    # Quit the driver after the test
    driver.quit()
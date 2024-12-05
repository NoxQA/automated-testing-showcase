import logging
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

log_dir = "/media/bladerunner95/Fast/Portfolio/selenium-automation-showcase/pythonProject/logs"
os.makedirs(log_dir, exist_ok=True)

# Create a unique log file name using the current timestamp
timestamp = time.strftime("%Y%m%d-%H%M%S")
log_file_path = os.path.join(log_dir, f"test_log_{timestamp}.log")

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,  # Ensure logging level is set to INFO
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path, mode="w"),  # Overwrite log file on each run
        logging.StreamHandler()  # Logs to console as well
    ],
    force=True  # Force logging configuration
)
logger = logging.getLogger()

# Log a test message to verify logging works
logger.info("Logging is now initialized.")

def pytest_configure(config):
    """Configure pytest to enable logging to the file."""
    logger.info("Initializing pytest logging configuration.")
    for handler in logging.getLogger().handlers:
        if isinstance(handler, logging.FileHandler):
            logger.info(f"Log file: {handler.baseFilename}")

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    prefs = {
        "download.default_directory": "/tmp/selenium_downloads",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "download.extensions_to_open": "applications/pdf,text/plain"
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)
    logger.info("WebDriver initialized in headless mode.")

    yield driver

    logger.info("Quitting WebDriver...")
    driver.quit()

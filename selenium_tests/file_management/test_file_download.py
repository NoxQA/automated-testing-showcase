import os
import time
import pytest
import shutil
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure  # Importing the logger from config.py


def test_file_downloader(driver):
    download_dir = os.path.expanduser("~/Downloads/selenium_downloads")

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        logger.info(f"Directory {download_dir} created.")  # Log the directory creation

    prefs = {
        "download.default_directory": download_dir,  # Set the download directory
        "download.prompt_for_download": False,  # Disable the download prompt
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }

    driver.execute_cdp_cmd('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': download_dir})

    url = "https://the-internet.herokuapp.com/download"
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".example"))
    )

    download_links = driver.find_elements(By.CSS_SELECTOR, ".example a")

    for link in download_links:
        file_name = link.text
        download_url = link.get_attribute("href")
        logger.info(f"Starting download for {file_name} from {download_url}")

        link.click()

        time.sleep(3)  # Adjust based on download speed

        downloaded_file_path = os.path.join(download_dir, file_name)
        if os.path.exists(downloaded_file_path):
            logger.info(f"Downloaded: {file_name}")
            os.remove(downloaded_file_path)  # Optional: remove the file after testing
        else:
            logger.info(f"Failed to download: {file_name}")

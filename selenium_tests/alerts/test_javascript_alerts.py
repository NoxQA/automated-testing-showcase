import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver  # Adjust import as necessary


@pytest.mark.usefixtures("driver")
def test_javascript_alerts(driver):
    # Step 1: Navigate to the JavaScript Alerts page
    logger.info("Navigating to the JavaScript Alerts page.")
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Step 2: Handle JavaScript Alert
    logger.info("Clicking the 'Click for JS Alert' button.")
    alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    alert_button.click()

    # Switch to alert and accept it
    logger.info("Switching to the alert dialog.")
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert_text = alert.text
    logger.info(f"Alert text: {alert_text}")
    assert alert_text == "I am a JS Alert", "Alert text does not match expected value."
    alert.accept()

    # Verify result message
    result_text = driver.find_element(By.ID, "result").text
    logger.info(f"Result after alert: {result_text}")
    assert result_text == "You successfully clicked an alert", "Unexpected result after accepting alert."

    # Step 3: Handle JavaScript Confirm (Accept and Cancel)
    logger.info("Clicking the 'Click for JS Confirm' button.")
    confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
    confirm_button.click()

    # Switch to confirm dialog and accept it
    logger.info("Switching to the confirm dialog (Accept).")
    confirm = WebDriverWait(driver, 10).until(EC.alert_is_present())
    confirm_text = confirm.text
    logger.info(f"Confirm dialog text: {confirm_text}")
    assert confirm_text == "I am a JS Confirm", "Confirm dialog text does not match expected value."
    confirm.accept()

    # Verify result message after accepting
    result_text = driver.find_element(By.ID, "result").text
    logger.info(f"Result after accepting confirm: {result_text}")
    assert result_text == "You clicked: Ok", "Unexpected result after accepting confirm dialog."

    # Click again and dismiss the confirm dialog
    confirm_button.click()
    logger.info("Switching to the confirm dialog (Cancel).")
    confirm = WebDriverWait(driver, 10).until(EC.alert_is_present())
    confirm.dismiss()

    # Verify result message after dismissing
    result_text = driver.find_element(By.ID, "result").text
    logger.info(f"Result after dismissing confirm: {result_text}")
    assert result_text == "You clicked: Cancel", "Unexpected result after dismissing confirm dialog."

    # Step 4: Handle JavaScript Prompt
    logger.info("Clicking the 'Click for JS Prompt' button.")
    prompt_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
    prompt_button.click()

    # Switch to prompt dialog, input text, and accept it
    logger.info("Switching to the prompt dialog.")
    prompt = WebDriverWait(driver, 10).until(EC.alert_is_present())
    prompt_text = prompt.text
    logger.info(f"Prompt dialog text: {prompt_text}")
    assert prompt_text == "I am a JS prompt", "Prompt dialog text does not match expected value."

    # Enter text into the prompt and accept
    input_text = "Test input"
    prompt.send_keys(input_text)
    prompt.accept()

    # Verify result message after entering text
    result_text = driver.find_element(By.ID, "result").text
    logger.info(f"Result after entering prompt input: {result_text}")
    assert result_text == f"You entered: {input_text}", "Unexpected result after entering input in the prompt dialog."

    # Test canceling the prompt
    prompt_button.click()
    logger.info("Switching to the prompt dialog for cancellation.")
    prompt = WebDriverWait(driver, 10).until(EC.alert_is_present())
    prompt.dismiss()

    # Verify result message after dismissing prompt
    result_text = driver.find_element(By.ID, "result").text
    logger.info(f"Result after dismissing prompt: {result_text}")
    assert result_text == "You entered: null", "Unexpected result after dismissing prompt dialog."

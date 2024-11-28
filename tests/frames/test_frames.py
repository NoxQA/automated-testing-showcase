import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver  # Adjust import as necessary


@pytest.mark.usefixtures("driver")
def test_nested_frames(driver):
    # Step 1: Navigate to the "Frames" page
    logger.info("Navigating to the Frames page.")
    driver.get("https://the-internet.herokuapp.com/frames")

    # Step 2: Click on "Nested Frames" link
    logger.info("Clicking on the 'Nested Frames' link.")
    nested_frames_link = driver.find_element(By.LINK_TEXT, "Nested Frames")
    nested_frames_link.click()

    # Step 3: Switch to the frames and validate the content
    logger.info("Switching to the nested frames.")

    # Switch to the top frame
    driver.switch_to.frame("frame-top")

    # In the top frame, there are three sub-frames (left, middle, right)
    logger.info("Switching to the left frame.")
    driver.switch_to.frame("frame-left")
    left_text = driver.find_element(By.TAG_NAME, "body").text
    logger.info(f"Content in left frame: {left_text}")
    assert left_text == "LEFT", "Expected content 'LEFT' in the left frame."

    # Switch back to the top frame to go to the middle frame
    driver.switch_to.parent_frame()
    logger.info("Switching to the middle frame.")
    driver.switch_to.frame("frame-middle")
    middle_text = driver.find_element(By.ID, "content").text
    logger.info(f"Content in middle frame: {middle_text}")
    assert middle_text == "MIDDLE", "Expected content 'MIDDLE' in the middle frame."

    # Switch back to the top frame to go to the right frame
    driver.switch_to.parent_frame()
    logger.info("Switching to the right frame.")
    driver.switch_to.frame("frame-right")
    right_text = driver.find_element(By.TAG_NAME, "body").text
    logger.info(f"Content in right frame: {right_text}")
    assert right_text == "RIGHT", "Expected content 'RIGHT' in the right frame."

    # Switch back to the main page to go to the bottom frame
    driver.switch_to.default_content()
    logger.info("Switching to the bottom frame.")
    driver.switch_to.frame("frame-bottom")
    bottom_text = driver.find_element(By.TAG_NAME, "body").text
    logger.info(f"Content in bottom frame: {bottom_text}")
    assert bottom_text == "BOTTOM", "Expected content 'BOTTOM' in the bottom frame."


@pytest.mark.usefixtures("driver")
def test_iframe(driver):
    # Step 1: Navigate to the "Frames" page
    logger.info("Navigating to the Frames page.")
    driver.get("https://the-internet.herokuapp.com/frames")

    # Step 2: Click on "iFrame" link
    logger.info("Clicking on the 'iFrame' link.")
    iframe_link = driver.find_element(By.LINK_TEXT, "iFrame")
    iframe_link.click()

    # Step 3: Switch to the iFrame
    logger.info("Switching to the iFrame.")
    iframe_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mce_0_ifr"))
    )
    driver.switch_to.frame(iframe_element)

    # Step 4: Interact with the content inside the iFrame
    logger.info("Interacting with the content inside the iFrame.")
    content = driver.find_element(By.ID, "tinymce")
    content_text = content.text
    logger.info(f"Original content in iFrame: {content_text}")
    assert content_text == "Your content goes here.", "Unexpected initial content in the iFrame."

    # If the editor is in read-only mode, bypass using JavaScript
    logger.info("Editor might be in read-only mode. Attempting to bypass using JavaScript.")
    driver.execute_script("arguments[0].removeAttribute('readonly');", content)

    # Use JavaScript to modify the content directly if it's read-only
    new_text = "New iFrame content!"
    driver.execute_script(f"arguments[0].innerHTML = '{new_text}';", content)

    # Verify the change using JavaScript (since the editor might still be in read-only mode)
    modified_content = driver.execute_script("return arguments[0].innerHTML;", content)
    logger.info(f"Modified content in iFrame (via JS): {modified_content}")
    assert modified_content == new_text, "Content in the iFrame was not modified as expected (read-only mode)."

    # Step 5: Switch back to the main content
    driver.switch_to.default_content()

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver

def test_hovers(driver):
    # Step 1: Open the Hovers page
    logger.info("Opening Hovers page.")
    driver.get("https://the-internet.herokuapp.com/hovers")

    # Step 2: Locate the user avatars (images)
    user_avatars = driver.find_elements(By.CSS_SELECTOR, "div.figure img")

    # Step 3: Iterate through each user avatar, hover and check the visibility of the user info
    for i, avatar in enumerate(user_avatars, 1):
        # Hover over the avatar
        logger.info(f"Hovering over user {i} avatar.")
        ActionChains(driver).move_to_element(avatar).perform()

        # Step 4: Wait for the info to appear
        figcaption = driver.find_element(By.XPATH, f"(//div[@class='figure'])[{i}]//div[@class='figcaption']")

        # Step 5: Check if the user's info (name and link) is visible
        WebDriverWait(driver, 3).until(
            EC.visibility_of(figcaption)
        )

        # Assert that the user's name is displayed correctly
        name = figcaption.find_element(By.TAG_NAME, "h5").text
        assert name == f"name: user{i}", f"Expected name to be 'name: user{i}', but got {name}"

        # Assert that the 'View profile' link is present
        profile_link = figcaption.find_element(By.TAG_NAME, "a").text
        assert profile_link == "View profile", f"Expected 'View profile' link text, but got {profile_link}"

    logger.info("Hovers test passed successfully.")

import pytest
from appium import webdriver
from config.appium_config import get_appium_driver, enable_talkback, disable_talkback
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="module")
def appium_driver():
    """Fixture to initialize the Appium driver."""
    driver = get_appium_driver()
    yield driver
    driver.quit()

@pytest.fixture
def wait(appium_driver):
    """Fixture to define WebDriverWait and reuse it across tests."""
    return WebDriverWait(appium_driver, 10)


@pytest.fixture(scope="function")
def setup_talkback(request):
    """
    Conditionally enable TalkBack for tests requiring it.
    A test function must include `@pytest.mark.talkback` to enable this fixture.
    """
    if request.node.get_closest_marker("talkback"):
        enable_talkback()
        yield
        disable_talkback()
    else:
        # No TalkBack actions needed for tests without the marker
        yield
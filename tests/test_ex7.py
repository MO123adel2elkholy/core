import pytest
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import os
import time
print('taking screen shots for your application ')
# tests.py


# this fuction is used to build take screen shotsc for your application
def take_screenshot(driver, name):
    time.sleep(1)
    os.makedirs(os.path.join(
        "screenshot", os.path.dirname(name)), exist_ok=True)
    driver.save_screenshot(os.path.join("screenshot", name))


# arrange fixture for selenium driver Phase1

@pytest.fixture
def selenium_driver(live_server):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=800,600")
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=options)
    yield driver
    driver.quit()


def test_screen_shots(live_server, selenium_driver):
    selenium_driver.get(("%s%s" % (live_server.url, "/admin/")))
    assert "Log in | Django site admin" in selenium_driver.title
    take_screenshot(selenium_driver, f"{selenium_driver.title}.png")

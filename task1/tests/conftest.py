import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def setup_browser():
    pytest.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def close_browser():
    print("close_browser")
    if pytest.browser is not None:
        pytest.browser.quit()


@pytest.fixture(autouse=True)
def base_test():
    setup_browser()
    yield
    close_browser()

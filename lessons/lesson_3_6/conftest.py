from selenium import webdriver

import pytest


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print("\nquit browser..")

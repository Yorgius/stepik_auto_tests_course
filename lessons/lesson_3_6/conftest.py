import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print("\nquit browser..")
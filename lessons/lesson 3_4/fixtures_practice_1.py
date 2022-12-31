from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    print("browser opened")
    yield browser
    browser.quit()
    print("browser closed")


@pytest.fixture(autouse=True)
def auto_fixture():
    print('auto fixture started')


class TestRegistrationForm:
    def test_reg_form_1(self, browser):
        browser.get("http://suninjuly.github.io/registration1.html")

        # Код, который заполняет обязательные поля
        browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first name')]").send_keys('alex')
        browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last name')]").send_keys('alex')
        browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]").send_keys('alex')

        # Отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text, "EXCEPT: WRONG TEXT"

    def test_reg_form_2(self, browser):
        browser.get("http://suninjuly.github.io/registration2.html")

        # Код, который заполняет обязательные поля
        browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first name')]").send_keys('alex')
        browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last name')]").send_keys('alex')
        browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]").send_keys('alex')

        # Отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text, "EXCEPT: WRONG TEXT"
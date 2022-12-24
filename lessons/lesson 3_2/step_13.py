from selenium import webdriver
from selenium.webdriver.common.by import By


import time
import unittest


class TestScraper(unittest.TestCase):
    def test_registration_form(self):

        links = [
            "http://suninjuly.github.io/registration1.html",
            "http://suninjuly.github.io/registration2.html"
        ]

        for link in links:

            browser = webdriver.Chrome()
            browser.get(link)

            # Код, который заполняет обязательные поля
            browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first name')]").send_keys('alex')
            browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last name')]").send_keys('alex')
            browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]").send_keys('alex')

            # ожидание перед нажатием на кнопку формы
            time.sleep(3)

            # Отправляем заполненную форму
            browser.find_element(By.CSS_SELECTOR, "button.btn").click()

            # ждем загрузки страницы
            time.sleep(3)

            # Проверяем, что смогли зарегистрироваться
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text, "Ololo WRONG TEXT"


if __name__ == "__main__":
    unittest.main()

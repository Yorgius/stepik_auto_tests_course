from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os


def work_with_form():
    dir_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir_path, 'txt_for_step_8.txt')
    try: 
        link = "http://suninjuly.github.io/file_input.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, "[placeholder*='first']").send_keys('alex')
        browser.find_element(By.CSS_SELECTOR, "[placeholder*='last']").send_keys('alex')
        browser.find_element(By.CSS_SELECTOR, "[placeholder*='email']").send_keys('alex')

        # Находим кнопку загрузки файла и передаем путь к файлу
        browser.find_element(By.ID, "file").send_keys(file_path)

        browser.find_element(By.TAG_NAME, 'button').click()
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    work_with_form()
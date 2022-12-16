from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math


# Вычисление функции от (x)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


# Функция для  автоматизированной работы на странице
def parse_page(url):
    try:
        browser = Chrome()
        browser.get(url)

        if WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100')):
            browser.find_element(By.ID, 'book').click()

        # Получаем значение (х)  и передаем в функцию вычисления
        x = browser.find_element(By.ID, 'input_value').text
        result = calc(x)

        # Взаимодействие с элементами страницы
        browser.find_element(By.ID, 'answer').send_keys(result)
        browser.find_element(By.ID, 'solve').click()
        
    finally:
        time.sleep(5)
        browser.quit()

if __name__ == '__main__':
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    parse_page(link)
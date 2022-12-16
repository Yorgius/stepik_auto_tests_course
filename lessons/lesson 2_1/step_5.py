from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def func():
    # Функция для  автоматизированной работы на странице

    link = 'https://suninjuly.github.io/math.html'
    try:
        browser = Chrome()
        browser.get(link)

        x = browser.find_element(By.ID, 'input_value')
        result = calc(x.text)

        browser.find_element(By.ID, 'answer').send_keys(result)
        browser.find_element(By.ID, 'robotCheckbox').click()
        browser.find_element(By.ID, 'robotsRule').click()
        browser.find_element(By.TAG_NAME, 'button').click()
    finally:
        time.sleep(5)
        browser.quit()


if __name__ == '__main__':
    func()
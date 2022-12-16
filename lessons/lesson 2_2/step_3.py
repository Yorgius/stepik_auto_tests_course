from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import math
import time

def calc(x, y):
  return str(int(x) + int(y))

def func():
    # Функция для  автоматизированной работы на странице

    link = 'http://suninjuly.github.io/selects1.html'
    try:
        browser = Chrome()
        browser.get(link)

        x = browser.find_element(By.ID, 'num1').text
        y = browser.find_element(By.ID, 'num2').text
        result = calc(x, y)

        select = Select(browser.find_element(By.ID, 'dropdown'))
        select.select_by_value(result)

        browser.find_element(By.TAG_NAME, 'button').click()
    finally:
        time.sleep(5)
        browser.quit()


if __name__ == '__main__':
    func()
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def func():
    # Функция для  автоматизированной работы на странице

    link = 'http://suninjuly.github.io/execute_script.html'
    try:
        browser = Chrome()
        browser.get(link)

        x = browser.find_element(By.ID, 'input_value').text
        result = calc(x)

        browser.find_element(By.ID, 'answer').send_keys(result)
        browser.find_element(By.ID, 'robotCheckbox').click()
        check = browser.find_element(By.ID, 'robotsRule')
        browser.execute_script("return arguments[0].scrollIntoView(true);", check)
        check.click()
        browser.find_element(By.TAG_NAME, 'button').click()

    finally:
        time.sleep(5)
        browser.quit()


if __name__ == '__main__':
    func()
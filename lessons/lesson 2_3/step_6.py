from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

import math
import time

# Вычисление функции от (x)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Функция для  автоматизированной работы на странице
def func():
    link = 'http://suninjuly.github.io/redirect_accept.html'

    try:
        browser = Chrome()
        browser.get(link)

        # Нажатие на кнопку button.btn
        browser.find_element(By.CSS_SELECTOR, "button.trollface").click()

        # Переключение на новую страницу
        new_window = browser.window_handles[-1]
        browser.switch_to.window(new_window)

        # Получаем значение (х)  и передаем в функцию вычисления
        x = browser.find_element(By.ID, 'input_value').text
        result = calc(x)

        # Взаимодействие с элементами страницы
        browser.find_element(By.ID, 'answer').send_keys(result)
        browser.find_element(By.TAG_NAME, 'button').click()

    finally:
        # Задержка перед закрытием окна браузера
        time.sleep(5)
        browser.quit()


if __name__ == '__main__':
    func()
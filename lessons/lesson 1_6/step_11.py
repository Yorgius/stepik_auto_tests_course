from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try: 
    link = "http://suninjuly.github.io/registration1.html"
    # link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first name')]").send_keys('alex')
    browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last name')]").send_keys('alex')
    browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]").send_keys('alex')

    time.sleep(3)

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
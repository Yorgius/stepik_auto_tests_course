from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from decouple import config

import pytest
import time
import math


def fill_in_the_authorization_form(browser):
    try:
        # дождаться кнопку авторизации и нажать её
        login_button = WebDriverWait(browser, 20).until(ec.presence_of_element_located((By.ID, 'ember33')))
        login_button.click()
        print('authorization button click')
        
        # отправить в инпут строку с логином
        email_input = browser.find_element(By.ID, 'id_login_email')
        email_input.send_keys(config('login', default=''))
        print('login send keys')

        # отправить в инпут строку с паролем
        psw_input = browser.find_element(By.ID, 'id_login_password')
        psw_input.send_keys(config('password', default=''))
        print('password send keys')

        # нажать кнопку отправки формы
        accept_login_button = browser.find_element(By.CLASS_NAME, 'sign-form__btn')
        accept_login_button.click()
        print('success button click')
    except Exception as e:
        assert False, f"Вызвано исключение во время авторизации: {e}"


@pytest.mark.parametrize('fragment', config('urls', cast=lambda urls: [url.strip() for url in urls.split(',')]))
def test_task_list(browser, fragment):
    browser.implicitly_wait(15)
    browser.get(f'https://stepik.org/lesson/{fragment}/step/1')
    
    fill_in_the_authorization_form(browser)
    
    # ожидане после авторизации
    time.sleep(5)
    
    try:
        # дождаться и получить элемент txtarea для ввода ответа на задание
        text_input = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'ember-text-area')))

        # элемент активен для ввода
        if not text_input.get_property('disabled'):
            text_input.send_keys(math.log(int(time.time())))
            print('enter result')

            # нажать button отправки формы
            accept_answer_button = browser.find_element(By.CLASS_NAME, 'submit-submission')
            accept_answer_button.click()
            print('success button click')
        
        # элемент найден
        print('already there is succes_message')
        success_message = WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))
        assert success_message.text == 'Correct!', success_message.text


    except Exception as e:
        assert False, f"Вызвано исключение: {e}"

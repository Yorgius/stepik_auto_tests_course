from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time


# Test authorization logic
def test_alien_message(browser):
    browser.get('https://stepik.org/lesson/236895/step/1')
    try:
        login_button = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.ID, 'ember33')))
        login_button.click()
        
        email_input = browser.find_element(By.ID, 'id_login_email')
        email_input.send_keys('test_login')

        psw_input = browser.find_element(By.ID, 'id_login_password')
        psw_input.send_keys('test_password')

        accept_button = browser.find_element(By.CLASS_NAME, 'sign-form__btn')
        accept_button.click()
        time.sleep(3)
    except Exception as e:
        print('some error happened', e)
from selenium.webdriver.common.by import By

import time


# test for the presence of the button <add to cart> on the page with different language settings
def test_check_for_add_to_cart_button(browser):
    url = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(url)

    # waiting to see the result
    time.sleep(5)

    add_to_cart_btns_in_page = browser.find_elements(
        By.CLASS_NAME,
        'btn-add-to-basket'
    )

    assert add_to_cart_btns_in_page, "<ADD TO CART> button not found for this site language setting"
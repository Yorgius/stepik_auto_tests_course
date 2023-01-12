from selenium.webdriver.common.by import By

import time


# test for the presence of the button <add to cart> on the page with different language settings
def test_func(browser_config: dict):
    browser: object = browser_config.get('browser')
    lang: str = browser_config.get('lang')

    url = f'http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/'
    browser.get(url)

    # waiting to see the result
    time.sleep(5)

    search_add_to_cart_btns_in_page = browser.find_elements(
        By.CLASS_NAME,
        'btn-add-to-basket'
    )

    assert search_add_to_cart_btns_in_page, f"<ADD TO CART> button not found for site <{lang}> language setting"
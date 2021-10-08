import time
from selenium.common.exceptions import NoSuchElementException
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_button(browser):
    try:
        browser.get(link)
        time.sleep(5)  # для визуальной проверки языка сайта
        button = browser.find_element_by_css_selector('#add_to_basket_form button')
        print('\nAdd to basket button found')
    except NoSuchElementException:  # для улучшения читабельности результатов теста (при ошибке NoSuchElementException)
        print('\nAdd to basket button not found')
        assert False,'Button not found'

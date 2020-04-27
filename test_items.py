from selenium.webdriver.common.by import By
import pytest
import time
from selenium import webdriver



class TestBasketBtn(object):
    def test_add_btn_is_available(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)

        #здесь можете поставить необходимое время для проверки надписи в браузере
        time.sleep(1)
        
        button = browser.find_element_by_css_selector(".btn-add-to-basket")

        #проверка: производится подсчет кнопок
        #если она одна, то переходим к print
        countOfBtns = len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"))

        #countOfBtns = 2 #можно раскомментить, чтоб проверить, что ассерт срабатывает
        #countOfBtns = 0 #можно раскомментить, чтоб проверить, что ассерт срабатывает

        if countOfBtns == 0:
            message = "Button not found"
        if countOfBtns > 1:
            message = "Selector is not unique"

        #если  0 = количество_кнопок или количество_кнопок > 1     
        assert countOfBtns == 1, message 

        #нужен ключ -s при запуске
        print ("Button is found, selector is unique")



import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_btn(browser, request):
    lang = request.config.getoption("--language")
    browser.get(link)
    
    wait = WebDriverWait(browser, 10)
    
    try:
        button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn-add-to-basket15')))
    except TimeoutException:
        assert False, 'Probably button "Add to basket" not found'
    


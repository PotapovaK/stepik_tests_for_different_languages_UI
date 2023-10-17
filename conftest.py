import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time

#"def pytest_addoption(parser)"функция, предоставляемая pytest для настройки пользовательских параметров командной строки. Она вызывается pytest перед началом тестов.
#"parser.addoption(...)"метод используется для добавления новой опции командной строки.
#'"--language"'аргумент командной строки, который я добавляю.
#'action="store"' Опция action="store" означает, что аргумент --language представляет собой значение, которое будет сохранено для дальнейшего использования.
#'help="specify language for tests"' Это описание аргумента, говорит что делает эта опция.

def pytest_addoption(parser):
    parser.addoption("--language", action="store", help="specify language for tests")
    
@pytest.fixture(scope="function")
def browser(request):
    language_UI = request.config.getoption("language")
    print(f"\nstart browser for test with language {language_UI}..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language_UI})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


    




import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default=None,
    #                 help="Choose browser: chrome or firefox")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: es or fr")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language=request.config.getoption("language")
    if language in ["en","fr"]:
        browser = None

        if browser_name == "chrome":
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
            print(f"\n Start chrome browser for test,language={language}...")
            browser = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", language)
            print(f"\n Start firefox browser for test,language={language}...")
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
    else:

        raise pytest.UsageError("--language should be en or fr")

    yield browser
    print("\n Quit browser..")
    browser.quit()

# конец


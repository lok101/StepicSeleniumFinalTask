from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Specify language")


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    if language is not None:
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--specify language")
    yield browser
    print("\nquit browser..")
    browser.quit()

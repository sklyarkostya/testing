import pytest
from selenium import webdriver


@pytest.fixture
def browser(request):
    """
    Fixture for initializing the browser and opening the homepage.
    When the test is over, the browser is closed.
    """

    driver = webdriver.Chrome()
    driver.get("https://dev1.urfu.ru/")
    driver.maximize_window()

    def fin():
        driver.close()
    request.addfinalizer(fin)

    return driver
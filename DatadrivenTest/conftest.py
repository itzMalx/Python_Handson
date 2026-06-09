import tempfile
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=["chrome", "firefox"])
def setup_and_teardown(request):

    # CHROME
    if request.param == "chrome":
        options = ChromeOptions()

        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    # FIREFOX
    elif request.param == "firefox":
        options = FirefoxOptions()

        options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")

    request.cls.driver = driver

    yield

    driver.quit()
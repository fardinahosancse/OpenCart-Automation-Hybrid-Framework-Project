from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import  allure
import pytest
from allure_commons.types import AttachmentType
global driver




#ErrorDetection#AdvanceExecution
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request,get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="miao", attachment_type=AttachmentType.PNG)




#Auto Browser Initialization
@pytest.fixture(params=["chrome"],scope="function")
def get_browser(request):
    if request.param =="chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version='114.0.5735.90').install()))

    #if request.param =="firefox":
        #driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    request.cls.driver = driver
    driver.get("http://localhost:8080/opencartsite/")
    driver.maximize_window()

    driver.implicitly_wait(20)
    yield driver
    driver.quit()

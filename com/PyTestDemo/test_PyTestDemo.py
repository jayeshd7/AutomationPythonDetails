from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class PyTestDemo():
    @pytest.fixture()
    def test_setup(self):
            global driver
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.implicitly_wait(10)
            driver.maximize_window()


    def test_openOrangeUrl(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        # Explicit wait
        driver.find_element_by_xpath("//input[@id='btnLogin']").click()
        title = driver.title
        assert title == "OrangeHRM"

    @pytest.yield_fixture()

    def test_tearDown(self):
        driver.close()
        driver.quit()







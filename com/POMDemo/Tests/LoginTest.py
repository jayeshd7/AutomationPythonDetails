

import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from com.POMDemo.Pages.LoginPages import LoginPage
from com.POMDemo.Pages.HomePages import HomePage
import HtmlTestRunner


class LoginTestCase(unittest.TestCase):
    # Class level setup
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_openOrangeUrl(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.submit_login()

        homepage = HomePage(driver)
        title = driver.title

        print(self.assertEqual(title, "OrangeHRM"))
        driver.implicitly_wait(3)
        homepage.click_welcome()
        driver.implicitly_wait(3)
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/jayeshdalal/PycharmProjects/AutomationPythonDetails/com/Reports', verbosity=2))






import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "....", "...."))

from com.POMDemo.Pages.LoginPages import LoginPage
from com.POMDemo.Pages.HomePages import HomePage
from com.POMDemo.utils import utils as utils



class LoginTestCase(unittest.TestCase):
    # Class level setup
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_openOrangeUrl(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.userName)
        login.enter_password(utils.password)
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
    unittest.main(verbosity=2)


'''
via command promat and run the test and genrated the reports.
python -m com.POMDemo.Tests.LoginTest

'''


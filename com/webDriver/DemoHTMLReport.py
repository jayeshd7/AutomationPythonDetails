import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner




class MyTestCase(unittest.TestCase):
    # Class level setup
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_openOrangeUrl(self):
        url = self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()
        title = self.driver.title
        print (title)
        print(self.driver.current_url)

        self.assertEqual(title, "OrangeHRM")

    def test_openGoogle(self):
        url = self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("automation step by step")
        # keys.keys (Enter )
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_name("q").send_keys(keys.Keys.ESCAPE)
        self.driver.find_element_by_name("btnK").click()
        self.driver.implicitly_wait(5)
        title = self.driver.title
        self.assertEqual(title, "automation step by step - Google Search")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/jayeshdalal/PycharmProjects/AutomationPythonDetails/com/Reports'),verbosity=2)



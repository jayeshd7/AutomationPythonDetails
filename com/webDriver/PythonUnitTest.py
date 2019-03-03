import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver =webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_openOrangeUrl(self):
        url = self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()
        title = self.driver.title
        print (title)
        print(self.driver.current_url)

        self.assertEqual(title,"OrangeHRM")



    def tearDown(self):
        self.driver.close()
        self.driver.quit()


'''
if __name__ == '__main__':
    unittest.main()
'''
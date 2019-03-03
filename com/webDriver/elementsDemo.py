from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager




def tearUp():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    login(driver)

def login(webdriver):
    driver.maximize_window()
    driver.refresh()
    url = driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
    driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
    driver.find_element_by_xpath("//input[@id='btnLogin']").click()
    print(driver.current_url)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    login()




from selenium import webdriver
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager

import time

driver =webdriver.Chrome(ChromeDriverManager().install())
url=driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("automation step by step")
#keys.keys (Enter )
driver.implicitly_wait(2)
driver.find_element_by_name("q").send_keys(keys.Keys.ESCAPE)

driver.find_element_by_xpath("//div[@class='FPdoLc VlcLAe']//input[@value=\"I\'m Feeling Lucky\"]").click()
#driver.find_element_by_name("btnK").click()
driver.implicitly_wait(5)
print(driver.current_url)
time.sleep(2)
driver.close();
driver.quit();











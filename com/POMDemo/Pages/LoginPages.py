from com.POMDemo.Locators.AllLocators import AllLocators

class LoginPage():


    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_xpath = AllLocators.username_textbox_xpath
        self.password_textbox_xpath = AllLocators.password_textbox_xpath
        self.submit_button_xpath = AllLocators.submit_button_xpath

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def submit_login(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()





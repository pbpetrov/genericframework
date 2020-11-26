from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import time
import  utilities.custom_logger as cl
import logging

class SignInPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# LOCATORS (the values are just examples)
    _login_link = "Sign in"
    _username_field = "user_emails"
    _password_field = "password"
    _email_field = "email"

# ACTIONS WITH PAGE OBJECTS
    def clickSignInLink(self):
        self.elementClick(self._login_link, locatorType="link" )
        time.sleep(5)

    def verifySignInPageIsLoaded(self):
        result = self.isElementPresent(self._username_field, locatorType="id")
        return result

    def enterUserName(self, username):
        self.sendKeys(username, self._username_field)
        time.sleep(3)

    def clearUserField(self):
        userField = self.getElement(self._username_field, locatorType='link')
        userField.clear()


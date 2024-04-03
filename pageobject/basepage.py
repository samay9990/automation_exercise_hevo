import time

from locators.basepage import BasePageLocators
from driverutils import DriverUtils
from configutils import ConfigUtils


class BasePage:

    def __init__(self):
        self.basepagelocators = BasePageLocators
        self.driver = DriverUtils()
        self.config = ConfigUtils()

    def navigate_to_url(self):
        """
        Navigating to url
        :return: None
        """
        self.driver.navigate_to_url()

    def sign_in(self):
        """
        Sign In
        :return: None
        """
        full_name = self.config.get_fullname()
        usermail = self.config.get_username()
        password = self.config.get_password()
        self.driver.send_keys_to_element(self.basepagelocators.full_name, full_name)
        self.driver.send_keys_to_element(self.basepagelocators.usermail, usermail)
        self.driver.send_keys_to_element(self.basepagelocators.password, password)
        self.driver.click_element(self.basepagelocators.submit_button)
        time.sleep(3)
        # self.driver.click_element(self.basepagelocators.reg_pwd).send_keys(password)
        # time.sleep(4)
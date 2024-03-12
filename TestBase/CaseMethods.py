import os
import sys

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from TestBase.TestBases import TestBase
from locators.locators import Locators


class CaseMethods(TestBase):


    def enter_firstname(self, locator, firstname):
        self.element_visible(locator).send_keys(firstname)

    def enter_lastname(self, locator, lastname):
        self.element_visible(locator).send_keys(lastname)

    def enter_email(self, locator, email):
        self.element_visible(locator).send_keys(email)

    def enter_password(self, locator, password):
        self.element_visible(locator).send_keys(password)

    def enter_repassword(self, locator, repassword):
        self.element_visible(locator).send_keys(repassword)

    def checking(self, val1, val2):
        assert val1 == val2

    def enter_country(self, countryId):
        country = f"[@value='{str(countryId)}']"
        by = self.locators.COUNTRY[0]
        xpath = self.locators.COUNTRY[1]+country
        locator = (by, xpath)
        self.element_visible(locator).click()

    def enter_city(self, city):
        self.element_visible(self.locators.CITY).send_keys(city)


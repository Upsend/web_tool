import os
import sys
sys.path.append(os.getcwd())
from TestBase.TestBases import TestBase
from locators.locators import Locators


class CaseMethods(TestBase):

    locators = Locators()

    def enter_firstname(self, firstname):
        self.element_visible(self.locators.FIRST_NAME).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.element_visible(self.locators.LAST_NAME).send_keys(lastname)

    def enter_email(self, email):
        self.element_visible(self.locators.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.element_visible(self.locators.PASSWORD).send_keys(password)

    def enter_repassword(self, repassword):
        self.element_visible(self.locators.REPASSWORD).send_keys(repassword)

    def checking(self, val1, val2):
        assert val1 == val2


import os
import sys
sys.path.append(os.getcwd())
from faker import Faker
from selenium.webdriver.common.by import By
from TestBase.CaseMethods import CaseMethods
from locators.locators import Locators


class TestRegister:

    locators = Locators
    fake = Faker("ru_RU")


    def test_registration_success(self, set_driver):
        """Успешная регистрация"""

        email = self.fake.ascii_free_email()

        web = CaseMethods(set_driver, "https://demowebshop.tricentis.com/")
        web.open()
        web.click(self.locators.REG_BTN)
        web.enter_firstname(self.fake.first_name())
        web.enter_lastname(self.fake.last_name())
        web.enter_email(email)
        web.enter_password(email)
        web.enter_repassword(email)
        web.click(self.locators.REGISTER_BUTTON)

        text = web.driver.find_element(By.CSS_SELECTOR, self.locators.FIN_FIELD).text
        acc_name = web.driver.find_element(By.CSS_SELECTOR, self.locators.ACC_NAME).text

        web.checking("Your registration completed", text)
        web.checking(acc_name, email)
        web.click(self.locators.CONTINUE_BUTTON)
        web.checking(web.getURL(), "https://demowebshop.tricentis.com/")

    def test_registration_wrong_characters(self, set_driver):
        """Проваленная регистарция не верные символы в тектовых полях"""

        #
        web = CaseMethods(set_driver, "https://demowebshop.tricentis.com/")
        web.open()
        web.click(self.locators.REG_BTN)

        web.enter_firstname("")
        web.click(self.locators.REGISTER_BUTTON)
        errorField = web.driver.find_element(By.XPATH, '//span[@data-valmsg-for="FirstName"]').text
        web.checking(errorField, "First name is required.")
        web.refresh()

        web.enter_lastname("")
        web.click(self.locators.REGISTER_BUTTON)
        errorField = web.driver.find_element(By.XPATH, '//span[@data-valmsg-for="LastName"]').text
        web.checking(errorField, "Last name is required.")
        web.refresh()

        web.enter_email("")
        web.click(self.locators.REGISTER_BUTTON)
        errorField = web.driver.find_element(By.XPATH, '//span[@data-valmsg-for="Email"]').text
        web.checking(errorField, "Email is required.")
        web.refresh()

        web.enter_email("asd@")
        web.click(self.locators.REGISTER_BUTTON)
        errorField = web.driver.find_element(By.XPATH, '//span[@data-valmsg-for="Email"]').text
        web.checking(errorField, "Wrong email")
        web.refresh()

        web.enter_email("asd@ede")
        web.click(self.locators.REGISTER_BUTTON)
        errorField = web.driver.find_element(By.XPATH, '//span[@data-valmsg-for="Email"]').text
        web.checking(errorField, "Wrong email")
        web.refresh()

        web.enter_password("123")
        web.enter_repassword("123")

        errorField = web.driver.find_element(By.XPATH, '//span[@data-valmsg-for="Password"]').text

        web.checking(errorField, "The password should have at least 6 characters.")
        web.refresh()
        web.enter_password("123123")
        web.enter_repassword("123")
        web.click(self.locators.REGISTER_BUTTON)

        errorField = web.driver.find_element(By.XPATH, '//span[@data-valmsg-for="ConfirmPassword"]').text

        web.checking(errorField, "The password and confirmation password do not match.")





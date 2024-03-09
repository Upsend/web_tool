import os
import sys
sys.path.append(os.getcwd())
import time
from faker import Faker
from selenium.webdriver.common.by import By
from TestBase.CaseMethods import CaseMethods
from locators.locators import Locators



class TestProfile:

    locators = Locators
    fake = Faker("ru_RU")

    def test_login_success(self, set_driver):

        web = CaseMethods(set_driver, "https://demowebshop.tricentis.com/")
        web.open()
        web.click(self.locators.LOGIN_BTN)
        web.enter_email('person09056@gmail.com')
        web.enter_password('123123')
        web.click(self.locators.LOG_IN_BUTTON)

        acc_name = web.driver.find_element(By.CSS_SELECTOR, self.locators.ACC_NAME).text

        web.checking(acc_name, 'person09056@gmail.com')

    def test_logout(self, set_driver):
        self.test_login_success(set_driver)
        web = CaseMethods(set_driver, "https://demowebshop.tricentis.com/")
        web.click(self.locators.LOGOUTBUTTON)

        url = web.getURL()

        web.checking(url, "https://demowebshop.tricentis.com/")
        web.element_visible(self.locators.REG_BTN)
        web.element_visible(self.locators.LOGIN_BTN)
        web.element_visible(self.locators.CART_BTN)
        web.element_visible(self.locators.WISHLIST_BTN)

    def test_change_acc_data(self, set_driver):

        self.test_login_success(set_driver)

        web = CaseMethods(set_driver, "https://demowebshop.tricentis.com/")
        acc_name = (By.CSS_SELECTOR, self.locators.ACC_NAME)
        web.click(acc_name)

        data = web.readfile("../data/AccountData.txt")

        firstname = web.driver.find_element(By.ID, self.locators.FIRST_NAME[1]).get_attribute('value')
        web.checking(firstname, data[0])

        lastname = web.driver.find_element(By.ID, self.locators.LAST_NAME[1]).get_attribute('value')
        web.checking(lastname, data[1])

        email = web.driver.find_element(By.ID, self.locators.EMAIL[1]).get_attribute('value')
        web.checking(email, data[2])

        web.driver.find_element(By.ID, self.locators.FIRST_NAME[1]).clear()
        web.driver.find_element(By.ID, self.locators.LAST_NAME[1]).clear()
        web.driver.find_element(By.ID, self.locators.EMAIL[1]).clear()

        web.writeFile("../data/AccountData.txt", "Danil\n"
                                                 "Azizov\n"
                                                 "person09056@gmail.com")
        data = web.readfile("../data/AccountData.txt")

        web.enter_firstname(data[0])
        web.enter_lastname(data[1])
        web.enter_email(data[2])
        web.click(self.locators.SAVE_BUTTON)

        errorFields = web.driver.find_elements(By.CSS_SELECTOR, self.locators.ERR_FIELD[1])

        for field in errorFields:
            web.checking("", field.text)

    def test_change_acc_data_wrong(self, set_driver):

        self.test_change_acc_data(set_driver)
        web = CaseMethods(set_driver, "https://demowebshop.tricentis.com/")

        web.driver.find_element(By.ID, self.locators.FIRST_NAME[1]).clear()
        web.driver.find_element(By.ID, self.locators.LAST_NAME[1]).clear()
        web.driver.find_element(By.ID, self.locators.EMAIL[1]).clear()

        web.writeFile("../data/AccountData.txt", "\n"
                                                 "\n"
                                                 "person09056@gmail")
        data = web.readfile("../data/AccountData.txt")

        web.enter_firstname(data[0])
        web.enter_lastname(data[1])
        web.enter_email(data[2])
        web.click(self.locators.SAVE_BUTTON)

        errorFields = web.driver.find_elements(By.CSS_SELECTOR, self.locators.ERR_FIELD[1])

        web.checking("First name is required.", errorFields[0].text)
        web.checking("Last name is required.", errorFields[1].text)
        web.checking("Wrong email", errorFields[2].text)

        #Возвращаем данные в исходное состояние
        web.writeFile("../data/AccountData.txt", "Danil\n"
                                                 "Azizov\n"
                                                 "person09056@gmail.com")












import os
import sys
sys.path.append(os.getcwd())
import time
from faker import Faker
from selenium.webdriver.common.by import By
from TestBase.CaseMethods import CaseMethods
from locators.default_locators import Locators
from locators.address_locators import AddressLocators



class TestProfile:

    locators = Locators
    addr_locators = AddressLocators
    fake = Faker("ru_RU")

    def test_login_success(self, set_driver):

        web = CaseMethods(set_driver, "https://demowebshop.tricentis.com/")
        web.open()
        web.click(self.locators.LOGIN_BTN)
        web.enter_email(self.locators.EMAIL, 'person09056@gmail.com')
        web.enter_password(self.locators.PASSWORD, '123123')
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

        web.enter_firstname(self.locators.FIRST_NAME, data[0])
        web.enter_lastname(self.locators.LAST_NAME, data[1])
        web.enter_email(self.locators.EMAIL, data[2])
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

        web.enter_firstname(self.locators.FIRST_NAME, data[0])
        web.enter_lastname(self.locators.LAST_NAME, data[1])
        web.enter_email(self.locators.EMAIL, data[2])
        web.click(self.locators.SAVE_BUTTON)

        errorFields = web.driver.find_elements(By.CSS_SELECTOR, self.locators.ERR_FIELD[1])

        web.checking("First name is required.", errorFields[0].text)
        web.checking("Last name is required.", errorFields[1].text)
        web.checking("Wrong email", errorFields[2].text)

        #Возвращаем данные в исходное состояние
        web.writeFile("../data/AccountData.txt", "Danil\n"
                                                 "Azizov\n"
                                                 "person09056@gmail.com")



    def test_add_address(self, set_driver):

        self.test_login_success(set_driver)
        web = CaseMethods(set_driver, "https://demowebshop.tricentis.com/")
        data = web.readfile("../data/AccountData.txt")

        firstname = data[0]
        lastname = data[1]
        email = data[2]
        country = self.fake.country()
        city = self.fake.city()
        address = self.fake.address()
        zipcode = self.fake.postcode()
        phone = self.fake.phone_number()

        acc_name = (By.CSS_SELECTOR, self.locators.ACC_NAME)
        web.click(acc_name)
        web.click(self.locators.ADDRESSES)
        web.click(self.addr_locators.NEW_ADDR_BTN)

        # проверяем, что поля firstname, lastname, email заполнены по умолчанию

        # firstname_default_value = web.driver.find_element(By.ID, self.locators.FIRST_NAME[1]).get_attribute('value')
        # web.checking(firstname, firstname_default_value)
        #
        # lastname_default_value = web.driver.find_element(By.ID, self.locators.LAST_NAME[1]).get_attribute('value')
        # web.checking(lastname, lastname_default_value)
        #
        # email_default_value = web.driver.find_element(By.ID, self.locators.EMAIL[1]).get_attribute('value')
        # web.checking(email, email_default_value)

        web.enter_firstname(self.addr_locators.FIRST_NAME, "Danil")
        web.enter_lastname(self.addr_locators.LAST_NAME, "Azizov")
        web.enter_email(self.addr_locators.EMAIL, "person09056@gmail.com")


        web.enter_country("88")
        web.enter_city(city)
        web.enter_address(address)
        web.enter_zip(zipcode)
        web.enter_phoneNumber(phone)
        web.click(self.addr_locators.SAVE_ADDRESS_BUTTON)

        #Проверяем, что введенные данные записались верно

        title = web.driver.find_element(By.XPATH, self.addr_locators.RES_TITLE[1]).text
        name = web.driver.find_element(By.CSS_SELECTOR, self.addr_locators.RES_NAME[1]).text
        mail = web.driver.find_element(By.CSS_SELECTOR, self.addr_locators.RES_EMAIL[1]).text
        phone_num = web.driver.find_element(By.CSS_SELECTOR, self.addr_locators.RES_PHONE[1]).text

        web.checking(title, f"{firstname} {lastname}")
        web.checking(name, f"{firstname} {lastname}")
        web.checking(mail, f"Email: {email}")
        web.checking(phone_num, f"Phone number: {phone}")

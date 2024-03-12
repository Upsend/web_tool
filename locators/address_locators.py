from selenium.webdriver.common.by import By


class AddressLocators:

    FIRST_NAME = (By.CSS_SELECTOR, "#Address_FirstName")
    LAST_NAME = (By.CSS_SELECTOR, "#Address_LastName")
    EMAIL = (By.CSS_SELECTOR, "#Address_Email")
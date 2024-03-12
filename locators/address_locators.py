from selenium.webdriver.common.by import By


class AddressLocators:
    """Локаторы на форме создания адреса"""

    FIRST_NAME = (By.CSS_SELECTOR, "#Address_FirstName")
    LAST_NAME = (By.CSS_SELECTOR, "#Address_LastName")
    EMAIL = (By.CSS_SELECTOR, "#Address_Email")
    ADDRESS1 = (By.CSS_SELECTOR, "#Address_Address1")
    POSTAL_CODE = (By.CSS_SELECTOR, "#Address_ZipPostalCode")
    PHONE_NUNBER = (By.CSS_SELECTOR, "#Address_PhoneNumber")
    COUNTRY = (By.XPATH, "//select[@id='Address_CountryId']/option")
    CITY = (By.CSS_SELECTOR, "#Address_City")

    """Кнопки на форме"""

    NEW_ADDR_BTN = (By.CSS_SELECTOR, ".add-address-button")
    SAVE_ADDRESS_BUTTON = (By.CSS_SELECTOR, ".save-address-button")

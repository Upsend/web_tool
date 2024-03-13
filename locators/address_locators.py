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

    """Поля в заолненном адресе"""

    RES_TITLE = (By.XPATH, "//div[@class='section address-item']/div[@class='title']/strong")
    RES_NAME = (By.CSS_SELECTOR, ".name")
    RES_EMAIL = (By.CSS_SELECTOR, ".email")
    RES_PHONE = (By.CSS_SELECTOR, ".phone")
    RED_ADDRESS1 = (By.CSS_SELECTOR, ".address1")
    RES_STATE_ZIP = (By.CSS_SELECTOR, ".city-state-zip")
    RES_COUNTRY = (By.CSS_SELECTOR, ".country")

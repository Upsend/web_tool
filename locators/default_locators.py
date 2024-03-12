from selenium.webdriver.common.by import By


class Locators:

    """Локаторы форм на странице"""

    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    EMAIL = (By.ID, "Email")

    PASSWORD = (By.ID, "Password")
    REPASSWORD = (By.ID, "ConfirmPassword")
    COUNTRY = ()
    CITY = ()
    ADDRESS = ()
    ZIP_CODE = ()
    PHONE_NUMBER = ()

    """Локаторы меню"""

    REG_BTN = (By.XPATH, "//a[text()='Register']")
    LOGIN_BTN = (By.XPATH, "//a[text()='Log in']")
    CART_BTN = (By.XPATH, "//span[text()='Shopping cart']")
    WISHLIST_BTN = (By.XPATH, "//span[text()='Wishlist']")
    ACC_NAME = ".header-links ul li a.account"

    """Кнопки"""

    REGISTER_BUTTON = (By.ID, "register-button")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, ".login-button")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".save-customer-info-button")
    LOGOUTBUTTON = (By.CSS_SELECTOR, ".ico-logout")

    """Локаторы в поле логина и регистрации"""

    FIN_FIELD = "div.result"
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".buttons .register-continue-button")
    ERR_FIELD = (By.CSS_SELECTOR, ".field-validation-error")


    """Локаторы сайдбара MY ACCOUNT"""

    CUSTOMER_INFO = (By.XPATH, "//a[text()='Customer info']")
    ADDRESSES = (By.XPATH, "//ul[@class='list']/li/a[text()='Addresses']")
    ORDERS = (By.XPATH, "//a[text()='Orders']")



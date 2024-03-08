from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class TestBase():

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def refresh(self):
        self.driver.refresh()

    def getURL(self):
        return self.driver.current_url

    def click(self, locator):
        self.element_visible(locator).click()

    def readfile(self, filename):
        with open(filename, "r") as file:
            data = []
            for line in file:
                data.append(line)
            data = [elem.rstrip() for elem in data]
        return data

    def writeFile(self, filename, filedata):
        with open(filename, "w") as file:
            file.write(filedata)

    def element_visible(self, locator):
        return wait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
    def all_elements_visible(self, locator):
        return wait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(locator)
        )




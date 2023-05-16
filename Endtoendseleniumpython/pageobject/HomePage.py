import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    name = (By.XPATH, '//input[@name="name"]')
    email = (By.XPATH, '//input[@name="email"]')
    password = (By.XPATH, '//input[@id="exampleInputPassword1"]')
    iceCream = (By.XPATH, '//input[@id="exampleCheck1"]')
    gender =  (By.CSS_SELECTOR, 'select[id="exampleFormControlSelect1"]')
    radiobtn = (By.CSS_SELECTOR, 'input[id="inlineRadio2"]')
    dob = (By.CSS_SELECTOR, 'input[name="bday"]')
    submitbtn = (By.CSS_SELECTOR, 'input[type="submit"]')
    successtext = (By.CSS_SELECTOR,'div[class="alert alert-success alert-dismissible"] strong')

    def __init__(self,driver):
        self.driver = driver

    def entername(self):
        return self.driver.find_element(*HomePage.name)
    def enteremail(self):
        return self.driver.find_element(*HomePage.email)
    def enterpass(self):
        return self.driver.find_element(*HomePage.password)
    def clickicecream(self):
        return self.driver.find_element(*HomePage.iceCream)
    def selectgender(self):
      return self.driver.find_element(*HomePage.gender)
    def clickradiobtn(self):
        return self.driver.find_element(*HomePage.radiobtn)
    def enterdob(self):
        return self.driver.find_element(*HomePage.dob)
    def clicksubmitbtn(self):
        return self.driver.find_element(*HomePage.submitbtn)
    def succesmessage(self):
        return self.driver.find_element(*HomePage.successtext)
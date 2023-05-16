#report.html will open in browser
#You have to copy the path reference and past it in your browser



import pytest
from selenium.webdriver.support.select import Select

from Utilties.BaseClass import BaseClass
from pageobject.HomePage import HomePage

class Test_FormSubmission(BaseClass):

    def test_formfill(self, getData):

        log = self.getLogger()
        homepage = HomePage(self.driver)
        # log.info logs every step where it is used
        #to understand it beter just open the "logfile.log" in the tests folder of your project.
        homepage.entername().send_keys(getData["name"])
        log.info("Entering Name")
        homepage.enteremail().send_keys(getData["email"])
        log.info("Entering Email")
        homepage.enterpass().send_keys(getData["password"])
        log.info("Entering pass")
        homepage.clickicecream().click()
        log.info("Clicking box")
        select = Select(homepage.selectgender())
        select.select_by_visible_text(getData["gender"])
        log.info("Entering gender")
        homepage.clickradiobtn().click()
        log.info("Clicking")
        homepage.enterdob().send_keys(getData["dob"])
        log.info("date of birth")
        homepage.clicksubmitbtn().click()
        log.info("Submitting")
        alerttext = homepage.succesmessage().text
        assert "Success" in alerttext
        self.driver.refresh()

    @pytest.fixture(params=[{"name" : "Jay", "email" : "Abc@gmail.com", "password" : "ABCDEF", "gender" : "Male", "dob": "12-12-1212"},
                            {"name" : "Vijay" , "email" : "bbc@gmail.com", "password" : "ABCDEF", "gender" : "Male", "dob": "13-13-1313"},
                            {"name" : "Jaya", "email" : "fbc@gmail.com", "password" : "ABCDEF", "gender" : "Female", "dob": "14-14-1414"}])

    def getData(self, request):
        return request.param








import sys, unittest, FlipTixShell, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

'''
    FlipTix selenium front end testing.
    
    Purpose - 
    
    Notes - Must have the latest driver and selenium bindings.
            http://seleniumhq.github.io/selenium/docs/api/py/index.html

    Method signature:

    
    Required:
  

    Test cases

'''
class TestGuiFrontEnd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.driver = webdriver.Firefox()
            cls.driver.get("https://www.fliptix.com/register/")
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.close()
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])



    def test_registration_landing(self):
        # Ensure we are on the correct page.
        self.assertIn("Register — FlipTix", self.driver.title, msg='Landing page failed.') 



    def test_register(self):
        # Enter the [Sell Tickets] button.
        self.driver.find_element_by_id(id_="block-yui_3_17_2_1_1533002875118_25794").click()
        # Enter an email address.
        self.driver.find_element_by_id(id_="email-yui_3_17_2_1_1533002875118_25800-field").send_keys(FlipTixShell.data['testVerifiedEmail'])
        # Enter a first name.
        self.driver.find_element_by_name(name='fname').send_keys(FlipTixShell.data['testFirstName'])
        # Enter a last name.
        self.driver.find_element_by_name(name='lname').send_keys(FlipTixShell.data['testLastName'])
        # Enter the area code.
        self.driver.find_element_by_xpath('//input[@data-title="Areacode"][@x-autocompletetype="phone-area-code"]').send_keys('714')
        # Enter next 3 digits.
        self.driver.find_element_by_xpath('//input[@data-title="Prefix"][@x-autocompletetype="phone-local-prefix"]').send_keys('222')
         # Enter final 4 digits.
        self.driver.find_element_by_xpath('//input[@data-title="Line"][@x-autocompletetype="phone-local-suffix"]').send_keys('1234')
        # Enter a password.
        self.driver.find_element_by_id(id_="password-yui_3_17_2_1_1533001026537_150664-field").send_keys(FlipTixShell.data['password'])

        time.sleep(5)





    # *********************************************************************
    # *                         VerifyBy tests                            *
    # *********************************************************************






def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestGuiFrontEnd('test_registration_landing'))
    suite.addTest(TestGuiFrontEnd('test_register'))

    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())



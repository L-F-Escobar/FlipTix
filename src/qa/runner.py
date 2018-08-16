import unittest, xmlrunner, os

from test import testRegisterUser
from test import testResendCode
from test import testLogin
from test import testLogoutLoginCheck # This one is 2 endpoints
from test import testGetUserById
from test import testVerifyUser
from test import testSendForgotPassword
from test import testChangePassword
from test import testVerifyForgotPasswordCode
from test import testSmokeGUI

# Initialize a test loader & test suite package.
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.suiteClass(testRegisterUser.suite())) #~REVIEWED         
suite.addTests(loader.suiteClass(testResendCode.suite())) #~REVIEWED      
suite.addTests(loader.suiteClass(testLogin.suite())) #~REVIEWED
suite.addTests(loader.suiteClass(testLogoutLoginCheck.suite())) #~REVIEWED
suite.addTests(loader.suiteClass(testGetUserById.suite())) #~REVIEWED
suite.addTests(loader.suiteClass(testVerifyUser.suite())) #~REVIEWED      
suite.addTests(loader.suiteClass(testSendForgotPassword.suite())) #~REVIEWED 
suite.addTests(loader.suiteClass(testChangePassword.suite())) #~REVIEWED               
suite.addTests(loader.suiteClass(testVerifyForgotPasswordCode.suite())) #~REVIEWED
# suite.addTests(loader.suiteClass(testSmokeGUI.suite()))

# Initialize an xml runner.
testRunner=xmlrunner.XMLTestRunner(output='data/testReports', verbosity=2)
 
# Run the suite & save the results.
results = testRunner.run(suite)
  
print(results)
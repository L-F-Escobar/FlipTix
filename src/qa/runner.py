import unittest, xmlrunner, os

from test import testRegisterUser
from test import testResendCode
from test import testLogin
from test import testLogoutLoginCheck # This one is 2 endpoints
from test import testGetUserById
from test import testVerifyUser
from test import testSendForgotPassword

# Initialize a test loader & test suite package.
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# suite.addTests(loader.suiteClass(testRegisterUser.suite()))
# suite.addTests(loader.suiteClass(testResendCode.suite()))
# suite.addTests(loader.suiteClass(testLogin.suite()))
# suite.addTests(loader.suiteClass(testLogoutLoginCheck.suite()))
# suite.addTests(loader.suiteClass(testGetUserById.suite()))
# suite.addTests(loader.suiteClass(testVerifyUser.suite()))
suite.addTests(loader.suiteClass(testSendForgotPassword.suite()))

# Initialize an xml runner.
testRunner=xmlrunner.XMLTestRunner(output='data/testReports', verbosity=2)
 
# Run the suite & save the results.
results = testRunner.run(suite)
  
print(results)
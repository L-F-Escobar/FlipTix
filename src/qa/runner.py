import unittest, xmlrunner, os

from test import testRegisterUser
from test import testResendCode

# Initialize a test loader & test suite package.
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# suite.addTests(loader.suiteClass(testRegisterUser.suite()))
suite.addTests(loader.suiteClass(testResendCode.suite()))

# Initialize an xml runner.
testRunner=xmlrunner.XMLTestRunner(output='data/testReports', verbosity=2)
 
# Run the suite & save the results.
results = testRunner.run(suite)
  
print(results)
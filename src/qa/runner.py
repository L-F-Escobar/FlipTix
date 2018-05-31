# import unittest, xmlrunner, os

# from test import  testGetTeamByLeague 
# from test import testForgotPassword
# from test import testGetReelTypes
# from test import testGetLeague
# from test import  testLogin
# from test import testConfirmRegistration
# from test import  testResendConfirmation
# from test import testCreateVideo
# from test import testGetVideoById
# from test import testDeleteVideo
# from test import testGetStoredVideos
# from test import testGetVideos

# # Initialize a test loader & test suite package.
# loader = unittest.TestLoader()
# suite  = unittest.TestSuite()

# suite.addTests(loader.suiteClass(testLogin.suite()))
# suite.addTests(loader.suiteClass(testForgotPassword.suite()))
# suite.addTests(loader.suiteClass(testGetReelTypes.suite()))
# suite.addTests(loader.suiteClass(testGetLeague.suite()))
# suite.addTests(loader.suiteClass(testResendConfirmation.suite()))
# suite.addTests(loader.suiteClass(testConfirmRegistration.suite()))
# suite.addTests(loader.suiteClass(testGetTeamByLeague.suite()))
# suite.addTests(loader.suiteClass(testCreateVideo.suite()))
# suite.addTests(loader.suiteClass(testGetVideoById.suite()))
# suite.addTests(loader.suiteClass(testDeleteVideo.suite()))
# suite.addTests(loader.suiteClass(testGetStoredVideos.suite())) # Currently returns {} always
# suite.addTests(loader.suiteClass(testGetVideos.suite()))

# # Initialize an xml runner.
# testRunner=xmlrunner.XMLTestRunner(output='data/testReports', verbosity=2)
 
# # Run the suite & save the results.
# results = testRunner.run(suite)
  
# print(results)
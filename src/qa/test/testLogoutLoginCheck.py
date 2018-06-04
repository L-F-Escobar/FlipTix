import sys, unittest, FlipTixShell

'''
    FlipTix logout & login check end point.
    
    Purpose - logs out a user who was previously logged in.
              checks the log in status of a user
    
    Notes - 

    Method signature:
        def logout(self, Authorization='', AuthorizationExclude=False):
        def login_check(self, Authorization='', cookies={}, AuthorizationExclude=False):
    
    Required:
        Authorization

    Test cases
        Successfully log out.

        Attempt to log out a user that is already logged out. 

        Attempt to log out with invalid auth key data.
'''
class TestLogout(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.user = FlipTixShell.FlipTix()   
            cls.user.login(email = FlipTixShell.data['testVerifiedEmail'], 
                           password = FlipTixShell.data['testPassword'])
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            pass
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])
    



    # Test successfully logging out.
    def test_success(self):
        responseBody = self.user.login_check(Authorization = self.user.GetSessionToken(),
                                             cookies = self.user.GetCookies())
        
        self.assertEqual(responseBody['result'], 'Logged in', 
                         msg= 'test_Success assert#1 has failed.')

        responseBody = self.user.logout(Authorization = self.user.GetSessionToken())
        
        self.assertEqual(responseBody['result'], 'Logged out', 
                         msg= 'test_Success assert#2 has failed.')

        responseBody = self.user.login_check(Authorization = self.user.GetSessionToken(),
                                             cookies = self.user.GetCookies())
        
        self.assertEqual(responseBody['error'], 'Token is no longer valid', 
                         msg= 'test_Success assert#3 has failed.')
    
    
        
    # Attempting to log out a user which was previously logged in.
    @unittest.skip("Should not work - user should already be logged out (BUG)")
    def test_doubleLogout(self):
        responseBody = self.user.login_check(Authorization = self.user.GetSessionToken(),
                                             cookies = self.user.GetCookies())
        
        self.assertEqual(responseBody['error'], 'Token is no longer valid', 
                         msg= 'test_doubleLogout assert#1 has failed.')

        responseBody = self.user.logout(Authorization = self.user.GetSessionToken())

        self.assertEqual(responseBody['result'], 'Logged out', 
                         msg='test_doubleLogout assert#2 has failed.')
        
        
        
    # Invalid authorization data.
    @unittest.skip("Should not work - user is hitting endpt with invalid auth key (BUG)")
    def test_invalidAuthorization(self):
        self.user.login(email = FlipTixShell.data['testVerifiedEmail'], 
                        password = FlipTixShell.data['testPassword'])
        
        responseBody = self.user.login_check(Authorization = self.user.GetSessionToken(),
                                             cookies = self.user.GetCookies())
        
        self.assertEqual(responseBody['result'], 'Logged in', 
                         msg= 'test_doubleLogout assert#1 has failed.')

        responseBody = self.user.logout(Authorization = 'invalid authorization')

        self.assertEqual(responseBody['result'], 'Logged out', 
                          msg='test_invalidAuthorization assert#1 has failed.')





def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestLogout('test_success'))
    suite.addTest(TestLogout('test_doubleLogout'))
    suite.addTest(TestLogout('test_invalidAuthorization'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
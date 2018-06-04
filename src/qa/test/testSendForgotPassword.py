import sys, unittest, FlipTixShell

'''
    FlipTix send forgot password end point.
    
    Purpose - sends a verification code to the users registered email. 
    
    Notes - 

    Method signature:
        def send_forgot_password(self, email='', emailExclude=False):
    
    Required:
        email

    Test cases
        Successfully successfully sending a verification code to the users email.

        Email missing from request call.
        Null Email value. 
        Int Email value.    
        Float Email value.   
        String Email value.
        Array Email value.  
'''
class TestSendForgotPassword(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.user = FlipTixShell.FlipTix()      
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            pass
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])
    



    # Test successfully sending a verification code to the users email.
    def test_success(self):
        # Log in.
        responseBody = self.user.send_forgot_password(email = FlipTixShell.data['testVerifiedEmail'])
        
        self.assertEqual(responseBody['result'], "Verification code has been sent. Please check your email.", 
                         msg= 'test_Success assert#1 has failed.')



    
    # *********************************************************************
    # *                         Email tests                               *
    # *********************************************************************
    
    
        
    # Missing Email information from request call.
    def test_missingEmail(self):
        # Missing Email value.
        responseBody = self.user.send_forgot_password(email = FlipTixShell.data['testVerifiedEmail'],
                                                      emailExclude = True)

        self.assertEqual(responseBody['error'], "Please submit a user email",
                         msg='test_missingEmail assert#1 has failed.')
        
        
        
    # Test a null Email.
    def test_nullEmail(self):
        # Null Email value.
        responseBody = self.user.send_forgot_password(email = '')

        self.assertEqual(responseBody['error'], "Please submit a user email",
                          msg='test_nullEmail assert#1 has failed.')



    # Test a int Email.
    @unittest.skip("Email parameter can be any integar value - (BUG)")
    def test_intEmail(self):
        # Int Email value.
        responseBody = self.user.send_forgot_password(email = 1)

        self.assertEqual(responseBody['error'], "",
                          msg='test_intEmail assert#1 has failed.')



    # Test a float Email.
    @unittest.skip("Email parameter can be any float value - (BUG)")
    def test_floatEmail(self):
        # Float Email value.
        responseBody = self.user.send_forgot_password(email = 1.2)

        self.assertEqual(responseBody['error'], "",
                          msg='test_floatEmail assert#1 has failed.')
        
        
        
    # Test a string Email value call.
    @unittest.skip("Email parameter can be any string value - (BUG)")
    def test_stringEmail(self):
        # String Email value.
        responseBody = self.user.send_forgot_password(email = 'This is not proper email format.')

        self.assertEqual(responseBody['error'], "",
                          msg='test_stringEmail assert#1 has failed.')



    # Test an array Email value call.
    @unittest.skip("Email parameter can be any string value - (BUG)")
    def test_arrayEmail(self):
        # Array Email value.
        responseBody = self.user.send_forgot_password(email = ['Invalid email format'])

        self.assertEqual(responseBody['error'], "",
                          msg='test_arrayEmail assert#1 has failed.')


    


def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestSendForgotPassword('test_success'))

    suite.addTest(TestSendForgotPassword('test_missingEmail'))
    suite.addTest(TestSendForgotPassword('test_nullEmail'))
    suite.addTest(TestSendForgotPassword('test_intEmail'))
    suite.addTest(TestSendForgotPassword('test_floatEmail'))
    suite.addTest(TestSendForgotPassword('test_stringEmail'))
    suite.addTest(TestSendForgotPassword('test_arrayEmail'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
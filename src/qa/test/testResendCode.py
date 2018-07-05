import sys, unittest, FlipTixShell

'''
    FlipTix registration end point.
    
    Purpose - endpoint send a verification code to the registered users email.
    
    Notes - 

    Method signature:
        def resend_code(self, verifyBy='', email='', verifyByExclude=False,  emailExclude=False):
    
    Required:
        verifyBy
        email

    Test cases
        Successfully re-send a verificatoin code.

        VerifyBy missing from request call.
        Null VerifyBy value. 
        Int VerifyBy value.    
        Float VerifyBy value.   
        String VerifyBy value.
        Array VerifyBy value.  

        Email missing from request call.
        Null Email value. 
        Int Email value.    
        Float Email value.   
        String Email value.
        Array Email value.  
'''
class TestResendCode(unittest.TestCase):

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
    



    # Test successfully resending a verification code.
    def test_success(self):
        # Log in.
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             email = FlipTixShell.data['testEmail'])
        
        self.assertEqual(responseBody['result'], "saved!", 
                         msg= 'test_Success assert#1 has failed.')




    # *********************************************************************
    # *                         VerifyBy tests                            *
    # *********************************************************************
    
    
        
    # Missing VerifyBy information from request call.
    def test_missingVerifyBy(self):
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             email = FlipTixShell.data['testEmail'],
                                             verifyByExclude = True)

        self.assertEqual(responseBody['error'], "Please specify email or phone",
                         msg='test_missingVerifyBy assert#1 has failed.')
        
        
        
    # Test a null VerifyBy.
    def test_nullVerifyBy(self):
        responseBody = self.user.resend_code(verifyBy = '',
                                             email = FlipTixShell.data['testEmail'])

        self.assertEqual(responseBody['error'], "Please specify email or phone",
                          msg='test_nullVerifyBy assert#1 has failed.')



    # Test a int VerifyBy.
    def test_intVerifyBy(self):
        responseBody = self.user.resend_code(verifyBy = 123456,
                                             email = FlipTixShell.data['testEmail'])

        self.assertEqual(responseBody['error'], "Please specify email or phone",
                          msg='test_intVerifyBy assert#1 has failed.')



    # Test a float VerifyBy.
    def test_floatVerifyBy(self):
        responseBody = self.user.resend_code(verifyBy = 1234.56,
                                             email = FlipTixShell.data['testEmail'])

        self.assertEqual(responseBody['error'], "Please specify email or phone",
                          msg='test_floatVerifyBy assert#1 has failed.')
        
        
        
    # Test a string VerifyBy value call.
    def test_stringVerifyBy(self):
        responseBody = self.user.resend_code(verifyBy = "This should not work",
                                             email = FlipTixShell.data['testEmail'])

        self.assertEqual(responseBody['error'], "Please specify email or phone",
                          msg='test_stringVerifyBy assert#1 has failed.')



    # Test an array VerifyBy value call.
    def test_arrayVerifyBy(self):
        responseBody = self.user.resend_code(verifyBy = ["This should not work", 123, 1.2],
                                             email = FlipTixShell.data['testEmail'])

        self.assertEqual(responseBody['error'], "Please specify email or phone",
                          msg='test_arrayVerifyBy assert#1 has failed.')



    
    # *********************************************************************
    # *                         Email tests                               *
    # *********************************************************************
    
    
        
    # Missing Email information from request call.
    def test_missingEmail(self):
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             email = FlipTixShell.data['testEmail'],
                                             emailExclude = True)

        self.assertEqual(responseBody['error'], "Please submit an email",
                         msg='test_missingEmail assert#1 has failed.')
        
        
        
    # Test a null Email.
    def test_nullEmail(self):
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             email = '')

        self.assertEqual(responseBody['error'], "Please submit an email",
                          msg='test_nullEmail assert#1 has failed.')



    # Test a int Email.
    # @unittest.skip("Email parameter can be any integar value - (BUG)")
    def test_intEmail(self):
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             email = 513516813158)

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_intEmail assert#1 has failed.')



    # Test a float Email.
    def test_floatEmail(self):
        # Float Email value.
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             email = 1.1)

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_floatEmail assert#1 has failed.')
        
        
        
    # Test a string Email value call.
    # @unittest.skip("Email parameter can be any string value - (BUG)")
    def test_stringEmail(self):
        # String Email value.
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             email = "This is not a valid email format!")

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_stringEmail assert#1 has failed.')



    # Test an array Email value call.
    # @unittest.skip("Email parameter can be any string value - (BUG)")
    def test_arrayEmail(self):
        # Array Email value.
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             email = "Email formats are not encased in arrays.")

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_arrayEmail assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestResendCode('test_success'))

    suite.addTest(TestResendCode('test_missingVerifyBy'))
    suite.addTest(TestResendCode('test_nullVerifyBy'))
    suite.addTest(TestResendCode('test_intVerifyBy'))
    suite.addTest(TestResendCode('test_floatVerifyBy'))
    suite.addTest(TestResendCode('test_stringVerifyBy'))
    suite.addTest(TestResendCode('test_arrayVerifyBy'))

    suite.addTest(TestResendCode('test_missingEmail'))
    suite.addTest(TestResendCode('test_nullEmail'))
    suite.addTest(TestResendCode('test_intEmail'))
    suite.addTest(TestResendCode('test_floatEmail'))
    suite.addTest(TestResendCode('test_stringEmail'))
    suite.addTest(TestResendCode('test_arrayEmail'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
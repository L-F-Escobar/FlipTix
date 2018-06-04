import sys, unittest, FlipTixShell

'''
    FlipTix verify user end point.
    
    Purpose - a user is email a verification code which is manually input 
    
    Notes - this endpoint can only be minimually automated due to the fact that is 
            requires manual code input and an email can only be registered once and
            not deleted.
            This end point cannot we automated to be tested successfully, only 
            unsucessful tests can be run.

    Method signature:
        def verify_user(self, verifyBy='', email='', verificationCode='', 
                   verifyByExclude=False,  emailExclude=False,
                   verificationCodeExclude=False):
    
    Required:
        verifyBy
        email
        verificationCode

    Test cases
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

        VerificationCode missing from request call.
        Null VerificationCode value. 
        Int VerificationCode value.    
        Float VerificationCode value.   
        String VerificationCode value.
        Array VerificationCode value. 
'''
class TestVerifyUser(unittest.TestCase):

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




    # *********************************************************************
    # *                         VerifyBy tests                            *
    # *********************************************************************
    
    
        
    # Missing VerifyBy information from request call.
    def test_missingVerifyBy(self):
        # Missing VerifyBy value.
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             email = FlipTixShell.data['testEmail'], 
                                             verificationCode = FlipTixShell.data['testVerificationCode'],
                                             verifyByExclude = True)

        self.assertEqual(responseBody['error'], "Please specify email or phone",
                         msg='test_missingVerifyBy assert#1 has failed.')
        
        
        
    # Test a null VerifyBy.
    def test_nullVerifyBy(self):
        # Null VerifyBy value.
        responseBody = self.user.verify_user(verifyBy = '', 
                                             email = FlipTixShell.data['testEmail'], 
                                             verificationCode = FlipTixShell.data['testVerificationCode'])

        self.assertEqual(responseBody['error'], "Please specify email or phone",
                          msg='test_nullVerifyBy assert#1 has failed.')



    # Test a int VerifyBy.
    def test_intVerifyBy(self):
        # Int VerifyBy value.
        responseBody = self.user.verify_user(verifyBy = 123456, 
                                             email = FlipTixShell.data['testEmail'], 
                                             verificationCode = FlipTixShell.data['testVerificationCode'])

        self.assertEqual(responseBody['error'], "Please specify email or phone",
                          msg='test_intVerifyBy assert#1 has failed.')



    # Test a float VerifyBy.
    def test_floatVerifyBy(self):
        # Float VerifyBy value.
        responseBody = self.user.verify_user(verifyBy = 12.35186, 
                                             email = FlipTixShell.data['testEmail'], 
                                             verificationCode = FlipTixShell.data['testVerificationCode'])

        self.assertEqual(responseBody['error'], "Please specify email or phone",
                          msg='test_floatVerifyBy assert#1 has failed.')
        
        
        
    # Test a string VerifyBy value call.
    def test_stringVerifyBy(self):
        # String VerifyBy value.
        responseBody = self.user.verify_user(verifyBy = "This is invalid", 
                                             email = FlipTixShell.data['testEmail'], 
                                             verificationCode = FlipTixShell.data['testVerificationCode'])

        self.assertEqual(responseBody['error'], "Please specify email or phone",
                          msg='test_stringVerifyBy assert#1 has failed.')



    # Test an array VerifyBy value call.
    def test_arrayVerifyBy(self):
        # Array VerifyBy value.
        responseBody = self.user.verify_user(verifyBy = ['invalid', 1, 1.1], 
                                             email = FlipTixShell.data['testEmail'], 
                                             verificationCode = FlipTixShell.data['testVerificationCode'])

        self.assertEqual(responseBody['error'], "Please specify email or phone",
                          msg='test_arrayVerifyBy assert#1 has failed.')



    
    # *********************************************************************
    # *                         Email tests                               *
    # *********************************************************************
    
    
        
    # Missing Email information from request call.
    def test_missingEmail(self):
        # Missing Email value.
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             email = FlipTixShell.data['testEmail'], 
                                             verificationCode = FlipTixShell.data['testVerificationCode'],
                                             emailExclude = True)

        self.assertEqual(responseBody['error'], "Please submit an email",
                         msg='test_missingEmail assert#1 has failed.')
        
        
        
    # Test a null Email.
    def test_nullEmail(self):
        # Null Email value.
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             email = '', 
                                             verificationCode = FlipTixShell.data['testVerificationCode'])

        self.assertEqual(responseBody['error'], "Please submit an email",
                          msg='test_nullEmail assert#1 has failed.')



    # Test a int Email.
    @unittest.skip("Unable to test int email value because error msg defaults to verification code")
    def test_intEmail(self):
        # Int Email value.
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             email = FlipTixShell.data['testEmail'], 
                                             verificationCode = FlipTixShell.data['testVerificationCode'])

        self.assertEqual(responseBody['message'], "Expected params.Email to be a string",
                          msg='test_intEmail assert#1 has failed.')



    # Test a float Email.
    @unittest.skip("Unable to test float email value because error msg defaults to verification code")
    def test_floatEmail(self):
        # Float Email value.
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             email = 6.66, 
                                             verificationCode = FlipTixShell.data['testVerificationCode'])

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_floatEmail assert#1 has failed.')
        
        
        
    # Test a string Email value call.
    def test_stringEmail(self):
        # String Email value.
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             email = "Invalid Format & User", 
                                             verificationCode = FlipTixShell.data['testVerificationCode'])

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_stringEmail assert#1 has failed.')



    # Test an array Email value call.
    def test_arrayEmail(self):
        # Array Email value.
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             email = ["Invalid Format & User"], 
                                             verificationCode = FlipTixShell.data['testVerificationCode'])

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_arrayEmail assert#1 has failed.')



    # *********************************************************************
    # *                          VerificationCode tests                   *
    # *********************************************************************
    
    
        
    # Missing VerificationCode information from request call.
    def test_missingVerificationCode(self):
        # Missing VerificationCode value.
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             email = FlipTixShell.data['testEmail'], 
                                             verificationCode = FlipTixShell.data['testVerificationCode'],
                                             verificationCodeExclude = True)

        self.assertEqual(responseBody['error'], "Please submit a verification code",
                         msg='test_missingVerificationCode assert#1 has failed.')
        
        
        
    # Test a null VerificationCode.
    def test_nullVerificationCode(self):
        # Null VerificationCode value.
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             email = FlipTixShell.data['testEmail'], 
                                             verificationCode = '')

        self.assertEqual(responseBody['error'], "Please submit a verification code",
                          msg='test_nullVerificationCode assert#1 has failed.')



    # Test a int VerificationCode.
    def test_intVerificationCode(self):
        # Int VerificationCode value.
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             email = FlipTixShell.data['testEmail'], 
                                             verificationCode = 111)

        self.assertEqual(responseBody['error'], "Your code has expired. Please request another verification code",
                          msg='test_intVerificationCode assert#1 has failed.')



    # Test a float VerificationCode.
    @unittest.skip("VerificationCode parameter can be any float value - (BUG)")
    def test_floatVerificationCode(self):
        # Float VerificationCode value.
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             email = FlipTixShell.data['testEmail'], 
                                             verificationCode = 1.1)

        self.assertEqual(responseBody['error'], "Your code has expired. Please request another verification code",
                          msg='test_floatVerificationCode assert#1 has failed.')
        
        
        
    # Test a string VerificationCode value call.
    @unittest.skip("VerificationCode parameter can be any string value - (BUG)")
    def test_stringVerificationCode(self):
        # String VerificationCode value.
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             email = FlipTixShell.data['testEmail'], 
                                             verificationCode = 'Anything will not do.')

        self.assertEqual(responseBody['error'], "Your code has expired. Please request another verification code",
                          msg='test_stringVerificationCode assert#1 has failed.')



    # Test an array VerificationCode value call.
    @unittest.skip("VerificationCode parameter can be any array value - (BUG)")
    def test_arrayVerificationCode(self):
        # Array VerificationCode value.
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             email = FlipTixShell.data['testEmail'], 
                                             verificationCode = ['test'])

        self.assertEqual(responseBody['error'], "Your code has expired. Please request another verification code",
                          msg='test_arrayVerificationCode assert#1 has failed.')
    
    




def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestVerifyUser('test_missingVerifyBy'))
    suite.addTest(TestVerifyUser('test_nullVerifyBy'))
    suite.addTest(TestVerifyUser('test_intVerifyBy'))
    suite.addTest(TestVerifyUser('test_floatVerifyBy'))
    suite.addTest(TestVerifyUser('test_stringVerifyBy'))
    suite.addTest(TestVerifyUser('test_arrayVerifyBy'))

    suite.addTest(TestVerifyUser('test_missingEmail'))
    suite.addTest(TestVerifyUser('test_nullEmail'))
    suite.addTest(TestVerifyUser('test_intEmail'))
    suite.addTest(TestVerifyUser('test_floatEmail'))
    suite.addTest(TestVerifyUser('test_stringEmail'))
    suite.addTest(TestVerifyUser('test_arrayEmail'))

    suite.addTest(TestVerifyUser('test_missingVerificationCode'))
    suite.addTest(TestVerifyUser('test_nullVerificationCode'))
    suite.addTest(TestVerifyUser('test_intVerificationCode'))
    suite.addTest(TestVerifyUser('test_floatVerificationCode'))
    suite.addTest(TestVerifyUser('test_stringVerificationCode'))
    suite.addTest(TestVerifyUser('test_arrayVerificationCode'))

    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
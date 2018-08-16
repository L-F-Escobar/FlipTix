import sys, unittest, FlipTixShell

'''
    FlipTix verify user end point.
    
    Purpose - a user is texted a verification code which is manually input 

    Method signature:
        def verify_user(self, verifyBy='', phone='', verificationCode='', 
                    verifyByExclude=False,  phoneExclude=False,
                    verificationCodeExclude=False):
    
    Required:
        verifyBy
        phone
        verificationCode

    Test cases
        Successfully verify a user.
        
        Verify a user that has already been verified.

        VerifyBy missing from request call.
        Null VerifyBy value. 
        Int VerifyBy value.    
        Float VerifyBy value.   
        String VerifyBy value.
        Array VerifyBy value.  

        phone missing from request call.
        Null phone value. 
        Int phone value.    
        Float phone value.   
        String phone value.
        Array phone value.  

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

            cls.user.register_user(verifyBy=FlipTixShell.data['testVerifyBy'], 
                                    email=FlipTixShell.data['testEmail'], 
                                    phone=FlipTixShell.data['testPhone'],
                                    firstName=FlipTixShell.data['testFirstName'], 
                                    lastName=FlipTixShell.data['testLastName'], 
                                    password=FlipTixShell.data['testPassword'])

            cls.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                 phone = FlipTixShell.data['testPhone'])                        
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            cls.user.delete_user(cls.user.GetUserId())
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])



    # Test successfully verifying a user.
    def test_success(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = self.user.GetResendCode())
        
        self.assertEqual(responseBody['result'], "Your phone has been verified!", 
                         msg= 'test_Success assert#1 has failed.')


    # Verify a user who has already been verified.
    def test_doubleVerify(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = self.user.GetResendCode())

        self.assertEqual(responseBody['error'], 'User already verified!',
                         msg='test_missingVerifyBy assert#1 has failed.')




    # *********************************************************************
    # *                         VerifyBy tests                            *
    # *********************************************************************
    
    
        
    # Missing VerifyBy information from request call.
    def test_missingVerifyBy(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = self.user.GetResendCode(),
                                             verifyByExclude = True)

        self.assertEqual(responseBody['error'], 'User already verified!',
                         msg='test_missingVerifyBy assert#1 has failed.')
        
        
        
    # Test a null VerifyBy.
    def test_nullVerifyBy(self):
        responseBody = self.user.verify_user(verifyBy = '', 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = self.user.GetResendCode())

        self.assertEqual(responseBody['error'], 'User already verified!',
                          msg='test_nullVerifyBy assert#1 has failed.')



    # Test a int VerifyBy.
    def test_intVerifyBy(self):
        responseBody = self.user.verify_user(verifyBy = 123456, 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = self.user.GetResendCode())

        self.assertEqual(responseBody['error'], 'User already verified!',
                          msg='test_intVerifyBy assert#1 has failed.')



    # Test a float VerifyBy.
    def test_floatVerifyBy(self):
        responseBody = self.user.verify_user(verifyBy = 12.35186, 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = self.user.GetResendCode())

        self.assertEqual(responseBody['error'], 'User already verified!',
                          msg='test_floatVerifyBy assert#1 has failed.')
        
        
        
    # Test a string VerifyBy value call.
    def test_stringVerifyBy(self):
        responseBody = self.user.verify_user(verifyBy = "This is invalid", 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = self.user.GetResendCode())

        self.assertEqual(responseBody['error'], 'User already verified!',
                          msg='test_stringVerifyBy assert#1 has failed.')



    # Test an array VerifyBy value call.
    def test_arrayVerifyBy(self):
        responseBody = self.user.verify_user(verifyBy = ['invalid', 1, 1.1], 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = self.user.GetResendCode())

        self.assertEqual(responseBody['error'], 'User already verified!',
                          msg='test_arrayVerifyBy assert#1 has failed.')



    
    # *********************************************************************
    # *                         Phone tests                               *
    # *********************************************************************
    
    
        
    # Missing Phone information from request call.
    def test_missingPhone(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = self.user.GetResendCode(),
                                             phoneExclude = True)

        self.assertEqual(responseBody['error'], "Please submit a phone number",
                         msg='test_missingPhone assert#1 has failed.')
        
        
        
    # Test a null Phone.
    def test_nullPhone(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = '', 
                                             verificationCode = self.user.GetResendCode())

        self.assertEqual(responseBody['error'], "Please submit a phone number",
                          msg='test_nullPhone assert#1 has failed.')



    # Test a int Phone.
    def test_intPhone(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = 6666666666666666666, 
                                             verificationCode = self.user.GetResendCode())

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_intPhone assert#1 has failed.')



    # Test a float Phone.
    def test_floatPhone(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = 6.66, 
                                             verificationCode = self.user.GetResendCode())

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_floatPhone assert#1 has failed.')
        
        
        
    # Test a string Phone value call.
    def test_stringPhone(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = "Invalid Format & User", 
                                             verificationCode = self.user.GetResendCode())

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_stringPhone assert#1 has failed.')



    # Test an array Phone value call.
    def test_arrayPhone(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = ["Invalid Format & User"], 
                                             verificationCode = self.user.GetResendCode())

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_arrayPhone assert#1 has failed.')



    # *********************************************************************
    # *                          VerificationCode tests                   *
    # *********************************************************************
    
    
        
    # Missing VerificationCode information from request call.
    def test_missingVerificationCode(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = self.user.GetResendCode(),
                                             verificationCodeExclude = True)

        self.assertEqual(responseBody['error'], "Please submit a verification code",
                         msg='test_missingVerificationCode assert#1 has failed.')
        
        
        
    # Test a null VerificationCode.
    def test_nullVerificationCode(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = '')

        self.assertEqual(responseBody['error'], "Please submit a verification code",
                          msg='test_nullVerificationCode assert#1 has failed.')



    # Test a int VerificationCode.
    def test_intVerificationCode(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = 111)

        self.assertEqual(responseBody['error'], 'Incorrect verification code',
                          msg='test_intVerificationCode assert#1 has failed.')



    # Test a float VerificationCode.
    def test_floatVerificationCode(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = 1.1)

        self.assertEqual(responseBody['error'], 'Incorrect verification code',
                          msg='test_floatVerificationCode assert#1 has failed.')
        
        
        
    # Test a string VerificationCode value call.
    def test_stringVerificationCode(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = 'Anything will not do.')

        self.assertEqual(responseBody['error'], 'Incorrect verification code',
                          msg='test_stringVerificationCode assert#1 has failed.')



    # Test an array VerificationCode value call.
    def test_arrayVerificationCode(self):
        responseBody = self.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                             phone = FlipTixShell.data['testPhone'], 
                                             verificationCode = ['test'])

        self.assertEqual(responseBody['error'], 'Incorrect verification code',
                          msg='test_arrayVerificationCode assert#1 has failed.')
    
    




def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestVerifyUser('test_success'))

    suite.addTest(TestVerifyUser('test_doubleVerify'))

    suite.addTest(TestVerifyUser('test_missingVerifyBy'))
    suite.addTest(TestVerifyUser('test_nullVerifyBy'))
    suite.addTest(TestVerifyUser('test_intVerifyBy'))
    suite.addTest(TestVerifyUser('test_floatVerifyBy'))
    suite.addTest(TestVerifyUser('test_stringVerifyBy'))
    suite.addTest(TestVerifyUser('test_arrayVerifyBy'))

    suite.addTest(TestVerifyUser('test_missingPhone'))
    suite.addTest(TestVerifyUser('test_nullPhone'))
    suite.addTest(TestVerifyUser('test_intPhone'))
    suite.addTest(TestVerifyUser('test_floatPhone'))
    suite.addTest(TestVerifyUser('test_stringPhone'))
    suite.addTest(TestVerifyUser('test_arrayPhone'))

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
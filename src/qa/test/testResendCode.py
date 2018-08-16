import sys, unittest, FlipTixShell

'''
    FlipTix registration end point.
    
    Purpose - endpoint send a verification code to the registered users phone.
    
    Notes - 

    Method signature:
        def resend_code(self, verifyBy='', phone='', verifyByExclude=False,  phoneExclude=False):
    
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

        phone missing from request call.
        Null phone value. 
        Int phone value.    
        Float phone value.   
        String phone value.
        Array phone value.  
'''
class TestResendCode(unittest.TestCase):

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
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            cls.user.delete_user(cls.user.GetUserId())
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])
    



    # Test successfully resending a verification code.
    def test_success(self):
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             phone = FlipTixShell.data['testPhone'])
        
        self.assertEqual(responseBody['result'], "saved!", 
                         msg= 'test_Success assert#1 has failed.')




    # *********************************************************************
    # *                         VerifyBy tests                            *
    # *********************************************************************
    
    
        
    # Missing VerifyBy information from request call.
    def test_missingVerifyBy(self):
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             phone = FlipTixShell.data['testPhone'],
                                             verifyByExclude = True)

        self.assertEqual(responseBody['error'], "Please specify google id or phone",
                         msg='test_missingVerifyBy assert#1 has failed.')
        
        
        
    # Test a null VerifyBy.
    def test_nullVerifyBy(self):
        responseBody = self.user.resend_code(verifyBy = '',
                                             phone = FlipTixShell.data['testPhone'])

        self.assertEqual(responseBody['error'], "Please specify google id or phone",
                          msg='test_nullVerifyBy assert#1 has failed.')



    # Test a int VerifyBy.
    def test_intVerifyBy(self):
        responseBody = self.user.resend_code(verifyBy = 123456,
                                             phone = FlipTixShell.data['testPhone'])

        self.assertEqual(responseBody['error'], "Please specify google id or phone",
                          msg='test_intVerifyBy assert#1 has failed.')



    # Test a float VerifyBy.
    def test_floatVerifyBy(self):
        responseBody = self.user.resend_code(verifyBy = 1234.56,
                                             phone = FlipTixShell.data['testPhone'])

        self.assertEqual(responseBody['error'], "Please specify google id or phone",
                          msg='test_floatVerifyBy assert#1 has failed.')
        
        
        
    # Test a string VerifyBy value call.
    def test_stringVerifyBy(self):
        responseBody = self.user.resend_code(verifyBy = "This should not work",
                                             phone = FlipTixShell.data['testPhone'])

        self.assertEqual(responseBody['error'], "Please specify google id or phone",
                          msg='test_stringVerifyBy assert#1 has failed.')



    # Test an array VerifyBy value call.
    def test_arrayVerifyBy(self):
        responseBody = self.user.resend_code(verifyBy = ["This should not work", 123, 1.2],
                                             phone = FlipTixShell.data['testPhone'])

        self.assertEqual(responseBody['error'], "Please specify google id or phone",
                          msg='test_arrayVerifyBy assert#1 has failed.')



    
    # *********************************************************************
    # *                         Phone tests                               *
    # *********************************************************************
    
    
        
    # Missing Phone information from request call.
    def test_missingPhone(self):
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             phone = FlipTixShell.data['testPhone'],
                                             phoneExclude = True)

        self.assertEqual(responseBody['error'], "Please submit a phone number",
                         msg='test_missingPhone assert#1 has failed.')
        
        
        
    # Test a null Phone.
    def test_nullPhone(self):
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             phone = '')

        self.assertEqual(responseBody['error'], "Please submit a phone number",
                          msg='test_nullPhone assert#1 has failed.')



    # Test a int Phone.
    def test_intPhone(self):
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             phone = 513516813158)

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_intPhone assert#1 has failed.')



    # Test a float Phone.
    def test_floatPhone(self):
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             phone = 1.1)

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_floatPhone assert#1 has failed.')
        
        
        
    # Test a string Phone value call.
    def test_stringPhone(self):
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             phone = "This is not a valid Phone format!")

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_stringPhone assert#1 has failed.')



    # Test an array Phone value call.
    def test_arrayPhone(self):
        responseBody = self.user.resend_code(verifyBy = FlipTixShell.data['testVerifyBy'],
                                             phone = "Email formats are not encased in arrays.")

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_arrayPhone assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestResendCode('test_success'))

    suite.addTest(TestResendCode('test_missingVerifyBy'))
    suite.addTest(TestResendCode('test_nullVerifyBy'))
    suite.addTest(TestResendCode('test_intVerifyBy'))
    suite.addTest(TestResendCode('test_floatVerifyBy'))
    suite.addTest(TestResendCode('test_stringVerifyBy'))
    suite.addTest(TestResendCode('test_arrayVerifyBy'))

    suite.addTest(TestResendCode('test_missingPhone'))
    suite.addTest(TestResendCode('test_nullPhone'))
    suite.addTest(TestResendCode('test_intPhone'))
    suite.addTest(TestResendCode('test_floatPhone'))
    suite.addTest(TestResendCode('test_stringPhone'))
    suite.addTest(TestResendCode('test_arrayPhone'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
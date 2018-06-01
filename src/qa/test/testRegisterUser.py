import sys, unittest, FlipTixShell

'''
    FlipTix registration end point.
    
    Purpose - endpoint requires user to confirm their account with a verification 
              code sent to their registered email
    
    Notes - this endpoint can only be minimually automated due to the fact that is 
            requires manual code input and an email can only be registered once and
            not deleted.

    Method signature:
        def register_user(self, verifyBy='', email='', phone='', firstName='',
                 lastName='', password='', verifyByExclude=False,
                 emailExclude=False, phoneExclude=False, firstNameExclude=False,
                 lastNameExclude=False, passwordExclude=False):
    
    Required:
        verifyBy
        email
        phone
        firstName
        lastName
        password

    Test cases
        VerifyBy missing from request call.
        Null Username value. 
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

        Phone missing from request call.
        Null Phone value. 
        Int Phone value.    
        Float Phone value.   
        String Phone value.
        Array Phone value. 

        FirstName missing from request call.
        Null FirstName value. 
        Int FirstName value.    
        Float FirstName value.   
        String FirstName value.
        Array FirstName value. 

        LastName missing from request call.
        Null LastName value. 
        Int LastName value.    
        Float LastName value.   
        String LastName value.
        Array LastName value. 

        Password missing from request call.
        Null Password value. 
        Int Password value.    
        Float Password value.   
        String Password value.
        Array Password value. 
'''
class TestResendConfirmation(unittest.TestCase):

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
        responseBody = self.user.

        self.assertEqual(responseBody['message'], "Missing required key 'VerifyBy' in params",
                          msg='test_missingVerifyBy assert#1 has failed.')
        
        
        
    # Test a null VerifyBy.
    def test_nullVerifyBy(self):
        # Null VerifyBy value.
        responseBody = self.user.

        self.assertEqual(responseBody['code'], "InvalidParameterException",
                          msg='test_nullVerifyBy assert#1 has failed.')



    # Test a int VerifyBy.
    def test_intVerifyBy(self):
        # Int VerifyBy value.
        responseBody = self.user.

        self.assertEqual(responseBody['message'], "Expected params.VerifyBy to be a string",
                          msg='test_intVerifyBy assert#1 has failed.')



    # Test a float VerifyBy.
    def test_floatVerifyBy(self):
        # Float VerifyBy value.
        responseBody = self.user.

        self.assertEqual(responseBody['message'], "Expected params.VerifyBy to be a string",
                          msg='test_floatVerifyBy assert#1 has failed.')
        
        
        
    # Test a string VerifyBy value call.
    def test_stringVerifyBy(self):
        # String VerifyBy value.
        responseBody = self.user.

        self.assertEqual(responseBody['message'], "VerifyBy/client id combination not found.",
                          msg='test_stringVerifyBy assert#1 has failed.')



    # Test an array VerifyBy value call.
    def test_arrayVerifyBy(self):
        # Array VerifyBy value.
        responseBody = self.user.

        self.assertEqual(responseBody['message'], "Expected params.VerifyBy to be a string",
                          msg='test_arrayVerifyBy assert#1 has failed.')



    
    # # *********************************************************************
    # # *                         Code tests                               *
    # # *********************************************************************
    
    
        
    # # Missing Code information from request call.
    # def test_missingCode(self):
    #     # Missing Code value.
    #     responseBody = self.user.confirm_registration(username = ReelyShell.data['TestNonConfirmedEmail'],
    #                                                   code = ReelyShell.data['TestCode'],
    #                                                   codeExclude = True)

    #     self.assertEqual(responseBody['error'], "Must provide confirmation code.",
    #                       msg='test_missingCode assert#1 has failed.')
        
        
        
    # # Test a null Code.
    # def test_nullCode(self):
    #     # Null Code value.
    #     responseBody = self.user.confirm_registration(username = ReelyShell.data['TestNonConfirmedEmail'],
    #                                                   code = '')

    #     self.assertEqual(responseBody['error'], "Must provide confirmation code.",
    #                       msg='test_nullCode assert#1 has failed.')



    # # Test a int Code.
    # def test_intCode(self):
    #     # Int Code value.
    #     responseBody = self.user.confirm_registration(username = ReelyShell.data['TestNonConfirmedEmail'],
    #                                                   code = 123)

    #     self.assertEqual(responseBody['code'], "InvalidParameterType",
    #                       msg='test_intCode assert#1 has failed.')



    # # Test a float Code.
    # def test_floatCode(self):
    #     # Float Code value.
    #     responseBody = self.user.confirm_registration(username = ReelyShell.data['TestNonConfirmedEmail'],
    #                                                   code = 12.3)

    #     self.assertEqual(responseBody['code'], "InvalidParameterType",
    #                       msg='test_floatCode assert#1 has failed.')
        
        
        
    # # Test a string Code value call.
    # def test_stringCode(self):
    #     # String Code value.
    #     responseBody = self.user.confirm_registration(username = ReelyShell.data['TestNonConfirmedEmail'],
    #                                                   code = "Invalid_Code")

    #     self.assertEqual(responseBody['message'], "Invalid verification code provided, please try again.",
    #                       msg='test_stringCode assert#1 has failed.')



    # # Test an array Code value call.
    # def test_arrayCode(self):
    #     # Array Code value.
    #     responseBody = self.user.confirm_registration(username = ReelyShell.data['TestNonConfirmedEmail'],
    #                                                   code = ['invalid_code', 123, 12.3])

    #     self.assertEqual(responseBody['code'], "InvalidParameterType",
    #                       msg='test_arrayCode assert#1 has failed.')
    
    
    
def suite():
    suite = unittest.TestSuite()

    # suite.addTest(TestResendConfirmation('test_missingUsername'))
    # suite.addTest(TestResendConfirmation('test_nullUsername'))
    # suite.addTest(TestResendConfirmation('test_intUsername'))
    # suite.addTest(TestResendConfirmation('test_floatUsername'))
    # suite.addTest(TestResendConfirmation('test_stringUsername'))
    # suite.addTest(TestResendConfirmation('test_arrayUsername'))

    # suite.addTest(TestResendConfirmation('test_missingCode'))
    # suite.addTest(TestResendConfirmation('test_nullCode'))
    # suite.addTest(TestResendConfirmation('test_intCode'))
    # suite.addTest(TestResendConfirmation('test_floatCode'))
    # suite.addTest(TestResendConfirmation('test_stringCode'))
    # suite.addTest(TestResendConfirmation('test_arrayCode'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
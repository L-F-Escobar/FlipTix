import sys, unittest, FlipTixShell

'''
    FlipTix registration end point.
    
    Purpose - endpoint requires user to confirm their account with a verification 
              code sent to their registered phone number.
    
    Notes - This endpoint can only be minimually automated due to the fact that is 
            requires manual code input.
            Many unittest will fail due to enduring validation issues on the back end.

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
        Successfully register a new user.

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
class TestRegisterUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.user = FlipTixShell.FlipTix()      
            cls.successMsg = 'User has been created successfully. Please check your phone for your verification code'
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    # @classmethod
    # def tearDownClass(cls):
    #     try:
    #         cls.user.delete_user(cls.user.GetUserId())
    #         cls.successMsg = None
    #     except:
    #         print("Unexpected error during tearDownClass:", sys.exc_info()[0])

    def tearDown(self):
        self.user.delete_user(self.user.GetUserId())


    # Test successfully registering a new users.
    def test_success(self):
        responseBody = self.user.register_user(verifyBy=FlipTixShell.data['testVerifyBy'], 
                                               email=FlipTixShell.data['testEmail'], 
                                               phone=FlipTixShell.data['testPhone'],
                                               firstName=FlipTixShell.data['testFirstName'], 
                                               lastName=FlipTixShell.data['testLastName'], 
                                               password=FlipTixShell.data['testPassword'])
        
        self.assertEqual(responseBody['result'], self.successMsg, 
                         msg= 'test_Success assert#1 has failed.')



    # *********************************************************************
    # *                         VerifyBy tests                            *
    # *********************************************************************
    
    
        
    # Missing VerifyBy information from request call.
    def test_missingVerifyBy(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'],
                                               verifyByExclude = True)

        self.assertEqual(responseBody['error'], "please submit a method of verification",
                         msg='test_missingVerifyBy assert#1 has failed.')
        
        
        
    # Test a null VerifyBy.
    def test_nullVerifyBy(self):
        responseBody = self.user.register_user(verifyBy = '', 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "please submit a method of verification",
                          msg='test_nullVerifyBy assert#1 has failed.')



    # Test a int VerifyBy.
    def test_intVerifyBy(self):
        responseBody = self.user.register_user(verifyBy = 123456789, 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "please submit a method of verification",
                          msg='test_intVerifyBy assert#1 has failed.')



    # Test a float VerifyBy.
    def test_floatVerifyBy(self):
        responseBody = self.user.register_user(verifyBy = 1.23456789, 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "please submit a method of verification",
                          msg='test_floatVerifyBy assert#1 has failed.')
        
        
        
    # Test a string VerifyBy value call.
    def test_stringVerifyBy(self):
        responseBody = self.user.register_user(verifyBy = "This is not valid data", 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "please submit a method of verification",
                          msg='test_stringVerifyBy assert#1 has failed.')



    # Test an array VerifyBy value call.
    def test_arrayVerifyBy(self):
        responseBody = self.user.register_user(verifyBy = ['Not valid', 123, 1.23], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "please submit a method of verification",
                          msg='test_arrayVerifyBy assert#1 has failed.')



    
    # *********************************************************************
    # *                         Email tests                               *
    # *********************************************************************
    
    
        
    # Missing Email information from request call.
    def test_missingEmail(self):
        # Missing Email value.
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'],
                                               emailExclude = True)

        self.assertEqual(responseBody['error'], "please submit an email",
                         msg='test_missingEmail assert#1 has failed.')
        
        
        
    # Test a null Email.
    def test_nullEmail(self):
        # Null Email value.
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = '', 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "please submit an email",
                          msg='test_nullEmail assert#1 has failed.')



    # Test a int Email.
    #@unittest.skip("Email parameter can be any integar value - (BUG)")
    def test_intEmail(self):
        # Int Email value.
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = 123546, 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['message'], "Expected params.Email to be a string",
                          msg='test_intEmail assert#1 has failed.')



    # Test a float Email.
    #@unittest.skip("Email parameter can be any float value - (BUG)")
    def test_floatEmail(self):
        # Float Email value.
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = 6587.4231, 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['message'], "Expected params.Email to be a string",
                          msg='test_floatEmail assert#1 has failed.')
        
        
        
    # Test a string Email value call.
    #@unittest.skip("Email parameter can be any string value - (BUG)")
    def test_stringEmail(self):
        # String Email value.
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = "Should not work", 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['message'], "Expected params.Email to be a string",
                          msg='test_stringEmail assert#1 has failed.')



    # Test an array Email value call.
    #@unittest.skip("Email parameter can be any string value - (BUG)")
    def test_arrayEmail(self):
        # Array Email value.
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = ['should not work', 1, 1.1], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['message'], "Expected params.Email to be a string",
                          msg='test_arrayEmail assert#1 has failed.')



    # *********************************************************************
    # *                          Phone tests                              *
    # *********************************************************************
    
    
        
    # Missing Phone information from request call.
    def test_missingPhone(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'],
                                               phoneExclude = True)

        self.assertEqual(responseBody['error'], "please submit a phone number",
                         msg='test_missingPhone assert#1 has failed.')
        
        
        
    # Test a null Phone.
    def test_nullPhone(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = '', 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "please submit a phone number",
                          msg='test_nullPhone assert#1 has failed.')



    # Test a int Phone.
    def test_intPhone(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = 1111111111111111111111111, 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "Invalid phone number",
                          msg='test_intPhone assert#1 has failed.')



    # Test a float Phone.
    def test_floatPhone(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = 11111.11111111111111111111, 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "Invalid phone number",
                          msg='test_floatPhone assert#1 has failed.')
        
        
        
    # Test a string Phone value call.
    def test_stringPhone(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = "This should not work", 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "Invalid phone number",
                          msg='test_stringPhone assert#1 has failed.')



    # Test an array Phone value call.
    def test_arrayPhone(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = ['totally broken'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "Invalid phone number",
                          msg='test_arrayPhone assert#1 has failed.')
    
    


    # *********************************************************************
    # *                         FirstName tests                            *
    # *********************************************************************
    
    
        
    # Missing FirstName information from request call.
    def test_missingFirstName(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'],
                                               firstNameExclude = True)

        self.assertEqual(responseBody['error'], "please submit a first name",
                         msg='test_missingFirstName assert#1 has failed.')
        
        
        
    # Test a null FirstName.
    def test_nullFirstName(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = '', 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "please submit a first name",
                          msg='test_nullFirstName assert#1 has failed.')



    # Test a int FirstName.
    def test_intFirstName(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = 123456, 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], 'Invalid firstName data.',
                          msg='test_intFirstName assert#1 has failed.')



    # Test a float FirstName.
    def test_floatFirstName(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = 1.1, 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], 'Invalid firstName data.',
                          msg='test_floatFirstName assert#1 has failed.')
        
        
        
    # Test a string FirstName value call.
    def test_stringFirstName(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = 'This should pass.', 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['result'], 'User has been created successfully. Please check your phone for your verification code',
                          msg='test_stringFirstName assert#1 has failed.')



    # Test an array FirstName value call.
    def test_arrayFirstName(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = ['This should not pass'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], 'Invalid firstName data.',
                          msg='test_arrayFirstName assert#1 has failed.')
    


    # *********************************************************************
    # *                         LastName tests                            *
    # *********************************************************************
    
    
        
    # Missing LastName information from request call.
    def test_missingLastName(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'],
                                               lastNameExclude = True)

        self.assertEqual(responseBody['error'], "please submit a last name",
                         msg='test_missingLastName assert#1 has failed.')
        
        
        
    # Test a null LastName.
    def test_nullLastName(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = '', 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "please submit a last name",
                          msg='test_nullLastName assert#1 has failed.')



    # Test a int LastName.
    def test_intLastName(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = 65484, 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "Invalid lastName data.",
                          msg='test_intLastName assert#1 has failed.')



    # Test a float LastName.
    def test_floatLastName(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = 85.25, 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "Invalid lastName data.",
                          msg='test_floatLastName assert#1 has failed.')
        
        
        
    # Test a string LastName value call.
    def test_stringLastName(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = 'should always pass', 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['result'], 'User has been created successfully. Please check your phone for your verification code',
                          msg='test_stringLastName assert#1 has failed.')



    # Test an array LastName value call.
    def test_arrayLastName(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = ['Should not pass'], 
                                               password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "Invalid lastName data.",
                          msg='test_arrayLastName assert#1 has failed.')




    # *********************************************************************
    # *                         Password tests                            *
    # *********************************************************************
    
    
        
    # Missing Password information from request call.
    def test_missingPassword(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = FlipTixShell.data['testPassword'],
                                               passwordExclude = True)

        self.assertEqual(responseBody['error'], "please submit both an email and password",
                         msg='test_missingPassword assert#1 has failed.')
        
        
        
    # Test a null Password.
    def test_nullPassword(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = '')

        self.assertEqual(responseBody['error'], "please submit both an email and password",
                          msg='test_nullPassword assert#1 has failed.')



    # Test a int Password.
    def test_intPassword(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = 123456789)

        self.assertEqual(responseBody['error'], 'Could not create this user',
                          msg='test_intPassword assert#1 has failed.')



    # Test a float Password.
    def test_floatPassword(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = 123.321)

        self.assertEqual(responseBody['error'], 'Could not create this user',
                          msg='test_floatPassword assert#1 has failed.')
        
        
        
    # Test a string Password value call.
    def test_stringPassword(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = "should pass")

        self.assertEqual(responseBody['result'], 'User has been created successfully. Please check your phone for your verification code',
                          msg='test_stringPassword assert#1 has failed.')



    # Test an array Password value call.
    def test_arrayPassword(self):
        responseBody = self.user.register_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                               email = FlipTixShell.data['testEmail'], 
                                               phone = FlipTixShell.data['testPhone'], 
                                               firstName = FlipTixShell.data['testFirstName'], 
                                               lastName = FlipTixShell.data['testLastName'], 
                                               password = ['probably should be passing'])

        self.assertEqual(responseBody['error'], 'Could not create this user',
                          msg='test_arrayPassword assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestRegisterUser('test_success'))

    suite.addTest(TestRegisterUser('test_missingVerifyBy'))
    suite.addTest(TestRegisterUser('test_nullVerifyBy'))
    suite.addTest(TestRegisterUser('test_intVerifyBy'))
    suite.addTest(TestRegisterUser('test_floatVerifyBy'))
    suite.addTest(TestRegisterUser('test_stringVerifyBy'))
    suite.addTest(TestRegisterUser('test_arrayVerifyBy'))

    suite.addTest(TestRegisterUser('test_missingEmail'))
    suite.addTest(TestRegisterUser('test_nullEmail'))
    suite.addTest(TestRegisterUser('test_intEmail'))
    suite.addTest(TestRegisterUser('test_floatEmail'))
    suite.addTest(TestRegisterUser('test_stringEmail'))
    suite.addTest(TestRegisterUser('test_arrayEmail'))

    suite.addTest(TestRegisterUser('test_missingPhone'))
    suite.addTest(TestRegisterUser('test_nullPhone'))
    suite.addTest(TestRegisterUser('test_intPhone'))
    suite.addTest(TestRegisterUser('test_floatPhone'))
    suite.addTest(TestRegisterUser('test_stringPhone'))
    suite.addTest(TestRegisterUser('test_arrayPhone'))

    suite.addTest(TestRegisterUser('test_missingFirstName'))
    suite.addTest(TestRegisterUser('test_nullFirstName'))
    suite.addTest(TestRegisterUser('test_intFirstName'))
    suite.addTest(TestRegisterUser('test_floatFirstName'))
    suite.addTest(TestRegisterUser('test_stringFirstName'))
    suite.addTest(TestRegisterUser('test_arrayFirstName'))

    suite.addTest(TestRegisterUser('test_missingLastName'))
    suite.addTest(TestRegisterUser('test_nullLastName'))
    suite.addTest(TestRegisterUser('test_intLastName'))
    suite.addTest(TestRegisterUser('test_floatLastName'))
    suite.addTest(TestRegisterUser('test_stringLastName'))
    suite.addTest(TestRegisterUser('test_arrayLastName'))

    suite.addTest(TestRegisterUser('test_missingPassword'))
    suite.addTest(TestRegisterUser('test_nullPassword'))
    suite.addTest(TestRegisterUser('test_intPassword'))
    suite.addTest(TestRegisterUser('test_floatPassword'))
    suite.addTest(TestRegisterUser('test_stringPassword'))
    suite.addTest(TestRegisterUser('test_arrayPassword'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
import sys, unittest, FlipTixShell

'''
    FlipTix login end point.
    
    Purpose - logs in a fully registered user.
    
    Notes - This end point cant be fully automated because a user that registers must
            verify their registration through manually inputing a code sent to their
            phone.

    Method signature:
        def login(self, email='', password='', emailExclude=False, passwordExclude=False):
    
    Required:
        email
        password

    Test cases
        Successfully log in.

        Email missing from request call.
        Null Email value. 
        Int Email value.    
        Float Email value.   
        String Email value.
        Array Email value.  

        Password missing from request call.
        Null Password value. 
        Int Password value.    
        Float Password value.   
        String Password value.
        Array Password value. 
'''
class TestLogin(unittest.TestCase):

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
    



    # Test successfully logging in.
    def test_success(self):
        responseBody = self.user.login(email = FlipTixShell.data['testEmail'], 
                                       password = FlipTixShell.data['testPassword'])
        
        self.assertEqual(responseBody['error'], "User has not been verified", 
                         msg= 'test_Success assert#1 has failed.')



    
    # *********************************************************************
    # *                         Email tests                               *
    # *********************************************************************
    
    
        
    # Missing Email information from request call.
    def test_missingEmail(self):
        responseBody = self.user.login(email = FlipTixShell.data['testEmail'], 
                                       password = FlipTixShell.data['testPassword'],
                                       emailExclude = True)

        self.assertEqual(responseBody['error'], 'Please submit an email or google id',
                         msg='test_missingEmail assert#1 has failed.')
        
        
        
    # Test a null Email.
    def test_nullEmail(self):
        responseBody = self.user.login(email = '', 
                                       password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "Please submit an email or google id",
                          msg='test_nullEmail assert#1 has failed.')



    # Test a int Email.
    def test_intEmail(self):
        responseBody = self.user.login(email = 111111111111111111111111, 
                                       password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_intEmail assert#1 has failed.')



    # Test a float Email.
    def test_floatEmail(self):
        responseBody = self.user.login(email = 8545646546546546546546, 
                                       password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_floatEmail assert#1 has failed.')
        
        
        
    # Test a string Email value call.
    def test_stringEmail(self):
        responseBody = self.user.login(email = 'This is not proper email format.', 
                                       password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_stringEmail assert#1 has failed.')



    # Test an array Email value call.
    def test_arrayEmail(self):
        responseBody = self.user.login(email = ['Invalid email format'], 
                                       password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "User was not found",
                          msg='test_arrayEmail assert#1 has failed.')


                
    # *********************************************************************
    # *                         Password tests                            *
    # *********************************************************************
    
    
        
    # Missing Password information from request call.
    def test_missingPassword(self):
        responseBody = self.user.login(email = FlipTixShell.data['testEmail'], 
                                       password = FlipTixShell.data['testPassword'],
                                       passwordExclude = True)

        self.assertEqual(responseBody['error'], "Please submit a password",
                         msg='test_missingPassword assert#1 has failed.')
        
        
        
    # Test a null Password.
    def test_nullPassword(self):
        responseBody = self.user.login(email = FlipTixShell.data['testEmail'], 
                                       password = '')

        self.assertEqual(responseBody['error'], "Please submit a password",
                          msg='test_nullPassword assert#1 has failed.')



    # Test a int Password.
    def test_intPassword(self):
        responseBody = self.user.login(email = FlipTixShell.data['testEmail'], 
                                       password = 8524567846321354168413181158165)

        self.assertEqual(responseBody['error'], 'User has not been verified',
                          msg='test_intPassword assert#1 has failed.')



    # Test a float Password.
    def test_floatPassword(self):
        responseBody = self.user.login(email = FlipTixShell.data['testEmail'], 
                                       password = 1.1)

        self.assertEqual(responseBody['error'], 'User has not been verified',
                          msg='test_floatPassword assert#1 has failed.')
        
        
        
    # Test a string Password value call.
    def test_stringPassword(self):
        responseBody = self.user.login(email = FlipTixShell.data['testEmail'], 
                                       password = 'This is not the correct password')

        self.assertEqual(responseBody['error'], 'User has not been verified',
                          msg='test_stringPassword assert#1 has failed.')



    # Test an array Password value call.
    def test_arrayPassword(self):
        responseBody = self.user.login(email = FlipTixShell.data['testEmail'], 
                                       password = ['Def not the correct password.'])

        self.assertEqual(responseBody['error'], 'User has not been verified',
                          msg='test_arrayPassword assert#1 has failed.')



def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestLogin('test_success'))

    suite.addTest(TestLogin('test_missingEmail'))
    suite.addTest(TestLogin('test_nullEmail'))
    suite.addTest(TestLogin('test_intEmail'))
    suite.addTest(TestLogin('test_floatEmail'))
    suite.addTest(TestLogin('test_stringEmail'))
    suite.addTest(TestLogin('test_arrayEmail'))

    suite.addTest(TestLogin('test_missingPassword'))
    suite.addTest(TestLogin('test_nullPassword'))
    suite.addTest(TestLogin('test_intPassword'))
    suite.addTest(TestLogin('test_floatPassword'))
    suite.addTest(TestLogin('test_stringPassword'))
    suite.addTest(TestLogin('test_arrayPassword'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
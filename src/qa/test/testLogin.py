import sys, unittest, FlipTixShell

'''
    FlipTix login end point.
    
    Purpose - logs in a fully registered user.
    
    Notes - 

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
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            pass
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])
    



    # Test successfully logging in.
    def test_success(self):
        # Log in.
        responseBody = self.user.login(email = FlipTixShell.data['testVerifiedEmail'], 
                                       password = FlipTixShell.data['testPassword'])
        
        self.assertEqual(responseBody['result'], "You have been logged in", 
                         msg= 'test_Success assert#1 has failed.')



    
    # *********************************************************************
    # *                         Email tests                               *
    # *********************************************************************
    
    
        
    # Missing Email information from request call.
    def test_missingEmail(self):
        # Missing Email value.
        responseBody = self.user.login(email = FlipTixShell.data['testVerifiedEmail'], 
                                       password = FlipTixShell.data['testPassword'],
                                       emailExclude = True)

        self.assertEqual(responseBody['error'], "Please submit an email or phone number",
                         msg='test_missingEmail assert#1 has failed.')
        
        
        
    # Test a null Email.
    def test_nullEmail(self):
        # Null Email value.
        responseBody = self.user.login(email = '', 
                                       password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "Please submit an email or phone number",
                          msg='test_nullEmail assert#1 has failed.')



    # Test a int Email.
    @unittest.skip("Email parameter can be any integar value - (BUG)")
    def test_intEmail(self):
        # Int Email value.
        responseBody = self.user.login(email = 1, 
                                       password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "",
                          msg='test_intEmail assert#1 has failed.')



    # Test a float Email.
    @unittest.skip("Email parameter can be any float value - (BUG)")
    def test_floatEmail(self):
        # Float Email value.
        responseBody = self.user.login(email = 1.2, 
                                       password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "",
                          msg='test_floatEmail assert#1 has failed.')
        
        
        
    # Test a string Email value call.
    @unittest.skip("Email parameter can be any string value - (BUG)")
    def test_stringEmail(self):
        # String Email value.
        responseBody = self.user.login(email = 'This is not proper email format.', 
                                       password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "",
                          msg='test_stringEmail assert#1 has failed.')



    # Test an array Email value call.
    @unittest.skip("Email parameter can be any string value - (BUG)")
    def test_arrayEmail(self):
        # Array Email value.
        responseBody = self.user.login(email = ['Invalid email format'], 
                                       password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['error'], "",
                          msg='test_arrayEmail assert#1 has failed.')


                
    # *********************************************************************
    # *                         Password tests                            *
    # *********************************************************************
    
    
        
    # Missing Password information from request call.
    def test_missingPassword(self):
        # Missing Password value.
        responseBody = self.user.login(email = FlipTixShell.data['testVerifiedEmail'], 
                                       password = FlipTixShell.data['testPassword'],
                                       passwordExclude = True)

        self.assertEqual(responseBody['error'], "Please submit a password",
                         msg='test_missingPassword assert#1 has failed.')
        
        
        
    # Test a null Password.
    def test_nullPassword(self):
        # Null Password value.
        responseBody = self.user.login(email = FlipTixShell.data['testVerifiedEmail'], 
                                       password = '')

        self.assertEqual(responseBody['error'], "Please submit a password",
                          msg='test_nullPassword assert#1 has failed.')



    # Test a int Password.
    def test_intPassword(self):
        # Int Password value.
        responseBody = self.user.login(email = FlipTixShell.data['testVerifiedEmail'], 
                                       password = 1)

        self.assertEqual(responseBody['error'], "Unable to login at this time",
                          msg='test_intPassword assert#1 has failed.')



    # Test a float Password.
    def test_floatPassword(self):
        # Float Password value.
        responseBody = self.user.login(email = FlipTixShell.data['testVerifiedEmail'], 
                                       password = 1.1)

        self.assertEqual(responseBody['error'], "Unable to login at this time",
                          msg='test_floatPassword assert#1 has failed.')
        
        
        
    # Test a string Password value call.
    def test_stringPassword(self):
        # String Password value.
        responseBody = self.user.login(email = FlipTixShell.data['testVerifiedEmail'], 
                                       password = 'This is not the correct password')

        self.assertEqual(responseBody['error'], "Incorrect Password, please try again",
                          msg='test_stringPassword assert#1 has failed.')



    # Test an array Password value call.
    def test_arrayPassword(self):
        # Array Password value.
        responseBody = self.user.login(email = FlipTixShell.data['testVerifiedEmail'], 
                                       password = ['Def not the correct password.'])

        self.assertEqual(responseBody['error'], "Unable to login at this time",
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
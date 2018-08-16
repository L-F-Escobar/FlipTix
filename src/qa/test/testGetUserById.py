import sys, unittest, FlipTixShell

'''
    FlipTix get user by id end point.
    
    Purpose - gets all the user data based off that users id.
    
    Notes - 

    Method signature:
        def get_user_by_id(self, userId=''):
    
    Required:
        userId

    Test cases
        Successfully get user data.

        Invalid user id. 



        
'''
class TestGetUserById(unittest.TestCase):

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

            cls.user.verify_user(verifyBy = FlipTixShell.data['testVerifyBy'], 
                                 phone = FlipTixShell.data['testPhone'], 
                                 verificationCode = cls.user.GetResendCode())

            cls.user.login(email = FlipTixShell.data['testEmail'], 
                           password = FlipTixShell.data['testPassword'])
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            cls.user.delete_user(cls.user.GetUserId())
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])
    



    # Test successfully getting a users data.
    def test_success(self):

        responseBody = self.user.get_user_by_id(userId = self.user.GetUserId())
        
        name = FlipTixShell.data['testFirstName'] + ' ' + FlipTixShell.data['testLastName']

        self.assertEqual(responseBody['name'], name, 
                         msg= 'test_Success assert#1 has failed.')

        self.assertEqual(responseBody['isVerified'], True, 
                         msg= 'test_Success assert#2 has failed.')
                    
        self.assertEqual(responseBody['phone'], FlipTixShell.data['testPhone'], 
                         msg= 'test_Success assert#3 has failed.')
        
        self.assertEqual(responseBody['email'], FlipTixShell.data['testEmail'], 
                         msg= 'test_Success assert#4 has failed.')

    
    

    # *********************************************************************
    # *                         UserId tests                              *
    # *********************************************************************
    
    
        
    # Missing UserId information from request call.
    def test_invalidUserId(self):
        responseBody = self.user.get_user_by_id(userId = 'invalidUserId')

        self.assertEqual(responseBody['error'], "could not get user",
                         msg='test_invalidUserId assert#1 has failed.')





def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestGetUserById('test_success'))
    
    suite.addTest(TestGetUserById('test_invalidUserId'))
    
    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
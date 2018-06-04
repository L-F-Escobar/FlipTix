import sys, unittest, FlipTixShell

'''
    FlipTix change password end point.
    
    Purpose - allows a user to change their existing password.
    
    Notes - 

    Method signature:
        def change_password(self, userId='', newPassword='', userIdExclude=False,
                            newPasswordExclude=False):
    
    Required:
        userId
        newPassword

    Test cases
        Successfully change a users password & then reset to default password.

        UserId missing from request call.
        Null UserId value. 
        Int UserId value.    
        Float UserId value.   
        String UserId value.
        Array UserId value.  

        NewPassword missing from request call.
        Null NewPassword value. 
        Int NewPassword value.    
        Float NewPassword value.   
        String NewPassword value.
        Array NewPassword value. 
'''
class TestSendForgotPassword(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.user = FlipTixShell.FlipTix()      
            cls.user.login(email = FlipTixShell.data['testVerifiedEmail'],
                           password = FlipTixShell.data['testPassword'])
        except:
            print("Unexpected error during setUpClass:", sys.exc_info()[0])


    @classmethod
    def tearDownClass(cls):
        try:
            pass
        except:
            print("Unexpected error during tearDownClass:", sys.exc_info()[0])
    



    # Test successfully changing a users password.
    def test_success(self):
        # First change the password.
        responseBody = self.user.change_password(userId = self.user.GetUserId(), 
                                                 newPassword = FlipTixShell.data['newPassword'])
        
        self.assertEqual(responseBody['result'], 
                         "Your password has been changed! Please log in.", 
                         msg= 'test_Success assert#1 has failed.')
    
        # Now log in with the new password.
        responseBody = self.user.login(email = FlipTixShell.data['testVerifiedEmail'],
                                       password = FlipTixShell.data['newPassword'])
        
        self.assertEqual(responseBody['result'], "You have been logged in", 
                         msg= 'test_Success assert#2 has failed.')
        
        # Reset to the previous password and ensure it has been set to the default password.
        responseBody =  self.user.change_password(userId = self.user.GetUserId(), 
                                                  newPassword = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['result'], 
                         "Your password has been changed! Please log in.", 
                         msg= 'test_Success assert#3 has failed.')

        responseBody = self.user.login(email = FlipTixShell.data['testVerifiedEmail'],
                                       password = FlipTixShell.data['testPassword'])

        self.assertEqual(responseBody['result'], "You have been logged in", 
                         msg= 'test_Success assert#4 has failed.')



    # *********************************************************************
    # *                         UserId tests                               *
    # *********************************************************************
    
    
        
    # Missing UserId information from request call.
    def test_missingUserId(self):
        # Missing UserId value.
        responseBody = self.user.change_password(userId = self.user.GetUserId(), 
                                                 newPassword = FlipTixShell.data['newPassword'],
                                                 userIdExclude = True)

        self.assertEqual(responseBody['error'], "Please submit a userId",
                         msg='test_missingUserId assert#1 has failed.')
        
        
        
    # Test a null UserId.
    def test_nullUserId(self):
        # Null UserId value.
        responseBody = self.user.change_password(userId = '', 
                                                 newPassword = FlipTixShell.data['newPassword'])

        self.assertEqual(responseBody['error'], "Please submit a userId",
                          msg='test_nullUserId assert#1 has failed.')



    # Test a int UserId.
    def test_intUserId(self):
        # Int UserId value.
        responseBody = self.user.change_password(userId = 85231564, 
                                                 newPassword = FlipTixShell.data['newPassword'])

        self.assertEqual(responseBody['error'], "User could not be found",
                          msg='test_intUserId assert#1 has failed.')



    # Test a float UserId.
    def test_floatUserId(self):
        # Float UserId value.
        responseBody = self.user.change_password(userId = 8.5231564, 
                                                 newPassword = FlipTixShell.data['newPassword'])

        self.assertEqual(responseBody['error'], "User could not be found",
                          msg='test_floatUserId assert#1 has failed.')
        
        
        
    # Test a string UserId value call.
    def test_stringUserId(self):
        # String UserId value.
        responseBody = self.user.change_password(userId = 'This is not a valid user id', 
                                                 newPassword = FlipTixShell.data['newPassword'])

        self.assertEqual(responseBody['error'], "Could not reset password",
                          msg='test_stringUserId assert#1 has failed.')



    # Test an array UserId value call.
    def test_arrayUserId(self):
        # Array UserId value.
        responseBody = self.user.change_password(userId = ['will not work'], 
                                                 newPassword = FlipTixShell.data['newPassword'])

        self.assertEqual(responseBody['error'], "Could not reset password",
                          msg='test_arrayUserId assert#1 has failed.')




    # *********************************************************************
    # *                         NewPassword tests                               *
    # *********************************************************************
    
    
        
    # Missing NewPassword information from request call.
    def test_missingNewPassword(self):
        # Missing NewPassword value.
        responseBody = self.user.change_password(userId = self.user.GetUserId(), 
                                                 newPassword = FlipTixShell.data['newPassword'],
                                                 newPasswordExclude = True)

        self.assertEqual(responseBody['error'], "Please submit a new password",
                         msg='test_missingNewPassword assert#1 has failed.')
        
        
        
    # Test a null NewPassword.
    def test_nullNewPassword(self):
        # Null NewPassword value.
        responseBody = self.user.change_password(userId = self.user.GetUserId(), 
                                                 newPassword = '')

        self.assertEqual(responseBody['error'], "Please submit a new password",
                          msg='test_nullNewPassword assert#1 has failed.')



    # Test a int NewPassword.
    def test_intNewPassword(self):
        # Int NewPassword value.
        responseBody = self.user.change_password(userId = self.user.GetUserId(), 
                                                 newPassword = 123456)

        self.assertEqual(responseBody['error'], "Could not reset password",
                          msg='test_intNewPassword assert#1 has failed.')



    # Test a float NewPassword.
    def test_floatNewPassword(self):
        # Float NewPassword value.
        responseBody = self.user.change_password(userId = self.user.GetUserId(), 
                                                 newPassword = 85.265)

        self.assertEqual(responseBody['error'], "Could not reset password",
                          msg='test_floatNewPassword assert#1 has failed.')
        
        
        
    # Test a string NewPassword value call.
    @unittest.skip("No need for this test - any string will pass")
    def test_stringNewPassword(self):
        # String NewPassword value.
        responseBody = self.user.change_password(userId = self.user.GetUserId(), 
                                                 newPassword = "Any string will pass")

        self.assertEqual(responseBody['error'], "",
                          msg='test_stringNewPassword assert#1 has failed.')



    # Test an array NewPassword value call.
    def test_arrayNewPassword(self):
        # Array NewPassword value.
        responseBody = self.user.change_password(userId = self.user.GetUserId(), 
                                                 newPassword = ['Should not work'])

        self.assertEqual(responseBody['error'], "Could not reset password",
                          msg='test_arrayNewPassword assert#1 has failed.')

    


def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestSendForgotPassword('test_success'))

    suite.addTest(TestSendForgotPassword('test_missingUserId'))
    suite.addTest(TestSendForgotPassword('test_nullUserId'))
    suite.addTest(TestSendForgotPassword('test_intUserId'))
    suite.addTest(TestSendForgotPassword('test_floatUserId'))
    suite.addTest(TestSendForgotPassword('test_stringUserId'))
    suite.addTest(TestSendForgotPassword('test_arrayUserId'))
    
    suite.addTest(TestSendForgotPassword('test_missingNewPassword'))
    suite.addTest(TestSendForgotPassword('test_nullNewPassword'))
    suite.addTest(TestSendForgotPassword('test_intNewPassword'))
    suite.addTest(TestSendForgotPassword('test_floatNewPassword'))
    suite.addTest(TestSendForgotPassword('test_stringNewPassword'))
    suite.addTest(TestSendForgotPassword('test_arrayNewPassword'))

    return suite
    
    
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
import requests, os, json

requests.packages.urllib3.disable_warnings()

# # Set API Development Environment.
# setEnv = ''
# if 'Environment' not in os.environ.keys():
#     # print('\n[AutoScript] Defaulting to staging.\n')
#     setEnv = 'http://ec2-13-57-43-46.us-west-1.compute.amazonaws.com:8082/'
# else:
#     # print('\n[AutoScript] Setting environment to', os.environ['Environment'], '\n')
#     if os.environ['Environment'] == 'local':
#         setEnv = 'api:3001'
#     elif os.environ['Environment'] == 'staging':
#         setEnv = 'https://adpq-staging.hotbsoftware.com'
#     elif os.environ['Environment'] == 'prod':
#         setEnv = 'https://adpq.hotbsoftware.com'
# setEnv.strip()

# for testing we will default set an environment
setEnv = 'http://ec2-52-53-244-112.us-west-1.compute.amazonaws.com:3001/'


# Set test output flag.
# True  - Test print statements will output to console.
# False - No console output.
if 'TESTOUTPUT' not in os.environ.keys():
    TestOutput = False
else:
    TestOutput = bool(os.environ['TESTOUTPUT'])

# FOR TESTING 
TestOutput = True
    
# Get all necessary data.
with open('data.json') as data_file:    
    data = json.load(data_file)

    

'''
    FlipTix Test Automation Shell 
    
    Shell provides a platform to run unittest scripts against. 
    
    Each class method corresponds to an end point. 
    
    Each method contains header/body dictionaries. Dict pairs can be
    entirely excluded or assigned any values, including null.
    
    def example(email='', emailExclude=False):
    
    If emailExclude flag is set to True during the method call, the keypair 
    will not be included in the request.
'''
class FlipTix:
    ## @var Save a BaseURL without API Version.
    BaseURL = setEnv
        
    ## @fn __init__ : Class initializations.
    def __init__(self, env=setEnv):
        # 
        self.SessionToken = '' # Header is Authorization = SessionToken
        self.UserId = ''
        self.environment = env
        self.loginCookie = {}



    ## @fn register_user : endpoint allows user to register with FlipTix, sends 
    #                      out confirmation email.
    #
    def register_user(self, verifyBy='', email='', phone='', firstName='',
                 lastName='', password='', verifyByExclude=False,
                 emailExclude=False, phoneExclude=False, firstNameExclude=False,
                 lastNameExclude=False, passwordExclude=False):
        
        url = self.environment + data["RegisterUser"]
        
        headers = {
            'Content-Type' : 'application/json'
        }
        
        body = {}
        
        if verifyByExclude == True:
            pass
        elif verifyBy != '':
            body['verifyBy'] = verifyBy
        else:
            body['verifyBy'] = ''
            
        if emailExclude == True:
            pass
        elif email != '':
            body['email'] = email
        else:
            body['email'] = ''
            
        if phoneExclude == True:
            pass
        elif phone != '':
            body['phone'] = phone
        else:
            body['phone'] = ''
            
        if firstNameExclude == True:
            pass
        elif firstName != '':
            body['firstName'] = firstName
        else:
            body['firstName'] = ''
            
        if lastNameExclude == True:
            pass
        elif lastName != '':
            body['lastName'] = lastName
        else:
            body['lastName'] = ''

        if passwordExclude == True:
            pass
        elif password != '':
            body['password'] = password
        else:
            body['password'] = ''
            
        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nregister_user\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        # Grab the request Id of a successful call.
        if 'result' in responseBody.keys():
            if responseBody['result'] == "User has been created successfully. Please check your email for your verification code":
                pass
                # self.requestId = responseBody['requestId']
        
        return responseBody



    ## @fn verify_user : sends out a confirmation code to the users email
    #
    def verify_user(self, verifyBy='', email='', verificationCode='', 
                    verifyByExclude=False,  emailExclude=False,
                    verificationCodeExclude=False):
        
        url = self.environment + data["VerifyUser"]
        
        headers = {
            'Content-Type' : 'application/json',
            'Cache-Control': 'no-cache'
        }
        
        body = {}
        
        if verifyByExclude == True:
            pass
        elif verifyBy != '':
            body['verifyBy'] = verifyBy
        else:
            body['verifyBy'] = ''
            
        if emailExclude == True:
            pass
        elif email != '':
            body['email'] = email
        else:
            body['email'] = ''

        if verificationCodeExclude == True:
            pass
        elif verificationCode != '':
            body['verificationCode'] = verificationCode
        else:
            body['verificationCode'] = ''
            
        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nverify_user\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        # Grab the request Id of a successful call.
        if 'result' in responseBody.keys():
            if responseBody['result'] == "Your email has been verified! Please log in":
                self.SessionToken = responseBody['sessionToken']
                self.UserId = responseBody['userId']
        
        return responseBody
    


    ## @fn resend_code : sends out a confirmation code to the users email
    #
    def resend_code(self, verifyBy='', email='', verifyByExclude=False,  emailExclude=False):
        
        url = self.environment + data["ResendCode"]
        
        headers = {
            'Content-Type' : 'application/json',
            'Cache-Control': 'no-cache'
        }
        
        body = {}
        
        if verifyByExclude == True:
            pass
        elif verifyBy != '':
            body['verifyBy'] = verifyBy
        else:
            body['verifyBy'] = ''
            
        if emailExclude == True:
            pass
        elif email != '':
            body['email'] = email
        else:
            body['email'] = ''
            
        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nresend_code\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)

        # If successful go in here.
        if 'result' in responseBody.keys():
            if responseBody['result'] == "saved!":
                pass
        
        return responseBody



    ## @fn login : endpoint allows user to login.
    #
    def login(self, email='', password='', emailExclude=False, passwordExclude=False):
        
        url = self.environment + data["Login"]
        
        headers = {
            'Content-Type' : 'application/json',
            'Cache-Control': 'no-cache'
        }
        
        body = {}
        
        if emailExclude == True:
            pass
        elif email != '':
            body['email'] = email
        else:
            body['email'] = ''
            
        if passwordExclude == True:
            pass
        elif password != '':
            body['password'] = password
        else:
            body['password'] = ''
            
        response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nlogin\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        # Grab the request Id of a successful call.
        if 'result' in responseBody.keys():
            if responseBody['result'] == "You have been logged in":
                self.SessionToken = responseBody['sessionToken']
                self.UserId = responseBody['userId']
                self.loginCookie = response.cookies.get_dict()
        
        return responseBody



    ## @fn logout : logs an active user out. Authorization = self.SessionToken
    #
    def logout(self, Authorization='', AuthorizationExclude=False):
        
        url = self.environment + data["Logout"]
        
        headers = {
            'Content-Type' : 'application/json'
        }

        if AuthorizationExclude == True:
            pass
        elif Authorization != '':
            headers['Authorization'] = self.SessionToken
        else:
            headers['Authorization'] = ''
            
        response = requests.request('POST', url, json={}, headers=headers)

        responseBody = response.json()
        
        if TestOutput == True:
            print('\nlogout\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        # If successful, go in here.
        if 'result' in responseBody.keys():
            if responseBody['result'] == "Logged out":
                # Update the cookie.
                self.loginCookie = response.cookies.get_dict()
        
        return responseBody



    ## @fn login_check : Authorization = self.SessionToken
    #
    def login_check(self, Authorization='', cookies={}, AuthorizationExclude=False):
        
        url = self.environment + data["LoginCheck"]
        
        headers = {
            'Content-Type' : 'application/json',
            'Cache-Control': 'no-cache'
        }

        if AuthorizationExclude == True:
            pass
        elif Authorization != '':
            headers['Authorization'] = self.SessionToken
        else:
            headers['Authorization'] = ''
            
        response = requests.request('POST', url, json={}, headers=headers, cookies=cookies, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nlogin_check\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    ## @fn get_user_by_id : pull up user data with their id.
    #
    def get_user_by_id(self, userId='', userIdExclude=False):
        
        url = self.environment + data["GetUserById"] + userId

        headers = {
            'Content-Type' : 'application/json',
            'Cache-Control': 'no-cache'
        }
            
        response = requests.request('GET', url, json={}, headers=headers, verify=False)
    
        responseBody = response.json()
        
        if TestOutput == True:
            print('\nget_user_by_id\n', responseBody)
            print('\nresponse.status_code: ', response.status_code)
        
        return responseBody



    def GetSessionToken(self):
        return self.SessionToken

    def GetUserId(self):
        return self.UserId
    
    def GetCookies(self):
        return self.loginCookie



def testClass():
    # Declare class objects. Create class instance. DONE
    user = FlipTix()


    # # Method signature. DONE
    # # def register_user(self, verifyBy='', email='', phone='', firstName='',
    # #             lastName='', password='', verifyByExclude=False,
    # #             emailExclude=False, phoneExclude=False, firstNameExclude=False,
    # #             lastNameExclude=False, passwordExclude=False):
    # user.register_user(data['testVerifyBy'], data['testEmail'], data['testPhone'],
    #                    data['testFirstName'], data['testLastName'], data['testPassword'])



    # Method signature. DONE
    # def verify_user(self, verifyBy='', email='', verificationCode='', 
    #                verifyByExclude=False,  emailExclude=False,
    #                verificationCodeExclude=False):
    user.verify_user(data['testVerifyBy'], data['testEmail'], data['testVerificationCode'])



    # # Method signature. DONE
    # # def resend_code(self, verifyBy='', email='', verifyByExclude=False,  emailExclude=False):
    # user.resend_code(data['testVerifyBy'], data['testEmail'])



    # # Method signature. DONE
    # # def login(self, email='', password='', emailExclude=False, passwordExclude=False):
    # user.login(data['testVerifiedEmail'], data['testPassword'])



    # # Method signature. DONE
    # # def logout(self, Authorization='', AuthorizationExclude=False):
    # user.logout(user.GetSessionToken())



    # # Method signature. DONE
    # # def login_check(self, Authorization='', cookies={}, AuthorizationExclude=False):
    # user.login_check(user.GetSessionToken(), user.GetCookies())



    # # Method signature. DONE
    # # def get_user_by_id(self, userId=''):
    # user.get_user_by_id(user.GetUserId())

# testClass()
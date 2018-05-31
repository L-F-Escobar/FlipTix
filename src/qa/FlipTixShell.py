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
setEnv = 'ec2-52-53-244-112.us-west-1.compute.amazonaws.com:3001/'


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
        pass
        # self.ClientID = data['ClientId']
        # self.AuthKey = ''
        # self.requestId = ''
        # self.environment = env
        # self.AccessToken = ''
        # self.LoginCookies = {}
        # self.ReelTypeIds = []
        # self.CreatedTeamId = []
        # self.CreatedvideoId = []



    # ## @fn register : endpoint allows user to register with reely, checks to ascertain 
    # #                 if they have registered before, then sends out confirmation email.
    # #
    # def register(self, email='', password='', phone='', company='',
    #              name='', emailExclude=False, passwordExclude=False,
    #              phoneExclude=False, companyExclude=False, nameExclude=False):
        
    #     url = self.environment + data["Register"]
        
    #     headers = {
    #         'Content-Type' : 'application/json',
    #         'Cache-Control': 'no-cache'
    #     }
        
    #     body = {}
        
    #     if emailExclude == True:
    #         pass
    #     elif email != '':
    #         body['email'] = email
    #     else:
    #         body['email'] = ''
            
    #     if passwordExclude == True:
    #         pass
    #     elif password != '':
    #         body['password'] = password
    #     else:
    #         body['password'] = ''
            
    #     if phoneExclude == True:
    #         pass
    #     elif phone != '':
    #         body['phone'] = phone
    #     else:
    #         body['phone'] = ''
            
    #     if companyExclude == True:
    #         pass
    #     elif company != '':
    #         body['company'] = company
    #     else:
    #         body['company'] = ''
            
    #     if nameExclude == True:
    #         pass
    #     elif name != '':
    #         body['name'] = name
    #     else:
    #         body['name'] = ''
            
    #     response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
    #     responseBody = response.json()
        
    #     if TestOutput == True:
    #         print('\nregister\n', responseBody)
    #         print('\nresponseBody: ', response.status_code)
        
    #     # Grab the request Id of a successful call.
    #     if 'statusCode' in responseBody.keys():
    #         if responseBody['statusCode'] == 200:
    #             self.requestId = responseBody['requestId']
        
    #     return responseBody



    # ## @fn confirm_registration : sends out a confirmation code to the users email
    # #
    # def confirm_registration(self, username='', code='',  
    #                          usernameExclude=False, codeExclude=False):
        
    #     url = self.environment + data["ConfirmRegistration"]
        
    #     headers = {
    #         'Content-Type' : 'application/json',
    #         'Cache-Control': 'no-cache'
    #     }
        
    #     body = {}
        
    #     if usernameExclude == True:
    #         pass
    #     elif username != '':
    #         body['username'] = username
    #     else:
    #         body['username'] = ''
            
    #     if codeExclude == True:
    #         pass
    #     elif code != '':
    #         body['code'] = code
    #     else:
    #         body['code'] = ''
            
    #     response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
    #     responseBody = response.json()
        
    #     if TestOutput == True:
    #         print('\nconfirm_registration\n', responseBody)
    #         print('\nresponseBody: ', response.status_code)
        
    #     # Grab the request Id of a successful call.
    #     if 'statusCode' in responseBody.keys():
    #         if responseBody['statusCode'] == 200:
    #             self.requestId = responseBody['requestId']
        
    #     return responseBody
    


    # ## @fn resend_confirmation : sends out a confirmation code to the users email
    # #
    # def resend_confirmation(self, username='', usernameExclude=False):
        
    #     url = self.environment + data["ResendConfirmation"]
        
    #     headers = {
    #         'Content-Type' : 'application/json',
    #         'Cache-Control': 'no-cache'
    #     }
        
    #     body = {}
        
    #     if usernameExclude == True:
    #         pass
    #     elif username != '':
    #         body['username'] = username
    #     else:
    #         body['username'] = ''
            
    #     response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
    #     responseBody = response.json()
        
    #     if TestOutput == True:
    #         print('\nresend_registration\n', responseBody)
    #         print('\nresponseBody: ', response.status_code)
        
    #     return responseBody



    # ## @fn login : endpoint allows user to login, passport package behind the 
    # #              scenes manages all authorization so no further accesskey is 
    # #              needed once logged in.
    # #
    # def login(self, email='', password='', emailExclude=False, passwordExclude=False):
        
    #     url = self.environment + data["Login"]
        
    #     headers = {
    #         'Content-Type' : 'application/json',
    #         'Cache-Control': 'no-cache'
    #     }
        
    #     body = {}
        
    #     if emailExclude == True:
    #         pass
    #     elif email != '':
    #         body['email'] = email
    #     else:
    #         body['email'] = ''
            
    #     if passwordExclude == True:
    #         pass
    #     elif password != '':
    #         body['password'] = password
    #     else:
    #         body['password'] = ''
            
    #     response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
    #     responseBody = response.json()
        
    #     if TestOutput == True:
    #         print('\nlogin\n', responseBody)
    #         print('\nresponseBody: ', response.status_code)
        
    #     # Grab the request Id of a successful call.
    #     if 'code' in responseBody.keys():
    #         if responseBody['code'] == "Authorized":
    #             self.AccessToken = responseBody['accessToken']
    #             self.LoginCookies = response.cookies.get_dict()
        
    #     return responseBody



    # ## @fn forgot_password : sends out an email with a code to renew password 
    # #                        for user if user exists in database
    # #
    # def forgot_password(self, email='', emailExclude=False):
        
    #     url = self.environment + data["ForgotPassword"]
        
    #     headers = {
    #         'Content-Type' : 'application/json',
    #         'Cache-Control': 'no-cache'
    #     }
        
    #     body = {}
        
    #     if emailExclude == True:
    #         pass
    #     elif email != '':
    #         body['email'] = email
    #     else:
    #         body['email'] = ''
            
    #     response = requests.request('POST', url, json=body, headers=headers, verify=False)
    
    #     responseBody = response.json()
        
    #     if TestOutput == True:
    #         print('\nforgot_password\n', responseBody)
    #         print('\nresponseBody: ', response.status_code)
        
    #     # Grab the request Id of a successful call.
    #     if 'message' in responseBody.keys():
    #         if responseBody['message'] == "Confirmation code sent to your phone or email":
    #             pass
    #             # self.AccessToken = responseBody['accessToken']
        
    #     return responseBody



    # ## @fn getReelTypes : gets list of reel types - will only work after user login
    # #
    # def getReelTypes(self, cookies={}):
        
    #     url = self.environment + data["GetReelTypes"]
            
    #     response = requests.request('GET', url, json={}, headers={}, cookies=cookies, verify=False)

    #     responseBody = response.json()

    #     if response.status_code == 200:
    #         self.ReelTypeIds = responseBody
        
    #     if TestOutput == True:
    #         print('\ngetReelTypes\n', response.text)
    #         print('\nresponseBody: ', responseBody)
        
    #     return responseBody



    # ## @fn get_leagues : gets list of leagues - will only work after user login
    # #
    # def get_leagues(self, cookies={}):
        
    #     url = self.environment + data["GetLeagues"]
            
    #     response = requests.request('GET', url, json={}, headers={}, cookies=cookies, verify=False)

    #     responseBody = response.json()
        
    #     if TestOutput == True:
    #         print('\nget_leagues\n', response.text)
    #         print('\nresponseBody: ', responseBody)
        
    #     return responseBody



    # ## @fn create_team : allows user to create a team within an existing league
    # #
    # def create_team(self, teamName='', League='', cookies={},
    #                 teamNameExclude=False, LeagueExclude=False):
        
    #     url = self.environment + data["CreateTeam"]
        
    #     headers = {
    #         'Content-Type' : 'application/json',
    #         'Cache-Control': 'no-cache'
    #     }
        
    #     body = {}
        
    #     if teamNameExclude == True:
    #         pass
    #     elif teamName != '':
    #         body['teamName'] = teamName
    #     else:
    #         body['teamName'] = ''
            
    #     if LeagueExclude == True:
    #         pass
    #     elif League != '':
    #         body['League'] = League
    #     else:
    #         body['League'] = ''
            
    #     response = requests.request('POST', url, json=body, headers=headers, cookies=cookies, verify=False)
    
    #     responseBody = response.json()
        
    #     if TestOutput == True:
    #         print('\ncreate_team\n', responseBody)
    #         print('\nresponseBody: ', response.status_code)
        
    #     # Save the created teams id.
    #     if response.status_code == 200:
    #         self.CreatedTeamId.append(responseBody[0]['ID'])
        
    #     return responseBody



    # ## @fn delete_team : delete team that user has previously created
    # #
    # def delete_team(self, cookies={}):
        
    #     url = self.environment + data["DeleteTeam"] + str(self.CreatedTeamId[0])

    #     headers = {
    #         'Content-Type' : 'application/json',
    #         'Cache-Control': 'no-cache'
    #     }

    #     print("\nURL:", url)
    #     g=input('PAUSE')
            
    #     response = requests.request('DELETE', url, json={}, headers=headers, cookies=cookies, verify=False)
    
    #     responseBody = response.json()
        
    #     if TestOutput == True:
    #         print('\ndelete_team\n', responseBody)
    #         print('\nresponseBody: ', response.status_code)
        
    #     return responseBody



    # ## @fn get_team_by_league : allows user to view all teams within a league
    # #
    # def get_team_by_league(self, cookies={}):
        
    #     url = self.environment + data["GetTeamByLeague"] + data['TestLeague']
        
    #     headers = {
    #         'Content-Type' : 'application/json',
    #         'Cache-Control': 'no-cache'
    #     }
            
    #     response = requests.request('GET', url, json={}, headers=headers, cookies=cookies, verify=False)
    
    #     responseBody = response.json()
        
    #     # if TestOutput == True:
    #     #     print('\nget_team_by_league\n', responseBody)
    #     #     print('\nresponseBody: ', response.status_code)
        
    #     return responseBody



    # ## @fn update_team : allows user to update a team they've created via id
    # #
    # def update_team(self, teamName='', League='', cookies={},
    #                 teamNameExclude=False, LeagueExclude=False):
        
    #     url = self.environment + data["UpdateTeam"] + str(self.CreatedTeamId[0])
        
    #     headers = {
    #         'Content-Type' : 'application/json',
    #         'Cache-Control': 'no-cache'
    #     }
        
    #     body = {}
        
    #     if teamNameExclude == True:
    #         pass
    #     elif teamName != '':
    #         body['teamName'] = teamName
    #     else:
    #         body['teamName'] = ''
            
    #     if LeagueExclude == True:
    #         pass
    #     elif League != '':
    #         body['League'] = League
    #     else:
    #         body['League'] = ''
            
    #     response = requests.request('PUT', url, json=body, headers=headers, cookies=cookies, verify=False)
    
    #     responseBody = response.json()
        
    #     if TestOutput == True:
    #         print('\nupdate_team\n', responseBody)
    #         print('\nstatus_code: ', response.status_code)
        
    #     return responseBody



    # ## @fn create_video : allows user to create a video
    # #
    # def create_video(self, awsUrl='', visitingTeam='', endTime=0, eventType='',
    #                  fullVideoId='', importance=0, profile='', score='', 
    #                  startTime=0, userId='', cookies={},
    #                  awsUrlExclude=False, visitingTeamExclude=False, endTimeExclude=False,
    #                  eventTypeExclude=False, fullVideoIdExclude=False, importanceExclude=False,
    #                  profileExclude=False, scoreExclude=False, startTimeExclude=False, 
    #                  userIdExclude=False):
        
    #     url = self.environment + data["CreateVideo"]
        
    #     headers = {
    #         'Content-Type' : 'application/json',
    #         'Cache-Control': 'no-cache'
    #     }
        
    #     body = {}
        
    #     if awsUrlExclude == True:
    #         pass
    #     elif awsUrl != '':
    #         body['awsUrl'] = awsUrl
    #     else:
    #         body['awsUrl'] = ''
            
    #     if visitingTeamExclude == True:
    #         pass
    #     elif visitingTeam != '':
    #         body['visitingTeam'] = visitingTeam
    #     else:
    #         body['visitingTeam'] = ''

    #     if endTimeExclude == True:
    #         pass
    #     elif endTime != '':
    #         body['endTime'] = endTime
    #     else:
    #         body['endTime'] = ''
            
    #     if eventTypeExclude == True:
    #         pass
    #     elif eventType != '':
    #         body['eventType'] = eventType
    #     else:
    #         body['eventType'] = ''

    #     if fullVideoIdExclude == True:
    #         pass
    #     elif fullVideoId != '':
    #         body['fullVideoId'] = fullVideoId
    #     else:
    #         body['fullVideoId'] = ''
            
    #     if importanceExclude == True:
    #         pass
    #     elif importance != '':
    #         body['importance'] = importance
    #     else:
    #         body['importance'] = ''

    #     if profileExclude == True:
    #         pass
    #     elif profile != '':
    #         body['profile'] = profile
    #     else:
    #         body['profile'] = ''
            
    #     if scoreExclude == True:
    #         pass
    #     elif score != '':
    #         body['score'] = score
    #     else:
    #         body['score'] = ''

    #     if startTimeExclude == True:
    #         pass
    #     elif startTime != '':
    #         body['startTime'] = startTime
    #     else:
    #         body['startTime'] = ''
            
    #     if userIdExclude == True:
    #         pass
    #     elif userId != '':
    #         body['userId'] = userId
    #     else:
    #         body['userId'] = ''
            
    #     response = requests.request('POST', url, json=body, headers=headers, cookies=cookies, verify=False)
    
    #     responseBody = response.json()
        
    #     if TestOutput == True:
    #         print('\ncreate_video\n', responseBody)
    #         print('\nstatus_code: ', response.status_code)
        
    #     # Save the created teams id.
    #     if response.status_code == 200:
    #         self.CreatedvideoId.append(responseBody[0]['ID'])
        
    #     return responseBody



    # ## @fn get_video_by_id : returns video as specified by parameter id
    # #
    # def get_video_by_id(self, cookies={}, videoId=''):
        
    #     if videoId == '':
    #         videoId = '123456'

    #     url = self.environment + data["GetVideoById"] + videoId

    #     headers = {
    #         'Content-Type' : 'application/json',
    #         'Cache-Control': 'no-cache'
    #     }
            
    #     response = requests.request('GET', url, json={}, headers=headers, cookies=cookies, verify=False)
    
    #     responseBody = response.json()
        
    #     if TestOutput == True:
    #         print('\nget_video_by_id\n', responseBody)
    #         print('\nresponse.status_code: ', response.status_code)
        
    #     return responseBody



    # ## @fn get_videos : returns list of user's videos
    # #
    # def get_videos(self, cookies={}):
        
    #     url = self.environment + data["GetVideos"]

    #     headers = {
    #         'Content-Type' : 'application/json',
    #         'Cache-Control': 'no-cache'
    #     }
            
    #     response = requests.request('GET', url, json={}, headers=headers, cookies=cookies, verify=False)
    
    #     responseBody = response.json()
        
    #     if TestOutput == True:
    #         print('\nget_videos\n', responseBody)
    #         print('\nresponse.status_code: ', response.status_code)
        
    #     return responseBody



    # ## @fn get_stored_videos : returns list of videos that user has stored
    # #
    # def get_stored_videos(self, cookies={}):
        
    #     url = self.environment + data["GetStoredVideos"]

    #     headers = {
    #         'Content-Type' : 'application/json',
    #         'Cache-Control': 'no-cache'
    #     }
            
    #     response = requests.request('GET', url, json={}, headers=headers, cookies=cookies, verify=False)
    
    #     responseBody = response.json()
        
    #     if TestOutput == True:
    #         print('\nget_stored_videos\n', responseBody)
    #         print('\nresponse.status_code: ', response.status_code)
        
    #     return responseBody



    # ## @fn delete_video : deletes video as specified by parameter id
    # #
    # def delete_video(self, cookies={}, videoId=''):
        
    #     if videoId == '':
    #         videoId = ('123456')

    #     url = self.environment + data["DeleteVideo"]  + videoId

    #     headers = {
    #         'Content-Type' : 'application/json',
    #         'Cache-Control': 'no-cache'
    #     }
            
    #     response = requests.request('DELETE', url, json={}, headers=headers, cookies=cookies, verify=False)
    
    #     responseBody = response.json()
        
    #     if TestOutput == True:
    #         print('\ndelete_video\n', responseBody)
    #         print('\nresponse.status_code: ', response.status_code)
        
    #     return responseBody



    # def GetLoginCookies(self):
    #     return self.LoginCookies

    # def GetClassicReelId(self):
    #     return self.ReelTypeIds[0]['ID']

    # def GetTopReelId(self):
    #     return self.ReelTypeIds[1]['ID']

    # def GetTrendingReelId(self):
    #     return self.ReelTypeIds[2]['ID']

    # def GetVideoId(self):
    #     if len(self.CreatedvideoId) == 0:
    #         return ''
    #     else:
    #         return self.CreatedvideoId[0]




def testClass():
    # Declare class objects. Create class instance. DONE
    user = FlipTix()


    # # Method signature. DONE
    # # def register(self, email='', password='', phone='', company='',
    # #              name='', emailExclude=False, passwordExclude=False,
    # #              phoneExclude=False, companyExclude=False, nameExclude=False):
    # user.register(data['TestEmail'], data['TestPassword'], data['TestPhone'], 
    #               data['TestCompany'], data['TestName'])


    # # Method signature. DONE
    # # confirm_registration(self, username='', code='',  usernameExclude=False, codeExclude=False):
    # user.confirm_registration(data['TestEmail'], '')


    # # Method signature. DONE
    # # resend_confirmation(self, username='', emailExclude=False):
    # user.resend_confirmation(data['TestNonConfirmedEmail'])


    # # Method signature. DONE
    # # def login(self, username='', password='',  usernameExclude=False, passwordExclude=False):
    # user.login(data['TestEmail'], data['TestPassword'])


    # # Method signature. DONE
    # #def forgot_password(self, email='', emailExclude=False):
    # user.forgot_password(data['TestEmail'])


    # # Method signature. DONE
    # # def getReelTypes(self, cookies={):
    # user.getReelTypes(user.GetLoginCookies())


    # # Method signature. DONE
    # # def get_leagues(self, cookies={}):
    # user.get_leagues(user.GetLoginCookies())


    # # Method signature. DONE
    # # def create_team(self, teamName='', League='', cookies={},
    # #                 teamNameExclude=False, LeagueExclude=False):
    # user.create_team(data['TestTeamName'], data['TestLeague'], user.GetLoginCookies())


    # # Method signature. DONE
    # # def delete_team(self, cookies={}):
    # user.delete_team(user.GetLoginCookies())


    # # Method signature. DONE
    # # def get_team_by_league(self, cookies={}):
    # user.get_team_by_league(user.GetLoginCookies())


    # # Method signature. DONE
    # # def update_team(self, teamName='', League='', cookies={},
    # #               teamNameExclude=False, LeagueExclude=False):
    # user.update_team(data['TestTeamName'], data['TestLeague'], user.GetLoginCookies())



    # # Method signature. DONE
    # # def create_video(self, awsUrl='', visitingTeam='', endTime=0, eventType='',
    # #                 fullVideoId='', importance=0, profile='', score='', 
    # #                 startTime=0, userId='', cookies={},
    # #                 awsUrlExclude=False, visitingTeamExclude=False, endTimeExclude=False,
    # #                 eventTypeExclude=False, fullVideoIdExclude=False, importanceExclude=False,
    # #                 profileExclude=False, scoreExclude=False, startTimeExclude=False, 
    # #                 userIdExclude=False):
    # user.create_video(data['TestAwsUrl'], data['TestVisitingTeam'], data['TestEndTime'], 
    #                   data['TestEventType'], data['TestFullVideoId'], data['TestImportance'], 
    #                   data['TestProfile'], data['TestScore'], data['TestStartTime'], 
    #                   data['TestUserId'], user.GetLoginCookies())
    


    # # Method signature. DONE
    # # def get_video_by_id(self, cookies={}, videoId=''):
    # user.get_video_by_id(user.GetLoginCookies(), user.GetVideoId())


    # # Method signature. DONE
    # # def get_videos(self, cookies={}):
    # user.get_videos(user.GetLoginCookies())


    # # Method signature. DONE
    # # def get_stored_videos(self, cookies={}):
    # user.get_stored_videos(user.GetLoginCookies())


    # # Method signature. DONE
    # # def delete_video(self, cookies={}, videoId=''):
    # user.delete_video({}, user.GetVideoId())

testClass()
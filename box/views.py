import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from boxsdk import Client, JWTAuth
from boxsdk.config import API
from boxsdk.object.user import User

import logging_network # Custom logger for use with Client

###
# Edit your ~/.bash_profile to include the following lines with your values
#   export BOX_SDK_CLIENTID=1234567890ABCD
#   export BOX_SDK_CLIENTSECRET=ABCDEFGHI1234
#   export BOX_SDK_EID=123456
###
client_id = os.environ.get('BOX_SDK_CLIENTID') # Your Client ID
client_secret = os.environ.get('BOX_SDK_CLIENTSECRET') # Your Client Secret
eid = os.environ.get('BOX_SDK_EID') # Enterprise ID number

# These will be set on Authentication
global access_token
global refresh_token

global authObject
global clientObject

###
#  The API seems to have changed so I had to write a workaround to get the list of app users.
#
# Edit: This is probably a bug.  The response format changes based on the settings at:
#   Box -> Admin Console -> Apps -> Custom Applications -> Actions -> Edit App
#
# This  is a good example of how to make calls directly to the API once authenticated
###
def listUsersWorkaround(client):
    url = '{0}/users'.format(API.BASE_API_URL)
    box_response = client.make_request('GET', url)
    response = box_response.json()
    return [User(client._session, item['id'], item) for item in response['entries'].values()]


### Called by the authentication method.
def _store_tokens(access_t, refresh_t):
    global access_token, refresh_token
    access_token=access_t
    refresh_token=refresh_t

    ### The SDK is supposed to refresh the token if/when it expires.
    ### This token will work for testing with PostMan or curl or others
    print "Access Token: {0}".format(access_token)
    ### JWT does not have refresh tokens.  This will be the Python type 'None'
    print "Refresh Token: {0}".format(refresh_token)
    return


###
# 1. Run the django server
#       python manage.py runserver
# 2. Navigate to localhost:8000/box/
#
#
# Python SDK at: https://github.com/box/box-python-sdk
#
###
def index(request):
    ###
    # You will need to place your RSA private key in /BoxApps/box/rsakey.pem
    #
    # After this auth method the access token will be set.
    #
    # Note: JWT does not use refresh tokens
    ###
    authObject = JWTAuth(client_id=client_id,
        client_secret=client_secret,
        enterprise_id=eid,
        rsa_private_key_file_sys_path=os.path.join(os.path.dirname(__file__),'rsakey.pem'),
        store_tokens=_store_tokens)

    ### This SDK allows for a custom network object. The one used here logs all calls to STDOUT
    clientObject = Client(authObject, network_layer=logging_network.LoggingNetwork())
    # client = Client(auth)

    ### Returns the user object for the developer account.
    ### Will error if the scope is not set to All Users.
    # me = client.user(user_id='me').get()
    # print 'user login: ' + me['login']

    # user = clientObject.create_user("Mike Neas")
    # authObject.authenticate_app_user(user)
    # root_folder = clientObject.folder(folder_id='0').get()
    # print 'folder owner: ' + root_folder.owned_by['login']
    # print 'folder name: ' + root_folder['name']

    context={
        "users_list":listUsersWorkaround(clientObject)
    }
    return render(request, "box/index.html", context)


def OAuth(request):
    return HttpResponseRedirect(request)


def deleteAll(request):
    ### DANGER: CANNOT BE UNDONE
    # print "Delete all App Users"
    # for u in client.users():
    #     print u.delete()
    return HttpResponse("Uncomment the code first.")



import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from boxsdk.config import API
from boxsdk.object.user import User
from box import jwtAuth

from jwtAuth import *

###
# Edit your ~/.bash_profile to include the following lines with your values
#   export BOX_SDK_CLIENTID=1234567890ABCD
#   export BOX_SDK_CLIENTSECRET=ABCDEFGHI1234
#   export BOX_SDK_EID=123456
###
# global client_id, client_secret, eid

### Example of how to make calls directly to the API after authentication
def listAllUsers(client):
    url = '{0}/users'.format(API.BASE_API_URL)
    box_response = client.make_request('GET', url)
    response = box_response.json()
    return [User(client._session, item['id'], item) for item in response['entries']]


###
# 1. Run the django server
#       python manage.py runserver
# 2. Navigate to localhost:8000/box/
#
###
def index(request):
    initializeClientAndAuthObjects()

    ### Use this to create users (for now)
    # user = clientObject.create_user("Daniel Kaplan")

    context={
        "users_list":jwtAuth.clientObject.users()
    }
    return render(request, "box/index.html", context) ### Gets index.html from /box/templates/box/


def detail(request, user_id):
    initializeClientAndAuthObjects()

    u = jwtAuth.clientObject.user(user_id=user_id).get() # Create a user object
    user_token = jwtAuth.authObject.authenticate_app_user(u) # Auth with that user
    user_client = Client(jwtAuth.authObject) # Create a new client for that user

    me = user_client.user(user_id='me').get() # Get the user's info
    print 'Sending detail view for: ' + me['name']

    # print 'user login: ' + me['login']

    context = {
        "user": jwtAuth.clientObject.user(user_id=user_id).get(),
        "token": user_token
    }
    return render(request, "box/detail.html", context)


### NOT COMPLETE
def deleteAll(request):
    ### DANGER: CANNOT BE UNDONE
    # print "Delete all App Users"
    for u in clientObject.users():
        print u.delete()
    return HttpResponse("Uncomment the code first.")






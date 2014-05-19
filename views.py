'''import these modules into your views file'''

from urllib2 import urlopen
from facebook import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
import datetime

'''this is the function that is called when the facebook login button is clicked in your html page
  to get this view to work change the following settings in the function
  client_id= set this to the client id that facebook give you when you set up your app
  client_secret= set this to the client secret that facebook give you when you set up your app'''

def facebookreturn(request):
    ##this opens the url to receive the access token from facebook that allows you to peform the API call to get user information
    
    code = request.GET.get('code')
    site=urlopen("https://graph.facebook.com/oauth/access_token?client_id="YOUR APPS CLIENT ID"&redirect_uri=http://localhost:8000/facebookreturn&client_secret="YOUR APPS CLIENT SECRET&code=%s#_=_" % code)
    site=site.read()
    
    ##this gets the token sent back into the right format for the API call
    site=site.replace("access_token=",'')
    m=site.find('&expires=')
    site=site[0:m]
    
    ##this is the API call that uses the facebook module to get the user data
    graph = GraphAPI(site)
    profile = graph.get_object("me")
    facebook_id= profile.get('id')
    username= profile.get('username')
    email= profile.get('email')
    name= profile.get('name')
    birthday= profile.get('birthday')
    birthday=datetime.datetime.strptime(birthday, '%m/%d/%Y').strftime('%Y-%m-%d')
    gender= profile.get('gender')
    link= profile.get('link')
    try:
        ##this checks if the user is registered on the system, if so it authenticates the user, if not it creates the user
        user=MyUser.objects.get(email=email)
        user = authenticate(username=email, password=facebook_id)
        return HttpResponse('this users email address is %s' % user)
    except ObjectDoesNotExist:
        New_user=MyUser.objects.create_user(email=email, date_of_birth=birthday, password=facebook_id, facebook_id=facebook_id, link=link, name=name, gender=gender, username=username)
        return HttpResponse("facebook id %s\n, username %s\n, email %s\n, name %s\n, birthday %s\n, gender %s\n, link %s" % (facebook_id, username, email, name, birthday, gender, link))
    

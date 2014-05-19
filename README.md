Django-facebook-login
=====================

Login in users on a custom user model in django using facebook

After searching for sometime I could not find a solution to the way i need to log users into a django built website using facebook so i have used a combination building a manual login flow as found on the facebook developers section here:

https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow/v2.0

To process the api calls in python i am using the python facebook module found here:

https://pypi.python.org/pypi/facebook-sdk/0.4.0

and then using the information return by the facebook login flow to fill in the details of a custom user model and create that user.

Within this custom user model the email address returned by the facebook api call is the username of the user and the facebook id returned is the password of the user.

To follow through this guide i have attached all the files needed with the code within them in orded to get the system running, you will need to edit your setting.py, urls.py, models.py, views.py and your .html file where your login button is found to match what I have within mine

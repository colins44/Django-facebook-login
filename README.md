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


STEP BY STEP GUILD TO GETTING THIS WORKING

Make sure you are using django 1.5 or higher as this allows custom user models

1. create an app in the facebook developers page, this app will give you a CLIENT KEY AND CLIENT SECRET, never display the CLIENT SECRET in your HTML page
2. Install the facebook module
3. Copy and paste the code from this repositories models.py file to your apps models.py file, this is the new custome users model code
4. Ammend your URLs.py file to include that included in this repositories urls.py file
5. Copy and paste the code within the views.py to your views.py file
6. run the command ./manage syncdb
7. The add the columns to your table by running ./manage.py dbshell this ALTER TABLE 'table name' ADD COLUMN 'column name' and type (these are displayed to you when you run ./manage.py syncdb)
8. start the server up using ./manage.py runserver localhost:8000 (NOTE IT NEEDS TO BE THIS ADDRESS DUE TO THE LINKS WITHIN THE HTML BUTTON)
9. Open up your webpage that you have placed the HTML code in, from this repositories FACEBOOK LOGIN BUTTON HTML and click the link, this should now run the function that calls the facebook API and creates a user on your database 
10. Find that user within your database and click the box "is admin" this will allow you to log into the admin part of your site (take note of your email address, which will become your username and your facebook id which will become your password)
11. Now add the code from this repositories setting.py file to your settings.py file
12. Now log out of your admin site and log back in using your new details (email address and facebook is)

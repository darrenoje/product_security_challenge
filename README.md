
# Zendesk Product Security
### The Zendesk Product Security Challenge

Hello friend,

We are super excited that you want to be part of the Product Security team at Zendesk.

**To get started, you need to fork this repository to your own Github profile and work off that copy.**

In this repository, there are the following files:
1. README.md - this file
2. project/ - the folder containing all the files that you require to get started
3. project/index.html - the main HTML file containing the login form
4. project/assets/ - the folder containing supporting assets such as images, JavaScript files, Cascading Style Sheets, etc. You shouldn’t need to make any changes to these but you are free to do so if you feel it might help your submission

As part of the challenge, you need to implement an authentication mechanism with as many of the following features as possible. It is a non exhaustive list, so feel free to add or remove any of it as deemed necessary.

✔ Input sanitization and validation
+ Escaping of html characters
+ Verify that password entered is allowed when creating an account

✔ Password hashed
+ Used Bcrypt hashing function which is a class of slow hashes 

✔ Prevention of timing attacks
+ Bcrypt offers infeasible timing attacks as it uses timing-safe comparison 
+ Bcrypt can also increase the cost factor, which increases security by slowing down the hashing

✔ Logging
+ Simple logging of events

✔ CSRF prevention
+ Used Flask-WTF implementation and included csrf tokens in html webpages

✔ Account lockout
+ Implemented a maximum number of attempts to login per session, failure to do so causes an account lockout

✔ Cookie
+ Cookie is returned in response

✔ HTTPS
+ Utilised on-the-fly certificates to serve the web application over HTTPS
+ Note: In order to run the web application, you need to trust the self-signed certificate

✔ Known password check
+ Implemented a check of user's set password against a list of common passwords courtesy from https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt

➖ Multi factor authentication
➖ Password reset / forget password mechanism

You will have to create a simple binary (platform of your choice) to provide any server side functionality you may require. Please document steps to run the application. Your submission should be a link to your Github repository which you've already forked earlier together with the source code and binaries.

Thank you!

-----------------------------------
**Pre-requisite to run the application**
1. Flask: *pip install flask*
2. Flask-WTF: *pip install flask_wtf*
3. SQLAlchemy: *pip install flask-sqlalchemy*
4. Bcrypt: *pip install bcrypt*

**How to run the application locally**
1. Run command: *python server.py*
2. Open https://127.0.0.1:5000/ in your preferred browser


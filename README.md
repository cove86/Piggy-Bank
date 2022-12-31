# Pbank
#### Video Demo:  https://youtu.be/u4vkEiWcCkE
#### Description:
  This is a flask app where you can register an account and keep track of loose change! You can make withdrawls and deposits and see your transaction history
  as all data is stored in a sqllite database. This has been built using python/flask & bootstrap.

The main app is stored in the pbank folder, I followed the flask tutorial to structure this project.

__initi __.py is where the app initialises from, this is the app factory and is where the app is created from, there are blueprints that call to the seperate functions of the app.

auth.py contains all of the logic for registering and logging in a user, it also contains a login_required wrapper function used to ensure only a logged in user has access to as certain page.

bank.py contains most of the logic of the app, balance and transactions.

db.py contains the initialisation of the database.

helpers.py contains some helper functions used by bank.py, logic around deposit, withdrawal, transactions and total amount are defined in here.

static contains a logo and styles.css file

templates contains allof the html used in the project, there is a base.html which is the template for all of the pages, jinja is used in some files to add logic to the pages themselves

# Pbank
#### Video Demo:  https://youtu.be/u4vkEiWcCkE
#### Description:
  This is a flask app where you can register an account and keep track of loose change! You can make withdrawls and deposits and see your transaction history
  as all data is stored in a sqllite database. This has been built using python/flask & bootstrap.

The main app is stored in the pbank folder, I followed the flask tutorial to structure this project.

__initi __.py is where the app initialises from, this is the app factory and is where the app is created from, there are blueprints that call to the seperate functions of the app.

auth.py contains all of the logic for registering and logging in a user, it also contains a login_required wrapper function used to ensure only a logged in user has access to as certain page.

bank.py contains all of the routes around the bank side of the app, there is a balance route that cotains the logic for the balance page on the website aswell as the deposit and withdraw button and functionality. The deposit, withdraw, enough_to_withdraw, tran_history, total functions are imported from helpers.py in order to build the logic for thius page.

db.py contains the initialisation of the database.

helpers.py contains some helper functions used by bank.py, logic around deposit, withdrawal, transactions and total amount are defined in here.

static contains a logo and styles.css file

templates contains all of the html used in the project, split into auth and bank folders, there is a base.html which is the template for all of the pages in the root of the templates folder. 

jinja is used to add logic in all of the html pages, in balance.htmlo it is used to add in each value from the database for each value and then to add the total amount at the end, in index.html it is used to only display certain links if the user is logged in and in transactions.html it is used to pull and display the transaction history from the database.

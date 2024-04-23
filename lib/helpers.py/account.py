
from models.shopper import Shopper

def create_account():
    pass

def login():
    ##use find username to set the user, then check pass based on user
    ##if password is correct set shopper to this shopper in the main page for store purposes
    pass

def account():
    print('Welcome, please login or create an account.')
    choice = input('Enter login or create > ')
    if (choice.lower() == 'login'):
        login()
    elif (choice.lower() == 'create'):
        create_account()
    else:
        print('Invalid choice')
        print('Please enter login if you have an account, or enter create if you would like to create an account')
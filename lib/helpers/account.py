
from models.shopper import Shopper

def create_account():
    while True:
        username = input('Username: ')
        if Shopper.check_username(username) == True:
            print('Username is taken')
            create_account()
        else:
            password = input('Password: ')
            funds = input('How much money would you like to add: ')
        try:
            shopper = Shopper.create_user(username, password, funds)
            print('Account created successfully')
            print(Shopper.get_all())
        except Exception as exc:
            print('An error occured creating your account, please try again')
        

def login():
    while True:
        username = input("enter username: ")
        user = Shopper.find_user_by_username(username)
        if user:
            password = input('Enter password: ')
            if user.password == password:
                print('login successful')
                print(f'Welcome back {user.username}!')
                return user
            else:
                print('Incorrect password')
        else:
            print('Username does not exist')
    


def account():
    while True:
        print('Welcome, do you have an account')
        choice = input('Y/N: ')
        if choice.upper() == 'Y':
            login()
            break
        elif choice.upper() == 'N':
            create_account()
            break
        else:
            print('Invalid choice, please enter either Y or N')
            

from models.shopper import Shopper

def account():
    while True:
        print('Welcome, do you have an account')
        choice = input('Y/N: ')
        if choice.upper() == 'Y':
            active_user = login()
            if active_user:
                return active_user
        elif choice.upper() == 'N':
            return create_account()
            
            
        else:
            print('Invalid choice, please enter either Y or N')


def create_account():
    while True:
        username = input('Username: ')
        if Shopper.check_username(username) == True:
            print('Username is taken')
        else:
            password = input('Password: ')
        try:
            user = Shopper.create_user(username, password)
            print('Account created successfully')
            return user
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
    
            
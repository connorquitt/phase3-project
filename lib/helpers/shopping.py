from models.book import Book
from models.shopper import Shopper

def view_collection():
    pass

def add_to_cart():
    pass

def view_cart():
    pass

def search():
    ##saerch by title, author, or genre
    pass

def checkout():
    pass

def shopping(user):
    print(f'Welcome {user.username}, how can I help you today?')
    print('1) view library')
    print('2) search')
    print('3) view cart')
    print('4) checkout')
    choice = input('Please select 1, 2, 3, or 4> ')
    if choice == '1':
        view_collection()
    elif choice == '2':
        search()
    elif choice == '3':
        view_cart()
    elif choice == '4':
        checkout() #need to import


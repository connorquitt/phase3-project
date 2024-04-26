from models.book import Book
from models.shopper import Shopper

cart = []

def view_collection():
    print(Book.get_all())

def add_to_cart():
    print('Please enter the id of the book you would like to add')
    id = input('> ')
    curr_book = Book.find_item_by_id(int(id))
    cart.append(curr_book)
    print(cart)

def view_cart():
    pass

def search():
    ##saerch by title, author, or genre
    pass

def checkout():
    pass

def shopping(user):
    while True:
        print(f'Welcome {user.username}, how can I help you today?')
        print('1) view library')
        print('2) search')
        print('3) view cart')
        print('4) checkout')
        choice = input('Please select 1, 2, 3, or 4> ')
        if choice == '1':
            view_collection()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            checkout() #need to import


from models.book import Book
from models.shopper import Shopper

cart = []

def view_collection():
    available_items = Book.get_all_available(1)
    for item in available_items:
        print(item.title)

def add_to_cart():
    print('Please enter the id of the book you would like to add')
    id = input('> ')
    curr_book = Book.find_item_by_id(int(id))
    cart.append(curr_book)

def view_cart():
    for item in cart:
        print(item.title)

def empty_cart():
    cart.clear()

def search():
    while True:
        print('How would you like to search?')
        choice = input('please enter author, title, or genre')
        if choice.lower() == 'author':
            print('author')
        elif choice.lower() == 'title':
            print('title')
        elif choice.lower() == 'genre':
            print('genre')
        else:
            print('Invalid choice, please select from author, title, or genre')

def checkout(user):
        if len(cart) > 0:
            for item in cart:
                print(item.title)
                Book.update_owner_id(user.id, item.id)
                if len(cart) == 0:
                    print('Cart is now empty')
                    break
        else:
            print("you're cart appears to be empty, please add items before checking out")

def view_owned_items(user):
    owned = Book.get_all_available(user.id)
    for item in owned:
        print(item.title)

def sell_items(user):
    owned = Book.get_all_available(user.id)
    for item in owned:
        Book.update_owner_id(1, item.id)
    print('done')

def shopping(user):
    while True:
        print(f'Welcome {user.username}, how can I help you today?')
        print('1) view library')
        print('2) search')
        print('3) add to cart')
        print('4) clear cart')
        print('5) view cart')
        print('6) checkout')
        print('7) view owned items')
        print('8) sell owned items')
        choice = input('Please select an option > ')
        if choice == '1':
            view_collection()
        elif choice == '2':
            search()
        elif choice == '3':
            add_to_cart()
        elif choice == '4':
            empty_cart()
        elif choice == '5':
            view_cart()
        elif choice == '6':
            checkout(user)
        elif choice == '7':
            view_owned_items(user)
        elif choice == '8':
            sell_items(user)

from models.book import Book
from models.shopper import Shopper

##move all cart functionality into one function so i don't have to do this loop and import it into shopping function

cart = []

def view_collection():
    print(Book.get_all())
    ##change to only print books with the owner id of 1

def add_to_cart():
    print('Please enter the id of the book you would like to add')
    id = input('> ')
    curr_book = Book.find_item_by_id(int(id))
    cart.append(curr_book)

def view_cart():
    print(cart[2])

def empty_cart():
    print(cart)
    cart.clear()
    print(cart)

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

def checkout():
    while True:
        if len(cart) > 0:
            for item in cart:
                ##change owner_id and remove from cart
                pass
        else:
            print("you're cart appears to be empty, please add items before checking out")

def shopping(user):
    while True:
        print(f'Welcome {user.username}, how can I help you today?')
        print('1) view library')
        print('2) search')
        print('3) add to cart')
        print('4) clear cart')
        print('5) view cart')
        print('6) checkout')
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
            checkout()


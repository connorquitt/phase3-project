from models.book import Book
from helpers.search import search
from helpers.approach_counter import approach_counter
from helpers.shopping_cart import shopping_cart
from helpers.shopping_cart import add_to_cart
from helpers.shopping_cart import view_collection
from models.shopper import Shopper



def shopping(user):
    while True:
        print(f'Welcome {user.username}, how can I help you today?')
        print('1) View All')
        print('2) Search')
        print('3) Cart')
        print('4) Buy/Sell Items')
        print('5) Leave Store')
        choice = input('Please select an option > ')
        if choice == '1':
            view_collection()
        elif choice == '2':
            search()
        elif choice == '3':
            shopping_cart()
        elif choice == '4':
            approach_counter(user)
        elif choice == '5':
            leave_store()

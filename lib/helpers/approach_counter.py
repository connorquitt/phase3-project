from models.book import Book
from helpers.shopping_cart import cart

def approach_counter(user):
    while True:
        print('1) Checkout')
        print('2) Sell Items')
        print('3) Back')
        choice = input('> ')
        if choice == '1':
            checkout(user)
        elif choice == '2':
            print('1) Return Items')
            print('2) View Owned Books')
            print('3) Donate New Book')
            print('4) Leave')
            choice = input('> ')
            if choice == '1':
                sell_items(user)
            elif choice == '2':
                view_owned_items(user)
            elif choice == '3':
                sell_new_item()
            elif choice == '4':
                return None
            else:
                print('Invalid choice, please select one of the options')
        elif choice == '3':
            return None
def sell_items(user):
    owned = Book.get_all_available(user.id)
    for item in owned:
        Book.update_owner_id(1, item.id)
    print('done')

def sell_new_item():
    print('Please tell us a little about the book!')
    title = input('Title > ')
    author = input('Author > ')
    genre = input('Genre > ')
    Book.create_item(title, author, genre)

def view_owned_items(user):
    owned = Book.get_all_available(user.id)
    for item in owned:
        print(item.title)

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
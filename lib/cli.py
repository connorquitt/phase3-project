# lib/cli.py

from models.shopper import Shopper
from models.book import Book

def leave_store():
    print('Goodbye!')
    exit()

def view_all_shoppers():
    for i, shopper in enumerate(Shopper.get_all(), start=1):
        print(f'{i}) {shopper.username} | Book Total: {len(shopper.books())}')

def select_shopper():
    while True:
        view_all_shoppers()
        shoppers = Shopper.get_all()
        choice = input('Please select shopper >')
        if choice.lower() == 'e':
            leave_store()
        elif choice.isnumeric() and len(shoppers) >= int(choice):
            current_shopper = shoppers[int(choice) -1]
            return current_shopper
        else:
            print('Invalid choice please try again')

def add_shopper():
    while True:
        print('Please enter shopper details')
        username = input('Username > ')
        password = input('Password > ')
        try:
            Shopper.create_user(username, password)

        except Exception as exc:
            print('Invalid shopper')
        print('Press enter to add another shopper')
        print('Press "e" to leave')
        choice = input('> ')
        if choice.lower() == 'e':
            return None

def view_collection():
    available_items = Book.get_all_available(1)
    for item in available_items:
        print(f'{item.id}) | {item.title} | {item.genre}')

def add_book_to_store():
    while True:
        print('Press enter to add a book')
        print('Press "e" to leave')
        choice = input('> ')
        if choice.lower() == 'e':
            return None
        else:
            print('Please tell us a little about the book!')
            title = input('Title > ')
            author = input('Author > ')
            genre = input('Genre > ')
            try:
                Book.create_item(title, author, genre)
            except Exception as exc:
                print('Invalid book')

def modify_or_delete_menu():
    while True:
        print('1) Modify a shopper')
        print('2) Delete a shopper')
        choice = input('> ')
        if choice.lower() == 'e':
            leave_store()
        elif choice == '1':
            modify_shopper = select_shopper()
            print('Update username? Y/N')
            update_username_choice = input('> ')
            if update_username_choice.lower() == 'y':
                username = input('Please enter new username > ')
                Shopper.update_username(username, modify_shopper.id)
                print('Update password? Y/N')
                update_password_choice = input('> ')
                if update_password_choice.lower() == 'y':
                    password = input('Please enter new password > ')
                    Shopper.update_password(password, modify_shopper.id)
            else:
                print('l;akjdf')
        elif choice == '2':
            delete_shopper = select_shopper()
            print(f'Are you sure you want to permenantly delete {delete_shopper.username}? Y/N')
            delete_choice = input('> ')
            if delete_choice.lower() == 'y':
                Shopper.delete_user(delete_shopper.id)
            elif delete_choice.lower() == 'n':
                print('Action canceled')
                return None
        else:
            print('Invalid choice, please select from the given options')

def stars():
    print('******************')

def main():
    while True:
        print('Welcome, how can I help you')
        print('Press "e" to leave at anytime')
        print('1) View all shoppers')
        print('2) Select shopper')
        print('3) Add shopper')
        print('4) Modify or delete shopper')
        print('5) View inventory')
        choice = input('> ')
        if choice.lower() == 'e':
            leave_store()
        elif choice == '1':
            view_all_shoppers()
        elif choice == '2':
            shopper = select_shopper()
        elif choice == '3':
            add_shopper()
        elif choice == '4':
            modify_or_delete_menu()
        elif choice == '5':
            view_collection()
            stars()
            add_book_to_store()
        else:
            print('Invalid choice, please select a number 1-5')
    


if __name__ == "__main__":
    main()




"""
1) Changing app to be an app for the owner
    - No longer need login or account stuff
    - the menu needs to start with seeing all users, select user, delete user, modify user, and view inventory (allow to add books that are "owned" by the store/delete books)
        - After selecting a user need to keep it saved similar to how account does, give options to view, add, or delete books that are owned by a shopper
            - Add books method to shopper to show all books owned by said shopper and give books a shopper method to show the owner of the book
    - Get the code for the numbering thing that nancy talked about
    -README needs to be done like rn
"""
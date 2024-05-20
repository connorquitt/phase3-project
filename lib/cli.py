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
                print('Invalid input please try again')
        elif choice == '2':
            shopper = select_shopper()
            delete_shopper(shopper)
        else:
            print('Invalid choice, please select from the given options')

def view_shopper_books(shopper):
        for i, book in enumerate(shopper.books(), start = 1):
            print(f"{i}) {book.title} | {book.author} | {book.genre}")

def add_books_to_shopper(shopper):
    while True:
        print(f"1) Add a new book to {shopper.username}")
        print(f"2) Add book from store inventory")
        print('Press "e" to leave')
        choice = input('> ')
        if choice.lower() == 'e':
            return None
        elif choice == '1':
            title = input('Title: ')
            author = input('Author: ')
            genre = input('Genre: ')
            try:
                Book.create_item(title, author, genre, owner_id=shopper.id)
            except Exception as exc:
                print('Invalid book')
        elif choice == '2':
            books = Book.get_all_available()
            view_collection()
            book_choice = input('Select which book to give > ')
            if book_choice.isnumeric() and len(books) >= int(book_choice):
                book = books[int(book_choice) -1]
                book.update_owner_id(shopper.id, book.id)
            else:
                print('Invalid choice, please select one one of the available options')

def delete_book_from_shopper(shopper):
    books = shopper.books()
    if len(books) >= 1:
        view_shopper_books(shopper)
        choice = input(f"Please select book to remove from {shopper.username}'s account > ")
        book = books[int(choice) -1]
        ##Store ID is 1, setting ID to one returns it to store inventory
        book.update_owner_id(1, book.id)
        print(book.title)
    else:
        print('Shopper has no books')

def delete_shopper(shopper):
    choice = input(f'Are you sure you want to delete {shopper.username}? Y/N')
    if choice.lower() == 'y':
        Shopper.delete_user(shopper.id)
    elif choice.lower() == 'n':
        print('Canceling action')

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
            shopper_menu(shopper)
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
    
def shopper_menu(shopper):
    while True:
        print(f"{shopper.username}'s menu: ")
        print(f"1) View {shopper.username}'s books")
        print(f"2) Add books to {shopper.username}") 
        print(f"3) Remove books from {shopper.username}")
        print(f"4) Delete {shopper.username}")
        print('Press "e" to leave')
        choice = input('> ')
        if choice.lower() == 'e':
            leave_store()
        elif choice == '1':
            view_shopper_books(shopper)
        elif choice == '2':
            add_books_to_shopper(shopper)
        elif choice == '3':
            delete_book_from_shopper(shopper)
        elif choice == '4':
            delete_shopper(shopper)

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
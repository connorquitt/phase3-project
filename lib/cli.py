# lib/cli.py
from helpers.helpers import leave_store, view_all_shoppers, select_shopper, add_shopper, view_collection, add_book_to_store, modify_or_delete_menu, view_shopper_books, add_books_to_shopper, delete_book_from_shopper, delete_shopper, stars
from models.book import Book

def main():
    while True:
        print('Welcome, how can I help you')
        print('Press "e" to leave at anytime')
        print('1) View all shoppers')
        print('2) Select shopper')
        print('3) Add shopper')
        print('4) Modify or delete shopper')
        print('5) View inventory')
        print('6) Add/delete book')
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
        elif choice == '6':
            print('1) Add book')
            print('2) Delete book')
            choice = input('> ')
            if choice.lower() == 'e':
                return None
            elif choice == '1':
                add_book_to_store()
            elif choice == '2':
                book = select_book()
                delete_book_from_store(book)

        else:
            print('Invalid choice, please select a number 1-5')

def select_book():
    view_collection()
    book_list = Book.get_all_available(1)
    choice = input('Please select book to delete > ')
    if choice.isnumeric():
        current_book = book_list[int(choice) - 1]
        return current_book

def delete_book_from_store(book):
    choice = input(f'Are you sure you want to permanently delete {book.title}? Y/N > ')
    if choice.lower() == 'y':
        Book.delete_item(book.id)
    if choice.lower() == 'n':
        return None
    
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
            return None
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



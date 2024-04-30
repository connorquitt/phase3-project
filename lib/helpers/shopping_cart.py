from models.book import Book

cart = []

def view_collection():
    available_items = Book.get_all_available(1)
    for item in available_items:
        print(f'{item.id}) | {item.title} | {item.genre}')

def shopping_cart():
    while True:
        print('1) View Cart')
        print('2) Add Books to Cart')
        print('3) Clear Cart')
        print('4) Back')
        choice = input('> ')
        if choice == '1':
            view_cart()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            empty_cart()
        elif choice == '4':
            return None
        else:
            print('Invalid choice')

def add_to_cart():
    view_collection()
    while True:
        print('Please enter the id of the book you would like to add, or enter back to leave cart')
        id = input('> ')
        if id.lower() == 'back':
            return None
        elif isinstance(int(id), int):
            try:
                curr_book = Book.find_item_by_id(int(id))
                cart.append(curr_book)
            except Exception as exc:
                print('Invalid id')
        else:
            print('Invalid choice, please select a valid id')

def view_cart():
    for item in cart:
        print(item.title)
    leave = input('Press enter to go back > ')
    if leave:
        return None

def empty_cart():
    cart.clear()
    print('Your cart has been cleared')
    leave = input('Press enter to go back > ')
    if leave:
        return None


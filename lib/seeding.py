from models.shopper import Shopper
from models.book import Book

def fill():
    Shopper.drop_table()
    Shopper.create_table()
    Book.drop_table()
    Book.create_table()


    Shopper.create_user('paul', 'password')
    Shopper.create_user('Josh', 'password')

    Book.create_item('Capitalist Realism', 'Mark Fisher', 'Political')
    Book.create_item('Steal as much as you can', 'Nathalie Olah', 'Political')
    Book.create_item('Tao Te Ching', 'Lao Tzu', 'Religious')
    Book.create_item('The Corrosion of Character', 'Richard Sennett', 'Political')

fill()

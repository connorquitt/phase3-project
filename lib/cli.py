# lib/cli.py

from models.shopper import Shopper
from models.book import Book
from helpers.account import account
from helpers.shopping import shopping


def main():
    active_shopper = account()
    print('leaving account function')
    shopping(active_shopper)




if __name__ == "__main__":
    main()

#NEED TO DO TMR
##set up checkout function to remove all items from cart and change their owner_id
##define shopper function to change owner_id
##change view_collection to only show the items with store owner_id
##define sell functions to sell any items owned by active shopper or to define new items to sell
##give function to Book class to show all books owned by active shopper
##define books function to show all books with that shoppers id
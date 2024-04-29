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
##set up checkout function to remove all items from cart and change their owner_id DONE
##define book function to change owner_id DONE
##change view_collection to only show the items with store owner_id DONE
##define sell functions to sell any items owned by active shopper or to define new items to sell DONE
##give function to Book class to show all books owned by active shopper DONE
##set up view functions to only show title and not the whole object DONE
##find way to add timers between things happening so its not so disorienting
##consolodate functions so each page is less disorienting
##set up way to sell new item (used to create new item)
##test the create property testers
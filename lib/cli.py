# lib/cli.py

from models.shopper import Shopper
from models.book import Book
from helpers.account import account
from helpers.shopping import shopping


def main():
    active_shopper = account()
    print('leaving account function')
    shopping(active_shopper)


                

def prompts():
    #Welcome to store
    #What can I help you with today?
    #View library
    #Sell items
    #Search for item
    #Search for genre
    #View cart
    #Are you ready to check out?
    #
    pass



if __name__ == "__main__":
    main()

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
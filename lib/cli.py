# lib/cli.py

from models.shopper import Shopper
from models.book import Book


def main():
    print(Shopper.get_all())
    print(Book.get_all())

def menu():
    print("Welcome to the store!")
    print("0. Exit the program")
    print("1. Enter Store")

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

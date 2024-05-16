# lib/cli.py

from helpers.account import account
from helpers.shopping import shopping


def main():
    user = account()
    shopping(user)




if __name__ == "__main__":
    main()




"""
DIFFERENCES ON LAPTOP:
1) delete account feature for shopper
   -Allows user to delete themselves from the system
2) Menu updated to change language to less money centric and ordered better
3) Added slight styling using blanks and *******
4) Made leaving program easier
5) Readme
"""
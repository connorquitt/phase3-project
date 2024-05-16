# lib/cli.py

from helpers.account import account
from helpers.shopping import shopping


def main():
    user = account()
    shopping(user)




if __name__ == "__main__":
    main()


##define manager mode (idk what that means but maybe set it up for them to see everything thats ever been available to use get_all)
##test the create property testers DONE
##Change order and make it where going back is uniform across everything so its not so weird

##It appears you have user_id as a foreign key but there is no class called user
##They need to match
##Also if your orm methods are up to date I suggest you cancel and meet with me first.
##But it may be different now since I can't see so much of your code
##If it is all corrected and pushed and you want to do it tomorrow I need to see your repo asap
##As it stands now only seeing the models I suggest we go through it together before your assessment
##I will look when you push it.  But if I don't see it by 3 I will go ahead and cancel your slot for tomorrow
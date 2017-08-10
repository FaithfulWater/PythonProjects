import turtle
import math

class User:
    # Define the fields and methods for your object here.
    def __init__(self, name, friends, password):
        self.user_name = name
        self.friends = []
        self.setpassword = password

    def set_user_name(self,name):
        input()
        self.user_name == input()

    def add_friend(self,friend):             #setter
        self.friends.append(friend)

    def change_user_name(self,name):         #setter
        self.user_name == name

    def change_password(self, password):     #setter
        self.setpassword == password

    def get_user_name(self):                 #getter
        return self.user_name

    def get_password(self):                  #getter
        return self.setpassword

    def get_friend(self):
        user1.addConnectionUser(user2)
        user2.addConnectionUser(user1)

class Network:
    # Define the fields and methods for your object here.
    def __init__(self,name):
        self.name = name
        self.users = []

    def add_user(self,users):             #setter
        user = input("Start as your user")
        x = 0
        for i in self.users:
            if user != self.users[i]:
                x += 1
            else:
                continue

        if x == len(self.users):
            self.users.append(users)
            print("Welcome")


    def add_connection(self,user1,user2):   #setter
        z == False
        for i in user1.friends:
            if user2 == user1.friends[i]:
                z == True
                print ("Yay! You're already friends!")

            else:
                continue
            if z == False:
                user1.addConnectionUser(user2)
                user2.addConnectionUser(user1)
                print ("Yay! You've become friends")


    def total_number_of_users(self):         #getter
        return len(self.users)

    def get_users(self):                    #getter
        return self.users



def main():
    # Define the program flow for your user interface here.
    #Matrix = Network()
    #Matrix.add_user
    #Matrix.add_connection
    Account = User()
    Account.set_user_name(name)
    Account.add_friend(friend)
    Account.setpassword(password)
    Account.change_user_name(name)
    while 10>9:
        act = input("what you want doooo?")
        if act == "Add account" :
            Account.set_user_name(name)

# Runs your program.

if __name__ == '__main__':
    main()

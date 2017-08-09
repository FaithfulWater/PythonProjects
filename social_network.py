class User:
    # Define the fields and methods for your object here.
    def __init__(self, name):
        self.user_name = name
        self.friends = []
        self.setpassword = password

    def add_friend(self,friend):             #setter
        self.friends.append(friend)

    def change_user_name(self,name):         #setter
        self.user_name = name

    def change_password(self, password):     #setter
        self.setpassword = password

    def get_user_name(self):                  #getter
        return self.user_name

    def get_password(self):                   #getter
        return self.setpassword


class Network:
    # Define the fields and methods for your object here.
    def __init__(self,name):
        self.users = []

    def add_users

def main():
    # Define the program flow for your user interface here.
    = User(,user_name)
    .add_friend()

# Runs your program.
if __name__ == '__main__':
    main():

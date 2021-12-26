import db
import encrypt
from sys import exit


def connect_to_db():
    pass


def get_account():
    pass


def add_account():
    pass


def copy_to_clipboard():
    pass


def login(password):
    if password == "":
        return True

def main():
    print("Welcome to the password manager please input the password to continue.")
    password = input()

    if not login(password):
        exit()

    selection = ""
    print("You're in!")
    print("Select your option")
    while selection.upper() != 'Q':
        pass


if __name__ == '__main__':
    main()

from db import DataBase
import encrypt
from sys import exit
import pyperclip
from simple_term_menu import TerminalMenu


def get_account():
    pass


def add_account():
    pass


def copy_to_clipboard(password):
    pyperclip.copy(password)


def login(password, data_base):
    if password == "":
        return True
    return False


def main():
    print("Welcome to the password manager please input the password to continue.")
    data_base = DataBase()

    password = input()

    if not login(password, data_base):
        exit()

    print("You're in!")

    options = ["Add account", "Get password", "Quit"]
    menu_entry_index = 0
    terminal_menu = TerminalMenu(options)

    while options[menu_entry_index] != "Quit":
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == "Get password":
            print("Getting password")


if __name__ == '__main__':
    main()

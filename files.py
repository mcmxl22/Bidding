"""
files Version 1.8
Python 3.7
"""

from os import path, remove


def create_files():
    """Create a file and/or confirm it."""
    file_name = input("Enter file name. ")

    if path.exists(file_name):
        print(f"{file_name} already exists!")

    else:
        with open(file_name, "w+"):
            if path.exists(file_name):
                print(f"{file_name} created!")


def delete_file():
    """Delete files."""
    file_name = input("Enter file to be deleted. ")
    confirm_file = input(f"Delete {file_name}? ")

    if confirm_file == "y":
        remove(file_name)
        print(f"{file_name} deleted!")


def file_options():
    """Choose what to do with a file."""
    while True:
        file_options = ["1 Create file", "2 Delete file", "3 Exit"]
        for i in file_options:
            print(i)
        file_choice = input("Choose an option. ")

        if file_choice in "1":
            create_files()

        elif file_choice in "2":
            delete_file()

        elif file_choice in "3":
            break


if __name__ == "__main__":
    file_options()

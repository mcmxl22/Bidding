#!/bin/python3
"""files Version 1.6
   Python 3.7.2"""

import os.path


def create_files(file_name):
    """Create a file and/or confirm it."""
    file_name = input('Enter file name. ')
    if os.path.exists(file_name):
        print(f'{file_name} already exists!')
    else:
        with open(file_name, 'w+'):
            if os.path.exists(file_name):
                print(f'{file_name} created!')


def delete_file(file_name):
    """Delete files."""
    file_name = input('Enter file to be deleted. ')
    confirm_file = input(f'Are you sure you want to delete {file_name}? ')
    if confirm_file is 'y':
        os.remove(file_name)
        print(f'{file_name} deleted!')


def file_options(file_name):
    """Choose what to do with a file."""
    while True:
        file_options = ['Create file', 'Delete file', 'Exit']
        for index, file in enumerate(file_options, start=1):
            print(index, file)
        file_choice = input('Choose an option. ')
        if file_choice in '1':
            create_files(file_name)
        elif file_choice in '2':
            delete_file(file_name)
        elif file_choice in '3':
            raise SystemExit


if __name__ == "__main__":
    file_options('file_name')

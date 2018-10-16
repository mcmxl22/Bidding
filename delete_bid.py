#!/usr/bin/env python3
'''By Micah M. 2018
   delete_bid version 1.2
   Python 3.7'''


import os
import sys
import subprocess


def delete():
    '''Delete a bid file.'''
    while True:
        file_name = input('Enter file to be deleted or press b to go back.\n> ')
        if file_name == 'b':
            Bid = [sys.executable, 'Bid.py']
            subprocess.call(Bid)
    
        if os.path.exists(file_name) is False:
            print(f'File {file_name} doesn\'t exist!')
    
        confirm = input(f'Are you sure you want to delete {file_name}?\n> ')
  
        if confirm == 'y':
            os.remove(file_name) 
            print('Done!')
    

if __name__ == "__main__":
    delete()

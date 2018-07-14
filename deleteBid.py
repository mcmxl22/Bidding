#! /usr/bin/env python
# By Micah M. 2018
# deleteBid version 1.02.02
# Python 3.7


import os
import sys
import subprocess


def delete():

    fileName = input('Enter file to be deleted or press b to go back.\n> ')
    if fileName == 'b':
        Bid = [sys.executable, 'Bid.py']
        subprocess.call(Bid)
    
    if os.path.exists(fileName) is False: # Check if database file exists.
        print(f'File {fileName} doesn\'t exist!')
        delete() 
    
    confirm = input(f'Are you sure you want to delete {fileName}?\n> ') # Confirm file to be deleted.
  
    if confirm == 'y':
        os.remove(fileName) 
        print('Done!')
        delete()
    else:
        delete()
    

if __name__ == "__main__":
    delete()


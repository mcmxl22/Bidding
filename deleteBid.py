#! /usr/bin/env python
# By Micah M. 2018
# deleteBid version 1.02.01
# Python 3.6.5


import os
import sys
import subprocess


def delete():

    fileName = input('Enter file to be deleted or press b to go back.\n> ')
    if fileName == 'b':
        Bid = [sys.executable, 'Bid.py']
        subprocess.call(Bid)
    
    if os.path.exists(fileName) is False: # Check if database file exists.
        print('File %s doesn\'t exist!' % fileName)
        delete() 
    
    confirm = input('Are you sure you want to delete %s?\n> ' % fileName) # Confirm file to be deleted.
  
    if confirm == 'y':
        os.remove(fileName) 
        print('Done!')
        delete()
    else:
        delete()
    

if __name__ == "__main__":
    delete()


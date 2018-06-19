#! /usr/bin/env python
# By Micah M. 2018
# deleteBid version 1.02.01
# Python 3.6.5


import os


def delete():

    fileName = input('Enter file to be deleted.\n> ')
    if os.path.exists(fileName) is False:
        print('File doesn\'t exist!')
        delete() 
    
    confirm = input('Are you sure you want to delete %s?\n> ' % fileName)
  
    if confirm == 'y':
        os.remove(fileName)
        delete()
    else:
        delete()
    

if __name__ == "__main__":
    delete()


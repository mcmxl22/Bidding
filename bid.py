#!/usr/bin/env python
'''By Micah M. 2018
   bid version 1.3
   Python 3.7'''


import subprocess
import sys


def bid():
    '''bid'''
    create_bid = [sys.executable, 'createbid.py']
    view_bid = [sys.executable, 'seebid.py']
    bid_options = ['1 create bid', '2 View bid', '3 Exit']

    print('\n'.join(bid_options))
    bid_choice = input('What do you want to do? ')

    if bid_choice in '1':
        subprocess.run(create_bid)

    elif bid_choice in '2':
        subprocess.run(view_bid)

    elif bid_choice in '3':
        raise SystemExit

    else:
        print('Invalid Answer!')
        bid()


if __name__ == "__main__":
    bid()

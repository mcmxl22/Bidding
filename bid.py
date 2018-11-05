#!/usr/bin/env python
'''By Micah M. 2018
   bid version 1.4
   Python 3.7.1'''


from create_bid import create_bid
from view_bid import view_bid


def bid(bid_options):
    '''bid'''
    while True:
        bid_options = ['1 Create bid', '2 View bid', '3 Exit']
        print('\n'.join(bid_options))
        bid_choice = input('What do you want to do? ')

        if bid_choice in '1':
            create_bid()

        elif bid_choice in '2':
            view_bid()

        elif bid_choice in '3':
            raise SystemExit

        else:
            print('Invalid Answer!')


if __name__ == "__main__":
    bid('bid_options')

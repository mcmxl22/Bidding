#!/usr/bin/env python
"""By Micah M. 2018
   Interface version 1.2
   Python 3.7.1"""

import sqlite3
from create_bid import create_bid


def interface(confirm):
    """Create interface allowing team members to bid on work."""
    while True:
        get_name = input('Enter your name. ')
        conn = sqlite3.connect('Bid.db')
        cursor = conn.cursor()
        sql = 'SELECT * FROM Bid WHERE Name=?'
        results = cursor.execute(sql, [get_name])
        bid_list = results.fetchall()
        options = ('1 Yes', '2 No', '3 Exit')
        print('\n'.join(options))
        confirm = input(f'Is this correct? {bid_list} ')
        cursor.close()

        if confirm in '1':
            create_bid()

        elif confirm in '2':
            interface(confirm)

        elif confirm in '3':
            raise SystemExit

        else:
            print('Invalid Entry!')


if __name__ == "__main__":
    interface('confirm')

#!/usr/bin/env python
'''By Micah M. 2018
   Interface version 1.1
   Python 3.7
   Requires create_bid.py'''


import sqlite3
import subprocess
import sys

def interface():
    '''Create interface allowing team members to bid on work.'''
    while True:
        get_name = input('Enter your name. ')
        conn = sqlite3.connect('Bid.db')
        cursor = conn.cursor()
        sql = 'SELECT * FROM Bid WHERE Name=?'
        results = cursor.execute(sql, [get_name])
        bid_list = results.fetchall()
        options = ('1 Yes', '2 No', '3 Exit')
        print('\n'.join(options))
        confirm = input(f'Is this correct? {bid_list}\n')
        cursor.close()

        if confirm == '1':
            bid_choice = [sys.executable, 'create_bid.py']
            subprocess.run(bid_choice)

        elif confirm == '2':
            interface()

        elif confirm == '3':
            raise SystemExit

        else:
            print('Invalid Entry!')

if __name__ == "__main__":
    interface()

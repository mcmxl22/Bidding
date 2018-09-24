#!/usr/bin/env python3
'''By Micah M. 2018
   bid_interface version 1
   Python 3.7
   requires createBid.py'''

import sqlite3
import subprocess
import sys

def interface():
    '''Create interface allowing team members to bid on work.'''
    # Enter name
    name = input('Enter your name. ')

    # confirm name and current bid
    conn = sqlite3.connect('Bid.db')
    cursor = conn.cursor()
    sql = 'SELECT * FROM Bid WHERE Name=?'
    results = cursor.execute(sql, [name])
    bid_list = results.fetchall()
    options = ('1 Yes', '2 No')
    print('\n'.join(options))
    confirm = input(f'Is this you? {bid_list}\n')
    cursor.close()

    # Enter desired bid line
    if confirm == '1':
        bid_choice = [sys.executable, 'createBid.py']
        subprocess.call(bid_choice)
        
    elif confirm == '2':
        interface()
    else:
        print('Invalid Entry')

if __name__ == "__main__":
    interface()

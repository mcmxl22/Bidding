#!/usr/bin/env python3
'''By Micah M. 2018
   createBid version 1.3
   Python 3.7'''

import sqlite3

def create_bid():
    '''create_bid'''
    conn = sqlite3.connect('Bid.db')
    cursor = conn.cursor()

    while True:
        Name = input('Team Member\'s name: ')
        Seniority = input('Team Member\'s seniority: ')
        bid_line = input('Team Member\'s bid: ')
        sql = '''insert into Bid
                 (Name, Seniority, bid_line)
                  values
                 (:tm_Name, :tm_Seniority, :tm_bid_line)'''
        cursor.execute(sql,
                      {'tm_Name': Name,
                       'tm_Seniority': Seniority,
                       'tm_BidLine': bid_line})
        conn.commit()
        cont = input('Add another team member? ')
        if cont[0].lower() == 'n':
            cursor.close()
            raise SystemExit


if __name__ == "__main__":
    create_bid()

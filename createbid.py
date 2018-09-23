#! /usr/bin/env python3
'''By Micah M. 2018
   createBid version 1.2
   Python 3.7'''


import sqlite3


class bid():

    def create_bid(self):

        conn = sqlite3.connect('Bid.db')
        cursor = conn.cursor()

        while True:
            Name = input('Team Member\'s name: ')
            Seniority = input('Team Member\'s seniority: ')
            BidLine = input('Team Member\'s bid: ')
            sql = '''insert into Bid
                     (Name, Seniority, bid_line)
                      values
                     (:em_Name, :em_Seniority, :em_bid_line)'''
            cursor.execute(sql,
                           {'em_Name': Name,
                            'em_Seniority': Seniority,
                            'em_BidLine': bid_line})
            conn.commit()
            cont = input('Add another team member? ')
            if cont[0].lower() == 'n':
                cursor.close()
                raise SystemExit


if __name__ == "__main__":
    bid = bid()
    bid.create_bid()

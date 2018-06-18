#! /usr/bin/env python
# By Micah M. 2018
# createBid version 1.01.02
# Python 3.6.5


import sqlite3



class bid():

    def createbid(self):

        conn = sqlite3.connect('bid.db')
        cursor = conn.cursor()

        while True:
            Name = input('Employee\'s name: ')
            Seniority = input('Employee\'s seniority: ')
            BidLine = input('Employee\'s bid: ')
            sql = '''insert into bid
                       (Name, Seniority, BidLine)
                       values
                       (:em_Name, :em_Seniority, :em_BidLine)''' 
            cursor.execute(sql,
                           {'em_Name': Name,
                            'em_Seniority': Seniority,
                            'em_BidLine': BidLine})
            conn.commit()
            cont = input('Add Another Employee? ')
            if cont[0].lower() == 'n':
                break
        cursor.close()

if __name__ == "__main__":
    bid = bid()
    bid.createbid()


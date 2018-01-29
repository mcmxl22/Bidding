#! /usr/bin/env python
# By Micah M. 2018
# createBid version 1.01
# Python 3.6.4


import sqlite3


conn = sqlite3.connect('Bid.db')
cursor = conn.cursor()
who = {1: 'Micah C McConnaughey', 2: 'name2', 3: 'name3'}


def bid():

    ask = input('Name? ')

    if ask == who[1]:
        results = cursor.execute("SELECT * FROM Bid WHERE names = (%s, %s, %s)"
                                 ('Micah C McConnaughey', 'name2', 'name3'))
        names = results.fetchall()
        print (names)
		
if __name__ == "__main__":
    bid()



class bid(object):

    def createbid(self):

        conn = sqlite3.connect('Bid.db')
        cursor = conn.cursor()

        while True:
            Name = input('Employee\'s name: ')
            Seniority = input('Employee\'s seniority: ')
            BidLine = input('Employee\'s bid: ')
            sql = '''insert into Bid
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

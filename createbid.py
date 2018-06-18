#! /usr/bin/env python
# By Micah M. 2018
# createBid version 1.02.02
# Python 3.6.5


import sqlite3



class bid():

    def createBid(self):

        while True:

            fileName = input('Enter file name.\n> ')
            conn = sqlite3.connect(fileName + '.db')
            cursor = conn.cursor()            
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
            cont = input('Add Another Employee?\n> ')
            if cont[0].lower() == 'n':
                cursor.close()
                raise SystemExit
        cursor.close()


    def createTable(self):

        creatFile = input('Do you want to create a new bid file?\n> ')

        if creatFile == 'y':

            fileName = input('What should the filename be?\n> ')
            conn = sqlite3.connect(fileName + '.db')
            cursor = conn.cursor()        
            print('Creating table.')
            sql = '''create table bid (
                Name text,
                Seniority int,
                Bidline int)'''
            cursor.execute(sql)
            print('Done!')
            bid.createBid()

        else:
            raise SystemExit

if __name__ == "__main__":
    bid = bid()
    bid.createTable()


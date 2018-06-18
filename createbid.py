#! /usr/bin/env python
# By Micah M. 2018
# createBid version 1.02.03
# createBid version 1.02.02
# Python 3.6.5


import sqlite3
import sys
import subprocess


class bid():

    def createBid(self):

        fileName = input('Enter file name.\n> ')
        conn = sqlite3.connect(fileName + '.db')
        cursor = conn.cursor()            
        Name = input('Team member\'s name: ')
        Seniority = input('Team member\'s seniority: ')
        BidLine = input('Team member\'s bid: ')
        sql = '''insert into bid
            (Name, Seniority, BidLine)
            values
            (:tm_Name, :tm_Seniority, :tm_BidLine)''' 
        cursor.execute(sql,
            {'tm_Name': Name,
             'tm_Seniority': Seniority,
             'tm_BidLine': BidLine})
        conn.commit()
        cont = input('Add another team member?\n> ')
        if cont[0].lower() == 'n':
            cursor.close()
            Bid = [sys.executable, 'Bid.py']
            subprocess.call(Bid)
        cursor.close()


<<<<<<< HEAD
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

=======
class bid():

    def createBid(self):

        while True:

            fileName = input('Enter file name.\n> ')
            conn = sqlite3.connect(fileName + '.db')
            cursor = conn.cursor()            
            Name = input('Team member\'s name: ')
            Seniority = input('Team member\'s seniority: ')
            BidLine = input('Team member\'s bid: ')
            sql = '''insert into bid
                       (Name, Seniority, BidLine)
                       values
                       (:tm_Name, :tm_Seniority, :tm_BidLine)''' 
            cursor.execute(sql,
                           {'tm_Name': Name,
                            'tm_Seniority': Seniority,
                            'tm_BidLine': BidLine})
            conn.commit()
            cont = input('Add another team member?\n> ')
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

>>>>>>> 70ed9465e3d0b2fb8e0991664635cffe44ed31ff
        else:
            raise SystemExit

if __name__ == "__main__":
    bid = bid()
    bid.createTable()

<<<<<<< HEAD
=======

>>>>>>> 70ed9465e3d0b2fb8e0991664635cffe44ed31ff

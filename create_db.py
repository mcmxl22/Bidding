#! /usr/bin/env python
# By Micah M. 2018
# create_db version 1.01
# Python 3.6.4


import sqlite3


class dataBase(object):

    def create(self):
        conn = sqlite3.connect('bid.db') 
        cursor = conn.cursor()
        sql = '''create table bid (
            Name text,
            Seniority int,
            Bidline int)'''
        cursor.execute(sql)
        cursor.close()

if __name__ == "__main__":
    bid = dataBase()
    bid.create()

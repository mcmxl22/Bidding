#! /usr/bin/env python
# By Micah M. 2018
# seeBid version 1.01
# Python 3.6.4


import sqlite3


def seeBid():
    conn = sqlite3.connect('Bid.db')
    cursor = conn.cursor()
    sql = '''select * from bid'''
    results = cursor.execute(sql)
    all_employees = results.fetchall()

    for employee in all_employees:
        print employee

if __name__ == "__main__":
    seeBid()

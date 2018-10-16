#!/usr/bin/env python3
'''By Micah M. 2018
   see_bid version 1.2
   Python 3.7'''


import sqlite3


def see_bid():
    '''view bid results'''
    conn = sqlite3.connect('Bid.db')
    cursor = conn.cursor()
    sql = '''select * from bid'''
    results = cursor.execute(sql)
    team_members = results.fetchall()
    for team in team_members:
        print(team)

if __name__ == "__main__":
    see_bid()

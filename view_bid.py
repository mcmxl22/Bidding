#!/bin/python3
"""
view_bid version 1.4
Python 3.7
"""


import sqlite3


def view_bid():
    """View a bid."""
    conn = sqlite3.connect("Bid.db")
    cursor = conn.cursor()
    sql = """select * from bid"""
    results = cursor.execute(sql)
    all_team_members = results.fetchall()
    for members in all_team_members:
        print(members)


if __name__ == "__main__":
    view_bid()

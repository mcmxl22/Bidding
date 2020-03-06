#!/bin/python3
"""
create_bid version 1.5
Python 3.7
"""


import sqlite3


def create_bid():
    """create_bid"""
    conn = sqlite3.connect("Bid.db")
    cursor = conn.cursor()

    while True:
        name = input("Name: ")
        seniority = input("Seniority: ")
        bid_line = input("Desired bid: ")
        sql = """insert into Bid
                 (Name, Seniority, Bidline)
                  values
                 (:tm_Name, :tm_Seniority, :tm_Bidline)"""
        cursor.execute(
            sql, {"tm_Name": name, "tm_Seniority": seniority, "tm_Bidline": bid_line}
        )
        conn.commit()
        add_member = input("Add another team member? ")
        if add_member[0].lower() in "n":
            cursor.close()
            exit(0)


if __name__ == "__main__":
    create_bid()

#!/bin/python3
"""
bid version 1.5
Python 3.7
"""


from create_bid import create_bid
from view_bid import view_bid
from numli import addnum


def bid(bid_options):
    """bid"""
    while True:
        bid_options = ["Create bid", "View bid", "Exit"]
        addnum(bid_options)
        bid_choice = input("What do you want to do? ")

        if bid_choice in "1":
            create_bid()

        elif bid_choice in "2":
            view_bid()

        elif bid_choice in "3":
            exit(0)

        else:
            print("Invalid Answer!")


if __name__ == "__main__":
    bid("bid_options")

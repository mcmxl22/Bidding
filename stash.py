#! /usr/bin/env python
# By Micah M. 2018
# stash
# Python 3.6.5


import os.path
import sqlite3
import sys
import subprocess


class teamInfo(object):

    def __init__(self):
        answer = ('y', 'n')
        createChoices = ('1 Create team list', '2 Exit\n')
        print(' \n'.join(createChoices))
        select = input('Select an option.\n> ')

        # Create team list.
        if select == '1':
            print(' \n'.join(answer))
            addMembers = input('Add a team member?\n> ')
            if addMembers.lower() == 'n':
                teamInfo()

            elif addMembers.lower() == 'y':
                #name = input('Enter name and seniority number. ')
                conn = sqlite3.connect('Bid.db')
                cursor = conn.cursor()

                while True:
                    Name = input('Team member\'s name: ')
                    Seniority = input('Team member\'s seniority: ')
                    bidLine = input('Team member\'s bid: ')
                    sql = '''insert into bid
                        (Name, Seniority, BidLine)
                        values
                        (:tm_Name, :tm_Seniority, :tm_bidLine)'''
                    cursor.execute(sql,
                        {'tm_Name': Name,
                        'tm_Seniority': Seniority,
                        'tm_BidLine': BidLine})
                    conn.commit()
                    cont = input('Add Another Employee?\n> ')
                    if cont[0].lower() == 'n':
                        break
                cursor.close()
            teamInfo()
				
        elif select == '2':
            raise SystemExit()

        else:
            print('Invalid entry!')
            teamInfo()


# Create a list of all existing bid lines.
class bidLineList(object):

    def __init__(self):
        addLine = input('Add a bid line? ')
        answer = ('y', 'n')
        print(' \n'.join(answer))

        if addLine.lower() == 'y':
            conn = sqlite3.connect('bid.db') 
            cursor = conn.cursor()
            sql = '''create table bid (
                Name text,
                Seniority int,
                Bidline int)'''
            cursor.execute(sql)
            cursor.close()

        elif addLine.lower() == 'n':
            print('Under development.')
            bidLineList()

        else:
            print('Invalid entry!')
            bidLineList()
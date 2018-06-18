#! /usr/bin/env python
# By Micah M. 2018
# Bid Version 1.01.05
# Python 3.6.5


import os.path
import csv
import sqlite3
import sys
import subprocess


#Create file(s).
def Files():

    filename = input('Enter file name.\n> ')
    close = f.close()
    if os.path.exists(filename):
        f = open(filename, 'a')
        close
    elif not os.path.exists(filename):
        print('{} {}{}'.format('Creating', filename, '.txt'))
        f = open(filename, 'w+')
        close
        print('Done!')


# Create lists of all bid lines, and all team members with their
# seniority numbers and current bid line numbers.
class teamInfo(object):

    def __init__(self):
        answer = ('y', 'n')
        createChoices = ('1 Create team list', '2 Exit\n')
        print(' \n'.join(createChoices))
        select = input('Select an option.\n> ')

        # Create team list
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
                    Name = input('Employee\'s name: ')
                    Seniority = input('Employee\'s seniority: ')
                    bidLine = input('Employee\'s bid: ')
                    sql = '''insert into Bid
                        (Name, Seniority, BidLine)
                        values
                        (:em_Name, :em_Seniority, :em_bidLine)'''
                    cursor.execute(sql,
                        {'em_Name': Name,
                        'em_Seniority': Seniority,
                        'em_BidLine': BidLine})
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



class Choices(object):

    def activityChoices(self):
        choice = Choices()
        entry = ('\nInvalid entry!\n')
        answer = ('y', 'n')
        actions = ('1 New Bid', '2 View available bid lines',
                   '3 View current bid assignments', '4 Edit bid lines',
                   '5 Edit team members', '6 Create Lists', '7 Delete bid' '8 Exit\n')
        print(' \n'.join(actions))

        select = input('Select an option.\n> ')

        if select == '1':
            createBid = [sys.executable, 'createbid.py']
            subprocess.call(createBid)

        # View available bid lines.
        elif select == '2':
            fileName = input('Enter file name.\n> ')
            with open(fileName, 'r') as fin:
                for i in fin.readlines():
                    print(i)
            choice.activityChoices()

        # View current bid assignments.
        elif select == '3':
            fileName = input('Enter file name.\n> ')
            with open(fileName, 'r') as fin:
                for i in fin.readlines():
                    print(i)
            choice.activityChoices()

        # Edit bid lines.
        elif select == '4':

            editActions = ('1 Change existing bidlines',
                            '2 Add new bid lines',
                            '3 Delete bid lines', '4 Back')

            print(' \n'.join(editActions))
            select = input('Select an option.\n> ')

            if select == '1':
                print('Under development')

            elif select == '2':
                print('Under development')
                choice.activityChoices()

            elif select == '3':
                print('Under development')
                choice.activityChoices()

            if select == '4':
                choice.activityChoices()

        # Edit team members.
        elif select == '5':
            editChoices = ('1 Change existing team members',
                           '2 Add new team members',
                           '3 Remove team members', '4 Back')

            print(' \n'.join(editChoices))
            select = input('Select an option.\n> ')

            if select == '1':
                print('Under development')
                choice.activityChoices()

            elif select == '2':
                print('Under development')
                choice.activityChoices()

            elif select == '3':
                print('Under development')
                choice.activityChoices()

            elif select == '4':
                choice.activityChoices()

            else:
                print(entry)
                choice.activityChoices()

        elif select == '6':
            print('\nunder development\n')
            choice.activityChoices()

        elif select == '7':
            deleteBid = [sys.executable, 'deleteBid.py']
            subprocess.call(deleteBid)            

        elif select == '8':
            raise SystemExit

        else:
            print(entry)
            choice.activityChoices()


if __name__ == "__main__":
    choices = Choices()
    choices.activityChoices()

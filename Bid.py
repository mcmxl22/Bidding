#! /usr/bin/env python
# By Micah M. 2018
# Bid Version 1.01.01
# Python 3.6.4


import os.path
import csv
import sqlite3
import sys
import subprocess


# Create file(s).
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
        Ask = ('y', 'n')
        createChoices = ('1 Create team list', '2 Exit\n')
        print(' \n'.join(createChoices))
        select = input('Select an option.\n> ')

        # Create team list
        if select == '1':
            print(' \n'.join(Ask))
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
        entry = ('Invalid entry!')
        answer = ('y', 'n')
        actions = ('1 New Bid', '2 View available bid lines',
                   '3 View current bid assignments', '4 Edit bid lines',
                   '5 Edit team members', '6 Create Lists', '7 Exit\n')
        print(' \n'.join(actions))

        select = input('Select an option.\n> ')

        if select == '1':
            print(' \n'.join(answer))

            ask = input('\nDo you want to start a new bid? ')

            if ask == 'y':
                bidLine = input('Enter your name. ')

                if bidLine in open('BidLines.csv').read():
                    print('Available bid lines.\n')
                    with open('BidLines.csv', 'r') as fin:
                        for i in fin.readlines():
                            print(i)
                            fin.close()

            else:
                choice.activityChoices()

        # View available bid lines.
        elif select == '2':
            bidLines = input('Enter file name.\n> ')
            with open(bidLines, 'r') as fin:
                for i in fin.readlines():
                    print(i)
            choice.activityChoices()

        # View current bid assignments.
        elif select == '3':
            viewAssignment = input('Enter file name.\n> ')
            with open(viewAssignment, 'r') as fin:
                for i in fin.readlines():
                    print(i)
            choice.activityChoices()

        # Edit bid lines.
        elif select == '4':

            editActions = ('1 Change existing bidlines',
                            '2 Add new bid lines',
                            '3 Delete bid lines', '4 Back')

            print(' \n'.join(editActions))
            chooseOption = input('Choose an option.\n> ')

            if chooseOption == '1':
                Files()
                # edit = input()
                print('Done!')

            elif chooseOption == '2':
                Files()
                # edit = input()
                print('Done!')
                choice.activityChoices()

            elif chooseOption == '3':
                Files()
                # edit = input()
                print('Done!')
                choice.activityChoices()

            if chooseOption == '4':
                choice.activityChoices()

        # Edit team members.
        elif select == '5':
            editChoices = ('1 Change existing team members',
                           '2 Add new team members',
                           '3 Remove team members', '4 Back')

            print(' \n'.join(editChoices))
            chooseOption = input('Choose an option.\n> ')

            if chooseOption == '1':
                Files()
                # edit = input()
                print('Done!')
                choice.activityChoices()

            elif chooseOption == '2':
                Files()
                # edit = input()
                print('Done!')
                choice.activityChoices()

            elif chooseOption == '3':
                Files()
                # edit = input()
                print('Done!')
                choice.activityChoices()

            elif chooseOption == '4':
                    choice.activityChoices()

            else:
                print(Entry)
                #print(editActions)
                choice.activityChoices()

        elif select == '6':
            print('\nunder development\n')
            choice.activityChoices()

        elif newAsk == '7':
            raise SystemExit()

        else:
            print(entry)
            choice.activityChoices()


class main(object):

    def __init__(self):
        choices = Choices()
        choices.activityChoices()


if __name__ == "__main__":
    main()

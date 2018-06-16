#! /usr/bin/env python
# By Micah M. 2018
# Bid Version 1.01
# Python 3.6.4


import os.path
import csv
import sqlite3
import sys
import subprocess

# Create file(s).
def Files():

    filename = input('Enter file name. ')
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
        createList = ' \n'.join(createChoices)
        print(createList)
        createAsk = input('What do you want to do? ')

        # Create team list
        if createAsk == '1':
            askChoice = ' \n'.join(Ask)
            print(askChoice)
            addMembers = input('Add a team member? ')
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
                    cont = input('Add Another Employee? ')
                    if cont[0].lower() == 'n':
                        break
                cursor.close()
            teamInfo()
				
        elif createAsk == '2':
            quit()

        else:
            print('Invalid entry!')
            teamInfo()


class bidLineList(object):
    # Create a list of all existing bid lines.
    def __init__(self):
        addLine = input('Add a bid line? ')
        Ask = ('y', 'n')
        askChoice = ' \n'.join(Ask)
        print(askChoice)

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

    def __init__(self):
        pass

    def activityChoices(self):
        choice = Choices()
        #data = Data()
        entry = ('Invalid entry!')
        ask = ('y', 'n')
        actions = ('1 New Bid', '2 View available bid lines',
                   '3 View current bid assignments', '4 Edit bid lines',
                   '5 Edit team members', '6 Create Lists', '7 Exit\n')
        actionsList = ' \n'.join(actions)
        print(actionsList)

        newAsk = input('Select an option.\n> ')

        if newAsk == '1':

            askChoice = ' \n'.join(ask)
            print(askChoice)

            ask = input('\nDo you want to start a new bid? ')

            if ask.lower() == 'y':
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
        elif newAsk == '2':
            bidLines = input('Enter file name.\n> ')
            with open(bidLines, 'r') as fin:
                for i in fin.readlines():
                    print(i)
            choice.activityChoices()

        # View current bid assignments.
        elif newAsk == '3':
            assignment = input('Enter file name.\n> ')
            with open(assignment, 'r') as fin:
                for i in fin.readlines():
                    print(i)
            choice.activityChoices()

        # Edit bid lines.
        elif newAsk == '4':

            editActions = ('1 Change existing bidlines',
                            '2 Add new bid lines',
                            '3 Delete bid lines', '4 Back')

            print(editActions)
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
        elif newAsk == '5':
            editChoices = ('1 Change existing team members',
                           '2 Add new team members',
                           '3 Remove team members', '4 Back')

            actionsList = ' \n'.join(editChoices)
            print(actionsList)
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

        elif newAsk == '6':
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

#! /usr/bin/env python
# By Micah M. 2018
# Bid Version 1.01
# Python 3.6.4


import os.path
import csv


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
class Data(object):

    def __init__(self, createChoices, createList):
        self.createChoices = createChoices
        self.createList = createList

    def createLists(self):

        choices = Choices()
        data = Data()
        invalidEntry = ('Invalid entry!')
        Ask = ('y', 'n')
        createChoices = ('1 Create team list', '2 Create bid line list',
                         '3 Back\n')

        createList = ' \n'.join(createChoices)
        print(createlist)

        createAsk = input('What do you want to do? ')

        # Create team list
        if createAsk == '1':
            Files()

            askChoice = ' \n'.join(Ask)
            print(askChoice)

            Add = input('Add a team member? ')
            if Add.lower() == 'n':
                data.Create_Lists()

            elif Add.lower() == 'y':
                name = input('Enter name and seniority number. ')
                print('Under development')
                data.Create_Lists()

            else:
                print(invalidEntry)
                data.Create_Lists()

        # Create a list of all existing bid lines.
        elif Create_Ask == '2':
            Files()

            print(askChoice)

            Add = input('Add a bid line? ')

            if Add.lower() == 'n':
                data.Create_Lists()

            elif Add.lower() == 'y':
                print('Under development.\n')
                data.Create_Lists()

            else:
                print(Entry)
                data.Create_Lists()

        elif Create_Ask == '3':
            choice.Activity_Choices()

        else:
            print(Entry)
            data.Create_Lists()


class Choices(object):

    def activityChoices(self):
        choice = Choices()
        data = Data()
        Entry = ('Invalid entry!')
        Ask = ('y', 'n')
        Actions = ('1 New Bid', '2 View available bid lines',
                   '3 View current bid assignments', '4 Edit bid lines',
                   '5 Edit team members', '6 Create Lists', '7 Exit\n')
        actionsList = ' \n'.join(Actions)
        print(actionsList)

        newAsk = input('Choose an option. ')

        if newAsk == '1':

            askChoice = ' \n'.join(Ask)
            print(askChoice)

            Ask = input('\nDo you want to start a new bid? ')

            if Ask.lower() == 'y':
                bidLine = input('Enter your name. ')

                if bidLine in open('BidLines.csv').read():
                    print('Available bid lines.\n')
                    with open('BidLines.csv', 'r') as fin:
                        for i in fin.readlines():
                            print(i)
                            fin.close()

            else:
                activityChoices()

        # View available bid lines.
        elif newAsk == '2':
            bidLines = input('Enter file name. ')
            with open(bidLines, 'r') as fin:
                for i in fin.readlines():
                    print(i)
            choice.activityChoices()

        # View current bid assignments.
        elif newAsk == '3':
            assignment = input('Enter file name. ')
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
            chooseOption = input('Choose an option. ')

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

            else:
                print(invalidEntry)
                print(editActions)

        # Edit team members.
        elif chooseOption == '5':
            editChoices = ('1 Change existing team members',
                            '2 Add new team members',
                            '3 Remove team members', '4 Back')

            print(editChoices)

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
                print(editActions)
                choice.activityChoices()

        elif editAsk == '6':
            data.Create_Lists()

        elif editAsk == '7':
            quit()

        else:
            print(Entry)
            choice.activityChoices()


class main(object):

    def __init__(self):
        choices = Choices()
        choices.activityChoices()


if __name__ == "__main__":
    main()

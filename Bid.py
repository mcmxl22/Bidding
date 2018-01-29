#! /usr/bin/env python
# By Micah M. 2017
# Bid Version 1.01
# Python 3.6.4

import os.path
import csv

# Create file(s).
def Files():
    filename = input('Enter file name.\n> ')
    close = f.close()
	
    if os.path.exists(filename):
        f = open(filename, 'a')
        close

    elif not os.path.exists(filename):
        print ('{} {}{}'.format('Creating', filename, '.txt\n'))
        f = open(filename, 'w+')
        close
        print ('Done!\n')

# Create lists of all bid lines, and all team members with their
# seniority numbers and current bid line numbers.
class Data(object):

    def Create_Lists(self):
        c = Choices()
        d = Data()
        Entry = ('Invalid entry!')
        Ask = ('y', 'n')
        Create_Choices = ('1 Create team list', '2 Create bid line list',
                          '3 Back\n')

        Create_List = ' \n'.join(Create_Choices)
        print (Create_List)

        Create_Ask = input('What do you want to do?\n> ')

        # Create team list
        if Create_Ask == '1':
            Files()

            Ask_choice = ' \n'.join(Ask)
            print (Ask_choice)

            Add = input('Add a team member?\n> ')

            if Add.lower() == 'n':
                d.Create_Lists()

            elif Add.lower() == 'y':
                name = input('\nEnter name and seniority number.\n> ')
                print (', '.join(name.split())), ('\nUnder development\n')
                d.Create_Lists()

            else:
                print (Entry)
                d.Create_Lists()

        # Create a list of all existing bid lines.
        elif Create_Ask == '2':
            Files()

            Ask_choice = ' \n'.join(Ask)
            print (Ask_choice)

            Add = input('Add a bid line?\n> ')

            if Add.lower() == 'n':
                d.Create_Lists()

            elif Add.lower() == 'y':
                print ('Under development\n')
                d.Create_Lists()

            else:
                print (Entry)
                d.Create_Lists()

        elif Create_Ask == '3':
            c.Activity_Choices()

        else:
            print(Entry)
            d.Create_Lists()

class Choices(object):

    def Activity_Choices(self):
        c = Choices()
        d = Data()
        Entry = ('Invalid entry!')
        Ask = ('y', 'n')
        Actions = ('1 New Bid', '2 View available bid lines',
                   '3 View current bid assignments', '4 Edit bid lines',
                   '5 Edit team members', '6 Create Lists', '7 Exit\n')
        Actions_List = ' \n'.join(Actions)
        print(Actions_List)

        New_Ask = input('Choose an option.\n> ')

        if New_Ask == '1':

            Ask_choice = ' \n'.join(Ask)
            print (Ask_choice)

            Ask = raw_input('\nDo you want to start a new bid?\n> ')

            if Ask.lower() == 'y':
                bdline = raw_input('Enter your name.\n> ')

                if bdline in open('BidLines.csv').read():
                    print('Available bild line(s).\n')
                    with open('BidLines.csv', 'r') as fin:
                        for i in fin.readlines():
                            print(i)
                            fin.close()
							
            else:   
                Activity_Choices()

        # View available bid lines.
        elif New_Ask == '2':
            lines = input('Enter file name.\n> ')
            with open(lines, 'r') as fin:
                for i in fin.readlines():
                    print(i)
            c.Activity_Choices()

        # View current bid assignments.
        elif New_Ask == '3':
            assignment = input('Enter file name.\n> ')
            with open(assignment, 'r') as fin:
                for i in fin.readlines():
                    print(i)
            c.Activity_Choices()

        # Edit bid lines.
        elif New_Ask == '4':

            Edit_Actions = ('1 Change existing bid line(s)',
                            '2 Add new bid line(s)', '3 Delete bid line(s)', '4 Back')

            Edit_choices = ' \n'.join(Edit_Actions)
            print (Edit_choices)

            Edit_Ask = input('Choose an option.\n> ')

            if Edit_Ask == '1':
                Files()
                # edit = input('...\n>')
                #...
                print ('Done!')

            elif Edit_Ask == '2':
                Files()
                # edit = input('...\n>')
                #...
                print ('Done!')
                c.Activity_Choices()

            elif Edit_Ask == '3':
                Files()
                # edit = input('...\n>')
                #...
                print ('Done!')
                c.Activity_Choices()

            if New_Ask == '4':
                c.Activity_Choices()

            else:
                print (Entry)
                print (Edit_Actions)

        # Edit team members.
        elif New_Ask == '5':
            Edit_Choices = ('1 Change existing team member(s)',
                            '2 Add new team member(s)', '3 Remove team member(s)', '4 Back')

            print '\n '.join(Edit_Choices)

            Edit_Ask = input('Choose an option.\n> ')

            if Edit_Ask == '1':
                Files()
                # edit = raw_input()
                #...
                print ('Done!')
                c.Activity_Choices()

            elif Edit_Ask == '2':
                Files()
                # edit = raw_input()
                #...
                print ('Done!')
                c.Activity_Choices()

            elif Edit_Ask == '3':
                Files()
                # edit = raw_input()
                #...
                print ('Done!')
                c.Activity_Choices()

            elif Edit_Ask == '4':
                c.Activity_Choices()

            else:
                print (Entry)
                print (Edit_Actions)
                c.Activity_Choices()

        elif New_Ask == '6':
            d.Create_Lists()

        elif New_Ask == '7':
            quit()

        else:
            print (Entry)
            c.Activity_Choices()

class main(object):

    def __init__(self):
        c = Choices()
        c.Activity_Choices()

if __name__ == "__main__":
    main()

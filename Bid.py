# By Micah M. 2017
# Bid Version 1.2 
# Python 2.7.13


import os.path
import csv

# create file.
def Files():
    filename = raw_input('Enter file name.\n> ')
		
    if os.path.exists(filename) == True:		
        f = open(filename, 'w')
        f.close()
		
    elif os.path.exists(filename) == False:
        print ('Creating ' + filename + '.txt\n')
        f = open(filename, 'w+')
        f.close()
        print ('Done!\n')
			
# Create lists of all bid lines, and all team members with their seniority numbers
# and current bid line numbers.
class Data(object):

    def Create_Lists(self):
        c = Choices()
        d = Data()
        Entry = ('Invalid entry!')
        Ask = ('y', 'n')
        Create_Choices = ('1 Create team list', '2 Create bid line list',
                          '3 Back\n')
        for i in Create_Choices:
            print ('%s' % i)

        Create_Ask = raw_input('What do you want to do?\n> ')

        # Create team list
        if Create_Ask == '1':
            Files()
				
            for i in Ask:
                print ('%s' % i)

            Add = raw_input('Add a team member? ')

            if Add == 'n':
                d.Create_Lists()

            elif Add == 'y':
                name = raw_input('\nEnter name and seniority number.\n> ')
                print (', '.join(name.split()))
                print ('\nUnder development\n')
                d.Create_Lists()

            else:
                print (Entry)
                d.Create_Lists()

        # Create a list of all existing bid lines.
        elif Create_Ask == '2':
            Files()
				
            for i in Ask:
                print ('%s' % i)
					
            Add = raw_input('Add a bid line?\n> ')
				
            if Add == 'n':
                d.Create_Lists()

            elif Add == 'y':
                # name = raw_input('Enter bid line.\n> '
                print ('Under development\n')
                d.Create_Lists()

            else:
                print (Entry)
                d.Create_Lists()

        elif Create_Ask == '3':
            c.Activity_Choices()

        else:
            print (Entry)
            d.Create_Lists()


class Choices(object):

    def Activity_Choices(self):
        c = Choices()
        d = Data()
        Entry = ('Invalid entry!')
        Answers = ('y', 'n')
        Actions = ('1 New Bid', '2 View available bid lines',
                   '3 View current bid assignments', '4 Edit bid lines',
                   '5 Edit team members', '6 Create Lists', '7 Exit\n')
        for i in Actions:
            print ('%s' % i)

        New_Ask = raw_input('Choose an option.\n> ')

        if New_Ask == '1':

            for i in Answers:
                print ('%s' % i)

            Ask = raw_input('\nDo you want to start a new bid?\n> ')

            if Ask == 'y':
                bdline = raw_input('Enter your name.\n> ')

                if bdline in open('BidLines.csv').read():
                    print ('True')
                    print ('Available bild line(s).\n')
                    with open('BidLines.csv', 'r') as fin:
                        for i in fin.readlines():
                            print(i)
                            fin.close()

        # View available bid lines.
        elif New_Ask == '2':
            # Display all existing bid lines.
            lines = raw_input('Enter file name.\n> ')
            with open(lines, 'r') as fin:
                for i in fin.readlines():
                    print(i)
            c.Activity_Choices()

        # View current bid assignments.
        elif New_Ask == '3':
            assignment = raw_input('Enter file name.\n> ')
            with open(assignment, 'r') as fin:
                for i in fin.readlines():
                    print(i)
            c.Activity_Choices()

        # Edit bid lines.
        elif New_Ask == '4':

            Edit_Actions = ('1 Change existing bid line(s)',
                            '2 Add new bid line(s)', '3 Delete bid line(s)', '4 Back')
            for i in Edit_Actions:
                print ('%s' % i)
				
            Edit_Ask = raw_input('Choose an option.\n> ')
			
            if Edit_Ask == '1':
                Files()
                #edit = raw_input('...\n>')
                # f.write(edit)
                #...
                f.close()
                print ('Done!')

            elif Edit_Ask == '2':
                Files()
                #edit = raw_input('...\n>')
                # f.write(edit)
                #...
                f.close()
                print ('Done!')
                c.Activity_Choices()

            elif Edit_Ask == '3':
                Files()
                #edit = raw_input('...\n>')
                # f.write(edit)
                #...
                f.close()
                print ('Done!')
                c.Activity_Choices()

            if New_Ask == '4':
                c.Activity_Choices()

            else:
                print (Entry)
                print (Edit_Actions)
            print ('Under development\n')

        # Edit team members.
        elif New_Ask == '5':
            Edit_Choices = ('1 Change existing team member(s)',
                            '2 Add new team member(s)', '3 Remove team member(s)', '4 Back')
            for i in Edit_Choices:
                print ('%s' % i)

            Edit_Ask = raw_input('Choose an option.\n> ')

            if Edit_Ask == '1':
                Files()
                #edit = raw_input('...\n>')
                # f.write(edit)
                #...
                print ('Done!')
                c.Activity_Choices()

            elif Edit_Ask == '2':
                Files()
                #edit = raw_input('...\n>')
                # f.write(edit)
                #...
                print ('Done!')
                c.Activity_Choices()

            elif Edit_Ask == '3':
                Files()
                #edit = raw_input('...\n>')
                # f.write(edit)
                #...
                print ('Done!')
                c.Activity_Choices()

            elif Edit_Ask == '4':
                c.Activity_Choices()

            else:
                print (Entry)
                print (Edit_Actions)
                c.Activity_Choices()
            print ('Under development\n')

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
